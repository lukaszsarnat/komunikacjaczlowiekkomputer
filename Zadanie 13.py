import pandas as pd
import aseegg as ag
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("sub-01_trial-08.csv", engine='python',header=None,names=("ABCDEF"))

t = np.linspace (0, 37.913, 200*37.913)
sygnal=dane["B"]
liczby=dane["F"]
index=dane["A"]
przefiltrowanySygnal1=ag.pasmowozaporowy(sygnal, 200, 49,51)
przefiltrowanySygnal2=ag.pasmowoprzepustowy(przefiltrowanySygnal1, 200, 1,50)
#indexing pozwala na pobieranie tylko jednej liczby z wielu ponad-progowych próbek
indexing=-500
for i in range(len(przefiltrowanySygnal2)):
    if przefiltrowanySygnal2[i]>0.05:
        if indexing+150<=i:
            indexing=i
            print(liczby[i])

f2 = plt.figure(figsize=(8, 12))
plot1=plt.subplot(3,1,1)
plot1.plot(t, sygnal)
plot1.set_ylabel("Amplituda [mV]")
plot1.set_xlim(0,38)
plot3=plt.subplot(3,1,2)
plot3.plot(t, przefiltrowanySygnal2)
plot3.set_ylabel("Amplituda [mV]")
plot3.set_xlim(0,38)
plot4=plt.subplot(3,1,3)
plot4.plot(t, liczby)
plot4.set_xlabel("Czas [s]")
plot4.set_ylabel("Wyświetlana liczba")
plot4.set_xlim(0,38)
plot4.set_ylim(0.5,5.5)
plt.show()
