import tkinter as tk
from tkinter import filedialog 
import webbrowser
import datetime
import os


#=================== C L A S E S =================== 
class menu():
    def __init__(self, seccion, identifi, nombre, precio, descrip):
        self.seccion = seccion
        self.identifi = identifi
        self.nombre = nombre
        self.precio = precio
        self.descrip = descrip

class token():
    def __init__(self, lexeme, fila, columna, tokeno):
        self.lexeme = lexeme
        self.fila = int(fila)
        self.columna = int(columna)
        self.tokeno = tokeno

class error():
    def __init__(self, fila, columna, caracte, descripci):
        self.fila = int(fila)
        self.columna = int(columna)
        self.caracte = caracte
        self.descripci = descripci

class clienteF():
    def __init__(self, nombreC, nit, direcc, propina):
        self.nombreC = nombreC
        self.nit = nit
        self.direcc = direcc
        self.propina = propina

class factura():
    def __init__ (self, cantidad, idenF):
        self.cantidad = int(cantidad) #pendiente quitarle int
        self.idenF = idenF



#================== M E T O D O S ================== 
def letra(caracter_L): #metodo para saber si es una letra 
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if caracter_L.upper() in abc :
        return True
    else:
        return False

def numero(caracter_N): #metodo para saber si es un numero
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    if caracter_N in nums :
        return True
    else:
        return False


    



