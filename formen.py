"""Umfang und Flaeche eines Rechtecks und eines Kreises"""

# importieren von randint
from random import randint

# rechteck mit den Attributen Laenge und Breite wird instanziert
class rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

# flaeche berechnet die Flaeche des Rechtecks
    def flaeche(self):
        return self.laenge * self.breite

# umfang berechnet den Umfang
    def umfang(self):
        return 2 * self.laenge + 2 * self.breite

# kreis mit dem Attribut Radius wird instanziert
class kreis:
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius

# flaeche berechnet die Flaeche des Kreises
    def flaeche(self):
        return self.radius * self.radius * kreis.pi

# umfang berechnet den Umfang des Kreises
    def umfang(self):
        return self.radius * 2 * kreis.pi

# Instanz des Rechtecks anlegen
re = rechteck(7, 5)

# Instanz des Kreises anlegen
kr = kreis(4)

# Flaeche und Umfang ausgeben
print('Die Fläche des Rechtecks beträgt: ' + str(re.flaeche()))
print('Die Fläche des Kreises beträgt: ' + str(kr.flaeche()))
print('Der Umfang des Rechtecks beträgt: ' + str(re.umfang()))
print('Der Umfang des Kreises beträgt: ' + str(kr.umfang()))

# generieren einer Zufallszahl
zufall = randint(1, 50)
print(zufall)
