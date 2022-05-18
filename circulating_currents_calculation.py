import numpy as np
import pandas as pd

#Podaci transformatora:
#S = 8000 kVA
#Napon = 35/10.5 kV
#Pk = 53.966 kW
#uk = 7.67 %

S = 8000
Z_post = 7.67
Pk = 53.966
U_sek = 10.5 

I_sek = S/(U_sek*np.sqrt(3))
print("Struja sekundara: " + str(I_sek) +" A")

R_post = Pk / S * 100
print("%R iznosi: " + str(R_post) + " %")

def struja_izjednacenja(e_post):
  Ic_post = (e_post *100)/(np.sqrt((R_post*2)**2+(Z_post*2)**2))
  Ic = (Ic_post /100)* I_sek
  return Ic

Ic_ret = round(struja_izjednacenja(100), 2)
Ic_ret

grupa_spoja = np.array([['Yy', 0.0], ['Dd', 0], ['Dz', 0], ['Yd', 1], ['Dy', 1], ['Dz', 1], ['Dd', 2], ['Dz', 2], ['Dd', 4], ['Dz', 4], ['Yd', 5], ['Dy', 5], ['Yz', 5], ['Yy', 6], ['Dd', 6], ['Dz', 6], ['Yd',7], ['Dy', 7], ['Yz', 7], ['Dd', 8], ['Dz', 8], ['Dd', 10], ['Dz', 10], ['Yd' , 11], ['Dy', 11], ['Yz', 11]])
len(grupa_spoja)
grupa_spoja
