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

lista_kuteva = np.array(range(676)).reshape((26, 26)) 

for i in range(len(grupa_spoja)):
  alfa1 = (float(grupa_spoja[i][1])*30)
  for j in range(len(grupa_spoja)):
    alfa2 = (float(grupa_spoja[j][1])*30)
    alfa = alfa2-alfa1
    lista_kuteva[i][j] = np.abs(alfa)

index =['Yy0', 'Dd0', 'Dz0', 'Yd1', 'Dy1', 'Dz1', 'Dd2', 'Dz2', 'Dd4', 'Dz4', 'Yd5', 'Dy5', 'Yz5', 'Yy6', 'Dd6', 'Dz6', 'Yd7', 'Dy7', 'Yz7', 'Dd8', 'Dz8', 'Dd10', 'Dz10', 'Yd11', 'Dy11', 'Yz11']

df = pd.DataFrame(lista_kuteva, columns= index, index=index)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

display(df)

#Razlika potencija delta E

matrica_razlike_napona = np.array(range(676)).reshape((26, 26))
matrica_razlike_napona = matrica_razlike_napona.astype('float64')

D_E = 0

for i in range(len(lista_kuteva)):
  for j in range(len(lista_kuteva)):
    kut_alfa = float(lista_kuteva[i][j])
    if kut_alfa > 180.0:
      kut_alfa = np.abs(kut_alfa-360.0)
    D_E = round(np.sin((kut_alfa/2.0)* np.pi/180)*U_sek*2.0, 4)
    #print(D_E)
    matrica_razlike_napona[i][j] = D_E

df = pd.DataFrame(matrica_razlike_napona, columns= index, index=index).astype(float)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.precision', 4)
#display(df)

#df.style.set_properties(**{'background-color': 'white',
                           #'color': 'black',
                           #'border-color': 'black',
                           #'border-width': '1px',
                           #'border-style': 'solid'})

df.style.apply(lambda x: ["background: orange" if v > 0 else "" for v in x], axis = 1)

display(df)

#print (df.dtypes)
