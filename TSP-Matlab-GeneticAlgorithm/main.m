clear;
clc;

%% Cities Declaration and Distances
cities_Num = 6;
citiesLocations = GetCitiesLocations();
citiesDistances = CalcCitiesDistances(cities_Num,citiesLocations);
allTimeFit = 1000000000;


%% Initializing Parameters
parametersList = GetParameters();
population_num = parametersList(1,1);
generations_num = parametersList(1,2);
crossover_rate = parametersList(1,3);
mutation_occurrence_rate = parametersList(1,4);
mutation_rate = parametersList(1,5);
elit_num = population_num/5;
elit_num2 = elit_num/4;

%% Genetic Main
repeat_num = 1;
%best fitness and time of each round
result_Round = nan(repeat_num,2);
%stat parameters
for rep=1:repeat_num
    population = GeneratePopulation(population_num,cities_Num);
    nextGeneration = population;
    genBestRoadsFit = nan(generations_num + 1, 1);
    tic;
    for gen=1:generations_num
        currentGeneration = nextGeneration;
        generation_fitness = CalcFitness(currentGeneration,citiesDistances,population_num,cities_Num);
        [sortFits, sortOrder] = sort(generation_fitness);

        [genBestRoadsFit,allTimeFit] = GetBestRoadFit(genBestRoadsFit,allTimeFit,sortFits,gen);
        minRoadCost = (genBestRoadsFit(gen,1));
        fprintf('Minimum path in %d. generation: %f \n', gen,minRoadCost);
        visualizeGeneration(citiesLocations, currentGeneration, sortFits, sortOrder,gen);
        [crossover_flag,mutation_flag] = GetStatus(crossover_rate,mutation_occurrence_rate);
        if crossover_flag
           %make child from elits
           genTop20per = Top20per(sortOrder,currentGeneration,population_num,cities_Num,elit_num);
           selectedTop20per = Selection(sortOrder,elit_num2);
           childsTop20per = CreateCrossovers(selectedTop20per,elit_num2,currentGeneration,cities_Num,citiesDistances);
           %make child from others
           selectedParents = Selection(sortOrder,elit_num);
           childs = CreateCrossovers(selectedParents,elit_num,currentGeneration,cities_Num,citiesDistances);
           %combine these two
           nextGeneration = Combine(childsTop20per,childs,population_num,elit_num,cities_Num);
        else
            nextGeneration = currentGeneration;
        end
    
        if mutation_flag
            nextGeneration = Mutation(nextGeneration,mutation_rate);
        end
    end
    %last time fitness and best calculation
    result_Round(rep,1)=allTimeFit;
    result_Round(rep,2)=toc;
    disp(result_Round(rep,2));
end

