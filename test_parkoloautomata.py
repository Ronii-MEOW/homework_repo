import unittest
from datetime import datetime as dt
from parkoloautomata import OradijJegy, NapiJegy

class TestOradijJegy(unittest.TestCase):
    def test_egy_ora(self):
        jegy = OradijJegy("M2", "MEOW-842",dt.strptime("08:00", "%H:%M"),dt.strptime("09:00", "%H:%M"))
        self.assertEqual(jegy.ar_szamitasa(), 500)

    def test_25_perc(self):
        jegy = OradijJegy("M2","MEOW-842",dt.strptime("08:00", "%H:%M"),dt.strptime("08:25", "%H:%M"))
        self.assertEqual(jegy.ar_szamitasa(), 500)

    def test_egy_ora_egy_perc(self):
        jegy = OradijJegy("M2","MEOW-842",dt.strptime("08:00", "%H:%M"),dt.strptime("08:01", "%H:%M"))
        self.assertEqual(jegy.ar_szamitasa(), 800)

    def test_harom_ora(self):
        jegy = OradijJegy("M2","MEOW-842",dt.strptime("08:00", "%H:%M"),dt.strptime("11:00", "%H:%M"))
        self.assertEqual(jegy.ar_szamitasa(), 1100)

    def test_het_ora_47_perc(self):
        jegy = OradijJegy("M2", "MEOW-842", dt.strptime("08:00", "%H:%M"), dt.strptime("15:47", "%H:%M"))
        self.assertEqual(jegy.ar_szamitasa(), 2500)

    def test_nyolc_ora(self):
        jegy = OradijJegy("M2","MEOW-842",dt.strptime("08:00", "%H:%M"),dt.strptime("16:00", "%H:%M"))
        self.assertEqual(jegy.ar_szamitasa(), 2500)