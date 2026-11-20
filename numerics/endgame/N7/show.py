import sys, json
for line in sys.stdin:
    line = line.strip()
    if not line.startswith('{'):
        print(line); continue
    d = json.loads(line)
    keys = ['v','eps','T_over_L0','legs','supQ','sup_bE','sup_B','sup_K','sup_span','max_hull_rate','sup_time_over_L','winding','seen_ok','secs_walk']
    print(" ".join((f"{k}={d[k]:.5g}" if isinstance(d[k], float) else f"{k}={d[k]}") for k in keys if k in d))