#================== M E T O D O S   A F D ================== 
def menu_afd(menu_txt, precioLim, precioLim_S):
    
    #cont_menu, cont_token, cont_error
    estado = 0
    char = ""
    lexema = ""
    #para guardar en la clase menu
    section = ""
    identi = ""
    name =""
    price = 0
    descrii = ""
    #para el reporte de tokens y errores 
    row = 1 
    colum = 0
    
    #para el reporte de errores
    descripc =""
    caract = "" #pendiente 
    #guardar errores
    vali_res = ""
    save_lex = ""
    save_lexx = False

    #control para estado
    controlE = 1
    #control para guardar el precio
    punto = False
    controlP = 0
    #control de errores
    error_menu = False
    i = 0
    while ( i<len(menu_txt)):
        char = menu_txt[i] #tomando el respectivo caracter 

        if (estado == 0): # ***** ESTADO 0 *****
            colum = colum +1
            if letra(char):
                estado = 1
                lexema = lexema + menu_txt[i]
            #AGREGANDO ALGO NUEVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
            elif (char == " "):
                estado = 1
            else: 
                estado = 1
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 1): # ***** ESTADO 1 *****
            colum = colum + 1
            if letra(char):
                estado = 1
                lexema = lexema + menu_txt[i]
               
            elif (char == "="):
                estado = 2
                if (lexema.upper() == "RESTAURANTE"):
                    cont_token.append(token(lexema, row, 1, "id_Restaurante"))
                    cont_token.append(token(char, row, colum, "Signo igual"))
                else: 
                    columT = colum - int(len(vali_res))
                    
                    cont_error.append(error(row, columT, lexema, "Restaurante invalido"))
                    #pendiente de borrar
                    cont_token.append(token(lexema, row, 1, "id_Restaurante"))
                    cont_token.append(token(char, row, colum, "Signo igual"))


            elif (char == " "):
                estado = 1

            else: 
                estado = 1
                vali_res = lexema + menu_txt[i]
                #AGREGANDO ALGO NUEVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 2): # ***** ESTADO 2 *****
            colum = colum +1
            if (char == "'"):
                lexema = ""
                estado = 3
                

                cont_token.append(token(char, row, colum, "Comilla simple"))

            elif (char == "\""):
                estado = 3
                error_menu = True
                cont_error.append(error(row, colum, "\"", "Caracter invalido"))

            elif (char == "\n"):
                estado = 2
            
            elif (char == " "):
                estado = 2
            
            else:
                estado = 2
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 3): # ***** ESTADO 3 *****
            colum = colum +1
            if (char == "'"):
                if (controlE == 1):
                    estado = 4
                    restaurante.append(lexema)
                    columT = colum - int(len(lexema))

                    cont_token.append(token(lexema, row, columT, "Nombre de restaurante"))
                    cont_token.append(token(char, row, colum, "Comilla simple"))
                    controlE = 2 #pendienteeee

                elif (controlE == 2): #nombre de la seccion
                    estado = 4
                    section = lexema
                    columT = colum - int(len(lexema))
                    cont_token.append(token(lexema, row, columT, "Nombre de seccion"))
                    cont_token.append(token(char, row, colum, "Comilla simple"))
                    
                    controlE = 3
                
                elif (controlE == 3): #nombre de la comida
                    estado = 4
                    name = lexema
                    columT = colum - int(len(lexema))
                    cont_token.append(token(lexema, row, columT, "Nombre de comida"))
                    cont_token.append(token(char, row, colum, "Comilla simple"))

                    controlE = 4
                
                elif (controlE == 4): #descripcion de la comida 
                    estado = 4
                    descrii = lexema
                    columT = colum - int(len(lexema))
                    cont_token.append(token(lexema, row, columT, "Descripcion de comida"))
                    cont_token.append(token(char, row, colum, "Comilla simple"))
                    #controlE = 2
      
            
            else: 
                estado = 3
                
                lexema = lexema + menu_txt[i]
        
        elif (estado == 4): # ***** ESTADO 4 *****
            colum = colum +1
            lexema = "" #nose que esta haciendo esto aqui :g
            if (char == "\n"): #este primer salto de linea identifica el nombre de la seccion 
                estado = 2 
                row = row + 1
                
                controlE = 2
                cont_token.append(token("\\n", row, colum, "Salto de linea"))
                colum = 0
            elif (char == ":"):
                estado = 5 
                controlE = 2
               
                cont_token.append(token(char, row, colum, "Dos puntos"))
            
            elif (char == ";"): #Empieza el proceso para guardar el precio
                estado = 10 
                lexema = ""
                controlE = 4
                cont_token.append(token(char, row, colum, "Punto y coma"))
            
            elif (char == "]"): #aqui guardo todo para mostrarlo en el html del menu
                estado = 14
                lexema = ""
                controlE = 2
                cont_token.append(token(char, row, colum, "Corchete cerrado"))
                #esto puede ir en el estado 14
                if(precioLim_S == True):
                    if (float(price) < float(precioLim) ):
                        #guardo los datos 
                        cont_menu.append(menu(section, identi, name, price, descrii))
                   
                        identi = ""
                        name = ""
                        price = 0
                        descrii = ""

                else:
                    cont_menu.append(menu(section, identi, name, price, descrii))
                    identi = ""
                    name = ""
                    price = 0
                    descrii = ""
            
            elif (char == " "):
                estado = 4

            else: 
                estado = 4
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))
                

        elif (estado == 5): # ***** ESTADO 5 *****
            colum = colum +1
            if (char == "\n"):
                estado = 6
                row = row + 1
                #controlE = 3
                cont_token.append(token("\\n", row, colum, "Salto de linea"))
                colum = 0
            elif (char == " "):
                estado = 5

            else: 
                estado = 5
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))
                
        
        elif (estado == 6): # ****** ESTADO 6 *****
            colum = colum +1
            if (char == "["):
                estado = 7
                cont_token.append(token(char, row, colum, "Corchete abierto"))

            elif (char == "\n"):
                estado = 6
                row = row + 1
                #controlE = 3 talvez 
                cont_token.append(token("\\n", row, colum, "Salto de linea"))
                colum = 0

            elif (char == " "):
                estado = 6
            elif (char == "("):
                estado = 7
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))
            
            else: 
                estado = 6
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        
        elif (estado == 7): # ***** ESTADO 7 *****
            colum = colum +1
            if letra(char): #el identificador obligatoriamente tiene que empezar con una letra
                estado = 8
                lexema = lexema + menu_txt[i]
                save_lex = lexema

            elif(char == " "):
                estado = 7
            else:
                estado = 7
                #pediente 
                save_lex = save_lex + char
                

                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 8): # ***** ESTADO 8 *****
            colum = colum +1
            if letra(char):
                estado = 8
                lexema = lexema + menu_txt[i]
                save_lex = lexema

            
            elif numero(char):
                estado = 8
                lexema = lexema + menu_txt[i]
                save_lex = lexema

            elif (char == "_"):
                estado = 8
                lexema = lexema + menu_txt[i]
                save_lex = lexema

            elif (char == ";"): #Para ir al estado 9 y seguir con las opciones 
                estado = 9
                identi = lexema
                columT = colum - int(len(lexema))

                if (save_lexx == True):
                    columTa = colum - int(len(save_lex))
                    cont_error.append(error(row, columTa, char, "Identificador invalido"))
                    save_lex = ""
                    save_lexx = False



                cont_token.append(token(lexema, row, columT, "Identificador"))
                cont_token.append(token(char, row, colum, "Punto y coma"))
                
             
            elif (char == " "):
                estado = 8
                #pendienteeeeee
                 
            else: 
                estado = 8
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 9): #***** ESTADO 9 *****
            colum = colum +1
            if (char == "'"): 
                estado = 3 #regreso al estado 3 para guardar la cadena, en este caso seria el nombre de la comida"
                
                cont_token.append(token(char, row, colum, "Comilla simple"))
                lexema = ""
                controlE = 3

            elif (char == "\""):
                estado = 3
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

            elif (char == " "):
                estado = 9
            else: 
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))


        elif (estado == 10): # ***** ESTADO 10 *****
            colum = colum + 1 
            if numero(char):
                estado = 11 #tiene que empezar con un numero obligatoriamente
                lexema = lexema + menu_txt[i]
            
            elif (char == " "):
                estado = 10 
            
            else:
                estado = 10
                error_menu = True

                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 11): # ***** ESTADO 11 *****
            colum = colum + 1
            if numero(char):
                estado = 11
                lexema = lexema + menu_txt[i]
                save_lex = lexema
                controlP = 1

            elif (char == "."):
                estado = 12
                lexema = lexema + menu_txt[i]
                save_lex = lexema
                controlP = 2
                cont_token.append(token(char, row, colum, "Punto"))
                
            
            elif (char == ";"):
                estado = 13
                columT = colum - int(len(lexema))
                if (controlP == 1): # numero entero
                    price = str(lexema) + ".00"

                elif (controlP == 2): # numero y punto 
                    price = str(lexema) + "00"

                elif (controlP == 3): # numero, punto y numero 
                    price = str(lexema + "0")
                
                elif (controlP == 4): # numero con mas decimales
                    #PENDIENTE DE REVISION
                    #price = lexema

                    lexema = float(lexema) 
                    price = float('{0:.2f}'.format(lexema)) #PENDIENTE DE REVISION

                                        #price
                cont_token.append(token(lexema, row, columT, "Precio de comida"))
                cont_token.append(token(char, row, colum, "Punto y coma"))

                if (save_lexx == True):
                    columTa = colum - int(len(save_lex))
                    cont_error.append(error(row, columTa, char, "Numero invalido"))
                    save_lex = ""
                    save_lexx = False

            elif (char == " "):
                estado = 11
            
            else: 
                estado = 11
                error_menu = True
                save_lex = save_lex + menu_txt[i]
               
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 12): # ***** ESTADO 12 *****
            colum = colum + 1
            if numero(char):
                if punto == False:
                    estado = 12
                    lexema = lexema + menu_txt[i]
                    save_lex = lexema
                    controlP = 3
                    punto = True
                
                else: 
                    estado = 12
                    controlP = 4
                    lexema = lexema + menu_txt[i]
                    save_lex = lexema

            elif (char == ";"):
                estado = 13 
                columT = colum - int(len(lexema))
                if (controlP == 1): # numero entero
                    price = str(lexema) + ".00"

                elif (controlP == 2): # numero y punto 
                    price = str(lexema) + "00"

                elif (controlP == 3): # numero, punto y numero 
                    price = str(lexema + "0")
                
                elif (controlP == 4): # numero con mas decimales
                    lexema = float(lexema)
                    price = float('{0:.2f}'.format(lexema))


                cont_token.append(token(price, row, columT, "Precio de comida"))

                cont_token.append(token(char, row, colum, "Punto y coma"))

                if (save_lexx == True):
                    columTa = colum - int(len(save_lex))
                    cont_error.append(error(row, columTa, char, "Numero invalido"))
                    save_lex = ""
                    save_lexx = False
            elif (char == " "):
                estado = 12

            else: 
                error_menu = True
                save_lex = save_lex + menu_txt[i]
             
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 13): # ***** ESTADO 13 *****
            colum = colum + 1 
            

            if (char == "'"):
                estado = 3
                controlE = 4
                
                cont_token.append(token(char, row, colum, "Comilla simple"))
                controlP = 0
                lexema = ""
            
            elif (char == " "):
                estado = 13
                
            else: 
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))
        
        elif (estado == 14): # ***** ESTADO 14 *****
            colum = colum + 1

            if (char == "\n"):
                estado = 15
                
                cont_token.append(token("\\n", row, colum, "Salto de linea"))
                row = row + 1
                colum = 0
                
            elif (char == " "):
                estado = 14

            else: 
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

        elif (estado == 15): # ***** ESTADO 15 *****
            colum = colum + 1
            if (char == "\n"):
                estado = 15
                
                cont_token.append(token("\\n", row, colum, "Salto de linea"))
                row = row + 1
                colum = 0
            
            elif (char == "'"):
                estado = 3
                controlE = 2
                cont_token.append(token(char, row, colum, "Comilla simple"))
                lexema = ""

            elif (char == "["):
                estado = 7 
                cont_token.append(token(char, row, colum, "Corchete abierto"))
                controlE = 3
            
            elif (char == "("):
                estado = 7
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))

            elif (char == " "):
                estado = 15

            else: 
                error_menu = True
                cont_error.append(error(row, colum, char, "Caracter invalido"))
                




                
            
            

                    



        



        



            
          





            

            


                
            





            



        

       


        


        
            
            



        



        
        #--------------------------
        i = i + 1 #contador del afd
        #--------------------------


    if (error_menu == True):
        ReportError()
                    
    else:
        showMenu()
    

