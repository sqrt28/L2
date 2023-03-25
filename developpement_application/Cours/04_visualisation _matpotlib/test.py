import matplotlib.pyplot as plt

temps = [1,2,3,4,5,6,7]
concentration = [5.5,7.2,11.8,13.6,19.1,21.7,29.4]
plt.scatter(temps,concentration, marker = "o", color = "blue")
plt.xlabel("Temps(h)")
plt.ylabel("concentration (mg/L")
plt.title("concentration de produit en fonction du temps")
plt.show()
