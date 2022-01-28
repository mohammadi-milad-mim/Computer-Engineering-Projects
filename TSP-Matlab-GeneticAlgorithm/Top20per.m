function nextGen = Top20per(sortOrder,currentGeneration,population_num,cities_Num,elit_num)
    nextGen = zeros(elit_num,cities_Num);
    %assigning
    for i=1:elit_num
        nextGen(i,:)=currentGeneration(sortOrder(i,1),:);
    end
end