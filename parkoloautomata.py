from datetime import datetime as dt





class ParkoloJegy:
    def __init__(self,hely,rendszam,belepes_ido,kilepes_ido):
        self.hely = hely
        self.rendszam = rendszam
        self.belepes_ido = belepes_ido
        self.kilepes_ido = kilepes_ido
class OradijJegy(ParkoloJegy):
    def ar_szamitasa(self):
           parkolas_idotartam = self.belepes_ido - self.kilepes_ido
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