def mostrarMenu ():
    html = open('proyecto1_menu.html','w')
    html.write("Nombre de restaurante: "+str(restaurante[0]))
    html.write("<br>")
    inicio ="""
    <html>
    <head>
    
    <title>Menu - P1</title>
    </head>
    <style type="text/css">
    table {
        width: 90%;
        background-color: white;
        text-align: left;
        border-collapse: collapse;
    }
    th, td{
        padding: 15px;
    }
    body{
        background-color: #58D68D;
        font-family: Arial;
    }
    thead{
        background-color: #246355;
        color: white;
        border-bottom: solid 5px #0F362D;
    }
    tr:nth-child(even){
        background-color: #ddd ;
    }
    tr:hover td{
        background-color: #369681;
        color: white;
    }
    div{
        background-color: #1D8348;
        font-family: Arial;
        width: 100%;
    }
    *{
        margin: 0px;
        padding: 0px;
    }
    </style>
    
    <body>
    <center>
    <div>
    <br>
    <br>
    <h1>Lenguajes Formales y de Programación</h1>
    <h3>Victor Alejandro Cuches de León   201807307</h3>
    <h3>Grupo B</h3>
    <br>
    <br>
    </div>
    <br>
   
    
    <table >
       <thead>
        <tr>
            <th>Seccion</th>
            <th>Identificador</th>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Descripcion</th>
        </tr>

       </thead> 
       
    """
    final="""
    <br>
    </table>
    </center>
    </body>
    </html>
    """
    html.write(inicio)
    
    no = 0
    for m in cont_menu:
        no = no + 1

        html.write("<tr>")
        html.write("<td>"+str(m.seccion)+"</td>")
        html.write("<td>"+str(m.identifi)+"</td>")
        html.write("<td>"+str(m.nombre)+"</td>")
        html.write("<td>"+str(m.precio)+"</td>")
        html.write("<td>"+str(m.descrip)+"</td>")
        html.write("</tr>")

       
    
    html.write(final)
    
    
    
    html.close()
    webbrowser.open_new_tab('proyecto1_menu.html')#Abrir automaticamente el html con los datos


