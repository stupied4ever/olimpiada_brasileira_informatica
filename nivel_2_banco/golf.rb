c,i=gets.split;c=[0]*c.to_i;p ('1'..i).map{h,a=gets.split.map &:to_i;e=[0,c.min-h].max;c[c.index c.min]=h+e+a;e>20?1:0}.inject &:+
