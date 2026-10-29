"""Graba el reel de Instagram (1080x1920, 30 fps) de un juego a partir de index.html?reel.

Uso: python3 render_reel.py CARPETA_DEL_JUEGO [cada_n_frames] [max_frames]
La carpeta debe tener reel_fonts.json: [["Familia", peso, "paquete-fontsource"], ...]
Las fuentes se leen de FONTS_DIR (por defecto ~/torre/node_modules/@fontsource).
Después: ffmpeg -framerate 30 -i CARPETA/frames/f%04d.jpg -c:v libx264 -crf 18 -pix_fmt yuv420p reel.mp4
"""
import asyncio, base64, json, os, pathlib, shutil, sys
from playwright.async_api import async_playwright

ROOT = pathlib.Path(sys.argv[1]).resolve()
EVERY = int(sys.argv[2]) if len(sys.argv) > 2 else 1
LIMIT = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
OUT = ROOT / "frames"
shutil.rmtree(OUT, ignore_errors=True); OUT.mkdir()
FONTS = pathlib.Path(os.environ.get("FONTS_DIR", "/home/claude/torre/node_modules/@fontsource"))
spec = json.loads((ROOT / "reel_fonts.json").read_text())

def b64(f):
    return "data:font/woff2;base64," + base64.b64encode(open(f, "rb").read()).decode()

FONT_CSS = "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url({b64(FONTS/pkg/'files'/f'{pkg}-latin-{w}-normal.woff2')})}}"
    for fam, w, pkg in spec)
LOADS = ",".join(f"document.fonts.load('{w} 40px \"{fam}\"')" for fam, w, _ in spec)

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
        await pg.wait_for_function("window.__ready===true", timeout=120000)
        await pg.evaluate(f"Promise.all([{LOADS}])")
        n = int(await pg.evaluate("window.__reelDuration") / 1000 * 30)
        for f in range(min(n, LIMIT)):
            await pg.evaluate("window.__step()")
            if f % EVERY == 0:
                await pg.screenshot(path=str(OUT / f"f{f:04d}.jpg"), type="jpeg", quality=92)
        print("frames", n)
        await b.close()

asyncio.run(main())
