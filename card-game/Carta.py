from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        super(Carta, self).__init__()
        self._personagem = personagem

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:
        energ = self._personagem.energia
        veloc = self._personagem.velocidade
        habil = self._personagem.habilidade
        resis = self._personagem.resistencia
        return energ + habil + veloc + resis

    @property
    def personagem(self) -> Personagem:
        return self._personagem