def orden_afd(orden_txt):
    #para manejar el afd
    estado = 0
    chara = ""
    lexma = ""
    #para guardar en la clase Cliente
    cliente =""
    nit = ""
    address =""
    propin = ""
    #para guardar en la clase Factura
    canti = 0
    id_F = ""
    #para el reporte de tokens y errores 
    rowo = 1 
    columa = int(0)
    #para el reporte de errores
    descripcF =""
    caracF = "" #pendiente 
    #control de decimales
    controlD = 0
    punto = False

    #control para guardar identificadores con errores y reportarlos
    idError = False
    space = False
    #control errores
    error_orden = False
        
    i = 0
    while ( i<len(orden_txt)):
        chara = orden_txt[i] #tomando el respectivo caracter para evaluarlo

        if (estado == 0): # ***** ESTADO 0 *****
            columa = columa + 1
            if (chara == "'"):
                estado = 1
                cont_token.append(token(chara, rowo, columa, "Comilla simple"))
            
            elif (chara == " "):
                estado = 0

            else: 
                #si viene un caracter no valido, lo marca como error 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif(estado == 1): # ***** ESTADO 1 *****
            columa = columa + 1 
            if letra(chara):
                estado = 2
                lexma = lexma + orden_txt[i]
            
            elif(chara == " "):
                estado = 1
            
            else: 
                #si viene un caracter no valido, lo marca como error 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif(estado == 2): # ***** ESTADO 2 *****
            columa = columa + 1
            if letra(chara):
                estado = 2
                lexma = lexma + orden_txt[i]
            
            elif(chara == " "):
                estado = 2
                lexma = lexma + orden_txt[i]
            
            elif (chara == "'"):
                estado = 3
                cliente = lexma
                columaT = columa - int(len(lexma))
                cont_token.append(token(lexma, rowo, columaT, "Nombre de cliente"))
                cont_token.append(token(chara, rowo, columa, "Comilla simple"))
                #PENDIENTE DE REVISION
                lexma = ""

            else: 
                #si viene un caracter no valido, lo marca como error 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif (estado == 3): # ***** ESTADO 3 *****
            columa = columa + 1
            if (chara == " "):
                estado = 3
            
            elif(chara == ","):
                estado = 4
                cont_token.append(token(chara, rowo, columa, "Coma"))

            else: 
                #si viene un caracter no valido, lo marca como error 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 4): # ***** ESTADO 4 *****
            columa = columa + 1 
            if (chara == " "):
                estado = 4
            
            elif (chara == "'"):
                estado = 5
                cont_token.append(token(chara, rowo, columa, "Comilla simple"))

            else: 
                #si viene un caracter no valido, lo marca como error 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 5): # ***** ESTADO 5 *****
            columa = columa + 1
            if numero(chara):
                estado = 6
                lexma = lexma + orden_txt[i]
            
            elif (chara == " "):
                estado = 5

            else: 
                #si viene un caracter no valido, lo marca como error 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif (estado == 6): # ***** ESTADO 6 *****
            #PENDIENTE DE CAMBIOS YA QUE NO SE SI COMO USAR EL GUION (-)
            columa = columa + 1
            if numero(chara):
                estado = 6
                lexma = lexma + orden_txt[i]

            elif (chara == "-"):
                estado = 6 
                lexma = lexma + orden_txt[i]

            elif (chara == " "):
                estado = 6
                #si viene un caracter no valido, lo marca como error 
                #cont_error.append(error(rowo, columa, chara, "Espacio en blanco invalido"))
            
            elif (chara == "'"):

                estado = 7
                nit = lexma 
                columaT = columa - int(len(lexma))

                cont_token.append(token(nit, rowo, columaT, "NIT de cliente"))                
                cont_token.append(token(chara, rowo, columa, "Comilla simple"))
                #PENDIENTE DE REVISION
                lexma = ""

            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 7): # ***** ESTADO 7 *****
            columa = columa + 1 
            if (chara == ","):
                estado = 8
                cont_token.append(token(chara, rowo, columa,"Coma"))
            
            elif (chara == " "):
                estado = 7 
            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 8): # ***** ESTADO 8 *****
            columa = columa + 1 
            if (chara == "'"):
                estado = 9
                cont_token.append(token(chara, rowo, columa, "Comilla simple"))

            elif (chara == " "):
                estado = 8

            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif (estado == 9): # ***** ESTADO 9 *****
            columa = columa + 1
            if letra(chara):
                estado = 10
                lexma = lexma + orden_txt[i]

            elif (chara == " "):
                estado = 9
            
            else:
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif (estado == 10): # ***** ESTADO 10 *****
            columa = columa + 1
            if letra(chara):
                estado = 10
                lexma = lexma + orden_txt[i]
            
            elif(chara == " " or chara == "." or chara == "-" or chara == ","): #tomando en cuenta los signos que pueden venir en una direccion
                estado = 10
                lexma = lexma + orden_txt[i]
            
            elif (chara == "'"):
                estado = 11 
                address = lexma 
                columaT = columa - int(len(lexma))

                cont_token.append(token(address, rowo, columaT, "Direccion del cliente"))                
                cont_token.append(token(chara, rowo, columa, "Comilla simple"))

                lexma = ""

            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif (estado == 11): # ***** ESTADO 11 *****
            columa = columa + 1 
            if (chara == ","):
                estado = 12
                cont_token.append(token(chara, rowo, columa, "Coma"))

            elif (chara == " "):
                estado = 11
            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 12): # ***** ESTADO 12 *****
            #empieza la lectura de la propina
            columa = columa + 1 
            if numero(chara):
                estado = 13
                lexma = lexma + orden_txt[i]
            
            elif (chara == " "):
                estado = 12
            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
            
        elif (estado == 13): # ***** ESTADO 13 *****
            columa = columa + 1
            
            if numero(chara):
                estado = 13
                lexma = lexma + orden_txt[i]

            elif (chara == "."):
                estado = 14 
                lexma = lexma + orden_txt[i]
                cont_token.append(token(chara, rowo, columa, "Punto"))
                controlD = 2
            
            elif(chara == "%"):
                estado = 15
                controlD = 1
                #guardo el numero sin el signo 
                propin = lexma 
                vali_propin = float(propin)
                #validando que la propina sea entre 0 a 100%
                if (float(vali_propin) > 100 or float(vali_propin) < 0):
                    error_orden = True
                    columaT = columa - int(len(lexma)) 
                    cont_error.append(error(rowo, columaT, propin +"%", "Propina excede del limite"))
               

                cont_token.append(token(chara, rowo, columa, "Signo de porcentaje"))
            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif (estado == 14): # ***** ESTADO 14 *****
            columa = columa + 1
            if numero(chara):
                if (punto == False):

                    estado = 14
                    lexma = lexma + orden_txt[i]
                    controlD = 3
                    punto = True
                
                else: 
                    estado = 14
                    lexma = lexma + orden_txt[i]
                    controlD = 4



            elif (chara == "%"):
                estado = 15
                propin = lexma 
                #validando que la propina sea entre 0 a 100%
                vali_propin = float(propin)
                if (float(vali_propin) > 100 or float(vali_propin) < 0):
                    error_orden = True
                    columaT = columa - int(len(lexma)) 
                    cont_error.append(error(rowo, columaT, propin+"%", "Propina excede del limite"))


                
                cont_token.append(token(chara, rowo, columa, "Signo de porcentaje"))
                
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 15): # ***** ESTADO 15 *****
            columa = columa + 1

            columaT = columa - int(len(lexma))
            if (controlD == 1): #numero entero 
                lexma = str(lexma) + ".00"
            
            elif (controlD == 2): #numero y punto
                lexma = str(lexma) + "00"
            
            elif (controlD == 3): #numero, punto y numero
                lexma = str(lexma) + "0"

            elif (controlD == 4): #numero con mas decimales
                lexma = float(lexma)

            cont_token.append(token(lexma, rowo, columaT, "Propina"))
            #cont_token.append(token("%", rowo, columa, "Signo de porcentaje"))

            if (chara == "\n"):
                estado = 16
                lexma = ""
                

                cont_cliente.append(clienteF(cliente, nit, address, propin))
                cont_token.append(token("\\n", rowo, columa, "Salto de linea"))
                #Termino de leer los datos del cliente
                rowo = rowo + 1
                columa = 0
               

                

            elif (chara == " "):
                estado = 15
            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))


        elif (estado == 16): # ***** ESTADO 16 *****
            columa = columa + 1 
            if (chara == "\n"):
                estado = 16
                rowo = rowo + 1
                columa = 0
            
            elif numero(chara):
                estado = 17 
                lexma = lexma + orden_txt[i]

            elif (chara == " "):
                estado = 16
            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 17): # ***** ESTADO 17 *****
            columa = columa + 1

            if numero(chara):
                estado = 17 
                lexma = lexma + orden_txt[i]
            
            elif (chara == ","):
                estado = 18
                canti = int(lexma)
                columaT = columa - int(len(lexma))

                cont_token.append(token(canti, rowo, columaT, "Cantidad de pedido"))
                cont_token.append(token(chara, rowo, columa, "Coma"))
                lexma = ""
                
            elif (chara == " "):
                estado = 20

            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))

        elif (estado == 18): # ***** ESTADO 18 *****
            columa = columa + 1

            if letra(chara): 
                estado = 19
                lexma = lexma + orden_txt[i]

            elif (chara == " "):
                estado = 18 
            
            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))
        
        elif (estado == 19): # ***** ESTADO 19 *****
            columa = columa + 1
            
            

            if letra(chara):
                estado = 19
                lexma = lexma + orden_txt[i]
                lexma2 = lexma 
            
            elif numero(chara):
                estado = 19
                lexma = lexma + orden_txt[i]
                lexma2 = lexma 
            
            elif (chara == "_"):
                estado = 19
                lexma = lexma + orden_txt[i]
                lexma2 = lexma 

            elif (chara == " "):
                estado = 19 
                space = True



                cont_error.append(error(rowo, columa, chara, "Espacio en blanco invalido"))
            
            elif (chara == "\n"):
                estado = 16 
                id_F = lexma 
                columaT = columa - int(len(lexma))
                if (idError == True):
                    idError = False
                    
                    
                    #guardando para los reportes de tokens y errores
                    cont_token.append(token(id_F, rowo, columaT, "Identificador de pedido (invalido)"))
                    cont_token.append(token("\\n", rowo, columa, "Salto de linea"))
                    cont_error.append(error(rowo, columaT, id_F, "Identificador desconocido"))

                    #guardando en la clase de factura
                    cont_factura.append(factura(canti, id_F))

                    #reseteando variables
                    lexma = ""
                    canti = 0
                    id_F = ""
                  

                    rowo = rowo + 1
                    columa = 0
                else:
                    #guardando para los reportes de tokens y errores
                    cont_token.append(token(id_F, rowo, columaT, "Identificador de pedido"))
                    cont_token.append(token("\\n", rowo, columa, "Salto de linea"))

                    #guardando en la clase de factura
                    cont_factura.append(factura(canti, id_F))

                    #reseteando variables
                    lexma = ""
                    canti = 0
                    id_F = ""
                  

                    rowo = rowo + 1
                    columa = 0
                    idError = False


            else: 
                if (space == False):
                    idError = True
                    lexma = lexma + orden_txt[i]
                    error_orden = True
                    cont_error.append(error(rowo, columa, chara, "Caracter desconocido"))
                else:
                    error_orden = True
                    cont_error.append(error(rowo, columa, chara, "Caracter desconocido"))

        elif(estado == 20): # ***** ESTADO 20 *****
            columa = columa + 1
            if (chara == " "):
                estado = 20

            elif (chara == ","):
                estado = 18 
                canti = int(lexma)
                columaT = columa - int(len(lexma))

                cont_token.append(token(canti, rowo, columaT, "Cantidad de pedido"))
                cont_token.append(token(chara, rowo, columa, "Coma"))

            else: 
                error_orden = True
                cont_error.append(error(rowo, columa, chara, "Caracter no valido"))




        i = i + 1


    if (error_orden == False):
        showFactura()
    else:
        ReportError()       

