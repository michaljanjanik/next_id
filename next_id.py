id_values = '0123456789abcdefghijklmnoprtuwvsxyz'

test="teofil"


def next_position(position):
    if position == 'z':
        position = '0'
        return position, False
    position = id_values[id_values.index(position) + 1]
    return position, True


def next_id(param_string):
    param = list(param_string)
    for position in range(1, len(param)):
        old_value = param[len(param) - position]
        param[len(param) - position], result = next_position(old_value)
        if result:
            break
        if position == len(param) - 1:
            return '0' * len(param)
    return "".join(param)


param = '0zzz111'
assert '0zzz112' == next_id(param)

param = 'zzzzz'
assert '00000' == next_id(param)

param = '0000z'
assert '00010' == next_id(param)

