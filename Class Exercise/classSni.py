# Class Exercise
# 010123102 Computer Programming Fundamental
#
# Class Exercise : Esport team
#
# Phattharanat Khunakornophat
# ID 5901012610091
# OCT 19 2016

class sniper:
  def __init__(self, name, range):
    self.name = name
    self.range = range
    print('initialize....{} , range {}km'.format(self.name, self.range))

  def fire(self, fire_range):
    if fire_range > self.range:
      print('{}km is too far'.format(fire_range))
    else:
      print('{}km killed enemy'.format(fire_range))

  def repair(self):
    self.price = self.range * 1250
    print(self.price)

print('init class (name, range(km))')
print('fire(range)')
print('repair()\n')

sni1 = sniper('L115A1',2)
sni1.fire(2)
sni1.fire(5)
sni1.repair()

print('\n')

sni2 = sniper('M82A1',4)
sni2.fire(3)
sni2.fire(4)
