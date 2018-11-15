
class Pojazd():
    marka = ''
    model = ''
    pojemnosc = 0
    konieMechaniczne = 0 # ZMIENNE
 
    def __init__(self, marka, model, pojemnosc, konieMechaniczne): # konstruktor - metoda wywolywana zawsze przy tworzeniu objektu danej klasy
        self.marka = marka
        self.model = model
        self.pojemnosc = pojemnosc
        self.konieMechaniczne = konieMechaniczne
 
    def pokazCoToZaMarka(self): # METODA
        print("marka tego pojazdu to: {}".format(self.marka))
 
    def pokazSrednieSpalanie(self): # zwykla metoda
        print("srednie spalanie")
 
        sredniaSpalania = self.obliczSrednieSpalanie()
 
        print(sredniaSpalania)
 
        print("litr/100 km")
 
    def obliczSrednieSpalanieNaMiescie(self, srednieSpalanie):
        return (srednieSpalanie * 1.4);
 
 
class Samochod(Pojazd):
    def obliczSrednieSpalanie(self):
        return (self.konieMechaniczne / self.pojemnosc)
 
class Autobus(Pojazd):
    def obliczSrednieSpalanie(self):
        return (self.konieMechaniczne * 0.8 / (self.pojemnosc / 2))
 
    def obliczSrednieSpalanieNaMiescie(self):
        srednieSpalanie = 80
        srednieSpalanieNaMiescie = super(Autobus, self).obliczSrednieSpalanieNaMiescie(srednieSpalanie)
        srednieSpalanieNaMiescie = srednieSpalanieNaMiescie * 1.9
 
        print(srednieSpalanieNaMiescie)
 
 
nowyPojazd = Samochod('BMW', 'E49', 3.2, 320)
 
nowyPojazd.pokazCoToZaMarka()
 
nowyPojazd.pokazSrednieSpalanie()
 
drugiPojazd = Samochod('BWM', 'M3', 6.2, 750)
 
drugiPojazd.pokazCoToZaMarka()
 
drugiPojazd.pokazSrednieSpalanie()
drugiPojazd.obliczSrednieSpalanieNaMiescie(67)
 
autobus = Autobus('Solaris', 'M5000', 24.0, 400)
 
autobus.pokazCoToZaMarka()
 
autobus.pokazSrednieSpalanie()
autobus.obliczSrednieSpalanieNaMiescie()
