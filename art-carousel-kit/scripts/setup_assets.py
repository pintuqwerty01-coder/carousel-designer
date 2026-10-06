"""Download the free third-party files the kit needs (only if they're missing), then check the toolchain.

Usage: python setup_assets.py
- Fonts: Preahvihear + Poppins 400/500/600/700 from the Google Fonts repository (SIL Open Font License).
- GSAP 3.14.2 from jsDelivr (free under GreenSock's standard licence).
Then reports whether Playwright/Chromium, Pillow, Node (npx) and ffmpeg are available.
"""
import pathlib, shutil, subprocess, urllib.request

KIT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "kit"
GF = "https://raw.githubusercontent.com/google/fonts/main/ofl"
FILES = {
    "fonts/Preahvihear-Regular.ttf": f"{GF}/preahvihear/Preahvihear-Regular.ttf",
    "fonts/Poppins-Regular.ttf": f"{GF}/poppins/Poppins-Regular.ttf",
    "fonts/Poppins-Medium.ttf": f"{GF}/poppins/Poppins-Medium.ttf",
    "fonts/Poppins-SemiBold.ttf": f"{GF}/poppins/Poppins-SemiBold.ttf",
    "fonts/Poppins-Bold.ttf": f"{GF}/poppins/Poppins-Bold.ttf",
    "gsap.min.js": "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js",
}

def main():
    for rel, url in FILES.items():
        dest = KIT / rel
        if dest.exists() and dest.stat().st_size > 1000: print("ok     ", rel); continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        print("fetch  ", rel, "<-", url)
        urllib.request.urlretrieve(url, dest)
    print()
    checks = {
        "Pillow": "python -c \"import PIL\"",
        "Playwright + Chromium": "python -c \"from playwright.sync_api import sync_playwright as s; p=s().start(); b=p.chromium.launch(); b.close(); p.stop()\"",
        "Node / npx": "npx --version",
        "ffmpeg": "ffmpeg -version",
    }
    for name, cmd in checks.items():
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(("ok     " if r.returncode == 0 else "MISSING"), name)
    print("\nIf anything is MISSING, see 'Setup' in SKILL.md. Planning, copy layout, scenes and cover prompts work without it;"
          "\nstills need Pillow + Playwright; MP4s also need Node and ffmpeg.")

if __name__ == "__main__":
    main()
