#include <iostream>
using namespace std;
#include <stdlib.h>
#include <time.h>

const int n=30;
const int m=100;

void printArr (char a[n][n]) {
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cout<<a[i][j]<<' ';
        }
        cout<<endl;
    }
}
void bombRandom (char a[n][n]) {
int i, j;
for (i=0; i<n; i++){
    for (j=0; j<n; j++){
        a[i][j]='0';
    }
}

srand(time(NULL));
for (int t=0; t<m; t++){
    i = rand() % n;
    j = rand() % n;
    a[i][j]='9';
}
}

int main () {
    char a[n][n];
    bombRandom (a);
    printArr (a);

}
