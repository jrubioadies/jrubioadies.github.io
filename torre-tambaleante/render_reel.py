import asyncio, os, sys, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "frames"
OUT.mkdir(exist_ok=True)
FONTS = ROOT / "node_modules/@fontsource"
EVERY = int(sys.argv[1]) if len(sys.argv) > 1 else 1   # 1 = todos los frames
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9

import base64
def b64(f): return "data:font/woff2;base64,"+base64.b64encode(open(f,'rb').read()).decode()
FONT_CSS = f"""
@font-face{{font-family:'Lilita One';src:url({b64(FONTS/'lilita-one/files/lilita-one-latin-400-normal.woff2')})}}
@font-face{{font-family:'Nunito';font-weight:500;src:url({b64(FONTS/'nunito/files/nunito-latin-500-normal.woff2')})}}
@font-face{{font-family:'Nunito';font-weight:700;src:url({b64(FONTS/'nunito/files/nunito-latin-700-normal.woff2')})}}
@font-face{{font-family:'Nunito';font-weight:800;src:url({b64(FONTS/'nunito/files/nunito-latin-800-normal.woff2')})}}
"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--allow-file-access-from-files"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        three = (ROOT / "node_modules/three/build/three.min.js").read_text()
        async def route(r):
            u = r.request.url
            if "three.min.js" in u:
                await r.fulfill(body=three, content_type="application/javascript")
            elif "fonts.g" in u:
                await r.fulfill(body="", content_type="text/css")
            else:
                await r.continue_()
        await pg.route("**/*", route)
        pg.on("console", lambda m: print("console:", m.text) if m.type in ("error", "warning") else None)
        pg.on("pageerror", lambda e: print("pageerror:", e))
        await pg.goto(f"file://{ROOT}/index.html?reel")
        await pg.add_style_tag(content=FONT_CSS)
        await pg.wait_for_function("window.__ready===true", timeout=30000)
        await pg.evaluate("Promise.all([document.fonts.load('120px \"Lilita One\"'),document.fonts.load('800 50px Nunito'),document.fonts.load('700 50px Nunito')])")
        dur = await pg.evaluate("window.__reelDuration")
        n = int(dur / 1000 * 30)
        saved = 0
        for f in range(min(n, LIMIT)):
            await pg.evaluate("window.__step()")
            if f % EVERY == 0:
                await pg.screenshot(path=str(OUT / f"f{f:04d}.jpg"), type="jpeg", quality=92, timeout=180000)
                saved += 1
        print("frames", n, "saved", saved)
        await b.close()

asyncio.run(main())
