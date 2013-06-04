import re
import sys

class Cliente():
    def __init__(self, line):
        self.t, self.d = line.split(" ")
        self.t, self.d = int(self.t), int(self.d)

def identifica_index_menor_espera( caixas ):
    return caixas.index(min(caixas))

def numero_clientes_insatisfeitos(entrada=sys.stdin):
    banco = entrada.readline().split(" ")
    quando_fica_livre = [0] * int(banco[0])
    clientes = int(banco[1])

    limite_espera = 20
    esperar = 0

    for x in xrange(clientes):
        cliente = Cliente(entrada.readline())

        proximo_livre = identifica_index_menor_espera(quando_fica_livre)

        espera = max([0, quando_fica_livre[proximo_livre] - cliente.t])

        quando_fica_livre[proximo_livre] = cliente.t + espera + cliente.d

        if espera > limite_espera:
            esperar = esperar + 1

    return esperar

