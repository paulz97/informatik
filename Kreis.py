"""Klasse Kreis mit dem Attribut Radius"""

# Kreis mit dem Attribut radius wird instanziert
class Kreis:
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius

# flache berechnet die Flaeche des Kreise
    def flaeche(self):
        return self.radius * self.radius * Kreis.pi

# umfang berechnet den Umfang
    def umfang(self):
        return 2 * self. radius * Kreis.pi

# Instanz des Kreises anlegen
kr = Kreis(9)

# Flaeche und Umfang ausgeben
print('Die Fläche beträgt: ' + str(kr.flaeche()))
print('Der Umfang beträgt: ' + str(kr.umfang()))

