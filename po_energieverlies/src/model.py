import math

m = 0.102
r = 0.026
g = 9.81
rho = 1.293
cwl = 0.47
cwr = 0.0008

maxt = 3
i = 0.001

def calculate(angle, d):
    # Constanten
    theta = math.radians(angle)

    # Variabelen
    t = 0
    s = 0
    v = 0
    a = 0

    array_t = []
    array_s = []
    array_v = []

    while s < d and t < maxt:
        a = (5/7)*(g*math.sin(theta)
                        - (cwl*rho*math.pi*(math.pow(r,2))*(math.pow(v,2)))/(m)
                        - cwr*g*math.cos(theta)
                        )
        v += a*i
        s += v*i
        t += i

        array_t.append(t)
        array_s.append(s)
        array_v.append(v)

    final = {
        "TotalTime" : t,
        "Time" : array_t,
        "Distance" : array_s,
        "Velocity" : array_v,
    }

    return final
    