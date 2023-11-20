filme1 = input()
notaL = float(input())
notaI = float(input())
filme2 = input()
notaL2 = float(input())
notaI2 = float(input())
filme3 = input()
notaL3 = float(input())
notaI3 = float(input())

if notaL > notaL2 and notaL > notaL3:
  print(f"O filme de terror escolhido foi...")
  if notaL <= 6:
      print(f"{filme1}?! Aldo provavelmente irá odiar um filme de terror com essa nota...")
  else:
    print(f"{filme1}! Esse filme de terror é maravilhoso... Aldo vai amar!")
elif notaL2 > notaL3 and notaL2 > notaL:
    print(f"O filme de terror escolhido foi...")
    if notaL2 <= 6:
      print(f"{filme2}?! Aldo provavelmente irá odiar um filme de terror com essa nota...")
    else:
      print(f"{filme2}! Esse filme de terror é maravilhoso... Aldo vai amar!")
elif notaL3 > notaL2 and notaL3 > notaL:
  print(f"O filme de terror escolhido foi...")
  if notaL3 <= 6:
    print(f"{filme3}?! Aldo provavelmente irá odiar um filme de terror com essa nota...")
  else:
    print(f"{filme3}! Esse filme de terror é maravilhoso... Aldo vai amar!")
else:
  print("Aldo continua sem saber qual filme assistir...")
  nota1 = notaL * notaI
  nota2 = notaL2 * notaI2
  nota3 = notaL3 * notaI3
  if nota1 > nota2 and nota1 > nota3:
    print(f"O filme de terror escolhido foi...")
    if notaL <= 6:
      print(f"{filme1}?! Aldo provavelmente irá odiar um filme de terror com essa nota...")
    else:
      print(f"{filme1}! Esse filme de terror é maravilhoso... Aldo vai amar!")
  elif nota2 > nota3 and nota2 > nota1:
    print(f"O filme de terror escolhido foi...")
    if notaL2 <= 6:
      print(f"{filme2}?! Aldo provavelmente irá odiar um filme de terror com essa nota...")
    else:
      print(f"{filme2}! Esse filme de terror é maravilhoso... Aldo vai amar!")
  else:
    print(f"O filme de terror escolhido foi...")
    if notaL3 <= 6:
      print(f"{filme3}?! Aldo provavelmente irá odiar um filme de terror com essa nota...")
    else:
      print(f"{filme3}! Esse filme de terror é maravilhoso... Aldo vai amar!")
  