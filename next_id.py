id_values = '0123456789abcdefghijklmnoprtuwvsxyz'

def next_position(position):
  if position=='z':
    position='0'
    return position, False
  position= id_values[id_values.index(position)+1]
  return position, True

def next_id(param_string):
  param = list(param_string)
  for position in range(1,len(param)):
    old_value = param[len(param)-position]
    param[len(param)-position], result = next_position(old_value)
    if result:
      break
    if position==len(param)-1:
      return '0'*len(param)
  return "".join(param)

param = '0zzz111'
if '0zzz112' == next_id(param) :
  print('OK 1')

param = 'zzzzz'
if '00000' == next_id(param) :
  print('OK 2')

param = '0000z'
if '00010' == next_id(param) :
  print('OK 3')
