import pickle
from modules.pajamu_irasas import PajamuIrasas
from modules.islaidu_irasas import IslaiduIrasas

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_zurnala()

    def gauti_zurnala(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
                return zurnalas
        except:
            zurnalas = []
            return zurnalas

    def irasyti_zurnala(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamas(self):
        suma = float(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def prideti_islaidas(self):
        suma = float(input("Suma: "))
        budas = input("Atsiskaitymo būdas: ")
        isigyta = input("Įsigyta prekė/paslauga: ")
        irasas = IslaiduIrasas(suma, budas, isigyta)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        return suma

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)