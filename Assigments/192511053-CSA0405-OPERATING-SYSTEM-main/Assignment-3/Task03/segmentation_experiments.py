import random
random.seed(7)
# First-fit variable-size allocator with explicit free-list coalescing.
arena=2*1024*1024
sizes=[random.randint(4*1024,96*1024) for _ in range(20)]
free=[(0,arena)]; allocated={}
def alloc(pid,size):
    global free
    for i,(start,length) in enumerate(free):
        if length>=size:
            allocated[pid]=(start,size)
            if length==size: free.pop(i)
            else: free[i]=(start+size,length-size)
            return True
    return False
def release(pid):
    global free
    start,size=allocated.pop(pid);free.append((start,size));free.sort()
    merged=[]
    for a,n in free:
        if merged and merged[-1][0]+merged[-1][1]==a: merged[-1]=(merged[-1][0],merged[-1][1]+n)
        else: merged.append((a,n))
    free=merged
for i,size in enumerate(sizes): alloc(i,size)
for i in range(0,20,2): release(i)
total_free=sum(n for _,n in free);largest=max(n for _,n in free)
print("20 random segment requests:",sizes)
print("Allocated segments after freeing alternating IDs:",len(allocated))
print("Free holes:",free)
print("Total free:",total_free,"bytes; largest hole:",largest,"bytes")
print("External-fragmentation indicator (1-largest/total):",round(1-largest/total_free,4))
print("Table comparison: 3 segments x 8-byte descriptors = 24 bytes")
print("2 MiB / 4 KiB = 512 page entries; at 8 bytes = 4096 bytes")
