function childs = CreateCrossovers(selectedParents,elit_num,currentGeneration,cities_Num,citiesDistances)
    numOfChilds = elit_num*4;
    childs = nan(numOfChilds,cities_Num);
    childNum = 1;
    for iter=1:elit_num
        par1idx = selectedParents(iter,1);
        par2idx = selectedParents(iter,2);
        par3idx = selectedParents(iter,3);
        par1 = currentGeneration(par1idx,:);
        par2 = currentGeneration(par2idx,:);
        par3 = currentGeneration(par3idx,:);

        %cross over p1, p2
        selChild = CrossOver2Par(par1,par2,cities_Num,citiesDistances);
        childs(childNum,:) = selChild(1,:);
        childNum = childNum+1;

        %cross over p2,p3
        selChild = CrossOver2Par(par2,par3,cities_Num,citiesDistances);
        childs(childNum,:) = selChild(1,:);
        childNum = childNum+1;

        %cross over p1,p3
        selChild = CrossOver2Par(par1,par3,cities_Num,citiesDistances);
        childs(childNum,:) = selChild(1,:);
        childNum = childNum+1;
        
        %cross over p1,p2,p3
        selChild = CrossOver3Par(par1,par2,par3,cities_Num,citiesDistances);
        childs(childNum,:) = selChild(1,:);
        childNum = childNum+1;

    end

end