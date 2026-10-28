"""Graba el reel de Instagram (1080x1920, 30 fps) a partir de index.html?reel.

Uso: python3 render_reel.py [cada_n_frames] [max_frames]
Necesita Playwright y las fuentes de @fontsource en ../torre/node_modules (o FONTS_DIR).
Luego: ffmpeg -framerate 30 -i frames/f%04d.jpg -c:v libx264 -crf 18 -pix_fmt yuv420p sudoku_reel.mp4
"""
import asyncio, base64, os, pathlib, sys
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "frames"
OUT.mkdir(exist_ok=True)
FONTS = pathlib.Path(os.environ.get("FONTS_DIR", ROOT.parent / "torre/node_modules/@fontsource"))
EVERY = int(sys.argv[1]) if len(sys.argv) > 1 else 1
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9

def b64(f):
    return "data:font/woff2;base64," + base64.b64encode(open(f, "rb").read()).decode()

FONT_CSS = "".join(
    f"@font-face{{font-family:'Bricolage Grotesque';font-weight:{w};src:url({b64(FONTS/f'bricolage-grotesque/files/bricolage-grotesque-latin-{w}-normal.woff2')})}}"
    for w in (500, 700, 800)
) + "".join(
    f"@font-face{{font-family:'Figtree';font-weight:{w};src:url({b64(FONTS/f'figtree/files/figtree-latin-{w}-normal.woff2')})}}"
    for w in (500, 600, 700)
)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1, color_scheme="light")
        async def route(r):
            if "fonts.g" in r.request.url:
                await r.fulfill(body="", content_type="text/css")
            else:
                await r.continue_()
        await pg.route("**/*", route)
        pg.on("pageerror", lambda e: print("pageerror:", e))
        await pg.goto(f"file://{ROOT}/index.html?reel")
        await pg.add_style_tag(content=FONT_CSS)
        await pg.wait_for_function("window.__ready===true", timeout=60000)
        await pg.evaluate("Promise.all([document.fonts.load('800 90px \"Bricolage Grotesque\"'),document.fonts.load('500 60px \"Bricolage Grotesque\"'),document.fonts.load('700 48px Figtree')])")
        n = int(await pg.evaluate("window.__reelDuration") / 1000 * 30)
        for f in range(min(n, LIMIT)):
            await pg.evaluate("window.__step()")
            if f % EVERY == 0:
                await pg.screenshot(path=str(OUT / f"f{f:04d}.jpg"), type="jpeg", quality=92)
        print("frames", n)
        await b.close()

asyncio.run(main())
