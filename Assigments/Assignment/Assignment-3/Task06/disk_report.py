import subprocess,shutil
print("RAID capacity for six 4 TB disks (decimal TB)")
n=6; d=4
for raid,cap in (("RAID 0",n*d),("RAID 1 (three mirrored pairs)",n*d/2),("RAID 5",(n-1)*d),("RAID 10",n*d/2),("RAID 6",(n-2)*d)):
 print(f"{raid:24s}: {cap:g} TB usable (before filesystem overhead)")
p=0.02
raid1_loss=1-(1-p*p)**3
raid5_loss=1-sum(__import__('math').comb(6,k)*(p**k)*((1-p)**(6-k)) for k in (0,1))
print(f"\nIllustrative independent per-disk failure probability={p:.0%} per chosen interval")
print(f"RAID 1 (three mirror pairs) data-loss probability={raid1_loss:.6%}")
print(f"RAID 5 data-loss probability (2+ disks fail)={raid5_loss:.6%}")
print("\nLinux block devices (lsblk):")
try: print(subprocess.run(["lsblk","-o","NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS"],capture_output=True,text=True,check=True).stdout)
except Exception as e: print("lsblk unavailable:",e)
print("Swap:")
try: print(subprocess.run(["swapon","--show"],capture_output=True,text=True).stdout or "(no active swap listed)")
except Exception as e: print("swapon unavailable:",e)
print("Disk speed benchmark is not run automatically: use a dedicated test disk and fio; never benchmark by writing to a production device.")
