function child = CrossOver2Par(par1,par2,cities_Num,citiesDistances)

    child1 = nan(1,cities_Num);
    child2 = nan(1,cities_Num);
    %randSlice = randi(cities_Num);
    randSlice = cities_Num/2;
    child1(1:randSlice) = par2(1:randSlice);
    child2(1:randSlice) = par1(1:randSlice);
    
    child1(randSlice+1:end) = par1(~(ismember(par1,child1)));
    child2(randSlice+1:end) = par2(~(ismember(par2,child2)));

    fit1 = CalcSingleFit(child1,cities_Num,citiesDistances);
    fit2 = CalcSingleFit(child2,cities_Num,citiesDistances);

    if (fit1 < fit2)
        child = child1;
    else
        child = child2;
    end


end