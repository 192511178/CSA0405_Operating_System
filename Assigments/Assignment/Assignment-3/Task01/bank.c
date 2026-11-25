#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
extern const char *encrypt_message(const char *);
int main(int argc, char **argv) {
    const char *msg = argc > 1 ? argv[1] : "bank-transfer-123";
    printf("PID=%ld\n", (long)getpid());
    printf("INPUT=%s\n", msg);
    printf("OUTPUT=%s\n", encrypt_message(msg));
    FILE *f = fopen("/proc/self/maps", "r");
    if (f) {
        char line[512]; puts("MAPS (first 12 entries):");
        for (int i=0; i<12 && fgets(line,sizeof line,f); ++i) fputs(line,stdout);
        fclose(f);
    }
    if (getenv("HOLD_MAPS")) sleep(2);
    return 0;
}
