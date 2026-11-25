#include <stdio.h>
#define PAGE_SIZE 2048
#define PAGES 8
int page_table[PAGES]={5,2,-1,7,0,-1,3,-1};
int main(void){
 unsigned a[]={0,1500,3100,6200,9000,2049};
 for(int i=0;i<6;i++){unsigned p=a[i]/PAGE_SIZE,d=a[i]%PAGE_SIZE;
 printf("%5u -> page %u offset %4u : ",a[i],p,d);
 if(p>=PAGES) puts("invalid address"); else if(page_table[p]<0) puts("page fault");
 else printf("physical %u\n",(unsigned)page_table[p]*PAGE_SIZE+d);}
}
