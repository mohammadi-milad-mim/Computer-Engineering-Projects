#include <iostream>
using namespace std;
const int n=30;
const int m=100;
void delete_flag (char map[n][n], int i, int j){
    if (map[i][j]=='^')
    map[i][j]='*';
}