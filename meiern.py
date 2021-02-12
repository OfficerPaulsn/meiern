class wuerfel():
  import random
  
  def erzeuge_wurf(anzahl_wuerfel):
    wurf = list()
    for wuerfel in range (anzahl_wuerfel):
      wurf.append(random.randint(1,6))
    return wurf
