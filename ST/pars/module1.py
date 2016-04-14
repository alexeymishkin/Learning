import re
from module2 import log_dir


class PosLog(object):
    def __init__(self, log_directory):
        self.log_directory = log_directory

    def max_fuel_value(self, day, at):
        directory = self.log_directory
        log = open('{}\{}.log'.format(directory, day), 'r')
        pos = log.read()
        pattern = re.compile('{}\|.*\|-27\|10.000\|(.*?)\|'.format(at))
        x = pattern.findall(pos)
        log.close()
        if len(x) > 0:
            return max(x)

    def last_connect(self, day, at):
        find = False
        directory = self.log_directory
        blk_size = 200
        flag = 2
        log = open('{}\{}.log'.format(directory, day), 'rb')

        log.seek(-blk_size, 2)
        while not find:

            tmp_data = log.read(199).decode('utf-8')
            print(tmp_data)
            blk_size += blk_size
            log.seek(-blk_size)
            #flag = 0
            #pattern = re.compile('({}.*)\s'.format(at))
            #a = re.search(pattern, tmp_data)
        log.close()
        #print(a.group())

a = PosLog(log_dir())
print(a.max_fuel_value(13, 10000000))
a.last_connect(13, 10022516)
