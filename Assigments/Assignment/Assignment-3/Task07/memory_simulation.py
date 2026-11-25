# Illustrative fixed working-set budget for 2 GiB RAM, no swap.
RAM=2048
tasks={"real_time_control_locked":128,"machine_learning":1536,"logging":128,"OS_and_services":256}
print("Memory budget (MiB)")
for k,v in tasks.items():print(f"{k:30s} {v:4d}")
print("Total:",sum(tasks.values()),"MiB of",RAM,"MiB")
print("Fourth task 500 MiB: total",sum(tasks.values())+500,"MiB; exceeds RAM by",sum(tasks.values())+500-RAM,"MiB")
print("Decision: reserve/lock control memory; cap ML working set; bound logging; reject or defer extra task.")
