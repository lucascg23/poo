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







