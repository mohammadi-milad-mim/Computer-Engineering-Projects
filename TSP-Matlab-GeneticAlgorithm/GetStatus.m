function [crossover, mutation] = GetStatus(crossover_rate,mutation_rate)
    randNum = randi(100);
    if crossover_rate > randNum
        crossover = true;
    else
        crossover = false;
    end
    if mutation_rate > randNum
        mutation = true;
    else
        mutation = false;
    end
end