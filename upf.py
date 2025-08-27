import sys
from urllib.parse import urlparse, parse_qsl

def value_type(v):
    try:
        float(v)
        return 'num'
    except ValueError:
        return 'str'

seen = set()
filter_params = "-p" in sys.argv

for line in sys.stdin:
    url = line.strip()
    if not url:
        continue

    parsed = urlparse(url)
    params = parse_qsl(parsed.query)

    if filter_params and not params:
        continue

    params_with_type = tuple([(p[0], value_type(p[1])) for p in params])
    key = (parsed.netloc, parsed.path, params_with_type)

    if key not in seen:
        print(url)
        seen.add(key)
