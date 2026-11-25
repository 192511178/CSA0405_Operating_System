mem_ns=100
fault_ms=8
print("Effective access time (P=page fault probability): EAT=(1-P)*100ns + P*(8ms)")
for denom in (1000,100000,1000000):
 p=1/denom
 eat=(1-p)*mem_ns+p*fault_ms*1_000_000
 print(f"fault rate 1/{denom:,}: {eat:.2f} ns")
# 10% slowdown threshold: EAT <= 110 ns
pmax=(110-mem_ns)/(fault_ms*1_000_000-mem_ns)
print(f"maximum fault probability for <=10% slowdown: {pmax:.8g} (about 1 in {1/pmax:,.0f})")
print("If all references are resident: approximately 100 ns; demand paging adds fault-service cost.")
