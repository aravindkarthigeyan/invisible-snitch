"""N7: Harry's path for start S + C_cut at a coarse eps_c (leg headings and durations), from the P6e simulator.
Usage: python coarse_path.py v eps_c [delta]   -> out/path_v{v}_e{eps_c}.npz"""
import sys, os, time, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'P6e'))
import sim
v = float(sys.argv[1]); epsc = float(sys.argv[2]); delta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
t = time.time()
res = sim.run(v, epsc, delta=delta, H=min(0.002, 2 * epsc))
path = res["path"]
tau = np.array([q[0] for q in path] + [res["tau_entry"]])
P = np.array([q[1] for q in path] + [res["P_entry"]])
u = np.array([q[2] for q in path])
out = os.path.join(os.path.dirname(__file__), 'out', f'path_v{v}_e{epsc}_d{delta}.npz')
np.savez(out, v=v, epsc=epsc, delta=delta, tau=tau, P=P, u=u, O=res["O"], Y=res["Y"], r_arm=res["r_arm"],
         base_label=res["base_label"], a_s=res["a_s"])
print(v, epsc, 'legs', len(u), 'tau_entry', res["tau_entry"], 'base_label', res["base_label"], 'secs', round(time.time() - t, 1))
