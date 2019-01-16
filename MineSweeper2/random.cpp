#include <iostream>
using namespace std;
#include <stdlib.h>
#include <time.h>

const int n=30;
const int m=100;


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
