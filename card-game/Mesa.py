from AbstractMesa import *
from Carta import Carta
from Jogador import Jogador


class Mesa(AbstractMesa):

    #Construtor fornecido, nao deve ser alterado
    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, cartaJogador2: Carta):
        super(Mesa, self).__init__()
        self._jogador1 = jogador1
        self._jogador2 = jogador2
        self._cartaJogador1 = cartaJogador1
        self._cartaJogador2 = cartaJogador2

    @property
    def jogador1(self) -> Jogador:
        return self._jogador1

    @property
    def jogador2(self) -> Jogador:
        return self._jogador2

    @property
    def carta_jogador1(self) -> Carta:
        return self._cartaJogador1

    @property
    def carta_jogador2(self) -> Carta:
        return self._cartaJogador2
