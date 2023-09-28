#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main(int arc, char*ar[])
{
int pid, ret;
char s[100];
pid=fork();
//check the value of pid variable to decide what to do
if(pid<0)
{
printf("\nError in creating process");
}
else if(pid>0)
{
wait(NULL);
printf("\n Paren Process: ");
printf("\n\tParent Process id: %d\n", getpid());
}
else
{
printf("\nChild process: ");
printf("\n\tChild Process id: %d\n", getpid());
printf("\n\tChild process parent id: %d\n",getppid());
}
return 0;
}