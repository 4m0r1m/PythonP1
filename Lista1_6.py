direcaop1 = input()
numerop1 = int(input())
direcaop2 = input()
corp2 = input()
plantp2 = input()
macanetap2 = input()
direcaop3 = input()
corp3 = input()
numerop3 = int(input())
plantp3 = input()
macanetap3 = input()
direcaop4 = input()
numerop4 = int(input())
corp5 = input()
numerop5 = int(input())
plantap5 = input()
florp5 = input()
macanetap5 = input()
cont = 0
dporta1 = ""
dporta2 = ""
dporta3 = ""
dporta4 = ""
dporta5 = ""
if (numerop1 % 2) == 0:
  if direcaop1 == "esquerda":
    cont += 150
    dporta1 += "CERTA"
  else:
    cont -= 150
    dporta1 += "ERRADA"
if (numerop1 % 2) != 0:
  if direcaop1 == "direita":
    cont += 150
    dporta1 += "CERTA"
  else:
    cont -= 150
    dporta1 += "ERRADA"
if (corp2 == "dourada" or corp2 == "prateada") or ((plantp2 == "avenca" or plantp2 == "espadinha") and (macanetap2 == "redonda")):
  if direcaop2 == "direita":
    cont += 200
    dporta2 += "CERTA"
  else:
    cont -= 200
    dporta2 += "ERRADA"
else:
  if direcaop2 == "esquerda":
    cont += 200
    dporta2 += "CERTA"
  else:
    cont -= 200
    dporta2 += "ERRADA"
if (((numerop3 % 5) == 0) and (plantp3 == "espadinha") and (macanetap3 == "quadrada")) or (corp3 == "perolada"):
  if direcaop3 == "esquerda":
    cont += 250
    dporta3 += "CERTA"
  else:
    cont -= 250
    dporta3 += "ERRADA"
else:
  if direcaop3 == "direita":
    cont += 250
    dporta3 += "CERTA"
  else:
    cont -= 250
    dporta3 += "ERRADA"
if ((numerop4 % 3) == 0) and ((numerop4 % 2) != 0) and ((numerop4 % 5) != 0):
  if direcaop4 == "direita":
    cont += 300
    dporta4 += "CERTA"
  else:
    cont -= 300
    dporta4 += "ERRADA"
else:
  if direcaop4 == "esquerda":
    cont += 300
    dporta4 += "CERTA"
  else:
    cont -= 300
    dporta4 += "ERRADA"
if (corp5 =="acobreada" and ((numerop5 % 2) != 0)) or macanetap5 == "triangular" or macanetap5 =="quadrada" and plantap5 == "jiboia":
  cont += 500
  dporta5 += "CERTA"
elif (corp5 == "prateada") and (florp5 != "margarida" or florp5 != "papoula" or florp5 != "cosmos") and (macanetap5 == "hexagonal" or macanetap5 == "redonda"):
  cont += 450
  dporta5 += "CERTA"
elif (corp5 == "dourada") and (florp5 == "lirio" or florp5 == "ixora") and (macanetap5 == "hexagonal"):
  cont += 400
  dporta5 += "CERTA"
else:
  cont -= 500
  dporta5 += "ERRADA"
print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")
print(f"{dporta1} {dporta2} {dporta3} {dporta4} {dporta5}")
if (cont > 0) and (dporta1 == "CERTA" and dporta2 == "CERTA" and dporta3 == "CERTA" and dporta4 == "CERTA" and dporta5 == "CERTA"):
  print(f"Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {cont} pontos!")
elif(cont > 0) and (dporta1 == "ERRADA" or dporta2 == "ERRADA" or dporta3 == "ERRADA" or dporta4 == "ERRADA" or dporta5 == "ERRADA"):
  print(f"Você passou com {cont} pontos, mas faça melhores escolhas da próxima vez.")
elif (cont < 0) and ( dporta1 == "ERRADA" and dporta2 == "ERRADA" and dporta3 == "ERRADA" and dporta4 == "ERRADA" and dporta5 == "ERRADA"):
  print(f"Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {cont} pontos.")
elif (cont < 0) and (dporta1 == "ERRADA" or dporta2 == "ERRADA" or dporta3 == "ERRADA" or dporta4 == "ERRADA" or dporta5 == "ERRADA"):
  print(f"Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {cont} pontos")