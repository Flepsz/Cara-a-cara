import random


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\33[m'

# improve the class
class CaraACara:
    def __init__(self):
        self.__palavras = {
            "Elon Musk": ["Tá lançando Foguete", "Fundador da SpaceX", "CEO da Tesla", "Bilionário", "Defensor da colonização de Marte"],
            "Oprah": ["Apresentadora", "Produtora", "Bilionária", "Filantropa", "Possui um clube do livro"],
            "Obama": ["Ex-presidente dos EUA", "Nobel da Paz", "Autor de livros", "Advogado", "Foi professor de direito"],
            "Beyonce": ["Cantora", "Dançarina", "Compositora", "Atriz", "Mulher mais bem paga da indústria da música em 2014"],
            "Stephen Hawking": ["Físico", "Cosmólogo", "Autor de livros", "Professor de matemática", "Defensor da exploração espacial"],
            "Beckham": ["Jogador de futebol", "Modelo", "Embaixador da UNICEF", "Empresário", "Marido de Victoria Beckham"],
            "Lebron James": ["Jogador de basquete", "Ativista", "Empresário", "Vencedor de quatro títulos da NBA", "Comentarista esportivo"],
            "Pelé": ["Jogador de futebol", "Conhecido como Rei do Futebol", "Nasceu em Três Corações - MG", "Venceu 3 Copas do Mundo pela Seleção Brasileira", "Considerado um dos maiores jogadores da história"],
            "Bolsonaro": ["Não é coveiro", "Ex-presidente do Brasil", "Imbroxável", "Tem histórico de atleta", "Bluepill"],
            "Lula": ["Gosta de uma cachacinha", "Ex-presidiário", "Eleito em 2002 e reeleito em 2006", "Foi metalúrgico antes de entrar na política", "Tem um dedo a menos"],
            "Neymar": ["Jogador de futebol", "Começou a carreira no Santos", "Atualmente joga no Paris Saint-Germain", "Conhecido por suas habilidades e dribles", "Já venceu a Liga dos Campeões da UEFA"],
            "Ayrton Senna": ["Piloto de Fórmula 1", "Bateu o coco", "Venceu três campeonatos mundiais de F1", "Faleceu em um acidente durante o GP de San Marino em 1994", "Considerado um dos maiores pilotos da história"],
            "Ana Maria Braga": ["Apresentadora de TV", "Conhecida pelo programa Mais Você", "Já trabalhou em diversas emissoras de televisão", "É conhecida por seu bordão 'Acorda, menina!'", "Também já lançou alguns livros de culinária"],
            "Chico Buarque": ["Cantor e compositor", "Nasceu no Rio de Janeiro - RJ", "Já lançou diversos álbuns e canções", "Famoso por suas letras engajadas e críticas sociais", "Também é escritor e já lançou alguns livros"],
            "Ronaldo Fenomeno": ["Jogador de futebol", "Jogou em diversos clubes famosos", "Venceu duas Copas do Mundo pela Seleção Brasileira", "Famoso por suas habilidades com a bola e finalizações precisas", "Atualmente trabalha como empresário"],
            "Cazuza": ["Cantor e compositor", "Nasceu no Rio de Janeiro - RJ", "Já lançou diversos álbuns solo e com a banda Barão Vermelho", "Famoso por suas letras poéticas e músicas de protesto", "Faleceu em decorrência da AIDS em 1990"],
        }
        self.__palavra_secreta = ""
        self.__dicas = []
        self.__tentativas = 5
        self.__chute = ""
        self.__dica_atual = 0
        
    def get_palavra_secreta(self):
        return self.__palavra_secreta

    def get_dicas(self):
        return self.__dicas

    def gerar_palavra(self):
        self.__palavra_secreta = random.choice(list(self.__palavras.keys()))

    def gerar_dicas(self):
        self.__dicas = random.sample(self.__palavras[self.__palavra_secreta], 5)

    def acertou(self):
        if self.__palavra_secreta == self.__chute:
            return True
        return False
    
    def jogar(self):
        
        self.gerar_palavra()
        self.gerar_dicas()       
        print(f"\n{Color.DARKCYAN}------------------------------------------------------------{Color.RESET}") 
        print(f"{Color.BLUE}===== JOGO DO CARA A CARA ====={Color.RESET}")
        print(f"{Color.BOLD}Descubra quem é você em {self.__tentativas} tentativas{Color.RESET}")
        print(f"{Color.BOLD}O tema é:{Color.RESET} {Color.BLUE}Famosos{Color.RESET}")
        print(f"\n{Color.BOLD}Quem Sou eu?!{Color.RESET}")
        while not self.acertou() and self.__tentativas > 0:
            print(f"\n{Color.YELLOW}Dica: {self.__dicas[self.__dica_atual]}{Color.RESET}")
            self.__dica_atual += 1
                
            self.__chute = input(f"\n{Color.PURPLE}Quem você acha que é?: {Color.RESET}").title().strip()
            # while not self.__chute.isalpha():
            #     self.__chute = input(f"\n{Color.PURPLE}Entrada inválida. Tente novamente: {Color.RESET}").title().strip()
            
            if not self.acertou():
                print(f"{Color.BOLD}Palavra Incorreta!{Color.RESET}")
                self.__tentativas -= 1
        
        if self.acertou():
            print(f"\n{Color.GREEN}Parabéns! Você acertou! Você era o(a) {''.join(self.__palavra_secreta)}.{Color.RESET}")
        else:
            print(f"\n{Color.RED}Suas tentativas acabaram! Você era o(a) {''.join(self.__palavra_secreta)}.{Color.RESET}")
            
        print(f"{Color.DARKCYAN}------------------------------------------------------------{Color.RESET}")


jogo = CaraACara()
jogo.jogar()
                                                                                   