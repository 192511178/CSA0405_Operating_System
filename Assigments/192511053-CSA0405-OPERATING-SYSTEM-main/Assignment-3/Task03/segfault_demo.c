#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>
int main(void){pid_t p=fork();if(p==0){volatile int *bad=(int*)0;*bad=1;_exit(0);}int st;waitpid(p,&st,0);if(WIFSIGNALED(st))printf("child terminated by signal %d (%s)\n",WTERMSIG(st),WTERMSIG(st)==SIGSEGV?"SIGSEGV":"other");return 0;}
