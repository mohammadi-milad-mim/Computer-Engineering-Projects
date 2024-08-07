function [ output_args ] = visualizeGeneration(citiesLocations, currentGeneration, sortFits, sortOrder,gen)
%Visualizing the cities and the best finded result according to algorithm.
    minPath = sortFits(1,1);
    [length, ~] = size(citiesLocations);
    xDots = citiesLocations(:,1);
    yDots = citiesLocations(:,2);
    title('Genetic Algorithms for TSP');
    plot(xDots,yDots, 'o', 'MarkerSize', 7.5, 'MarkerFaceColor', 'blue');
    xlabel('X Dimension');
    ylabel('Y Dimension');
    axis equal
    hold on
    bestPopPath = currentGeneration(sortOrder(1,1),:);
    bestX = zeros(1,length+1);
    bestY = zeros(1,length+1);
    for j=1:length
       bestX(1,j) = citiesLocations(bestPopPath(1,j),1);
       bestY(1,j) = citiesLocations(bestPopPath(1,j),2);
    end
    bestX(1,length+1) = citiesLocations(bestPopPath(1,1),1);
    bestY(1,length+1) = citiesLocations(bestPopPath(1,1),2);
title('Genetic Algorithms for TSP');
    plot(bestX(1,:),bestY(1,:), 'red', 'LineWidth', 1.25);
    legend('Cities', 'Path');
    axis equal
    grid on
    text(-40,99,sprintf('Generation number this path was found: %d path fitness: %.2f',gen, minPath),'FontSize',10);
    drawnow
    hold off
end