import re


def clean(arg):
  arg = re.sub('^\s+', '', arg)
  arg = re.sub('\s+$', '', arg)
  while re.search('\s+', arg, flags=re.UNICODE+re.IGNORECASE) != None:
    arg = re.sub('\s+', ',', arg)
  return arg

def buildin_f(x, y):
  try:
    a = int(x)
    b = int(y)
  except:
    raise TypeError("Invalid Int")
  return a*b + a + 2*b - 1


def buildin_g(x):
  try:
    int(x)
  except:
    raise TypeError("Invalid Int")
  return int(x)**2+2*int(x)

def buildin_lul():
  return '0'



def parse(x):
  expr = ''
  x = clean(x)
  print("In:"+ x)
  while (x):
    if re.match('^[,]', x, flags=re.UNICODE + re.IGNORECASE):
      x = re.sub('^[,]', '', x)
      expr += ','
    elif re.match('^[)]', x, flags=re.UNICODE + re.IGNORECASE):
      x = re.sub('^[)]', '', x)
      expr += ')'
    elif re.match('^\w+', x, flags=re.UNICODE+re.IGNORECASE):
      expr += repr(re.search('^\w+', x, re.UNICODE).group(0))
      x = re.sub('^\w+', '', x)
    elif re.match('^[$][(]\w+', x, flags=re.UNICODE+re.IGNORECASE):
      expr += "buildin_" + re.search('\w+', x).group(0)
      expr += '('
      x = re.sub('^[$][(]\w+', '', x)
    elif re.match('\{\{[0-9]\}\}', x, flags=re.U+re.IGNORECASE):
      expr += repr(re.search('\{\{[0-9]\}\}', x, re.UNICODE).group(0))
      x = re.sub('\{\{[0-9]\}\}', '', x)
    else:
      raise TypeError("invalid syntax")
  while re.search('[(][,]', expr):
    expr = re.sub('[(][,]', '(', expr)
  expr = "[" + expr + ']'
  print('result expression:' + expr)
  return expr



def commandParse(expr, arg):
  for i in range(len(arg)):
    expr = re.sub('\{\{' + str(i) + '\}\}', str(arg[i]), expr)
  exprAfter = eval(expr)
  print("result:"+repr(exprAfter))

def cmd_f(arg):
    name = 'cmd_f'
    expr = "{{1}} says $(f $(g {{0}}) $(lul)) LUL {{2}}"
    for i in range(len(arg)):
      expr = re.sub('\{\{' + str(i) + '\}\}', str(arg[i]), expr)
    exprAfter = eval(parse(expr))
    print(exprAfter)

cmd_f([10, 'Kappa', 'PogChamp'])

