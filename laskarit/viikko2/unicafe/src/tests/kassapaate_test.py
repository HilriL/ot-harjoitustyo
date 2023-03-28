import unittest

from kassapaate import Kassapaate
from maksukortti import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    # rahan määrä kassassa
    def test_rahamaara_alussa_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # myydyt maukkaat

    def test_myydyt_maukkaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # myydyt edulliset

    def test_myydyt_edulliset_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # käteinen

    def test_kateinen_edullinen_kassa_kasvaa_kun_maksu_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateinen_edullinen_vaihtoraha_oikein_kun_maksu_riittaa(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(maksu, 60)

    # maukas

    def test_kateinen_maukas_kassa_kasvaa_kun_maksu_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateinen_maukas_vaihtoraha_oikein_kun_maksu_riittaa(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(maksu, 100)

    # määrä kasvaa

    def test_kateinen_edullinen_myytyjen_maara_kasvaa_kun_maksu_riittää(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 1)


    def test_kateinen_maukas_myytyjen_maara_kasvaa_kun_maksu_riittää(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    # kassa ei muutu

    def test_kateinen_edullinen_kassa_ei_muutu_jos_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(150)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateinen_maukas_kassa_ei_muutu_jos_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(150)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # oikea vaihtoraha

        def test_kateinen_edullinen_vaihtoraha_oikein_kun_maksu_ei_riita(self):
            maksu = self.kassapaate.syo_edullisesti_kateisella(100)

            self.assertEqual(maksu, 100)

        def test_kateinen_maukas_vaihtoraha_oikein_kun_maksu_ei_riita(self):
            maksu = self.kassapaate.syo_maukkaasti_kateisella(100)

            self.assertEqual(maksu, 100)

    # lounaiden määrä ei muutu jos maksu ei riitä

        def test_kateinen_edullinen_myytyjen_maara_ei_muutu_jos_maksu_ei_riita(self):
            self.kassapaate.syo_edullisesti_kateisella(150)

            self.assertEqual(self.kassapaate.edulliset, 0)


        def test_kateinen_maukas_myytyjen_maara_ei_muutu_jos_maksu_ei_riita(self):
            self.kassapaate.syo_maukkaasti_kateisella(150)

            self.assertEqual(self.kassapaate.maukkaat, 0)





    



    





    