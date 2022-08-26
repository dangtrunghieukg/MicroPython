def map(x_in, inMin, inMax, outMin, outMax):
    return int((x_in - inMin)*(outMax - outMin) / (inMax - inMin)) + outMin
