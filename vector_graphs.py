import matplotlib.pyplot as plt
import numpy as np

# Angle calculation
def kut(alfa):
  alfa_deg = (alfa * np.pi) /180
  i = np.cos(alfa_deg) * U
  j = np.sin(alfa_deg) * U

  return i,j

# Vector graph

plt.figure(figsize=(10,10))

#Osi i,y
plt.quiver(-8, 0, 16,0, scale_units='xy', angles = 'xy', scale =1, color = 'black',linewidths=0.5, edgecolors='k')
plt.quiver(0, -3, 0,16, scale_units='xy', angles = 'xy', scale =1, color = 'black',linewidths=0.5, edgecolors='k')
plt.text(0, 13, r"  j", ha='left', va= 'top' , fontsize= 20)
plt.text(8, -0.5, r"  i", ha='left', va= 'top' , fontsize= 20)

#Primarna strana
plt.quiver(0, 0, 5.25,9.093, scale_units='xy', angles = 'xy', scale =1, color = 'b', linewidths=2, edgecolors='b')
plt.quiver(0,0,-5.25,9.093,  scale_units='xy', angles = 'xy', scale =1 , color = 'g',linewidths=2, edgecolors='g')
plt.quiver(-5.25,9.093,5.25*2,0, scale_units='xy', angles = 'xy', scale =1 , color = 'r',linewidths=2, edgecolors='r')

plt.text(5.25, 9.093, r"  $\overline{U_1}$<-30°", ha='left', va= 'top' , fontsize= 20)
plt.text(-5.25,9.093, r"$\overline{U_2}$<+30°  ", ha='right', va= 'top' , fontsize= 20)
plt.text(1, 10.5, r"$\overline{\Delta E}$ = $\overline{U_1}$ - $\overline{U_2}$", ha='left', va= 'top' , fontsize= 20)

plt.xlim(-9,9)
plt.ylim(-4,14)
plt.grid()
plt.show()