def mostrarFactura():
    html = open('proyecto1_factura.html','w')
   
    html.write("<br>")
    for f in cont_cliente:
    
        html.write("<h1>DATOS DEL CLIENTE</h1>")
        html.write("Nombre: "+str(f.nombreC))
        html.write("<br>")
        html.write("NIT: "+str(f.nit))
        html.write("<br>")
        html.write("Direccion: "+str(f.direcc))
        html.write("<br>")
        html.write("Propina: "+str(f.propina)+"%")
        

       
    
 
    
    
    
    html.close()
    webbrowser.open_new_tab('proyecto1_factura.html')#Abrir automaticamente el html con los datos

def ReportPrueba():
    html = open('proyecto1_token.html','w')
    #html.write("Nombre de restaurante: "+str(restaurante[0]))
    html.write("<br>")
    inicio ="""
    <html>
    <head>
    
    <title>Tokens - P1</title>
    </head>
    <style type="text/css">
    table {
        width: 90%;
        background-color: white;
        text-align: left;
        border-collapse: collapse;
    }
    th, td{
        padding: 15px;
    }
    body{
        background-color: #58D68D;
        font-family: Arial;
    }
    thead{
        background-color: #246355;
        color: white;
        border-bottom: solid 5px #0F362D;
    }
    tr:nth-child(even){
        background-color: #ddd ;
    }
    tr:hover td{
        background-color: #369681;
        color: white;
    }
    div{
        background-color: #1D8348;
        font-family: Arial;
        width: 100%;
    }
    *{
        margin: 0px;
        padding: 0px;
    }
    </style>
    
    <body>
    <center>
    <div>
    <br>
    <br>
    <h1>REPORTE DE TOKENS</h1>
    <h3>Victor Alejandro Cuches de León   201807307</h3>
    <h3>Grupo B</h3>
    <br>
    <br>
    </div>
    <br>
   
    
    <table >
       <thead>
        <tr>
            <th>No.</th>
            <th>Lexema</th>
            <th>Fila</th>
            <th>Columna</th>
            <th>Token</th>
        </tr>

       </thead> 
       
    """
    final="""
    <br>
    </table>
    </center>
    </body>
    </html>
    """
    html.write(inicio)
    
    no = 0
    for i in cont_token:
        no = no + 1

        html.write("<tr>")
        html.write("<td>"+str(no)+"</td>")
        html.write("<td>"+str(i.lexeme)+"</td>")
        html.write("<td>"+str(i.fila)+"</td>")
        html.write("<td>"+str(i.columna)+"</td>")
        html.write("<td>"+str(i.tokeno)+"</td>")
        html.write("</tr>")



       
    
    html.write(final)
    
    
    
    html.close()
    webbrowser.open_new_tab('proyecto1_token.html')#Abrir automaticamente el html con los datos


