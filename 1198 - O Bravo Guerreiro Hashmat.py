while True:
  try:
    hashmatSoldiers, oponentSoldiers = input().split()
    hashmatSoldiers = int(hashmatSoldiers)
    oponentSoldiers = int(oponentSoldiers)
    if (hashmatSoldiers > oponentSoldiers):
      print (hashmatSoldiers - oponentSoldiers)
    else:
      print(oponentSoldiers - hashmatSoldiers)
  except EOFError:  
    break
