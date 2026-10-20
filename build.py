"""Turn the published Claude artifact HTML into a standalone index.html for GitHub Pages.

Usage: python3 build.py path/to/artifact.html
"""
import sys

src = open(sys.argv[1], encoding="utf-8").read()
i = src.index("</style>") + len("</style>")
head, body = src[:i], src[i:]
head = head.replace("<style>", "<style>\nhtml,body{margin:0}\n[hidden]{display:none!important}\nimg{max-width:100%}\n:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}\n", 1)
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
       '<meta property="og:title" content="Brazil Runoff Watch">\n'
       '<meta property="og:description" content="Lula vs Flávio: every runoff poll graded against Oct 4, our projection, vote math by region, and the debate reaction.">\n'
       + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
open(__file__.rsplit("/", 1)[0] + "/index.html" if "/" in __file__ else "index.html", "w", encoding="utf-8").write(out)
print("index.html written")
