#include <iostream>
using namespace std;

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