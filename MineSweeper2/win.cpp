#include <iostream>
using namespace std;
const int n=30;
const int m=100;
void win (char map[n][n]){
    // if he have won the game;
    int c=0;
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            if (map[i][j]=='*')
            c++;
        }
    }
    if (c==m){
        cout<<endl<<"You won the game! :)";
        system("pause");
    }
    
}