"""Klasse Rechteck mit den Attributen Laenge und Breite"""

# Rechteck mit den Attribute Laenge und Breite wird instanziert
class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

# flache berechnet die Flaeche des Rechtecks
    def flaeche(self):
        return self.laenge * self.breite

# umfang berechnet den Umfang
    def umfang(self):
        return 2 * self.laenge + 2 * self.breite

# Instanz des Rechtecks anlegen
re = Rechteck(7, 5)

# Flaeche und Umfang ausgeben
print('Die Fläche beträgt: ' + str(re.flaeche()))
print('Der Umfang beträgt: ' + str(re.umfang()))
