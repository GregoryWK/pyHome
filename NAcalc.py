#Numerical Aperature Calculator
import numpy as np

n0 = 1
anglMax = 45
angl_rad = np.radians(anglMax)
NA = n0*np.sin(angl_rad)

print({NA})