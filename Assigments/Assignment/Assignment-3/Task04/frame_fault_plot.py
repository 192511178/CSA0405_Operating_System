import matplotlib.pyplot as plt
ref=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
def lru_faults(fr):
 f=[];last={};faults=0
 for i,p in enumerate(ref):
  if p in f:last[p]=i;continue
  faults+=1
  if len(f)<fr:f.append(p)
  else:v=min(f,key=lambda x:last[x]);f[f.index(v)]=p
  last[p]=i
 return faults
xs=list(range(1,11));ys=[lru_faults(x) for x in xs]
plt.figure(figsize=(6,3));plt.plot(xs,ys,marker='o',color='black');plt.xlabel('Number of frames');plt.ylabel('LRU page faults');plt.title('Page faults versus frame count');plt.grid(True,linestyle=':');plt.tight_layout();plt.savefig('evidence/page_faults_vs_frames.png',dpi=180)
print('LRU faults by frame count:',list(zip(xs,ys)))
