# Segmentation with paging (conceptual x86-style translation)

Logical address: **selector : offset** → segment descriptor lookup (base, limit, access rights)
→ linear address = base + offset (after limit/protection check) → page directory/table lookup
→ physical frame + page offset. In 32-bit protected mode, segmentation produces a linear address;
paging then translates that address to a physical address. Modern x86-64 uses a largely flat
segmentation model, while paging remains the principal memory-management mechanism.
