### login

from tkinter import *
from random import randint
import conversiones
import interfaz
def base_ventana():
    login.withdraw()
    root=Toplevel()
    root.title("BASES")
    root.resizable(0,0)

    Frame2=Frame(root, width=600, height=600)


    Frame2.pack()

    Label2=Label(Frame2,text="ELIJA LA BASE NUMERICA DEL JUEGO",font="algerian")
    Label2.place(x=130,y=30)

######################################### DECIMAL #################################

    def decimal():
        
        
        
        
        mat=[["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"]]
        random1=randint(1,4)
        random2=randint(1,4)
        if (random1== 1 or random1== 3):
            return decimal()
        if (random2==1 or random2==3):
            return decimal()
        else:
            juego_ventana(10)  
            root.destroy()
            y=randint(0,3)
            f=randint(0,3)
            r=randint(0,3)
            w=randint(0,3)
            mat[r][w]=str(random2)
            mat[f][y]=str(random1)
            return recorrer_aux(mat)
    def recorrer_aux(d):
        return recorrer_aux2(d,0,0,"")
    def recorrer_aux2(d,fila,col,result):
        if(col==len(d[0])):
            print(result+"\n")

            return recorrer_aux2(d,fila+1,0,"")
        else:
            if(fila==len(d)):
                return 
            else:
                result=(result+d[fila][col]+"\t")
                return recorrer_aux2(d,fila,col+1,result)

        


   # def arriba(x):
    #def abajo():
   # def izquierda():
   # def derecha():
       


################################################## BINARIO #############################333 



    def binario():
        mat=[["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"]]
        random1=randint(1,4)
        random2=randint(1,4)
        if (random1== 1 or random1== 3):
            return binario()
        if (random2==1 or random2==3):
            return binario()
        else:
            juego_ventana(2)  
            root.destroy()
            y=randint(0,3)
            f=randint(0,3)
            r=randint(0,3)
            w=randint(0,3)
            mat[r][w]=str(convs.bina(random2))
            mat[f][y]=str(convs.bina(random1))
            return recorrer_aux(mat)
    def recorrer_aux(d):
        return recorrer_aux2(d,0,0,"")
    def recorrer_aux2(d,fila,col,result):
        if(col==len(d[0])):
            print(result+"\n")
            return recorrer_aux2(d,fila+1,0,"")
        else:
            if(fila==len(d)):
                return 
            else:
                result=(result+d[fila][col]+"\t")
                return recorrer_aux2(d,fila,col+1,result)
        
        
########################################################### OCTAL ############################################3

        
    def octal():


        
        mat=[["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"]]
        random1=randint(1,4)
        random2=randint(1,4)
        if (random1== 1 or random1== 3):
            return octal()
        if (random2==1 or random2==3):
            return octal()
        else:
            juego_ventana(8)  
            root.destroy()
            y=randint(0,3)
            f=randint(0,3)
            r=randint(0,3)
            w=randint(0,3)
            mat[r][w]=str(convs.octal(random2))
            mat[f][y]=str(convs.octal(random1))
            return recorrer_aux(mat)
    def recorrer_aux(d):
        return recorrer_aux2(d,0,0,"")
    def recorrer_aux2(d,fila,col,result):
        if(col==len(d[0])):
            print(result+"\n")
            return recorrer_aux2(d,fila+1,0,"")
        else:
            if(fila==len(d)):
                return 
            else:
                result=(result+d[fila][col]+"\t")
                return recorrer_aux2(d,fila,col+1,result)


