#include <stdio.h>
typedef struct {const char *name; unsigned base,limit; int readable,writable;} Segment;
int main(void){
 Segment s[]={{"code",10000,4096,1,0},{"data",20000,2048,1,1},{"stack",30000,1024,1,1}};
 unsigned test[][2]={{0,120},{1,1500},{2,1023},{0,4096},{1,2048},{2,0},{0,2048},{1,17}};
 for(int i=0;i<8;i++){
  unsigned seg=test[i][0],off=test[i][1];
  if(seg>=3){puts("invalid segment");continue;}
  printf("%s offset=%u: ",s[seg].name,off);
  if(off>=s[seg].limit) puts("SEGMENTATION FAULT (limit exceeded)");
  else printf("physical=%u\n",s[seg].base+off);
 }
 FILE *maps=fopen("/proc/self/maps","r");
 if(maps){char line[512];puts("\n/proc/self/maps (first 12 entries):");for(int i=0;i<12 && fgets(line,sizeof line,maps);i++)fputs(line,stdout);fclose(maps);}
 return 0;
}
