import sys, json
for line in sys.stdin:
    line = line.strip()
    if not line.startswith('{'): print(line[:200]); continue
    d = json.loads(line)
    print(' '.join((f"{k}={x:.4g}" if isinstance(x, float) else f"{k}={x}") for k, x in d.items() if k not in ('opts',)))
