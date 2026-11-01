"""Tell Bing, Yandex, and other IndexNow engines that pages changed.

Run from the repo root after Netlify has deployed your changes:
    python3 tools/indexnow.py                 # submit every URL in sitemap.xml
    python3 tools/indexnow.py /insights/foo/  # submit specific paths
The key file (b5b3571b4a8b4a54b7c96ec45531b5ec.txt) must stay at the site root.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "walkerig.com"
KEY = "b5b3571b4a8b4a54b7c96ec45531b5ec"


def main():
    if len(sys.argv) > 1:
        urls = [f"https://{HOST}{p}" for p in sys.argv[1:]]
    else:
        urls = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text())
    body = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": urls,
    }).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req) as r:
        print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")


if __name__ == "__main__":
    main()
