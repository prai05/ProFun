# Class Exercise
# 010123102 Computer Programming Fundamental
#
# Class Exercise : Esport team
#
# Phattharanat Khunakornophat
# ID 5901012610091
# OCT 19 2016


class team:
  cnt = 0 # Count team

  def __init__(self, name, cap):
    self.name = name
    self.member = []
    self.member.append(cap)

  def add(self, player):
    self.member.append(player)

  def detail(self):
    team.cnt += 1
    print(team.cnt)
    print('Team: {}'.format(self.name))
    print('member: {}\n'.format(self.member))

# init Navi team
Navi = team('Natus Vincere', 'Dendi')
# add Navi player
Navi.add('GeneRaL')
Navi.add('Ditya Ra')
Navi.add('SoNNeikO')
Navi.add('Artstyle')
# Show Navi detail
Navi.detail()

# init EG team
EG = team('Evil Geniuses', 'Cr1t-')
# add EG player
EG.add('Suma1L')
EG.add('UNiVeRsE')
EG.add('zai')
EG.add('Arteezy')
# Show EG detail
EG.detail()

RTTI7 = team('Road to TI7', 'PSYCHOPATH')
RTTI7.detail()
