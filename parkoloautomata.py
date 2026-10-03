from datetime import datetime as dt
from colorama import Fore, Style,init

def keret(fuggveny):
    def belso(self):
        print(Fore.LIGHTCYAN_EX+ "─────────────────── ᯓ⛟ ─────────────────────")
        fuggveny(self)
        print(Fore.LIGHTCYAN_EX + "─────────────────── ᯓ⛟ ─────────────────────" + Style.RESET_ALL)
    return belso

class ParkoloJegy:
    def __init__(self,hely,rendszam,belepes_ido,kilepes_ido):
        self.hely = hely
        self.rendszam = rendszam
        self.belepes_ido = belepes_ido
        self.kilepes_ido = kilepes_ido

    @keret
    def kiir(self):
        print("PARKOLÓJEGY")
        print("Parkolóhely:", self.hely)
        print("Rendszám:", self.rendszam)
        print("Belépés:", self.belepes_ido.strftime("%H:%M"))
        print("Kilépés:", self.kilepes_ido.strftime("%H:%M"))
        print("Fizetendő:", self.ar_szamitasa(), "Ft")


class OradijJegy(ParkoloJegy):
    def ar_szamitasa(self):
           parkolas_idotartam = self.kilepes_ido - self.belepes_ido
           parkolas_perc = parkolas_idotartam.seconds // 60
           parkolas_ora = parkolas_perc // 60
           if parkolas_perc % 60 != 0:
               parkolas_ora += 1
           if parkolas_ora <= 1:
               return 500
           ar = 500 + (parkolas_ora - 1) * 300
           if ar > 2500:
               return 2500
           return ar

class NapiJegy(ParkoloJegy):
    def ar_szamitasa(self):
        return 2500


def main():
    while True:
        print(Fore.LIGHTCYAN_EX + "─────────────────── ᯓ⛟ ─────────────────────" + Style.RESET_ALL)
        print("PARKOLÓAUTOMATA")
        print(Fore.LIGHTCYAN_EX + "─────────────────── ᯓ⛟ ─────────────────────" + Style.RESET_ALL)
        hely =input("Parkolóhely: ")
        rendszam = input("Rendszám: ")
        belepes = input("Belépés ideje (ÓRA:PERC): ")
        kilepes = input("Kilépés ideje (ÓRA:PERC): ")
        belepes_ido = dt.strptime(belepes, "%H:%M")
        kilepes_ido = dt.strptime(kilepes, "%H:%M")
        print(Fore.LIGHTCYAN_EX + "─────────────────── ᯓ⛟ ─────────────────────" + Style.RESET_ALL)
        print("Milyen jegyet szeretnél?")
        print("1. Óradíjas jegy")
        print("2. Napijegy")

        valasztas = input("Választás: ")
        match valasztas:
            case "1":
                jegy =OradijJegy(hely,rendszam,belepes_ido,kilepes_ido)
            case "2":
                jegy = NapiJegy(hely,rendszam,belepes_ido,kilepes_ido)
            case _:
                print("Nincs ilyen menüpont, számot adj meg! (1 / 2)")
                return
        jegy.kiir()


