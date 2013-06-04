import StringIO
import unittest

from banco import Banco
import banco

class TestaFilaBanco(unittest.TestCase):
    def test_primeiro_caso_unicamp(self):
        entrada = """1 5
0 10
0 10
1 10
2 10
30 10
"""
        entrada = StringIO.StringIO(entrada)
        self.assertEqual(Banco(entrada).numero_clientes_insatisfeitos(), 1)

    def test_segundo_caso_unicamp(self):
        entrada = """3 16
0 10
0 10
0 10
3 10
5 10
7 10
11 10
13 10
14 10
15 10
16 10
17 10
18 3
19 10
20 10
23 3
"""
        entrada = StringIO.StringIO(entrada)
        self.assertEqual(Banco(entrada).numero_clientes_insatisfeitos(), 2)

if __name__ == '__main__':
    unittest.main()
