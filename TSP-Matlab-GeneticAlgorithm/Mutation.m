function nextGen = Mutation(nextGeneration,mutation_rate)
    [population_num,cities_Num] = size(nextGeneration);

    for i=1:population_num
        randNum = randi(100,1,1);
        if randNum < mutation_rate
            while 1
                randIdx1 = randi(cities_Num);
                randIdx2 = randi(cities_Num);
                if ~(randIdx1 == randIdx2)
                    [nextGeneration(i,randIdx1),nextGeneration(i,randIdx2)] = Swap(nextGeneration(i,randIdx1),nextGeneration(i,randIdx2));
                    break;
                end
            end
        end
    end
    nextGen = nextGeneration;

end