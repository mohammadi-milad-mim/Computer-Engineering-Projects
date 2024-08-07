function distances = CalcCitiesDistances(cities_Num,citiesLocations)
%Maybe the distance between each cities should be given
%And also maybe there is no road from two specific cities
%It can be manhatan distance

    distances = zeros(cities_Num);
    for i=1:cities_Num
        for j=1:cities_Num
            %Bases on
            x = abs(citiesLocations(i,1)-citiesLocations(j,1));
            y = abs(citiesLocations(i,2)-citiesLocations(j,2));
            distances(i,j)=sqrt((x)^2 + (y)^2);
        end
    end
    %Dont need to calculate all the table, just calculate the top then
end