######################################## HEXADECIMAL ###########################################     
    def hexadecimal():
        mat=[["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"],
             ["0","0","0","0"]]




        random1=randint(1,4)
        random2=randint(1,4)
        if (random1== 1 or random1== 3):
            return hexadecimal()
        if (random2==1 or random2==3):
            return hexadecimal()
        else:
            juego_ventana(16)  
            root.destroy()
            y=randint(0,3)
            f=randint(0,3)
            r=randint(0,3)
            w=randint(0,3)
            mat[r][w]=str(convs.dec_hex(random2))
            mat[f][y]=str(convs.dec_hex(random1))
            return recorrer_aux(mat)
    def recorrer_aux(d):
        return recorrer_aux2(d,0,0,"")
    def recorrer_aux2(d,fila,col,result):
        if(col==len(d[0])):
            print(result+"\n")
            return recorrer_aux2(d,fila+1,0,"")
        else:
            if(fila==len(d)):
                return 
            else:
                result=(result+d[fila][col]+"\t")
                return recorrer_aux2(d,fila,col+1,result)
        
############################################################################################# ELECCION DE BASE #############################################################################  

    BINARIO=Button(Frame2,text="BINARIO",bg="orange",fg="white",font="Century",relief="groove",bd=35, command=binario)
    BINARIO.place(x=100,y=90)



    OCTAL=Button(Frame2,text="OCTAL",bg="orange",fg="white",font="Century",relief="groove",bd=35,command=octal)
    OCTAL.place(x=100,y=195)



    HEXADECIMAL=Button(Frame2,text="HEXADECIMAL",bg="orange",fg="white",font="Century",relief="groove",bd=35,command=hexadecimal)
    HEXADECIMAL.place(x=100,y=300)



    DECIMAL=Button(Frame2,text="DECIMAL",bg="orange",fg="white",font="Century",relief="groove",bd=35,command=decimal)
    DECIMAL.place(x=100,y=405)
