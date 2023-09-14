
#include<stdio.h>

void main()
{
for(int i=1;i<100;i++)
{
if( i%2==0)
{
printf("this is even");
}
else if( i%2!=0)
{
printf("this is odd");
}
else
{
printf("this is unknown");
}

}
int index=1;
int faktoril=5;
while (index<=5)
{
     faktoril=faktoril*index ;
     index=index+1;
}
printf(faktoril);
}
