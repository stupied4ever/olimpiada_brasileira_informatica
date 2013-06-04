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

    def atender(self, cliente):
        espera = max([0, self.ocupado_ate - cliente.t])

        self.ocupado_ate = cliente.t + espera + cliente.d
        return espera

class Banco():
    def __init__(self, entrada=sys.stdin):
        total_caixas, total_clientes = entrada.readline().split(" ")
        total_caixas, total_clientes = int(total_caixas), int(total_clientes)

        self.caixas = [Caixa() for i in range(total_caixas)]
        self.clientes = [Cliente(entrada.readline()) for linha in range(total_clientes)]

    def numero_clientes_insatisfeitos(self):
        esperar = 0

        for cliente in self.clientes:
            if self.__iniciar_atendimento(cliente) > 20:
                esperar = esperar + 1

        return esperar

    def __iniciar_atendimento(self, cliente):
        return self.__proximo_caixa_livre().atender(cliente)

    def __proximo_caixa_livre(self):
        return min(self.caixas,key=attrgetter('ocupado_ate'))

if __name__ == '__main__':
    print Banco().numero_clientes_insatisfeitos()