def ReportError():
    html = open('proyecto1_error.html','w')
    #html.write("Nombre de restaurante: "+str(restaurante[0]))
    html.write("<br>")
    inicio ="""
    <html>
    <head>
    
    <title>Errores - P1</title>
    </head>
    <style type="text/css">
    table {
        width: 90%;
        background-color: white;
        text-align: left;
        border-collapse: collapse;
    }
    th, td{
        padding: 15px;
    }
    body{
        background-color: #58D68D;
        font-family: Arial;
    }
    thead{
        background-color: #246355;
        color: white;
        border-bottom: solid 5px #0F362D;
    }
    tr:nth-child(even){
        background-color: #ddd ;
    }
    tr:hover td{
        background-color: #369681;
        color: white;
    }
    div{
        background-color: #1D8348;
        font-family: Arial;
        width: 100%;
    }
    *{
        margin: 0px;
        padding: 0px;
    }
    </style>
    
    <body>
    <center>
    <div>
    <br>
    <br>
    <h1>REPORTE DE ERRORES</h1>
    <h3>Victor Alejandro Cuches de León   201807307</h3>
    <h3>Grupo B</h3>
    <br>
    <br>
    </div>
    <br>
   
    
    <table >
       <thead>
        <tr>
            <th>No.</th>
            <th>Fila</th>
            <th>Columna</th>
            <th>Caracter</th>
            <th>Descripción</th>
        </tr>

       </thead> 
       
    """
    final="""
    <br>
    </table>
    </center>
    </body>
    </html>
    """
    html.write(inicio)
    
    no = 0
    for i in cont_error:
        no = no + 1

        html.write("<tr>")
        html.write("<td>"+str(no)+"</td>")
        html.write("<td>"+str(i.fila)+"</td>")
        html.write("<td>"+str(i.columna)+"</td>")
        html.write("<td>"+str(i.caracte)+"</td>")
        html.write("<td>"+str(i.descripci)+"</td>")
        html.write("</tr>")


    html.write(final)
    
    
    
    html.close()
    webbrowser.open_new_tab('proyecto1_error.html')#Abrir automaticamente el html con los datos


def showMenu():
    html = open('MENU.html','w')
    

    parte1 = """
    <html>
	<head>
		<title>Menu</title>
	</head>
    <style type="text/css">
    body{
        background: url("img/p12.jpg");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    @font-face{
        font-family:  Avocado Creamy;
        src: url(fuentes/Avocado\ Creamy.otf);
    }
    #name{
        background-color: gray;
        width: 100%;
        opacity: 0.8;
      

        font-family: Avocado Creamy;
        font-size: 30;
         
    }
    #contenido{
        background-color: gray;
       
        opacity: 0.8;
        
        
        width: 100%;
        
    }
    table, td{
        border: 3px solid black;
        border-collapse: collapse;
        align-items: center;
        
    }
    td{
        padding: 10px;
    }
    #pricee{
        text-align: center;
    }
   
    </style>
	<body>
        <center>
            <div id="name">
            <br>
    """
    
    parte2 = """
        <br>
            </div> 
        </center>
        <br>
        <div id="contenido">
            <center>
            <br>
    """
    parte3 = """
    <br>
            <table style="width: 80%">
    """
    parte4 = """
        <br>
        <br>
        </center>

        </div>
        
	</body>
    </html>

    """

    html.write(parte1)
    html.write("<h1>"+str(restaurante[0])+"</h1>")
    html.write(parte2)

    first = False
    for i in cont_menu:
    
        if (first == False):
            html.write("<h3>"+str(i.seccion)+"</h3>")
            secA = i.seccion
            first = True
        else:
            if (i.seccion != secA):
                html.write("<h3>"+str(i.seccion)+"</h3>")
                secA = i.seccion

    #html.write("<h3>"+"SECCION"+"</h3>") #PENDIENTE DE CAMBIOS!!!

        html.write(parte3)

    #PARTE DEL FOR
        html.write("<tr>")
        html.write("<td width="+"85%"+" height="+"20px"+">")
        html.write("<b>"+str(i.nombre)+"</b>") #AQUI VA EL NOMBRE DE LA COMIDA
        html.write("</td>")
        html.write("<td rowspan="+"2"+" id="+"pricee"+">")
        html.write("<font size = "+"5"+"><b>"+"Q. "+str(i.precio)+"</b></font>") #AQUI VA EL PRECIO
        html.write("</td>")
        html.write("</tr>")
        html.write("<tr>")
        html.write("<td width="+"85%"+" height="+"20px"+">")
        html.write("<b>"+str(i.descrip)+"</b>") #AQUI VA LA DESCRIPCION DE LA COMIDA
        html.write("</td>")
        html.write("</tr>")

        html.write("</table>")
       



    html.write(parte4)


    html.close()
    webbrowser.open_new_tab('MENU.html')#Abrir automaticamente el html con los datos


