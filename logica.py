from random import randint
import random 
from tkinter import *
import time 
mat=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

########################################################## FUNCION 1

def matriz(mat):
    random1=randint(1,4)
    random2=randint(1,4)
    if (random1== 1 or random1== 3):
        return matriz(mat)
    if (random2==1 or random2==3):
        return matriz(mat)
    else:
        y=randint(0,3)
        f=randint(0,3)
        r=randint(0,3)
        w=randint(0,3)
        if ((y+r)==(r+w)):
            return matriz(mat)
        else:
            mat[r][w]=(random2)
            mat[f][y]=(random1)

            print(" 2048 :´v")
            return recorrer_aux(mat)



################### Revisa si gané #####################################


###### ME DICE SI LA MATRIZ ESTA LLENA  #######

def lleno(matriz,fila,col):
    if fila>len(matriz)-1:
        print("PERDISTE")
    else:
        if col==len(matriz[0])-1:
            if matriz[fila][col]==0:
                return random_despues(matriz)
            else:
                col=0
                return lleno(matriz,fila+1,col)
        else:
            if matriz[fila][col]==0:
                return random_despues(matriz)
            else:
                return lleno(matriz,fila,col+1)
            
        




    
 

######## ACOMODA LA MATRIZ AL FINAL  #############

def acomodar_aux(matriz):
    return recorrer_aux3(matriz,0,0,"")
def recorrer_aux3(matriz,fila,col,result):
    if(col==len(matriz[0])):
        print(result+"\n")
        return recorrer_aux3(matriz,fila+1,0,"")
    else:
        if(fila==len(matriz)):
            print("\t","P","\t","E","\t","R","\t","D","\t","I","\t","S","\t","T","\t","E")
        else:
            result=(result+str(matriz[fila][col])+"\t")
            return recorrer_aux3(matriz,fila,col+1,result)



########################################################################################################################### MOVIMIENTOS #################################################################################################
        
####################### MOVIMIENTO HACIA ARRIBA ###############################
def mov_arriba(b):
    return mov_arriba_aux(b,len(b)-1,0)


def mov_arriba_aux(matriz,fila,col):
    if (col>len(matriz[0])-1):
        return lleno(matriz,0,0)
    else:
        if (matriz[fila-1][col]==0):
            matriz[fila-1][col]=matriz[fila][col]
            matriz[fila][col]=0
            if fila==1:
                fila=len(matriz)-1
                return mov_arriba_aux(matriz,fila,col+1)
            else:
                return mov_arriba_aux(matriz,fila-1,col)
            
        if (matriz[fila-1][col]==matriz[fila][col]):
            matriz[fila-1][col]= ((matriz[fila-1][col])*2)
            matriz[fila][col]=0
            if fila==1:
                fila=len(matriz)-1
                return mov_arriba_aux(matriz,fila,col+1)
            else:
                return mov_arriba_aux(matriz,fila-1,col)
        else:
            if fila==1:
                fila=len(matriz)-1
                return mov_arriba_aux(matriz,fila,col+1)
            else:
                return mov_arriba_aux(matriz,fila-1,col)
            


######## FILTRO PARA ACOMODAR ##################



##############################################################filtro 3 arriba 
        

            

##################### MOVIMIENTO HACIA ABAJO ##############################
            
def mov_abajo(b):
    return mov_abajo_aux(b,0,0)


def mov_abajo_aux(matriz,fila,col):
    if (col>len(matriz[0])-1):
        
        return filtro_abajo(matriz,0,0)
    else:
        if (matriz[fila+1][col]==0):
            matriz[fila+1][col]=matriz[fila][col]
            matriz[fila][col]=0
            if fila==2:
                fila=0
                return mov_abajo_aux(matriz,fila,col+1)
            else:
                return mov_abajo_aux(matriz,fila+1,col)
            
        if (matriz[fila+1][col]==matriz[fila][col]):
            matriz[fila+1][col]= ((matriz[fila+1][col])*2)
            matriz[fila][col]=0
            if fila==2:
                fila=0
                return mov_abajo_aux(matriz,fila,col+1)
            else:
                return mov_abajo_aux(matriz,fila+1,col)
        else:
            if fila==2:
                fila=0
                return mov_abajo_aux(matriz,fila,col+1)
            else:
                return mov_abajo_aux(matriz,fila+1,col)



################# FILTRO DE "ABAJO" #############




def filtro_abajo(matriz,fila,col):
    if (col>len(matriz[0])-1):
        
        return lleno(matriz,0,0)
    else:
        if (matriz[fila+1][col]==0):
            matriz[fila+1][col]=matriz[fila][col]
            matriz[fila][col]=0
            if fila==2:
                fila=0
                return filtro_abajo(matriz,fila,col+1)
            else:
                return filtro_abajo(matriz,fila+1,col)
        else:
            if fila==2:
                fila=0
                return filtro_abajo(matriz,fila,col+1)
            else:
                return filtro_abajo(matriz,fila+1,col)

            



#################### MOVIMIENTO HACIA LA DERECHA ###########################################
def mov_derecha(d):
    return derecha_aux(d,0,0) 

