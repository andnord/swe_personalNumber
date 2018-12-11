import re
import datetime

def personNr(s):
    if int(s[:4]) < now.year-65:
            return 'felTooOld'
    if len(s) == 13 or len(s) == 12:
        if s[8] != '-':
            s = s[:8] + '-' + s[-4:]
    else:
        return 'felFormat'

    personnumret = s
    sistaSiffran = str(personnumret[-1])
    s = s[:-1]
    
    siffror = [int(d) for d in re.sub(r'\D', '', s)][-9:]
    summering_av_siffror = sum(x if x < 5 else x - 9 for x in siffror[::2])
    check_siffror = sum(siffror, summering_av_siffror) % 10
    
    kontrollsiffra = str(10 - check_siffror if check_siffror else 0)
    
    if kontrollsiffra == sistaSiffran:
        return True
    return False

now = datetime.datetime.now()
print(personNr(""))
