class Loja:
    def __init__(self, nome, pedidos, comissao):
        self._nome = nome
        self._pedidos = pedidos
        self._comissao = comissao

    @property
    def pedidos(self):
        return self._pedidos

    @pedidos.setter
    def pedidos(self, pedidos):
        self._pedidos = pedidos

    def entrega_um_pedido(self, motoboy):
        motoboy_exclusivo = self.valida_exclusividade(motoboy)
        if motoboy_exclusivo:
            self.executa_entrega(motoboy)
        if motoboy._exclusividade is None:
            self.executa_entrega(motoboy)

    def executa_entrega(self, motoboy):
        lista_pedidos = [pedido for pedido in self._pedidos]
        pedido = lista_pedidos[-1]
        nova_lista = lista_pedidos[0:-1]
        motoboy.pedidos_recebidos = pedido
        self.efetua_pagamento([pedido], motoboy)
        self.pedidos = nova_lista

    def valida_exclusividade(self, motoboy):
        if motoboy._exclusividade == self._nome:
            return True
        return False

    def entrega_todos_pedidos(self, motoboy):
        lista_pedidos = [pedido for pedido in self.pedidos]
        motoboy.pedidos_recebidos = lista_pedidos
        self.efetua_pagamento(lista_pedidos, motoboy)
        self._pedidos = None

    def efetua_pagamento(self, pedidos, motoboy):
        valor_pagamento = motoboy._taxa_entrega
        for pedido in pedidos:
            valor_pagamento += (pedido._valor * self._comissao)/100
        motoboy.valor_recebido = valor_pagamento