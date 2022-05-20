from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        super(Personagem, self).__init__()
        self._energia = energia
        self._habilidade = habilidade
        self._velocidade = velocidade
        self._resistencia = resistencia
        self._tipo = tipo

    @property
    def tipo(self) -> Tipo:
        return self._tipo

    @property
    def energia(self) -> int:
        return self._energia

    @property
    def habilidade(self) -> int:
        return self._habilidade

    @property
    def velocidade(self) -> int:
        return self._velocidade

    @property
    def resistencia(self) -> int:
        return self._resistencia