def showFactura():
    html = open('FACTURA.html','w')

    partea = """
    <html>
	<head>
		<title>Factura</title>
	</head>
    <style type="text/css">

    body{
        background-color: #DFDBE5;
        background-image: url("data:image/svg+xml,%3Csvg width='42' height='44' viewBox='0 0 42 44' xmlns='http://www.w3.org/2000/svg'%3E%3Cg id='Page-1' fill='none' fill-rule='evenodd'%3E%3Cg id='brick-wall' fill='%239C92AC' fill-opacity='0.4'%3E%3Cpath d='M0 0h42v44H0V0zm1 1h40v20H1V1zM0 23h20v20H0V23zm22 0h20v20H22V23z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }
    #cuadro{
        background-color: white;
        width: 50%;
        border: 4px solid black;
    }
    #datos{
        text-align: left;
        padding-left: 30px;
    }
    #tablaa{
        
        padding-left: 30px;
        padding-right: 30px;
    }
    table{
        width: 100%;
      

    }
    th, td{
        text-align: left;
       
    }
    td{
        padding-top: 10px;
        padding-bottom: 10px;
    }
    #abajo{
        
        border-bottom: 1px solid black;

    }
    #arriba{
        border-top: 1px solid black;
    }
    

    </style>


    <body>
        <br>
       <br>

        <center>
            <div id="cuadro">
                <section>


    """
    parteb = """
    </section>
                <section id="datos">
                    <br>
                    Datos del cliente
                    <br>
    """
    partec = """
    <br>
                    <br>
                    Descripción
                    <br>
                    <br>
                </section>
                <section id="tablaa">
                    <table>
                    <tr>
                            <th>Cantidad</th>
                            <th>Concepto</th>
                            <th>Precio</th>
                            <th>Total</th>
                        </tr>

    """

    parted = """

    </table>
                </section>
                <br>
                <br>
                
                
            </div>

        </center>
        <br>
        <br>
        

    </body>
    </html>
    """
    fecha = datetime.datetime.now()
    fecha = fecha.strftime('%d/%m/%Y')
    html.write(partea)
    html.write("<br>")
    html.write(str(restaurante[0]))
    html.write("<br>"+"Factura No. 01"+"<br>") #PENDIENTEEEEEEEE
    html.write("Fecha: "+str(fecha))#PENDIENTEEEEEE
    html.write(parteb)
    propi = ""
    for q in cont_cliente:

        html.write("Nombre: "+str(q.nombreC))
        html.write("<br>")
        html.write("NIT: "+str(q.nit))
        html.write("<br>")
        html.write("Dirección: "+str(q.direcc))
        html.write("<br>")
        propi = q.propina
    
    html.write(partec)

    list_comida = []
    list_id = []
    list_precios = []
    for n in cont_menu:
        list_comida.append(n.nombre)
        list_id.append(n.identifi)
        list_precios.append(n.precio)
        
    #PENDIENTEEEEEEEEEEEEEE
    subtotal = 0
    for h in cont_factura:
        for l in range(len(list_comida)):
            if (h.idenF == list_id[l]):

                html.write("<tr>")
                html.write("<td width="+"15%"+">"+str(h.cantidad)+"</td>")
                html.write("<td width="+"45%"+">"+str(list_comida[l])+"</td>")
                html.write("<td width="+"20%"+">"+str(list_precios[l])+"</td>")
                total = float(list_precios[l]) * int(h.cantidad)
                html.write("<td width="+"20%"+">"+str(total)+"</td>")
                html.write("</tr>")
                subtotal = subtotal + total


        




    html.write("</table>")
    html.write("<table>")
    html.write("<tr>")
    html.write("<td width="+"80%"+" id="+"arriba"+">Subtotal</td>")
    html.write("<td width="+"20%"+" id="+"arriba"+">"+str(subtotal)+"</td>")   
    html.write("</tr>")
    r_propina = float(subtotal) * (float(propi)/100)
    r_propina = float('{0:.2f}'.format(r_propina))

    html.write("<tr>")
    html.write("<td width="+"80%"+" id="+"abajo"+">Propina ("+propi+"%)"+"</td>")
    html.write("<td width="+"20%"+" id="+"abajo"+">"+str(r_propina)+"</td>")   
    html.write("</tr>")
    s_total = float(subtotal) + float(r_propina)
    s_total = float('{0:.2f}'.format(s_total))
    html.write("<tr>")
    html.write("<td width="+"80%"+">Total</td>")
    html.write("<td width="+"20%"+">"+str(s_total)+"</td>")   
    html.write("</tr>")


    html.write(parted)



    html.close()
    webbrowser.open_new_tab('FACTURA.html')#Abrir automaticamente el html con los datos
    

def showArbol():

    with open("file_.dot", mode="w") as t:
        t.write("digraph arbolP1{\n")

        t.write("\""+str(restaurante[0]) +"\""+ "[shape = box] \n")

        first = False
        for i in cont_menu:
    

            if (first == False):
                precio_ = str(i.precio)
                nodo = str(i.nombre) + " | " + str(i.descrip) + " | Q. " + precio_
                t.write("\""+str(restaurante[0])+"\""+" -> "+"\""+i.seccion+"\""+"\n")
                t.write("\""+str(i.seccion)+"\""+"->"+"\""+nodo+"\""+"\n")
                secA = i.seccion
                first = True

            else:
                if (i.seccion != secA):
                    precio_ = str(i.precio)
                    nodo = str(i.nombre) + " | " + str(i.descrip) + " | Q. " + precio_
                    t.write("\""+str(restaurante[0])+"\""+" -> "+"\""+i.seccion+"\""+"\n")
                    t.write("\""+str(i.seccion)+"\""+" -> "+"\""+nodo+"\""+"\n")
                    secA = i.seccion
                else:
                    precio_ = str(i.precio)
                    nodo = str(i.nombre) + " | " + str(i.descrip) + " | Q. " + precio_
                    
                    t.write("\""+str(i.seccion)+"\""+" -> "+"\""+nodo+"\""+"\n")
            


        t.write("}")

    #os.system('dot -Tpdf file_t1.dot -o grafo_t1.pdf')
    os.system("dot -Tpdf \"" + os.path.abspath("file_.dot") + "\" -o \"" + os.path.abspath("file_.pdf") + "\" -Gcharset=utf-8")

    os.startfile(os.path.abspath("file_.pdf"))













            






    

