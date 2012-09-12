from jarray import array
import java.awt.Color as Color


def getPoints(attack_color, defend_color):
    #print attack_color
    ha, sa, va = Color.RGBtoHSB(attack_color[0],attack_color[1],attack_color[2],None)
    hd, sd, vd = Color.RGBtoHSB(defend_color[0],defend_color[1],defend_color[2],None)
    #if hd > 0.5:
    #   hd = 1-hd
    #return abs(ha-hd)
    return min(abs(ha-hd),1-abs(ha-hd))

c1 = (255,0,0)
c2 = (255,255,0)

print getPoints(c1, c2)
print getPoints(c2, c1)

