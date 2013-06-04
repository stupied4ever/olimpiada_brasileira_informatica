import re
import sys

def identifica_index_menor_espera( caixas ):
    return caixas.index(min(caixas))


banco = sys.stdin.readline().split(" ")
quando_fica_livre = [0] * int(banco[0])
clientes = int(banco[1])

limite_espera = 20
esperar = 0

for x in xrange(clientes):
    cliente = sys.stdin.readline().split(" ")
    chegou = int(cliente[0])
    atendimento = int(cliente[1])

    proximo_livre = identifica_index_menor_espera( quando_fica_livre )

    espera = max([0, quando_fica_livre[proximo_livre] - chegou])

    quando_fica_livre[proximo_livre] = chegou + espera + atendimento

    if espera > limite_espera:
        esperar = esperar + 1

print esperar

