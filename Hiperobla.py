centro = (0,0)
vertices = [(0,0), (0,0)]
focos = [(0,0), (0,0)]
asintotas =
semimayor =
semimenor =
c = ((a^2) + (b^2))^(1/2)
#c distancia del centro al foco
#a distancia centro y vertice

#y = asintotas
#las asintotas son dos lineas rectas que se aproximan a la hiperbola pero nunca la tocan

y = b/(a*x)
yp = -b/(a*x)

#excentricidad
e = c/a
# la excentricidad es siempre mayor a uno

class hiperoblaHor:

    def __init__(self):
        self.x =
        self.y =
        self.a =
        self.b =
        self.uno = ((x^2)/(a^2) - (y^2)/(b^2))
        self.centro = (0,0)
        self.unohk = (((x-h)^2)/(a^2) - ((y-k)^2)/(b^2))

class hiperoblaVer:

    def __init__(self):
        self.x =
        self.y =
        self.a =
        self.b =
        self.uno = ((y^2)/(a^2) - (x^2)/(b^2))
        self.centro = (0,0)
        self.unohk = (((y-k)^2)/(a^2) - ((x-h)^2)/(b^2))
