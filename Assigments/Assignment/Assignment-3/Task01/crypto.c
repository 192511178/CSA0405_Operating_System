#include <stdio.h>
#include <string.h>
const char *encrypt_message(const char *s) {
    static char out[512]; size_t n=strlen(s);
    if(n>sizeof(out)-1) n=sizeof(out)-1;
    for(size_t i=0;i<n;i++) out[i]=(char)(s[i]^0x5a);
    out[n]='\0'; return out;
}
