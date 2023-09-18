import time
nombre = int(input("Quel nombre voulez-vous élevez à la puissance ? "))
puissance = int(input("A quelle puissance voulez-vous l'élevez ? "))
start = time.time_ns()
print(nombre ** puissance)
end = time.time_ns() - start
print (end)