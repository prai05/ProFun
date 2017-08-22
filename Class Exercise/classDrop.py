# Class Exercise
# 010123102 Computer Programming Fundamental
#
# Class Exercise : Esport team
#
# Phattharanat Khunakornophat
# ID 5901012610091
# OCT 19 2016

class mid:
  Drop = []
  def __init__(self, subject, mean, score):
    self.subject = subject
    self.mean = mean
    self.score = score
    print('\ninit...{} mean {} your score {}'.format(self.subject, self.mean, self.score))

  def drop(self):
    if self.mean > self.score:
      print('I will Drop this subject')
      mid.Drop.append(self.subject)
    else:
      print('Good')

  def d(self):
    print(mid.Drop)

math = mid('Math', 31, 12)
math.drop()

phy = mid('Physics', 41, 68)
phy.drop()

profun = mid('Pro Fun', 60, 62)
profun.drop()

manso = mid('Man So', 50, 42)
manso.drop()

print('\n')
print(mid.Drop)
