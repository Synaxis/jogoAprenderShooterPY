import unittest
from jogo import colisao

class TesteColisao(unittest.TestCase):

    def test_colisao_verdadeira(self):
        self.assertTrue(colisao(10,10,15,15))

    def test_colisao_falsa(self):
        self.assertFalse(colisao(10,10,100,100))

    def test_limite(self):
        self.assertTrue(colisao(0,0,19,19))

if __name__ == "__main__":
    unittest.main()
