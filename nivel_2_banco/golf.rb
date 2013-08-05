c,i=gets.split;c=[0]*c.to_i;p ('1'..i).select{h,a=gets.split.map &:to_i;e=[0,c.min-h].max;c.sort![0]=h+e+a;e>20}.count
