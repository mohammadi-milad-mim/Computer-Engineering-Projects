function fitValue = CalcSingleFit(road,cities_Num,citiesDistances)
    roadCosts = 0;
    for c=1:cities_Num
       if ~(c==cities_Num)
            roadCosts=roadCosts+citiesDistances(road(c),road(c+1));
       else
            roadCosts=roadCosts+citiesDistances(road(c),road(1));
       end
     end
     fitValue = (1/roadCosts)*1000000000;

end