from AbstractControladorJogo import *
from Personagem import Personagem
from Carta import Carta
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        super(ControladorJogo, self).__init__()
        self._baralho = []
        self._personagens = []

    '''
    Retorna o baralho
    @return o baralho
    '''
    @property
    def baralho(self) -> list:
        return self._baralho

    '''
    Retorna a lista de personagems
    @return a lista de personagems
    '''
    @property
    def personagems(self) -> list:
        return self._personagens

    '''
    Permite incluir um novo Personagem na lista de personagens do jogo
    @param energia Energia do novo Personagem
    @param habilidade Habilidade do novo Personagem
    @param velocidade Velocidade do novo Personagem
    @param resistencia Resistencia do novo Personagem
    @param tipo TipoPersonagem (Enum) do novo Personagem.
    Deve ser utilizado TipoPersonagem.TIPO
    @return Retorna o Personagem incluido na lista
    '''
    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        self._personagens.append(Personagem(energia, habilidade, velocidade,
                                            resistencia, tipo))
        return self._personagens[-1]

    '''
     Permite incluir uma nova Carta no baralho do jogo
     @param personagem Personagem da nova carta que sera incluida
     @return Retorna a Carta que foi incluida no baralho
     '''
    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        self._baralho.append(Carta(personagem))
        return self._baralho[-1]

    '''
    Inicia o jogo, distribuindo aleatoriamente 5 cartas do baralho
    para cada jogador, a distribuicao nao precisa ser aleatoria

    @param jogador1 Jogador 1
    @param jogador2 Jogador 2
    '''
    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        cartas_placeholder = self._baralho[:]
        for _ in range(5):
            carta1 = random.randint(0, len(cartas_placeholder) - 1)
            jogador1.cartas.append(carta1)
            cartas_placeholder.remove(carta1)
            carta2 = random.randint(0, len(cartas_placeholder) - 1)
            jogador2.cartas.append(carta2)
            cartas_placeholder.remove(carta2)

    '''
     Realiza uma jogada, ou seja:
     1. Recebe a mesa onde estao as cartas lancadas pelo Jogador 1
     e pelo Jogador 2
     2. Compara os valores totais das cartas dos jogadores que estao
     na mesa
     3. Apos comparacao:

     O jogador que ganhar a rodada recebe a carta do jogador perdedor
     sendo assim ele deve chamar o metodo inclui_carta_na_mao para as
     duas cartas que estao na mesa

     Caso ocorra empate ambos os jogadores devem chamar o metodo
     inclui_carta_na_mao com suas respectivas cartas da mesa

     4.Ao final do metodo o jogador que estiver com a mao vazia
     perde o jogo, caso ambos ainda tenham cartas na mao retorne
     None para indicar que por enquanto ninguem venceu o jogo.

     @param mesa Mesa atual, contendo: Jogador 1, Jogador 2,
     Carta do Jogador 1 e Carta do Jogador 2
     @return Retorna o Jogador vencedor da rodada.
     Caso ocorra empate entre os jogadores, retorna None
    '''
    def jogada(self, mesa: Mesa) -> Jogador:
        if (mesa._cartaJogador1.valor_total_carta()
            >
                mesa._cartaJogador2.valor_total_carta()):
            mesa._jogador1.inclui_carta_na_mao(mesa._cartaJogador1)
            mesa._jogador1.inclui_carta_na_mao(mesa._cartaJogador2)
        elif (mesa._cartaJogador1.valor_total_carta()
                <
                mesa._cartaJogador2.valor_total_carta()):
            mesa._jogador2.inclui_carta_na_mao(mesa._cartaJogador1)
            mesa._jogador2.inclui_carta_na_mao(mesa._cartaJogador2)
        else:
            mesa._jogador1.inclui_carta_na_mao(mesa._cartaJogador1)
            mesa._jogador2.inclui_carta_na_mao(mesa._cartaJogador2)

        if mesa._jogador1.mao and mesa._jogador2.mao:
            return None
        elif mesa._jogador1.mao:
            return mesa._jogador1
        elif mesa._jogador2.mao:
            return mesa._jogador2
        else:
            return None
