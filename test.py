import unittest
from delivery import *
from pedidos import *
from loja import *
from motoboy import *

moto1 = Motoboy('João', 2, None, None)
moto2 = Motoboy('Carlos', 2, None, None)
moto3 = Motoboy('Alberto', 2, None, None)
moto4 = Motoboy('Bruna', 2, 'Magazine', None)
moto5 = Motoboy('Luiza', 3, None, None)

pedido1_loja1 = Pedido(50, 'pedido1')
pedido2_loja1 = Pedido(50, 'pedido2')
pedido3_loja1 = Pedido(50, 'pedido3')

pedido1_loja2 = Pedido(50, 'pedido1')
pedido2_loja2 = Pedido(50, 'pedido2')
pedido3_loja2 = Pedido(50, 'pedido3')
pedido4_loja2 = Pedido(50, 'pedido4')

pedido1_loja3 = Pedido(50, 'pedido1')
pedido1_loja3 = Pedido(50, 'pedido2')
pedido1_loja3 = Pedido(100, 'pedido3')

pedidos_loja1 = Pedidos([pedido1_loja1, pedido2_loja1, pedido3_loja1])
pedidos_loja2 = Pedidos([pedido1_loja2, pedido2_loja2,
                        pedido3_loja2, pedido4_loja2])
pedidos_loja3 = Pedidos([pedido1_loja3, pedido1_loja3, pedido1_loja3])

loja1 = Loja('Magazine', pedidos_loja1, 5)
loja2 = Loja('Americanas', pedidos_loja2, 5)
loja3 = Loja('Casas Bahia', pedidos_loja3, 15)


mock_teste1 = {
    'nome_loja': 'Magazine',
    'nome_motoboy': 'Bruna',
    'quantidade_pedidos': 3,
    'valor_rececbido_pelo_motoboy': 4.5
}

mock_teste2 = {'nome_loja': 'Magazine', 'nome_motoboy': 'João',
               'quantidade_pedidos': 2, 'valor_rececbido_pelo_motoboy': 4.5} 

mock_teste3 = {'nome_loja': 'Americanas', 'nome_motoboy': 'Carlos',
               'quantidade_pedidos': 4, 'valor_rececbido_pelo_motoboy': 4.5}  

mock_teste4 = {'nome_loja': 'Magazine', 'nome_motoboy': 'João',
               'quantidade_pedidos': 1, 'valor_rececbido_pelo_motoboy': 9.0} 

mock_teste5 = {'nome_loja': 'Casas Bahia', 'nome_motoboy': 'Alberto',
               'quantidade_pedidos': 3, 'valor_rececbido_pelo_motoboy': 47.0} 


class MyTest(unittest.TestCase):
    def test_exclusive_motoboy(self):
        self.assertEqual(executa_entrega(loja1, moto4), mock_teste1)
    
    def test_non_exclusive_motoboy(self):
        self.assertEqual(executa_entrega(loja1, moto1), mock_teste2)

    def test_non_exclusive_motoboy_another_store(self):
        self.assertEqual(executa_entrega(loja2, moto2), mock_teste3)

    def test_non_exclusive_motoboy_another_get_all_items(self):
        self.assertEqual(executa_entrega(loja1, moto1, True), mock_teste4)

    def test_non_exclusive_motoboy_another_store_all_items(self):
        self.assertEqual(executa_entrega(loja3, moto3, True), mock_teste5)


if __name__ == '__main__':
    unittest.main()
