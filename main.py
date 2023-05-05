import random


class Color:
    """
    Cores ASCII
    """
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


class CaraACara:
    def __init__(self):
        """
        Init que tem as informações iniciais com a escolha de modo de jogo e os getters e setters.
        """
        print("======== ESCOLHA UM MODO DE JOGO ========")
        print("[1] - Famosos")
        print("[2] - Veículos")

        op = int(input("Sua escolha: "))

        if op == 1:
            self.__tema = "Famosos"
            self.__palavras = {
                "Elon Musk": ["Tá lançando Foguete", "Fundador da SpaceX", "CEO da Tesla", "Bilionário", "Defensor da colonização de Marte"],
                "Oprah": ["Apresentadora", "Produtora", "Bilionária", "Filantropa", "Possui um clube do livro"],
                "Obama": ["Ex-presidente dos EUA", "Nobel da Paz", "Autor de livros", "Advogado", "Foi professor de direito"],
                "Beyonce": ["Cantora", "Dançarina", "Compositora", "Atriz", "Mulher mais bem paga da indústria da música em 2014"],
                "Stephen Hawking": ["Físico", "Cosmólogo", "Autor de livros", "Professor de matemática", "Defensor da exploração espacial"],
                "Beckham": ["Jogador de futebol", "Modelo", "Embaixador da UNICEF", "Empresário", "Marido de Victoria Beckham"],
                "Lebron James": ["Jogador de basquete", "Ativista", "Empresário", "Vencedor de quatro títulos da NBA", "Comentarista esportivo"],
                "Pelé": ["Jogador de futebol", "Conhecido como Rei do Futebol", "Nasceu em Três Corações - MG", "Venceu 3 Copas do Mundo pela Seleção Brasileira", "Considerado um dos maiores jogadores da história"],
                "Neymar": ["Jogador de futebol", "Começou a carreira no Santos", "Atualmente joga no Paris Saint-Germain", "Conhecido por suas habilidades e dribles", "Já venceu a Liga dos Campeões da UEFA"],
                "Ayrton Senna": ["Piloto de Fórmula 1", "Bateu o coco", "Venceu três campeonatos mundiais de F1", "Faleceu em um acidente durante o GP de San Marino em 1994", "Considerado um dos maiores pilotos da história"],
                "Ana Maria Braga": ["Apresentadora de TV", "Conhecida pelo programa Mais Você", "Já trabalhou em diversas emissoras de televisão", "É conhecida por seu bordão 'Acorda, menina!'", "Também já lançou alguns livros de culinária"],
                "Chico Buarque": ["Cantor e compositor", "Nasceu no Rio de Janeiro - RJ", "Já lançou diversos álbuns e canções", "Famoso por suas letras engajadas e críticas sociais", "Também é escritor e já lançou alguns livros"],
                "Ronaldo Fenomeno": ["Jogador de futebol", "Jogou em diversos clubes famosos", "Venceu duas Copas do Mundo pela Seleção Brasileira", "Famoso por suas habilidades com a bola e finalizações precisas", "Atualmente trabalha como empresário"],
                "Cazuza": ["Cantor e compositor", "Nasceu no Rio de Janeiro - RJ", "Já lançou diversos álbuns solo e com a banda Barão Vermelho", "Famoso por suas letras poéticas e músicas de protesto", "Faleceu em decorrência da AIDS em 1990"],
        }
        elif op == 2:
            self.__tema = "Veículos"
            self.__palavras = {
                "Ford Mustang": ["Carro esportivo americano icônico", "Apresentado em 1964", "Design agressivo", "Potência do motor V8", "Disponível em várias cores"],
                "Harley Davidson": ["Marca americana de motocicletas", "Fundada em 1903","Som característico do motor V-Twin", "Estilo clássico e nostálgico","Usada em filmes de estrada"],
                "Ferrari": ["Fabricante de carros esportivos italianos", "Fundada em 1947 por Enzo Ferrari","Símbolo de luxo e velocidade", "Modelos incluem o 488 GTB, F8 Tributo e SF90 Stradale","Famosa por competir na Fórmula 1"],
                "BMW": ["Fabricante alemã de carros de luxo", "Fundada em 1916","Slogan 'A última máquina de direção'", "Modelos incluem o Série 3, Série 5 e X5","Inovações tecnológicas como o sistema iDrive"],
                "Ducati": ["Marca italiana de motocicletas", "Fundada em 1926", "Foco em desempenho e estilo","Modelos incluem a Panigale V4, Multistrada V4 e Diavel 1260","Sucesso em corridas de motociclismo"],
                "Jeep Wrangler": ["Veículo off-road americano icônico", "Design quadrado e robusto","Tração nas quatro rodas","Conhecido por sua capacidade de atravessar terrenos difíceis","História remonta ao Jeep original usado na Segunda Guerra Mundial"],
                "Yamaha R1": ["Motocicleta esportiva japonesa", "Famosa por sua velocidade e desempenho","Motor de quatro cilindros em linha", "Design agressivo","Atualizações regulares para manter-se competitiva no mercado"],
                "Audi RS7": ["Sedan esportivo alemão", "Potência do motor V8 biturbo", "Design elegante e moderno", "Tecnologia avançada como tração nas quatro rodas quattro e Virtual Cockpit", "Modelo mais potente da linha Audi A7"],
                "Kawasaki Ninja": ["Marca japonesa de motocicletas esportivas", "Design aerodinâmico","Famosa por sua velocidade e manobrabilidade","Modelos incluem a ZX-6R, ZX-10R e H2R","Usada em competições de corrida de motociclismo"],
                "Chevrolet Camaro": ["Carro esportivo americano", "Apresentado em 1966","Design muscular e agressivo", "Modelos incluem o SS, ZL1 e Z/28","Famoso por aparecer em filmes como Transformers"],
                "Toyota Supra": ["Carro esportivo japonês", "Introduzido em 1978","Famoso pelo desempenho e dirigibilidade", "Modelos incluem o MKIII e MKIV","Design aerodinâmico e elegante"]
            }

        self.__palavra_secreta = ""
        self.__dicas = []
        self.__tentativas = 5
        self.__chute = ""
        self.__dica_atual = 0

    @property
    def get_palavra_secreta(self):
        """
        Getter que pega a palavra/coisa e retorna.
        :return: Palavra/Coisa
        """
        return self.__palavra_secreta

    @property
    def get_dicas(self):
        """
        Getter de dicas.
        :return: Dicas
        """
        return self.__dicas

    def gerar_palavra(self):
        """
        Ele gera/escolhe a palavra embaralando elas e escolhendo uma.
        :return: Palavra
        """
        self.__palavra_secreta = random.choice(list(self.__palavras.keys()))

    def gerar_dicas(self):
        """
        Ele pega e embaralha a dica de acordo com a palavra escolhida.
        :return: Dicas
        """
        self.__dicas = random.sample(self.__palavras[self.__palavra_secreta], 5)

    def acertou(self):
        """
        Função que verifica se o input do usuário corresponde a palavra escolhida.
        :return: Se ele acertou ou não.
        """
        if self.__palavra_secreta == self.__chute:
            return True
        return False
    
    def jogar(self):
        """
        Função principal que executa toda a lógica do jogo.
        """
        self.gerar_palavra()
        self.gerar_dicas()       
        print(f"\n{Color.DARKCYAN}------------------------------------------------------------{Color.RESET}") 
        print(f"{Color.BLUE}===== JOGO DO CARA A CARA ====={Color.RESET}")
        print(f"{Color.BOLD}Descubra quem é você em {self.__tentativas} tentativas{Color.RESET}")
        print(f"{Color.BOLD}O tema é:{Color.RESET} {Color.BLUE}{self.__tema}{Color.RESET}")
        print(f"\n{Color.BOLD}Quem Sou eu?!{Color.RESET}")
        while not self.acertou() and self.__tentativas > 0:
            print(f"\n{Color.YELLOW}Dica: {self.__dicas[self.__dica_atual]}{Color.RESET}")
            self.__dica_atual += 1
            try:
                self.__chute = input(f"\n{Color.PURPLE}Quem você acha que é?: {Color.RESET}").title().strip()
            except:
                self.__chute = input(
                    f"\n{Color.PURPLE}Entrada inválida. Tente novamente: {Color.RESET}").title().strip()
            
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
                                                                                   