###################################################################################################################################################################################################################################
################################################################################## VENTANA DE JUEGO #########################################################################################
def juego_ventana(base):
    
    

    score1=Label(root,text="SCORE",bg="#793a4b",fg="white")
    score1.place(x=1000,y=360)
    
    score2=Label(root,text="0" ,bg="#FACC2E",fg="white")
    score2.place(x=1050,y=360,width=110,height=80)

    
    tiempo=Label(root, text="TIMER", bg="#793a4b",fg="white")
    tiempo.place(x=1000,y=100)
    
    tiempo2=Label(root, text="0:00", bg="#FACC2E",fg="white")
    tiempo2.place(x=1050,y=100,width=110,height=80)

    d5=lienzo.create_rectangle(700,570,100,40,fill="#E6E6E6")
    

    


   
    NUMEROS1=Label(lienzo, text="0"  , bg="#FACC2E",font=("Comic Sans MS",10),fg="white")
    NUMEROS1.place(x=145,y=50,width=120,height=120)

    
    
    NUMEROS2=Label(lienzo,text=0,bg="#FFBF00",font=("Comic Sans MS",10),fg="white")
    NUMEROS2.place(x=145,y=180,width=120,height=120)
    
    NUMEROS3=Label(lienzo,text=0,bg="#DBA901",font=("Comic Sans MS",10),fg="white")
    NUMEROS3.place(x=145,y=310,width=120,height=120)
    
    NUMEROS4=Label(lienzo,text=0,bg="#FE9A2E",font=("Comic Sans MS",10),fg="white")
    NUMEROS4.place(x=145,y=440,width=120,height=120)
    
    NUMEROS5=Label(lienzo,text=0,bg="#FFBF00",font=("Comic Sans MS",10),fg="white")
    NUMEROS5.place(x=275,y=50,width=120,height=120)
    
    NUMEROS6=Label(lienzo,text=0,bg="#FACC2E",font=("Comic Sans MS",10),fg="white")
    NUMEROS6.place(x=275,y=180,width=120,height=120)
    
    NUMEROS7=Label(lienzo,text=0,bg="#FACC2E",font=("Comic Sans MS",10),fg="white")
    NUMEROS7.place(x=275,y=310,width=120,height=120)
    
    NUMEROS8=Label(lienzo,text=0,bg="#F7D358",font=("Comic Sans MS",10),fg="white")
    NUMEROS8.place(x=275,y=440,width=120,height=120)



    
    
    NUMEROS9=Label(lienzo,text=0,bg="#FFBF00",font=("Comic Sans MS",10),fg="white")
    NUMEROS9.place(x=405,y=50,width=120,height=120)
    
    NUMEROS10=Label(lienzo,text=0,bg="#FAAC58",font=("Comic Sans MS",10),fg="white")
    NUMEROS10.place(x=405,y=180,width=120,height=120)
    
    NUMEROS11=Label(lienzo,text=0,bg="#FACC2E",font=("Comic Sans MS",10),fg="white")
    NUMEROS11.place(x=405,y=310,width=120,height=120)
    
    NUMEROS12=Label(lienzo,text=0,bg="#FE9A2E",font=("Comic Sans MS",10),fg="white")
    NUMEROS12.place(x=405,y=440,width=120,height=120)
    
    NUMEROS13=Label(lienzo,text=0,bg="#DBA901",font=("Comic Sans MS",10),fg="white")
    NUMEROS13.place(x=535,y=50,width=120,height=120)
    
    NUMEROS14=Label(lienzo,text=0,bg="#D7DF01",font=("Comic Sans MS",10),fg="white")
    NUMEROS14.place(x=535,y=180,width=120,height=120)
    
    NUMEROS15=Label(lienzo,text=0,bg="#B18904",font=("Comic Sans MS",10),fg="white")
    NUMEROS15.place(x=535,y=310,width=120,height=120)
    
    NUMEROS16=Label(lienzo,text=0,bg="#FACC2E",font=("Comic Sans MS",10),fg="white")
    NUMEROS16.place(x=535,y=440,width=120,height=120)


    score1=Label(root,text="SCORE",bg="#793a4b",fg="white")
    score1.place(x=1000,y=360)
    
    score2=Label(root,text="0" ,bg="#FACC2E",fg="white")
    score2.place(x=1050,y=360,width=110,height=80)

    
    tiempo=Label(root, text="TIMER", bg="#793a4b",fg="white")
    tiempo.place(x=1000,y=100)
    
    tiempo2=Label(root, text="0:00", bg="#FACC2E",fg="white")
    tiempo2.place(x=1050,y=100,width=110,height=80)




    root.bind("<Right>",r)
    root.bind("<Left>",l)
    root.bind("<Up>",up)
    root.bind("<Down>",d)
    


def up(event):
    print("hola")
    
    
def l(event):
    print("izquierda")

def d(event):
    print("abajo")
def r(event):
    print("derecha")

    
    

################################################################################## VENTANA DEL JUEGO ################################################################################## ##################################################################################     

login=Tk()
login.title("2048")
login.resizable(0,0)

Framelogin=Frame(login, width=1080, height=720)
Framelogin.pack()
imagen=PhotoImage(file="2048.png")
Framelogin.config(bg="aliceblue")



listo=Button(Framelogin, text="Presione Enter",bg="orange",fg="white",font="Century",relief="groove",bd=10)
listo.place(x=650,y=100)


logintexto=Entry(Framelogin)
logintexto.place(x=443,y=120)
logintexto.config(fg="white",bg="orange",justify="center")
def enterPress(event):
    if(logintexto.get()!=""):
        return base_ventana()
    
logintexto.bind("<Return>",enterPress)

########### ACCIONES DE LAS TECLAS ################### 







Label3=Label(Framelogin, image=imagen)
Label3.place(x=225,y=180)
Label4=Label(Framelogin,text="INTRODUZCA SU NICKNAME",bg="aliceblue",font=("Comic Sans MS",10),fg="black")
Label4.place(x=430,y=100)
Label2=Label(Framelogin,text="¡BIENVENIDO A 2048!",bg="aliceblue",font=("Comic Sans MS",40),fg="Darkorange")
Label2.place(x=250,y=30)







login.mainloop()


