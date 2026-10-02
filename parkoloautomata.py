class ParkoloJegy:
    def __init__(self,hely,rendszam,belepes_ido,kilepes_ido):
        self.hely = hely
        self.rendszam = rendszam
        self.belepes_ido = belepes_ido
        self.kilepes_ido = kilepes_ido
class OradijJegy(ParkoloJegy):
    def ar_szamitasa(self):
            pass

class NapiJegy(ParkoloJegy):
    def ar_szamitasa(self):
        pass