def derecha_aux(matriz,fila,col):
    if (fila>len(matriz[0])-1):
        
        return filtro_derecha(matriz,0,0)
    else:
        if (matriz[fila][col+1]==0):
            matriz[fila][col+1]=matriz[fila][col]
            matriz[fila][col]=0
            if col==2:
                col=0
                return derecha_aux(matriz,fila+1,col)
            else:
                return derecha_aux(matriz,fila,col+1)
            
        if (matriz[fila][col+1]==matriz[fila][col]):
            matriz[fila][col+1]= ((matriz[fila][col+1])*2)
            matriz[fila][col]=0
            if col==2:
                col=0
                return derecha_aux(matriz,fila+1,col)
            else:
                return derecha_aux(matriz,fila,col+1)
        else:
            if col==2:
                col=0
                return derecha_aux(matriz,fila+1,col)
            else:
                return derecha_aux(matriz,fila,col+1)
#################### filtro de movimiento hacia la izquierda ###########################################
def filtro_derecha(matriz,fila,col):
    if (fila>len(matriz[0])-1):
        
        return lleno(matriz,0,0)
    else:
        if (matriz[fila][col+1]==0):
            matriz[fila][col+1]=matriz[fila][col]
            matriz[fila][col]=0
            if col==2:
                col=0
                return filtro_derecha(matriz,fila+1,col)
            else:
                return filtro_derecha(matriz,fila,col+1)
            
        else:
            if col==2:
                col=0
                return filtro_derecha(matriz,fila+1,col)
            else:
                return filtro_derecha(matriz,fila,col+1)
            
            
############ MOVIMIENTO HACIA LA IZQUIERDA ################################################
def mov_izquierda(d):
    return izquierda_aux(d,0,len(d[0])-1) 

def izquierda_aux(matriz,fila,col):
    if (fila>len(matriz[0])-1):
        
        return filtro_izquierda(matriz,0,len(matriz[0])-1)
    else:
        if (matriz[fila][col-1]==0):
            matriz[fila][col-1]=matriz[fila][col]
            matriz[fila][col]=0
            if col==1:
                col=len(matriz[0])-1
                return izquierda_aux(matriz,fila+1,col)
            else:
                return izquierda_aux(matriz,fila,col-1)
            
        if (matriz[fila][col-1]==matriz[fila][col]):
            matriz[fila][col-1]= ((matriz[fila][col-1])*2)
            matriz[fila][col]=0
            if col==1:
                col=len(matriz[0])-1
                return izquierda_aux(matriz,fila+1,col)
            else:
                return izquierda_aux(matriz,fila,col-1)
        else:
            if col==1:
                col=len(matriz[0])-1
                return izquierda_aux(matriz,fila+1,col)
            else:
                return izquierda_aux(matriz,fila,col-1)


            
#    #     #   ############ MOVIMIENTO HACIA LA IZQUIERDA ##############     #  #  # 
def filtro_izquierda(matriz,fila,col):
    if (fila>len(matriz[0])-1):
        
        return lleno(matriz,0,0)
    else:
        if (matriz[fila][col-1]==0):
            matriz[fila][col-1]=matriz[fila][col]
            matriz[fila][col]=0
            if col==1:
                col=len(matriz[0])-1
                return filtro_izquierda(matriz,fila+1,col)
            else:
                return filtro_izquierda(matriz,fila,col-1)
            
        if (matriz[fila][col-1]==matriz[fila][col]):
            matriz[fila][col-1]= ((matriz[fila][col-1])*2)
            matriz[fila][col]=0
            if col==1:
                col=len(matriz[0])-1
                return filtro_izquierda(matriz,fila+1,col)
            else:
                return filtro_izquierda(matriz,fila,col-1)
        else:
            if col==1:
                col=len(matriz[0])-1
                return filtro_izquierda(matriz,fila+1,col)
            else:
                return filtro_izquierda(matriz,fila,col-1)

######################################################################################################################### MOVIMIENTOS ##############################################################################################

################################# GENERADOR DE RANDOMS DURANTE EL JUEGO ####################################
    

    
def random_despues(matriz):
    random=randint(1,4)
    if random==1:
        return random_despues(matriz)
    else:
        w=randint(1,3)
        r=randint(1,3)
        if matriz[w][r]!=0:
            return random_despues(matriz)
        else:
            matriz[w][r]=random
            return recorrer_aux(matriz)
    
    



#####################################################################################

#####################################################################################


def dar_direccion(b):
    print("ELIGIR DIRECCIÓN","(arriba)","(derecha)","(izquierda)","(abajo)")
    c=input()
    if (c=="arriba"):
        return mov_arriba(b)
    if(c=="abajo"):
        return mov_abajo(b)
    if(c=="derecha"):
        return mov_derecha(b)
    if (c=="izquierda"):
        return mov_izquierda(b)
    else:
        print("No es una direccion valida")
        return dar_direccion(b)




    
################ acomoda la matriz ##############  FUNCION 2
def recorrer_aux(matriz):
    return recorrer_aux2(matriz,0,0,"")
def recorrer_aux2(matriz,fila,col,result):
    if(col==len(matriz[0])):
        print(result+"\n")
        return recorrer_aux2(matriz,fila+1,0,"")
    else:
        if(fila==len(matriz)):
            return dar_direccion(matriz)
        else:
            result=(result+str(matriz[fila][col])+"\t")
            return recorrer_aux2(matriz,fila,col+1,result)
matriz(mat)

