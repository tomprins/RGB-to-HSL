###########################
##   Author: Tom Prins   ##
###########################

#!!RGB and HSL values are given from 0-1, and the hue values from 0–360°!!

def RGBtoHSL(r, g, b):
    # cmin becomes the lowest, and cmax becomes the highest value of r, g and b
    cmin = min(r, g, b)
    cmax = max(r, g, b)

    # The hue is determined by which color has the lowest, and which has the highest value
    if r == cmax and b == cmin:
        h = ((g-cmin)/(cmax-cmin))*60
    elif g == cmax and b == cmin:
        h = ((g-cmin)/(cmax-cmin))*60 + 60
    elif g == cmax and r == cmin:
        h = ((g-cmin)/(cmax-cmin))*60 + 120
    elif b == cmax and r == cmin:
        h = ((g-cmin)/(cmax-cmin))*60 + 180
    elif b == cmax and g == cmin:
        h = ((g-cmin)/(cmax-cmin))*60 + 240
    else:
        h = ((g-cmin)/(cmax-cmin))*60 + 300

    # The saturation is calculated by the following forumla
    s = (cmax-cmin)/(1-abs(cmin+cmax-1))
    # The lightness is just the middle of the cmin and cmax values
    l = (cmin + cmax)/2

    # Finally, round the values to 2 decimals, and return them
    return round(h, 2), round(s, 2), round(l, 2)


def HSLtoRGB(h, s, l):
    # Calculate the cmin and cmin, with the Saturation and Lightness
    # The cmin and cmax are needed for determining the RGB value
    cmin = l + s * abs(l-0.5)-0.5*s
    cmax = l - s * abs(l-0.5)+0.5*s

    def B(h):
        # A while loop to make sure the hue angle is between 1° and 360°
        while(h <= 0):
            h = 360 + h
        # If the hue is between certain values, return the appropriate RGB value
        if h > 0 and h <= 120:
            return cmin
        elif h > 120 and h <= 180:
            return cmin + (cmax - cmin) * ((h % 360 - 120)/60)
        elif h > 180 and h <= 300:
            return cmax
        else:
            return cmax - (cmax - cmin) * ((h % 360 - 300)/60)

    # Finally, round the values to 2 decimals, and return them
    return (round(B(h-120), 2), round(B(h+120), 2), round(B(h), 2))


print("RGB to HSL:", RGBtoHSL(0.4, 0.5, 0.6))  # (210.0, 0.2, 0.5)
print("HSL to RGB:", HSLtoRGB(100, 0.5, 0.6))  # (0.533, 0.8, 0.4)
