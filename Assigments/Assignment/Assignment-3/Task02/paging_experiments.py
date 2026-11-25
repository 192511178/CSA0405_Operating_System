import random, math, os, subprocess
random.seed(42)
sizes=[random.randint(1, 8*1024*1024) for _ in range(100)]
print("Internal fragmentation for 100 seeded process sizes")
for ps in (1024,4096,2*1024*1024):
    waste=sum((-s)%ps for s in sizes)
    print(f"page_size={ps:>7} bytes total_waste={waste:>10} bytes average={waste/100:.1f} bytes")
print("\nPage table entries (one-level, one entry per virtual page)")
for bits in (32,48):
    entries=2**bits//4096
    print(f"{bits}-bit: {entries:,} entries; at 8 bytes/entry = {entries*8:,} bytes ({entries*8/2**20:.2f} MiB)")
print("\nTLB effective access time, memory=100 ns, TLB lookup=10 ns")
for hit in (.80,.95,.99):
    eat=hit*(10+100)+(1-hit)*(10+200)
    print(f"hit={hit:.0%}: {eat:.2f} ns")
print("No TLB: 200 ns (two memory accesses)")
try:
    p=subprocess.run(["/usr/bin/time","-v","python3","-c","x=bytearray(16*1024*1024); sum(x)"],capture_output=True,text=True)
    print("\nLinux page-size:",os.sysconf("SC_PAGE_SIZE"))
    for line in p.stderr.splitlines():
        if "page faults" in line or "Maximum resident" in line: print(line.strip())
except Exception as e: print("time measurement unavailable:",e)
