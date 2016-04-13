import re
import os


def max_fuel_value(file, at):
    log = open(file, 'r')
    pos = log.read()
    pattern = re.compile('{}\|.*\|-27\|10.000\|(.*?)\|'.format(at))
    x = pattern.findall(pos)
    log.close()
    if len(x) > 0:
        return max(x)

def log_dir():
    path = open('C:\STMatix\STM Diagnostics\STM_Diagnostics.ini', 'r')
    diagn_ini = path.read()
    log_path_pt = re.compile('Log Path=(.*?PosLogs)')
    x = log_path_pt.findall(diagn_ini)
    path.close()
    if len(x) != 0:
        log_path = x[0]
        return log_path

def main():
    if log_dir() != None:
        while True:
            at = input('АТ (\'q\' для выхода ): ')
            if at == 'q':
                break
            else:
                for x in range(1, 32):
                    if x < 10:
                        pos_path = log_dir() + '\\' + '0' + str(x) + '.log'
                    else:
                        pos_path = log_dir() + '\\' + str(x) + '.log'
                    print('День ', x)
                    if os.path.exists(pos_path):
                        print('Максимальное показание датчика: ', max_fuel_value(pos_path, int(at)))
                    else:
                        print('Лог не найден')
    else:
        print('Папка с логами не найдена')

if __name__ == '__main__':
    main()