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
}