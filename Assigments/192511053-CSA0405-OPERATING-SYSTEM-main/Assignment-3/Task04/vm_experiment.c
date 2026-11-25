#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/resource.h>
#include <string.h>
int main(int argc,char **argv){
 size_t mb=argc>1?(size_t)strtoul(argv[1],NULL,10):64;
 size_t n=mb*1024*1024;
 char *p=mmap(NULL,n,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);
 if(p==MAP_FAILED){perror("mmap");return 1;}
 struct rusage before,after; getrusage(RUSAGE_SELF,&before);
 for(size_t i=0;i<n;i+=4096)p[i]=1;
 getrusage(RUSAGE_SELF,&after);
 printf("touched=%zu MiB minor_faults_delta=%ld major_faults_delta=%ld\n",mb,
  after.ru_minflt-before.ru_minflt,after.ru_majflt-before.ru_majflt);
 pid_t pid=fork();
 if(pid==0){p[0]=2; _exit(0);}
 waitpid(pid,NULL,0);
 puts("fork child wrote one private page (copy-on-write demonstration)");
 munmap(p,n);return 0;
}
