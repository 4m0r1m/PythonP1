local = input()
hora = int(input())
resposta = input()
if local == "Salão":
  print("Em direção ao salão!")
  horaTeste = hora - 2
  print(f"Pra chegar na hora, vou ter que sair de {horaTeste} horas.")
  if resposta == "Sim, Pearl! Siga seus sonhos!":
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
  else:
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
elif local == "Praça":
  print("Para a praça eu vou!")
  horaTeste = hora - 2
  print(f"Pra chegar na hora, vou ter que sair de {horaTeste} horas.")
  if resposta == "Sim, Pearl! Siga seus sonhos!":
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
  else:
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
elif local == "Centro da cidade":
  print("Faz tempo que não visito o centro, mal posso esperar!")
  horaTeste = hora - 1
  print(f"Pra chegar na hora, vou ter que sair de {horaTeste} horas.")
  if resposta == "Sim, Pearl! Siga seus sonhos!":
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
  else:
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
