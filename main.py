import random

class CaraACara:
    def __init__(self):
        self.__palavras = {
            "computador": ["Eletrônico", "Tem tela", "Usado para trabalho e lazer", "Processa informações", "Tem periféricos"],
            "bicicleta": ["Meio de transporte", "Tem rodas", "Não usa combustível", "Pode ser de várias cores", "Tem guidão"],
            "avião": ["Meio de transporte", "Voa", "Tem asas", "Pode ser comercial ou militar", "Pode ter janelas"],
            "girafa": ["Animal", "Tem pescoço comprido", "Vive na savana", "Tem manchas na pelagem", "Alcança folhas de árvores altas"],
            "piano": ["Instrumento musical", "Tem teclas", "Produz som", "Pode ser de cauda ou vertical", "Frequentemente é preto ou branco"]
        }
        self.__palavra_secreta = ""
        self.__dicas = []
        self.__tentativas = 5
        self.__chute = ""
        
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
        while not self.acertou() and self.__tentativas > 0:
            print("Tente acertar!")
            
            print("\nDicas: ")
            for dica in self.__dicas:
                print(dica)
                
            self.__chute = input("Digite seu chute: ").lower()
        
        if self.acertou():
            print("\nParabéns! Você acertou a palavra secreta '{}'.".format(self.__palavra_secreta))
        else:
            print("\nSuas tentativas acabaram! A palavra secreta era '{}'.".format(self.__palavra_secreta))
            
jogo = CaraACara()
jogo.jogar()
