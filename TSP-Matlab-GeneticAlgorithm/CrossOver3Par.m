function child = CrossOver3Par(par1,par2,par3,cities_Num,citiesDistances)

    child1 = nan(1,cities_Num);
    child2 = nan(1,cities_Num);
    child3 = nan(1,cities_Num);
    mid = cities_Num/2;
    randSlice1 = randi(mid-1);
    randSlice2 = randi(mid-1)+mid;
    child1(1:randSlice1) = par2(1:randSlice1);
    child2(1:randSlice1) = par1(1:randSlice1);
    child3(1:randSlice1) = par3(1:randSlice1);
    
    child1(randSlice1+1:end) = par1(~(ismember(par1,child1)));
    child2(randSlice1+1:end) = par2(~(ismember(par2,child2)));
    child3(randSlice1+1:end) = par3(~(ismember(par3,child3)));

    fit1 = CalcSingleFit(child1,cities_Num,citiesDistances);
    fit2 = CalcSingleFit(child2,cities_Num,citiesDistances);

    if (fit1 < fit2)
        child = child1;
    else
        child = child2;
    end
end