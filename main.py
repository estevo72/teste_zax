from delivery import *

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
print('--------------------------------')
executa_entrega(loja1, moto1)
print('--------------------------------')
executa_entrega(loja2, moto2)
print('--------------------------------')
executa_entrega(loja3, moto3)
print('--------------------------------')
executa_entrega(loja1, moto4)
print('--------------------------------')
executa_entrega(loja2, moto5)
print('--------------------------------')
executa_entrega(loja1, moto1, True)
print('--------------------------------')
executa_entrega(loja2, moto2, True)
print('--------------------------------')
executa_entrega(loja3, moto3, True)
print('--------------------------------')
executa_entrega(loja1, moto4, True)
print('--------------------------------')
teste = executa_entrega(loja2, moto5, True)
print('--------------------------------')
print(teste)

