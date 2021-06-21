class Fabryki:
    def fabryka1(self,cena1,cena2,wartosc1,wartosc2,poziom,hajs):
        pobor=(cena1*wartosc1*poziom)+hajs*poziom
        produkcja=(wartosc2*cena2*poziom)
        return produkcja-pobor,wartosc1*poziom,wartosc2*poziom

    def fabryka2(self,cena1,cena2,cena3,wartosc1,wartosc2,wartosc3,poziom,hajs):
        pobor=(cena1*wartosc1*poziom)+(cena2*wartosc2*poziom)+poziom*hajs
        produkcja=(wartosc3*cena3*poziom)
        return produkcja-pobor,poziom*wartosc1,poziom*wartosc2,poziom*wartosc3
    def fabryka3(self,cena1,cena2,cena3,cena4,wartosc1,wartosc2,wartosc3,wartosc4,poziom,hajs):
        pobor=(cena1*wartosc1*poziom)+(wartosc2*poziom*cena2)+(wartosc3*poziom*cena3)+poziom*hajs
        produkcja=(cena4*poziom*wartosc4)
        return produkcja-pobor,poziom*wartosc1,poziom*wartosc2,poziom*wartosc3,poziom*wartosc4

