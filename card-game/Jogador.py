from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        super(Jogador, self).__init__()
        self._nome = nome
        self._cartas = []

    '''
    @return Retorna o nome do jogador
    '''
    @property
    def nome(self) -> str:
        return self._nome

    '''
    Retira uma das cartas do Jogador. Esta operacao eh utilizada para realizar uma jogada (baixar uma carta na mesa)
    A carta sai da mao (ou seja, a carta sai da lista das cartas que o jogador possui)
    @return Retorna a Carta que foi retirada da mao do jogador (lista das cartas que ele possui)
    '''
    def baixa_carta_da_mao(self) -> Carta:
        carta_removida = self._cartas[random.randint(0, len(self._cartas)-1)]
        self._cartas.remove(carta_removida)
        return carta_removida


    '''
    @return Retorna a mao atual do jogador (lista das cartas que ele possui)
    '''
    @property
    def mao(self) -> list:
        return self._cartas

    '''
    Inclui na mao do jogador a carta passada como parametro
    @param carta Carta que sera incluida na mao do jogador
    '''
    def inclui_carta_na_mao(self, carta:Carta):
        self._cartas.append(carta)
