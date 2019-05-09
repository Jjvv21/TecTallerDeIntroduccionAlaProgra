import time

def tiempo(minutos,segundos):
    if(minutos==0 and segundos==0):
        print(0,':',00)
        return 0 
        
    if (segundos==00):
        print(minutos,':',segundos)
        minutos=minutos-1
        segundos=60
        return tiempo(minutos,segundos-1)
    print(minutos,':',segundos)
    time.sleep(1)
    return tiempo(minutos,segundos-1)


tiempo(5,0)
