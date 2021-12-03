class Motoboy:
    def __init__(self, nome, taxa_entrega, exclusividade, pedidos_recebidos):
        self._nome = nome
        self._taxa_entrega = taxa_entrega
        self._exclusividade = exclusividade
        self._pedidos_recebidos = pedidos_recebidos
        self._valor_recebido = 0.0

    @property
    def pedidos_recebidos(self):
        return self._pedidos_recebidos

    @pedidos_recebidos.setter
    def pedidos_recebidos(self, pedidos):
        self._pedidos_recebidos = pedidos

    @property
    def valor_recebido(self):
        return self._valor_recebido

    @valor_recebido.setter
    def valor_recebido(self, valor):
        self._valor_recebido = self._valor_recebido + valor