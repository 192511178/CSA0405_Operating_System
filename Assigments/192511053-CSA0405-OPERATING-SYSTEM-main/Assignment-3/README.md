# Operating Systems Assignment 3 – CO3

Student: B Santhosh Kumar
Register Number: 192511053
Course: CSA0405 – Operating Systems
Compiler: GCC 14.2.0
Environment used for package evidence: Debian GNU/Linux 13 (trixie), x86_64; Linux kernel 6.18.57; Python 3.13.5; page size 4096 bytes.
C standard: C11. Typical command: `gcc -std=c11 -Wall -Wextra file.c -o program`; add `-ldl` for `dlopen`, and `-pthread` if a pthread program is added.

## Repository structure
Each Task01–Task07 folder contains source, a `run.sh` or equivalent runner, task notes, and its own `evidence/` folder. Screenshots and captured outputs are kept within the relevant task folder.

## Run
From the repository root:
```sh
for d in Task{01..07}; do (cd "$d" && ./run.sh); done
```
Some measurements are host-dependent. The included outputs describe the environment above and should be rerun on the student's submission machine before final GitHub submission.

## Task summary
- Task01: static/shared linking, dynamic loading, ldd, maps, size and timing checks.
- Task02: page translation, required TODO implementation, page-table sizing, TLB and fragmentation calculations.
- Task03: segment base/limit translation, boundary checks, process map inspection and table/fragmentation illustration.
- Task04: demand paging calculations, memory-touch/page-fault experiment and fork copy-on-write demonstration.
- Task05: FIFO/LRU/Optimal, completed LRU TODO, Belady anomaly and workload simulation.
- Task06: Linux block-device/swap inspection and RAID capacity calculations.
- Task07: locked-memory timing demonstration and 2 GiB edge-device allocation plan.


