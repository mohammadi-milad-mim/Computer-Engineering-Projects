void find_number (int a[10][10])
{
    int i,j,c;
    for(i=0;i<10;i++)
    {
        for(j=0;j<10;j++)
        {
            if(a[i][j]!=9)
            {
            c=0;
            if(a[i+1][j+1]==9)
                c++;
            if(a[i][j+1]==9)
                c++;
                if(a[i+1][j]==9)
                c++;
                if(i-1>=0)@@ -0,0 +1,38 @@
#include <iostream>
using namespace std;
#include <stdlib.h>
#include <time.h>

const int n=30;
const int m=100;

void printArr (char map[n][n]) {
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cout<<map[i][j]<<' ';
        }
        cout<<endl;
    }
}
void bombRandom (char map[n][n]) {
int i, j;
for (i=0; i<n; i++){
    for (j=0; j<n; j++){
        map[i][j]='0';
    }
}

srand(time(NULL));
for (int t=0; t<m; t++){
    i = rand() % n;
    j = rand() % n;
    map[i][j]='9';
}
}
