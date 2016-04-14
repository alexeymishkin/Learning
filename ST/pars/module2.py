import re

def log_dir():
    path = open('C:\STMatix\STM Diagnostics\STM_Diagnostics.ini', 'r')
    diagn_ini = path.read()
    log_path_pt = re.compile('Log Path=(.*?PosLogs)')
    x = log_path_pt.findall(diagn_ini)
    path.close()
    if len(x) != 0:
        log_path = x[0]
        return log_path