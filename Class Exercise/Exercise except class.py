# 010123102 Computer Programming Fundamental
#
# Exercise 2
# except class
#
# Phattharanat Khunakornophat
# ID 5901012610091
# OCT 19 2016


# exception class
class duplicate_name(Exception):
  pass
class invalid_age(Exception):
  pass
class too_young(Exception):
  pass
class invalid_email(Exception):
  pass

# example list for add to data
example_tuple = [
  ('chuan', 'chuan@kmutnb.ac.th', 19),
  ('pinoy', 'pinoy@philippines', 20), # invalid email
  ('dragon player', 'ryuka_waga@tekiwo.kurau', 18),
  ('dragon player', 'ryujin_no_@kenwo.kurae', 19), # username duplicate
  ('bobo', 'bobo@noob.com', 3), # age < 16
  ('farmer', 'farm90min@for.fat', -3),
]

# data
data = {}

# init data class
class adddata:
  def __init__(self, name, mail):
    self.name = name
    self.mail = mail

# check for error
for name, mail, age in example_tuple:
  try:
    if name in data:
      raise duplicate_name()
    if age < 16:
      raise too_young()
    if age < 0:
      raise invalid_age()
    mail_parts = mail.split('@')
    if len(mail_parts) != 2 or not mail_parts[0] or not mail_parts[1]:
      raise invalid_email()
  except duplicate_name:
    print('duplicate_name_exception')
  except invalid_age:
    print('invalid_age_exception')
  except too_young:
    print('invalid_email_exception')
  except invalid_email:
    print('invalid_email_exception')
  else:
    data[name] = mail
    print('Valid data')

print(data)




