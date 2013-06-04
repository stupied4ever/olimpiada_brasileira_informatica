import re
import sys
from operator import attrgetter

class Cliente():
    def __init__(self, line):
        self.t, self.d = line.split(" ")
        self.t, self.d = int(self.t), int(self.d)

class Caixa():
    def __init__(self):
        self.ocupado_ate = 0

    @staticmethod
    def proximo_livre(caixas):
        return min(caixas,key=attrgetter('ocupado_ate'))

def identifica_index_menor_espera( caixas ):
    return caixas.index(min(caixas))

def numero_clientes_insatisfeitos(entrada=sys.stdin):
    banco = entrada.readline().split(" ")
    caixas_abertos = [Caixa() for i in range(int(banco[0]))]
    quando_fica_livre = [0] * int(banco[0])
    clientes = int(banco[1])

    limite_espera = 20
    esperar = 0

    for x in xrange(clientes):
        cliente = Cliente(entrada.readline())

        # proximo_livre = identifica_index_menor_espera(quando_fica_livre)
        proximo_caixa_livre = Caixa.proximo_livre(caixas_abertos)

        espera = max([0, proximo_caixa_livre.ocupado_ate - cliente.t])

        proximo_caixa_livre.ocupado_ate = cliente.t + espera + cliente.d

        if espera > limite_espera:
            esperar = esperar + 1

    return esperar

