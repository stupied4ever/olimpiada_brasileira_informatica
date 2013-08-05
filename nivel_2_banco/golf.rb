c,n=gets.split.map{|x|[0]*x.to_i};p n.select{t,d=gets.split.map &:to_i;e=[0,c.min-t].max;c.sort![0]=t+e+d;e>20}.count
