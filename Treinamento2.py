
x = int(input())
z = int(input())
hogs = float(((x - 34)**2 + (z - 220)**2)**(1/2))
kaka = float(((x - 0)**2 + (z - 0)**2)**(1/2))
soli = float(((x - 140)**2 + (z - 456)**2)**(1/2))
print(f"Distancia para Hogsmeade: {hogs:.2f}")
print(f"Distancia para Kakariko: {kaka:.2f}")
print(f"Distancia para Solitude: {soli:.2f}")