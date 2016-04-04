# 1
def squares(inp_list):
    if type(inp_list) == tuple:
        out_list = tuple(x ** 2 for x in inp_list)
        print(out_list)
        return out_list
    elif type(inp_list) == list:
        out_list = [x ** 2 for x in inp_list]
        print(out_list)
        return out_list
    else:
        print('неподходящий тип')


# 2
def symmetry(inp_str):
    if inp_str[:len(inp_str) // 2] == inp_str[len(inp_str):(len(inp_str) - 1) // 2:-1]:
        return True
    else:
        return False


# 3
def three(inp_list):
    res = {}
    for x in inp_list:
        res[x] = x % 3 == 0
    return res


# 4
def chet_nechet(inp_list):
    res = []
    if len(inp_list) % 2 == 0:
        for x in inp_list:
            if x % 2 == 0:
                res.append(x)
    else:
        for x in inp_list:
            if x % 2 != 0:
                res.append(x)
    return res


# 5, 7
def separatop(inp_list):
    chet = []
    nechet = []
    for x in inp_list:
        if x % 2 == 0:
            chet.append(x)
        else:
            nechet.append(x)
    chet.sort()
    chet.reverse()
    nechet.sort()
    inp_list = nechet + chet
    print(inp_list)
    return inp_list


# 6
def classificator(inp_dict):
    res = {}
    for x in inp_dict.values():
        if str(type(x))[8:-2] in res.keys():
            res[str(type(x))[8:-2]] += 1
        else:
            res[str(type(x))[8:-2]] = 1
    return res


# 8
def double_tuple(input_tuple):
    res = []
    for x in range(0, len(input_tuple), 2):
        if x != len(input_tuple) - 1:
            a = (input_tuple[x], input_tuple[x + 1])
            res.append(a)
        else:
            a = (input_tuple[x],)
            res.append(a)
    return tuple(res)


# 9
def simpler(input_list):
    res = []
    for x in range(len(input_list)):
        for y in input_list[x]:
            res.append(y)
    return res
