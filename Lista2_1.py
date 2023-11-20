cont = 0
contmusicas = 0
musica = ""
if musica == "long live":
    print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {contmusicas} músicas.")
    contmusicas += 1
while ((cont >= 0) and (musica != "long live")):
  musica = str(input())
  if musica == "os fãs estão formando uma ciranda":
    cont -= 3
    if cont < 0:
        print(f"A Taylor só conseguiu cantar {contmusicas} músicas e a sessão foi interrompida.")
  elif (musica == "os fãs estão ligando os flashes e atrapalhando a visão") or (musica == "os fãs estão dançando na frente da tela") or (musica == "os fãs estão gritando o nome da Taylor e atrapalhando a música"):
    cont -= 2
    if cont < 0:
        print(f"A Taylor só conseguiu cantar {contmusicas} músicas e a sessão foi interrompida.")
  elif (musica == "os fãs estão cantando as músicas em coro") or (musica == "houve um pedido de casamento na sessão"):
    cont += 2
  elif cont < 0:
    print(f"A Taylor só conseguiu cantar {contmusicas} músicas e a sessão foi interrompida.")
    musica += "long live"
  elif musica == "long live":
      contmusicas += 1
      print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {contmusicas} músicas.")
  else:
    contmusicas += 1
    cont += 1
print (cont)