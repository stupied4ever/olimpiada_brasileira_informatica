class AutoCorretor
  def distancia(de, ate)
    return 0 if de == ate
    return de.size  if ate.nil? || ate.empty?
    return ate.size if de.nil?  || de.empty?
    distancia = 0

    if de.size != ate.size
      menor, maior = [de,ate].sort{|a,b| a.size <=> b.size}
      diferenca = maior.size - menor.size
      if [maior[0...diferenca], menor].flatten.join == maior
        distancia += diferenca
      end
      if [menor, maior.reverse[0...diferenca].reverse].flatten.join == maior
        distancia += diferenca
      end
    end

    return distancia
  end
end
