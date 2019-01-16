#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

const int n=10;//martix will be n*n
const int m=10;//number of boomb

void find_number (char [n][n]);
void printArr (char [n][n]);
void bombRandom (char [n][n]);
void show (int,int,char [n][n],char [n][n]);
void gameover (int ,int ,int &,char [n][n]);
void put_flag (char [n][n],int,int);
void win (char [n][n],int &,char [n][n]);


int main ()
{
    char map[n][n],lead[n][n];
    int i,j,k,flag;
    bombRandom (lead);
    find_number(lead);
    printArr(lead);

    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            map[i][j]='*';
        }
    }
    
    while (int loop=1)
    {
        do
        {
        cout<<"row:"<<endl;
        cin>>i;
        cout<<"colum0:"<<endl;
        cin>>j;
        }while(!(((i<n)&&(i>=0))&&((j<n)&&(j>=0))));

        do
        {
        cout<<"if you want to dig enter 1, for notation enter 2"<<endl;
        cin>>k;
        }while((k!=1)&&(k!=2));

        if(k==2)
        {
            put_flag(map,i,j);
            printArr(map);
        }
        else
        {
            if(map[i][j]=='^')
            {
                do
                {
                    cout<<"are you sure?"<<endl<<"1:yes"<<endl<<"2:no";
                    cin>>k;
                }while((k!=1)&&(k!=2));
                if(k==1)
                {
                    gameover(i,j,flag,lead);
                    if(flag==1)
                    {
                        return 0;
                    }
                   show(i,j,map,lead);
                   printArr(map);
                }
                else{continue;}
            }
            else
            {
                gameover(i,j,flag,lead);
                    if(flag==1)
                    {
                        return 0;
                    }
                   show(i,j,map,lead);
                   printArr(map);
            }
        }
        flag=0;
        win(map,flag,lead);
        if(flag==1)
        {
            return 0;
        }

    }


}
void bombRandom (char lead[n][n]) {
int i, j;
for (i=0; i<n; i++){
    for (j=0; j<n; j++){
        lead[i][j]='0';
    }
}

srand(time(NULL));
for (int t=0; t<m; t++){
    i = rand() % n;
    j = rand() % n;
    lead[i][j]='9';
}

}
void printArr (char a[n][n]) {
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cout<<a[i][j]<<' ';
        }
        cout<<endl;
    }
}

void find_number (char lead[n][n])
{
    int i,j,c;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(lead[i][j]!='9')
            {
            c=0;
            if((i+1<n)&&(j+1<n))
            {if(lead[i+1][j+1]=='9')
                c++;}
                if(j+1<n)
            {if(lead[i][j+1]=='9')
                c++;}
                if(i+1<n)
                {if(lead[i+1][j]=='9')
                c++;}
                if(i-1>=0)
                {
                    if(lead[i-1][j]=='9')
                c++;
                if(j+1<n)
                    {if(lead[i-1][j+1]=='9')
                c++;}
                }
                if(j-1>=0)
                {
                    if(lead[i][j-1]=='9')
                c++;
                if(i+1<n)
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

void put_flag (char map[n][n], int i, int j){
    map[i][j]='^';
}

void show (int i,int j,char map[n][n],char lead[n][n])
{
if((lead[i][j]=='0')&&(map[i][j]!='0'))
{map[i][j]=lead[i][j];
    if(i+1<n){
        show (i+1,j,map,lead);
        }
    else{
        map[i][j]=lead[i][j];
        }

    if(j+1<n){
        show (i,j+1,map,lead);
    }
    else{
        map[i][j]=lead[i][j];
        }

    if((i+1<n)&&(j+1<n)){
        show (i+1,j+1,map,lead);
    }
    else{
        map[i][j]=lead[i][j];
        }

    if(i-1>=0){
        show (i-1,j,map,lead);
    }
    else{
        map[i][j]=lead[i][j];
        }

    if(j-1>=0){
        show (i,j-1,map,lead);
    }
    else{
        map[i][j]=lead[i][j];
        }

    if((i-1>=0)&&(j-1>=0)){
        show (i-1,j-1,map,lead);
    }
    else{
        map[i][j]=lead[i][j];
        }

     if((i+1<n)&&(j-1>=0)){
         show (i+1,j-1,map,lead);
     }
    else{
        map[i][j]=lead[i][j];
        }
    
    if((i-1>=0)&&(j+1<n)){
        show (i-1,j+1,map,lead);
    }
    else{
        map[i][j]=lead[i][j];
        }

}

else
    {
        map[i][j]=lead[i][j];
    }
}


void gameover (int i,int j,int &flag,char lead [n][n]){
    // if clicked on bomb!
    if (lead[i][j]==57){
            flag=1;
        cout<<endl<<"Game Over! :("<<endl;
        for (int i=0; i<n; i++)
            {
        for (int j=0; j<n; j++)
        {
            cout<<lead[i][j]<<' ';
        }
        cout<<endl;
    }
    }
}

void win (char map[n][n],int &flag,char lead[n][n])
{
    // if he have won the game;
    int c=0;
    for (int i=0; i<n; i++)
        {
        for (int j=0; j<n; j++)
        {
            if (map[i][j]=='*'||map[i][j]=='^')
            c++;
        }
    }
    if (c==m)
        {
            flag=1;
        cout<<endl<<"You won the game! :)"<<endl;
     for (int i=0; i<n; i++)
            {
        for (int j=0; j<n; j++)
        {
            cout<<lead[i][j]<<' ';
        }
        cout<<endl;
    }

    }
}

