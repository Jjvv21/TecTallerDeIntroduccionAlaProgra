###DECIMAL A OCTAL 
def octal(x):
    if x<8:
        return x
    else:
        return oct_aux(x,1,0)

def oct_aux(d,i,e):
    residuo=(d%8)*10**e
    cociente=(d-d%8)/8
    if cociente<8:
    
        return int(cociente*10**i+residuo)
    else:
        residuo=d%8*10**e
        w=(d-d%8)/8
        return residuo+oct_aux(w,i+1,e+1)




###DECIMAL A BINARIO


def bina(y):
    if isinstance(y,int):
        if y==0:
            return 0
        elif y==1:
            return 1
        else:
            return bina_aux(y,1,0)
    else:
        return "ERROR" 
        
def bina_aux(d,i,e):
    residuo=(d%2)*10**e
    cociente=(d-d%2)/2
    if cociente<2:
        return int(cociente*10**i+residuo)
    else:
        residuo=d%2*10**e
        w=(d-d%2)/2
        return int(residuo)+bina_aux(w,i+1,e+1)



###BINARIO A DECIMAL

def dec(x):
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        x=str(x)
        return dec_aux(x,len(x)-1,0,1)

def dec_aux(b,i,e,a):
    res=0
    if i==0:
        f=2**e
        return res+(2**e*int(b[i]))
    else:
        res=res+((2**e)*int(b[i]))
        i=len(b)-1
        return res+dec_aux(b,i-a,e+1,a+1)


###OCTAL A DECIMAL

def oct_dec(x):
    if x<8:
        return x
    else:
        x=str(x)
        return dec_aux(x,len(x)-1,0,1)

def dec_aux(b,i,e,a):
    res=0
    if i==0:
        f=8**e
        return res+(8**e*int(b[i]))
    else:
        res=res+((8**e)*int(b[i]))
        i=len(b)-1
        return res+dec_aux(b,i-a,e+1,a+1)






###HEXADECIMAL A DECIMAL
def hex_dec(x):
    if isinstance (x,int):
        if x<10:
            return x
    else:
        return hex_str_aux(str(x))
            
def hex_str_aux(d):
    if d=="a":
        return 10
    if d=="b":
        return 11
    if d=="c":
        return 12 
    if d=="d":
        return 13
    if d=="e":
        return 14
    if d=="f":
        return 15
    else:
        return hex_aux(str(d))


def hex_aux(f):
    if len(f)>1:
        return hexa_aux(f,len(f)-1,0,1)

def hexa_aux(d,i,e,a):
    res=0
    if i==0:
        f=16**e
        return res+(16**e*int(d[i]))
    else:
        res=res+((16**e)*int(d[i]))
        i=len(d)-1
        return res+hexa_aux(d,i-a,e+1,a+1)


### hay que agregarle la lectura de letras en los numeros hex que tengan más de 1 digito 


def octalxd(num):
    if num==0:
        return ""
    else:
        return octalxd(num//8)+str(num%8)
 


###DECIMAL A HEXADECIMAL 
def dec_hex(num):
    if num<=9:
        return num
    if 9<num<16:
        if num==10:
            print("a")
        if num==11:
            print("b")
        if num==12:
            print("c")
        if num==13:
            print("d")
        if num==14:
            print("e")
        if num==15:
            print("f")
    else:
        return cambio_de_base_auxiliar(num,0,0)

def cambio_de_base_auxiliar(d,i,e):
    res=((d%16)*10**e)
    cociente=(d-d%16)/16
    if cociente<16:
        if res==10:
            return str(int(cociente))+"a"
        if res==11:
            return str(int(cociente))+"b"
        if res==12:
            return str(int(cociente))+"c"
        if res==13:
            return str(int(cociente))+"d"
        if res==14:
            return str(int(cociente))+"e"
        if res==15:
            return str(int(cociente))+"f"
        else:
            return str(int(cociente*10**i))+str(res)
    res=((d%16)*10**e)
    cociente=(d-d%16)/16
    if res <16:
        if cociente==10:
            return "a"+str(int(cociente))
        if cociente==10:
            return "b"+str(int(cociente))
        if cociente==10:
            return "c"+str(int(cociente))
        if cociente==10:
            return "d"+str(int(cociente))
        if cociente==10:
            return "e"+str(int(cociente))
        if cociente==10:
            return "f"+str(int(cociente))
        else:
            return str(int(cociente*10**i))+str(res)
        
        
    
    else:
        res=str(d%16*10**e)
        if d%16==10:
            return res+"a"+oct_aux(w,i+1,e+1)
        if d%16==11:
            return res+"b"+oct_aux(w,i+1,e+1)
        if d%16==12:
            return res+"c"+oct_aux(w,i+1,e+1)
        if d%16==13:
            return res+"d"+oct_aux(w,i+1,e+1)
        if d%16==14:
            return res +"e"+oct_aux(w,i+1,e+1)
        if d%16==15:
            return res +"f"+oct_aux(w,i+1,e+1)
        else:
            res=str(d%16*10**e)
            w=(d-d%16)/16
            return cambio_de_base_auxiliar(w,i+1,e+1)

    
            


