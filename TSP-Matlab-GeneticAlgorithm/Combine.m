function nextGen = Combine(elits,childs,population_num,elit_num,cities_Num)
    nextGen = zeros(population_num,cities_Num);
    %assigning
    nextGen(1:elit_num,:) = elits(1:end,:);
    nextGen(elit_num+1:end,:) = childs(1:end,:);
end