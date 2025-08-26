import sys
from urllib.parse import urlparse, parse_qsl

def value_type(v):
    try:
        float(v)
        return 'num'
    except ValueError:
        return 'str'

seen = set()

for line in sys.stdin:
    url = line.strip()
    if not url:
        continue

    parsed = urlparse(url)

    params_with_type = tuple([(p[0], value_type(p[1])) for p in parse_qsl(parsed.query)])

    key = (parsed.netloc, parsed.path, params_with_type)

    if key not in seen:
        print(url)
        seen.add(key)