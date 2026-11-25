import random,time
from collections import defaultdict,deque
import matplotlib.pyplot as plt
def simulate(ref,n,kind):
 frames=[];last={};faults=0;hand=0
 positions=defaultdict(deque)
 if kind=="OPT":
  for i,p in enumerate(ref):positions[p].append(i)
 for i,p in enumerate(ref):
  if kind=="OPT":
   positions[p].popleft()
  if p in frames:
   last[p]=i;continue
  faults+=1
  if len(frames)<n:frames.append(p)
  elif kind=="FIFO":frames[hand]=p;hand=(hand+1)%n
  elif kind=="LRU":
   victim=min(frames,key=lambda x:last[x]);frames[frames.index(victim)]=p
  else:
   victim=max(frames,key=lambda x:(positions[x][0] if positions[x] else len(ref)))
   frames[frames.index(victim)]=p
  last[p]=i
 return faults
random.seed(17)
local=[random.choice(range(8)) if random.random()<.85 else random.randrange(64) for _ in range(100000)]
random_ref=[random.randrange(256) for _ in range(100000)]
for label,ref in (("locality",local),("random",random_ref)):
 print(label)
 rows=[]
 for f in range(3,11):
  row=[simulate(ref,f,k) for k in ("FIFO","LRU","OPT")];rows.append(row);print(f,f"FIFO={row[0]}",f"LRU={row[1]}",f"Optimal={row[2]}")
 if label=="locality":
  plt.figure(figsize=(6,3))
  for j,k in enumerate(("FIFO","LRU","Optimal")):plt.plot(range(3,11),[x[j] for x in rows],marker='o',label=k,color='black',linestyle=['-','--',':'][j])
  plt.xlabel('Frames');plt.ylabel('Page faults');plt.title('Replacement faults — locality workload');plt.legend();plt.grid(True,linestyle=':');plt.tight_layout();plt.savefig('evidence/faults_vs_frames.png',dpi=180)
print("Timing (100,000 references; Python reference implementation; machine-dependent)")
for kind in ("FIFO","LRU","OPT"):
 t=time.perf_counter();simulate(local,8,kind);print(kind,f"{time.perf_counter()-t:.4f}s")
