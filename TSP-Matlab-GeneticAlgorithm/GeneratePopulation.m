function population = GeneratePopulation(population_num,cities_Num)
%we should be careful of not to make circular same pathes
    population = zeros(population_num,cities_Num);
    for i=1:population_num
        population(i,:) = randperm(cities_Num);
    end
end