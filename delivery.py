from pedido import *
from pedidos import *
from loja import *
from motoboy import *


def executa_entrega(loja, motoboy=None, entregar_todos=False):
    if motoboy is None and loja is None:
        print("Não foi fornecido motoboy ou loja para executar a função.")
        return

    data = {
            'nome_loja': loja._nome,
            'nome_motoboy': '',
            'quantidade_pedidos': 0,
            'valor_rececbido_pelo_motoboy': 0
        }

    if loja:
        print(f'O nome da loja é {loja._nome}.')
        if loja._pedidos is None:
            print('Não há mais produtos na loja para entregas.')
            return data
        print(f'{len(loja._pedidos)} é a quantidade total de pedidos para entrega.')
        data['quantidade_pedidos'] = len(loja._pedidos)

        if motoboy:
            print(f'{motoboy._nome} é o motoboy para essa entrega.')
            data['nome_motoboy'] = motoboy._nome
            if entregar_todos:
                loja.entrega_todos_pedidos(motoboy)
                print(
                    f'O valor que o motoboy recebeu pelas entregas foi de R${motoboy.valor_recebido:0.2f}')
                data['valor_rececbido_pelo_motoboy'] = motoboy.valor_recebido
            else:
                loja.entrega_um_pedido(motoboy)
                print(
                    f'O valor que o motoboy recebeu pelas entregas foi de R${motoboy.valor_recebido:0.2f}')
                data['valor_rececbido_pelo_motoboy'] = motoboy.valor_recebido

        else:
            print('Não foi recebido nenhum motoboy.')
    
    return data
