#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
#include <stdlib.h>
typedef const char *(*enc_fn)(const char *);
int main(int argc,char **argv) {
    const char *lib=argc>1?argv[1]:"./libcrypto_demo.so";
    void *h=dlopen(lib,RTLD_NOW);
    if(!h){fprintf(stderr,"dlopen failed: %s\n",dlerror());return 2;}
    dlerror(); enc_fn fn=(enc_fn)dlsym(h,"encrypt_message");
    const char *e=dlerror(); if(e){fprintf(stderr,"dlsym failed: %s\n",e);dlclose(h);return 3;}
    printf("runtime output: %s\n",fn("bank-transfer-123"));
    dlclose(h); return 0;
}
