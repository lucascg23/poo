class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.idade=idade
        self.peso = peso
        self.comendo=False
        self.falando=False
        self.dormindo=False
    def falar (self):
        if self.falando:
            print("nao pode falar pois ja esta falando")
        elif self.dormindo:
            print("nao pode dormir pois ja esta dormindo")
        elif self.comendo:
            print("nao pode comer pois ja esta comendo")
        else:
            self.falando==True
            print("começou a falar")

    def comer (self):
        if self.falando:
            print("nao pode falar pois ja esta falando")
        elif self.dormindo:
            print("nao pode dormir pois ja esta dormindo")
        elif self.comendo:
            print("nao pode comer pois ja esta comendo")
        else:
            self.comendo==True
            print("começou a comer")

    def dormir(self):
        if self.dormindo == True:
            print(f"O {self.dormindo} esta dormindo")
        elif self.falando== True:
            print("nao pode dormir pq ta falando")
        elif self.comendo==True:
            print("nnão pode dormie pq ta comendo")
        else:
            print("foi dormir")
            self.dormindo = True
class ContaBancaria():
    def __init__(self, numero, nome, tipo):
        self.numero=numero
        self.nome=nome
        self.tipo=tipo


        self.saldo=0
        self.status=False

    def AtivarConta(self):
        if self.status==False:
            self.status=True
            print("ativei sua conta")
    def Depositar(self):
        if self.status==True:
            print("Deposite seu dinheito: ")
    def Sacar(self):
        if self.saldo>0:
            print(f"você tem {self.saldo} pra sacar, quanto voce deseja sacar?")
        else:
            print("Voce nao tem dinheiro pra sacar")
    def DesativarConta(self):
        if self.saldo>0:

            print(f"")
class Animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"O{self.nome}foi comer...")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar (self):
        print(f"O {self.nome} foi miando...")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def muge (self):
        print(f"O {self.nome} está mugindo ...")
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latindo (self):
        print(f"O {self.nome} está latindo ...")
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def grunindo (self):
        print(f"O {self.nome} está grunindo ...")
class Ingresso():
    def __init__(self, valor):
        self.valor=valor
    def imprimeValor(self):
        print(f"o valor é {self.valor}")
class IngressoVip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor*=1.5
    def adicional (self):
        print(f"o valor do vip é {self.valor}")
class Forma():
    def __int__(self):
        self.area=0
        self.perimetro=0
class Retangulo(Forma):
    def __init__(self):
        super().__init__()
        self.base=0
        self.altura=0
    def calculaArea(self, base, altura):
        self.area=base*altura
        print(self.area)
class Atleta():
    def __init__(self):
        self.aposentado=False
        self.peso=0
    def aponsentar (self):
        self.aposentado=True

        print("ta aposentado")

    def aquecer (self):
        print("esta aquecendo")
        self.aquecer=True
class Corredor(Atleta):
    def __init__(self):
        super().__init__()
    def correr(self):
        print("correndo")












