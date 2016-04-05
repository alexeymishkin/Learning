# 1
def vov(input_text):
    max_vov = 0
    vovs = 'AOUIEYaouiey'
    temp = input_text.split(' ')
    for word in temp:
        max_vov_temp = 0
        for l in word:
            if l in vovs:
                max_vov_temp += 1
        if max_vov_temp > max_vov:
            max_vov = max_vov_temp
    return max_vov


# 2
def max_len(input_text):
    temp = input_text.split(' ')
    len_ind = []
    for i, word in enumerate(temp):
        temp[i] = word.strip('.,!? ')
        len_ind.append(len(temp[i]))
    for i, l in enumerate(len_ind):
        if l == max(len_ind):
            print(temp[i])
    return


# 3,7
def reverse(input_text):
    text_t = input_text.strip('.').split('.')[::-1]
    for i, predl in enumerate(text_t):
        text_t[i] = predl.split(' ')[::-1]
        for j, word in enumerate(text_t[i]):
            text_t[i][j] = word[::-1]
        text_t[i] = '.' + ' '.join(text_t[i])
    text_t = ' '.join(text_t)
    return text_t


# 5
def sum_dig(inp_str):
    res = 0
    for d in inp_str:
        res += int(d)
    return res


# 6
def simple():
    res = [2]
    x = 3
    while x < 10000:
        sim = True
        for i in range(2, x):
            if x % i == 0:
                sim = False
        if sim:
            res.append(x)
        x += 1
    return res


# 8
def a_a_a(input_text):
    glasn = 'aeuioy'
    res = 0
    temp = input_text.split(' ')
    for i, word in enumerate(temp):
        temp[i] = word.strip('.,;:').lower()
        for j, l in enumerate(temp[i][1:-1], start=1):
            if l == 'a' and (temp[i][j - 1] not in glasn and temp[i][j + 1] not in glasn):
                res += 1
    return res
