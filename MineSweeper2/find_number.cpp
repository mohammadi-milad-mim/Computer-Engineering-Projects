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
