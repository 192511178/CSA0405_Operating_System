#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/resource.h>
#include <unistd.h>
#include <time.h>
static void run(int random_order){size_t pages=8192,ps=(size_t)sysconf(_SC_PAGESIZE),n=pages*ps;volatile unsigned char *p=mmap(NULL,n,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);if(p==MAP_FAILED){perror("mmap");return;}size_t *order=malloc(pages*sizeof(*order));for(size_t i=0;i<pages;i++)order[i]=i;if(random_order){srand(42);for(size_t i=pages-1;i>0;i--){size_t j=(size_t)rand()%(i+1),t=order[i];order[i]=order[j];order[j]=t;}}struct rusage a,b;getrusage(RUSAGE_SELF,&a);for(size_t i=0;i<pages;i++)p[order[i]*ps]=1;getrusage(RUSAGE_SELF,&b);printf("%s: minor_faults=%ld major_faults=%ld pages=%zu\n",random_order?"random":"sequential",b.ru_minflt-a.ru_minflt,b.ru_majflt-a.ru_majflt,pages);free(order);munmap((void*)p,n);}
int main(void){run(0);run(1);return 0;}
