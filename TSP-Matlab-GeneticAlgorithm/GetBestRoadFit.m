function [bests,theBest] = GetBestRoadFit(genBestRoadsFit,allTimeFit,sortFits,gen)
    tmp = sortFits(1,1);
    genBestRoadsFit(gen,1)=tmp;
    if tmp<allTimeFit
        theBest = tmp;
    else
        theBest = allTimeFit;
    end
    bests = genBestRoadsFit;
end