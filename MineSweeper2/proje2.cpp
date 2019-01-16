#include<iostream>
using namespace std;

void find_number (char lead[10][10])
{
    int i,j,c;
    for(i=0;i<10;i++)
    {
        for(j=0;j<10;j++)
        {
            if(lead[i][j]!='9')
            {
            c=0;
            if((i+1<10)&&(j+1<10))
            {if(lead[i+1][j+1]=='9')
                c++;}
                if(j+1<10)
            {if(lead[i][j+1]=='9')
                c++;}
                if(i+1<10)
                {if(lead[i+1][j]=='9')
                c++;}
                if(i-1>=0)
                {
                    if(lead[i-1][j]=='9')
                c++;
                if(j+1<10)
                    {if(lead[i-1][j+1]=='9')
                c++;}
                }
                if(j-1>=0)
                {
                    if(lead[i][j-1]=='9')
                c++;
                if(i+1<10)
                    {if(lead[i+1][j-1]=='9')
                c++;}
                }
                if((i-1>=0)&&(j-1>=0))
                {
                    if(lead[i-1][j-1]=='9')
                c++;
                }
                lead[i][j]=c+48;
            }
        }
    }
}
int v=0;
void show (int i,int j,char map[10][10],char lead[10][10])
{
if((lead[i][j]=='0')&&(map[i][j]!='0'))
{map[i][j]=lead[i][j];
    if(i+1<10)
    {show (i+1,j,map,lead);}
    else{map[i][j]=lead[i][j];}
    if(j+1<10)
    show (i,j+1,map,lead);
    else{map[i][j]=lead[i][j];}
    if((i+1<10)&&(j+1<10))
    show (i+1,j+1,map,lead);
    else{map[i][j]=lead[i][j];}
    if(i-1>=0)
    show (i-1,j,map,lead);
    else{map[i][j]=lead[i][j];}
    if(j-1>=0)
    show (i,j-1,map,lead);
    else{map[i][j]=lead[i][j];}
    if((i-1>=0)&&(j-1>=0))
    show (i-1,j-1,map,lead);
    else{map[i][j]=lead[i][j];}
     if((i+1<10)&&(j-1>=0))
    show (i+1,j-1,map,lead);
    else{map[i][j]=lead[i][j];}
    if((i-1>=0)&&(j+1<10))
    show (i-1,j+1,map,lead);
    else{map[i][j]=lead[i][j];}

}

else
    {
        map[i][j]=lead[i][j];
    }

   /* for(int m=0;m<10;m++)
    {
        for(int n=0;n<10;n++)
           {
            cout<<map[m][n]<<' ';
           }
        cout<<endl;
    }
cout<<endl;
v++;
if (v==30)
system("pause");*/
}

int main ()
{
    int m,n,i,j;
    char lead[10][10],map[10][10];
    for(m=0;m<10;m++)
    {
        for(n=0;n<10;n++)
           {map[m][n]='*';
           }
    }
    lead[0][0]='9';
    lead[0][1]='9';
    lead[0][2]='9';
    lead[0][3]='9';
    lead[0][4]='9';
    lead[0][5]='9';
    

    lead[0][5]='9';
    lead[1][5]='9';
    lead[2][5]='9';
    lead[3][5]='9';
    lead[4][5]='9';
    lead[5][5]='9';


    lead[4][0]='9';
    lead[4][1]='9';
    lead[4][2]='9';
    lead[4][3]='9';
    lead[4][4]='9';
    lead[4][5]='9';


    lead[0][0]='9';
    lead[1][0]='9';
    lead[2][0]='9';
    lead[3][0]='9';
    lead[4][0]='9';
    lead[5][0]='9';

   

    find_number(lead);
for(m=0;m<10;m++)
    {
        for(n=0;n<10;n++)
           {
            cout<<lead[m][n]<<' ';
           }
        cout<<endl;
    }
    cin>>i>>j;
    show (i,j,map,lead);
    for(m=0;m<10;m++)
    {
        for(n=0;n<10;n++)
           {
            cout<<map[m][n]<<' ';
           }
        cout<<endl;
    }
}
