class Pedidos():
    def __init__(self, lista_pedidos):
        self._pedidos = lista_pedidos

    def __iter__(self):
        return iter(self._pedidos)

    def __len__(self):
        return len(self._pedidos)