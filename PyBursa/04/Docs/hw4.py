# 1
import string


def percentage(input_text):
    res = {}
    for letter in input_text.lower():
        if letter in string.ascii_lowercase:
            res[letter] = res.setdefault(letter, 0) + 1
    input_text_lenght = float(sum(res.values()))
    for k, v in res.items():
        res[k] = round(v/input_text_lenght * 100, 1)
    return res


# 2
def ellipsis_1(input_text, limit=0):
    if limit >= len(input_text) or limit == 0:
        return input_text
    else:
        if input_text[limit - 1] == ' ' or input_text[limit] == ' ':
            return input_text[:limit].strip(' ') + '...'
        else:
            if ' ' in input_text[:limit]:
                while input_text[limit] != ' ' and input_text[limit]:
                    limit -= 1
            return input_text[:limit] + '...'