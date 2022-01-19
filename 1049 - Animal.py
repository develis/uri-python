is_vertebrate = input()
subclass = input()
food = input()

if is_vertebrate == "vertebrado":
  if subclass == "ave":
    if food == "carnivoro":
      print("aguia")
    else:
      print("pomba")
  else:
      if food == "onivoro":
        print("homem")
      else:
        print("vaca")
else:
  if subclass == "inseto":
    if food == "hematofago":
      print("pulga")
    else:
      print("lagarta")
  else:
    if food == "hematofago":
      print("sanguessuga")
    else:
      print("minhoca")