#===================== M A I N ===================== 
opc_menu = 0
#variables que me funcionaran como switch en el limite del precio
menu_ready = False
orden_ready = False
menu2_ready = False
#varibles que guardaran el contenido de los archivos 
texto_orden = ""
texto_menu = ""
#listas donde guardare el contenido de menu y factura, para luego usarlas en el html
cont_menu = []
cont_factura = []
cont_token = []
cont_error = []
cont_cliente = []
#guardando el nombre del restaurante
restaurante = []
#control de errores en el menu y orden
#error_menu = False
#error_orden = False

while(opc_menu!=6):
    print("==========================================")
    print("------------------------------------------")
    print("            PROYECTO 1 - LFP")
    print(" Lenguajes Formales y de Programación B-")
    print("Victor Alejandro Cuches de León 201807307")
    print("------------------------------------------")
    print("==========================================\n")
    print("Menu principal")
    print("1. Cargar Menu ")
    print("2. Cargar orden ")
    print("3. Generar menu")
    print("4. Generar factura")
    print("5. Generar arbol")
    print("6. Salir")
    opc_menu = int(input("Selecione una opcion: "))
    print("")
    if (opc_menu == 1):
        print("============ C A R G A R  M E N U ============")
        nameFile_menu = filedialog.askopenfilename(title = "Seleccione archivo", filetypes = (( "*.txt", "*.lfp"),))
        txt_file_m = open(nameFile_menu, "r", encoding="utf-8")
        with txt_file_m as fil: #para leer linea por linea del archivo
            texto_menu = fil.read()

        texto_menu = texto_menu + " " #contendra todo el contenido para luego usar el afd

        txt_file_m.close()
        menu_ready = True #para saber si ya esta el menu cargado y realizar el menu y arbol
        print("¡Se ha cargado con exito el menu!")

    elif(opc_menu == 2):
        print("============ C A R G A R  O R D E N ============")
        nameFile_orden = filedialog.askopenfilename(title = "Seleccione archivo", filetypes = (( "*.txt", "*.lfp"),))
        txt_file_o = open(nameFile_orden, "r", encoding="utf-8")
        with txt_file_o as filo: #para leer linea por linea del archivo
            texto_orden = filo.read()

        texto_orden= texto_orden + " " #contendra todo el contenido para luego usar el afd

        txt_file_o.close()
        orden_ready = True #para saber si ya esta la orden cargada y realizar la factura
        print("¡Se ha cargado con exito la orden!")
        


    elif(opc_menu == 3):
        limit_precio = False #para saber si acepto limite en precios o no y filtrar mientras se guardan los datos, es como un switch
        limite = 0 #cantidad de precio limite
        print("============ M E N U ============")
        if (menu_ready == True):
            print("¿Desea poner un limite en los precios? (Si/No)")
            respuesta = input()

            if (respuesta.upper()=="SI"):
                limit_precio = True
                limite = int(input("Ingrese el limite de precios: "))
                menu_afd(texto_menu, limite, limit_precio)
                #mostrarMenu()
                menu2_ready = True                
                    
             

            elif (respuesta.upper()=="NO"):
                print("Se le mostraran todas las opciones del menu")
                menu_afd(texto_menu, limite, limit_precio)
                #mostrarMenu()
                menu2_ready = True
                
                
                

            else:
                print("Selccione una respuesta correcta, Si o No")
            
            
            
        else: 
            print("Debe cargar el menu para ejecutar esta opcion")

        #mostrar el menu en html

    elif(opc_menu == 4):
        print("============ F A C T U R A ============")

        if(orden_ready==True):
            print("Se esta generando la orden")
            orden_afd(texto_orden)
            #mostrarFactura()
            #metodo para leer y luego generar la orden
            
            


        else :
            print("Debe cargar la orden para ejecutar esta opcion")
       

    elif(opc_menu == 5):
        print("============ A R B O L ============")
        if(menu_ready==True):
            if (menu2_ready == True):

                print("Se esta generando el arbol")
                #mostrar arbol en pdf
                showArbol()
            else:
                limit_precio = False #para saber si acepto limite en precios o no y filtrar mientras se guardan los datos, es como un switch
                limite = 0 #cantidad de precio limite
                print("¿Desea poner un limite en los precios? (Si/No)")
                respuesta = input()

                if (respuesta.upper()=="SI"):
                    limit_precio = True
                    limite = int(input("Ingrese el limite de precios: "))
                    menu_afd(texto_menu, limite, limit_precio)
                    #mostrarMenu()
                    showArbol()
                    menu2_ready = True                
                    
             

                elif (respuesta.upper()=="NO"):
                    print("Se le mostraran todas las opciones del menu")
                    menu_afd(texto_menu, limite, limit_precio)
                    #mostrarMenu()
                    showArbol()
                    menu2_ready = True
                                

                else:
                    print("Selccione una respuesta correcta, Si o No")


        else :
            print("Debe cargar el menu para ejecutar esta opcion")

    elif(opc_menu == 6):
        ReportPrueba()
       
        
        print("........................................")
        print("Lenguajes Formales y de Programacion B-")
        print("Nombre: Victor Alejandro Cuches de León")
        print("Carnet: 201807307")
        print("Correo: vcuches55@gmail.com")
        input("adios...")
    
    elif(opc_menu == 7):
        if(menu_ready == True):

            mostrarMenu()
        elif(orden_ready == True):

            mostrarFactura()

    elif (opc_menu == 8):
        #alternativa para mostrar el menu correcto
        showMenu()
    elif (opc_menu == 9):
        #alternativa para mostrar la factura correcta
        showFactura()
    elif (opc_menu == 10):
        #alternativa para mostrar el arbol
        showArbol()
    elif(opc_menu<1 or opc_menu>10):
        print("Seleccione una opcion correcta")




