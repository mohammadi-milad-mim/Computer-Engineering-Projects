function sel = Selection(sortOrder,elit_num)
       sel = zeros(elit_num,3);
       valids = sortOrder(1:elit_num*5);
       for i=1:elit_num
           sel(i,:) = randsample(valids, 3);
       end
end