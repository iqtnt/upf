import sys
from urllib.parse import urlparse, parse_qsl

def value_type(v):
    try:
        float(v)
        return 'num'
    except ValueError:
        return 'str'

allowed_args = ["-p", "-ext"]

for arg in sys.argv[1:]:
    if arg.startswith("-") and arg not in allowed_args:
        print(f"Error: Unknown argument '{arg}'.")
        sys.exit(1)

seen = set()
filter_params = "-p" in sys.argv

exts = []
if "-ext" in sys.argv:
    idx = sys.argv.index("-ext") + 1
    if idx < len(sys.argv):
        exts = sys.argv[idx].split(",")
        exts = [e.strip().lower() for e in exts if e.strip()]

exclude_patterns = [
    "v1?ray=",
    ".ttf?v=",
    ".css?ver=",
    ".css?v=",
    ".css?r=",
    ".js?v=",
    ".js?ver=",
    ".js?r=",
    "&ver=",
    ".gif?ray=",
    ".svg?v=",
    ".woff2?v=",
    ".woff?v=",
    ".eot?v=",
    "wp-json/oembed/1.0/embed?url="
]

if sys.stdin.isatty():
    print("Please provide URLs: cat urls.txt | python script.py")
    sys.exit(1)

for line in sys.stdin:
    url = line.strip()
    if not url:
        continue

    if filter_params and any(pattern in url for pattern in exclude_patterns):
        continue

    parsed = urlparse(url)
    params = parse_qsl(parsed.query)

    if filter_params and not params:
        continue

    if exts and not any(parsed.path.lower().endswith("." + e) for e in exts):
        continue

    params_with_type = tuple([(p[0], value_type(p[1])) for p in params])
    key = (parsed.netloc, parsed.path, params_with_type)

    if key not in seen:
        print(url)
        seen.add(key)
