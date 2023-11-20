numero = int(input())
local1 = input()
local2 = input()
local3 = input()
numeroL1 = len(local1)
numeroL2 = len(local2)
numeroL3 = len(local3)
if numero == 1:
  if numeroL1 > numeroL2 and numeroL1 > numeroL3:
    print(local1)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
  elif numeroL2 > numeroL1 and numeroL2 > numeroL3:
    print(local2)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
  elif numeroL3 > numeroL1 and numeroL3 > numeroL1:
    print(local3)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
  else:
    print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
    if local1 > local2 and local1 > local3:
      print(local1)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif local2 > local1 and local2 > local3:
      print(local2)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif local3 > local2 and local3 > local1:
      print(local3)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    else:
      print('"AAAAAA! Um fantasma me assustou!"')
      print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')
elif numero == 2:
  if numeroL1 < numeroL2 and numeroL1 < numeroL3:
    print(local1)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
  elif numeroL2 < numeroL1 and numeroL2 < numeroL3:
    print(local2)
    print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
  elif numeroL3 < numeroL1 and numeroL3 < numeroL2:
    print(local3)
    print('Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
  else:
    print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
    if local1 > local2 and local1 > local3:
      print(local1)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif local2 > local1 and local2 > local3:
      print(local2)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    elif local3 > local2 and local3 > local1:
      print(local3)
      print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
    else:
      print('"AAAAAA! Um fantasma me assustou!"') 
      print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')
print('(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)')