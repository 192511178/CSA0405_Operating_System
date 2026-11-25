#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <time.h>
#include <sys/resource.h>
#include <unistd.h>
static double ns(struct timespec a,struct timespec b){return (b.tv_sec-a.tv_sec)*1e9+(b.tv_nsec-a.tv_nsec);}
int main(int argc,char **argv){
 int lock=argc>1 && strcmp(argv[1],"lock")==0;
 const size_t n=8*1024*1024; volatile unsigned char *p=mmap(NULL,n,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);
 if(p==(void*)-1){perror("mmap");return 1;}
 if(lock && mlock((void*)p,n)!=0){perror("mlock (limit/permission may prevent locking)");munmap((void*)p,n);return 2;}
 for(size_t i=0;i<n;i+=4096)p[i]=1;
 struct timespec a,b;double max=0,total=0;
 for(int r=0;r<10000;r++){clock_gettime(CLOCK_MONOTONIC,&a);for(size_t i=0;i<n;i+=4096)p[i]++;clock_gettime(CLOCK_MONOTONIC,&b);double d=ns(a,b);if(d>max)max=d;total+=d;}
 printf("mode=%s iterations=10000 max_loop_ns=%.0f mean_loop_ns=%.0f\n",lock?"mlock":"unlocked",max,total/10000);
 if(lock)munlock((void*)p,n);munmap((void*)p,n);return 0;
}
