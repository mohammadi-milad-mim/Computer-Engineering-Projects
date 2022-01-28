function fit = CalcFitness(currentGeneration,citiesDistances,population_num,cities_Num)
    %roadCosts = zeros(population_num,1);
    fit = ones(population_num,1);
    for p=1:population_num
        fit(p) = CalcSingleFit(currentGeneration(p,:),cities_Num,citiesDistances);
    end
end