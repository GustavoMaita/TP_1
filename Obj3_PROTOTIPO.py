<<<<<<< HEAD
from tkinter import Tk, Frame, Label, Entry, Button, messagebox
import doctest

def devolver_valor(clave):
    valores_fijos = {
        # VENTANA PRINCIPAL - VALORES FIJOS NO HARDCODEADOS
        "icono_vppal": "uba.ico",
        "titulo_vppal": "TP Grupal Parte 1 - Grupo: PROTOTIPO",
        "color_vppal": "grey",
        
        "ancho_frame_vppal": 430,
        "alto_frame_vppal": 200,
        "color_frame_vppal": "grey",
        
        "color_etiqueta_vppal": "grey", 
        "texto_etiqueta_1_vppal": "Construido por:\n Gustavo Alfredo Maita\n Agostina Armando\n Selena Escobar\n Guido Tiscornia\n",
        "posicion_etiqueta_1_x_vppal": 140,
        "posicion_etiqueta_1_y_vppal": 95,
        "texto_etiqueta_2_vppal": "Bienvenido a la aplicación de mensajes secretos del grupo PROTOTIPO.\n Para continuar presione continuar, de lo contrario cierre la ventana",
        "posicion_etiqueta_2_x_vppal": 20,
        "posicion_etiqueta_2_y_vppal": 20,
        
        "texto_boton_continuar_vppal": "Continuar",
        "posicion_boton_continuar_x_vppal": 170,
        "posicion_boton_continuar_y_vppal": 65,


        # VENTANA CONTINUAR - VALORES FIJOS NO HARDCODEADOS
        "icono_vcont": "uba.ico",
        "titulo_vcont": "TP Grupal Parte 1 - Grupo: PROTOTIPO",
        
        "ancho_frame_vcont": 430,
        "alto_frame_vcont": 150,
        
        "texto_ingrese_msj_vcont": "Ingrese mensaje:",
        "posicion_ingrese_msj_x_vcont": 20,
        "posicion_ingrese_msj_y_vcont": 20,
        "posicion_cuadrousuario_x_vcont": 160,
        "posicion_cuadrousuario_y_vcont": 20,
        
        "texto_clave_vcont": "Clave:",
        "posicion_clave_x_vcont:": 20,
        "posicion_clave_y_vcont": 40,
        "posicion_cuadroclave_x_vcont": 160,
        "posicion_cuadroclave_y_vcont": 40,
        
        
        # BOTONES - VENTANA CONTINUAR  - VALORES FIJOS NO HARDCODEADOS
        "cifrar_cesar": "Cifrar mensaje\n César",
        "posicion_x_cifrar_cesar": 8,
        "posicion_y_cifrar_cesar": 62,
        
        "descifrar_cesar": "Descifrar mensaje\n César",
        "posicion_x_descifrar_cesar": 206,
        "posicion_y_descifrar_cesar": 62,
        
        "cifrar_atbash": "Cifrar mensaje\n Atbash",
        "posicion_x_cifrar_atbash": 106,
        "posicion_y_cifrar_atbash": 62,
        
        "descifrar_atbash": "Descifrar mensaje\n Atbash",
        "posicion_x_descifrar_atbash": 320,
        "posicion_y_descifrar_atbash": 62,
    }
    return valores_fijos[clave]

def crear_ventana_principal():
#HECHO POR TISCORNIA GUIDO JUAN
    
    raiz = Tk()
    raiz.iconbitmap(devolver_valor("icono_vppal"))
    raiz.title(devolver_valor("titulo_vppal"))
    raiz.resizable(0,0)
    raiz.config(bg=devolver_valor("color_vppal"))

    miFrame = Frame(raiz,width=devolver_valor("ancho_frame_vppal"), height=devolver_valor("alto_frame_vppal"),bg=devolver_valor("color_frame_vppal"))
    miFrame.pack()
    
    Label(miFrame, bg=devolver_valor("color_etiqueta_vppal"), text = (devolver_valor("texto_etiqueta_1_vppal"))).place(x=devolver_valor("posicion_etiqueta_1_x_vppal"), y=devolver_valor("posicion_etiqueta_1_y_vppal"))
    Label(miFrame, text = (devolver_valor("texto_etiqueta_2_vppal"))).place(x=devolver_valor("posicion_etiqueta_2_x_vppal"),y=devolver_valor("posicion_etiqueta_2_y_vppal"))
    
    botonContinuar =Button(raiz,text=devolver_valor("texto_boton_continuar_vppal"), command= lambda: crear_ventana_continuar())
    botonContinuar.place(x=devolver_valor("posicion_boton_continuar_x_vppal") , y=devolver_valor("posicion_boton_continuar_y_vppal"))
    
    raiz.mainloop()

   
def crear_ventana_continuar():
#HECHO POR MAITA GUSTAVO ALFREDO    

    raiz = Tk()
    raiz.iconbitmap(devolver_valor("icono_vcont"))
    raiz.title(devolver_valor("titulo_vcont"))
    miFrame = Frame(raiz,width=devolver_valor("ancho_frame_vcont"), height=devolver_valor("alto_frame_vcont"))

    miFrame.pack()

    Label(raiz, text = (devolver_valor("texto_ingrese_msj_vcont"))).place(x=devolver_valor("posicion_ingrese_msj_x_vcont"),y=devolver_valor("posicion_ingrese_msj_y_vcont"))
    cuadroUsuario = Entry(miFrame)
    cuadroUsuario.place(x=devolver_valor("posicion_cuadrousuario_x_vcont"), y=devolver_valor("posicion_cuadrousuario_y_vcont"))

    Label(miFrame, text = (devolver_valor("texto_clave_vcont"))).place(x=20,y=40)
    cuadroClave = Entry(miFrame)
    cuadroClave.place(x=devolver_valor("posicion_cuadroclave_x_vcont"), y=devolver_valor("posicion_cuadroclave_y_vcont"))
    cuadroClave.config()

    botonCifradoCesar = Button(raiz,text=devolver_valor("cifrar_cesar"), command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
    botonCifradoCesar.place(x=devolver_valor("posicion_x_cifrar_cesar"),y=devolver_valor("posicion_y_cifrar_cesar"))

    botonCifradoAtbash = Button(raiz,text=devolver_valor("cifrar_atbash"), command= lambda: cifrado_atbash(cuadroUsuario))
    botonCifradoAtbash.place(x=devolver_valor("posicion_x_cifrar_atbash"),y=devolver_valor("posicion_y_cifrar_atbash"))

    botonDecifradoCesar = Button(raiz,text=devolver_valor("descifrar_cesar"), command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
    botonDecifradoCesar.place(x=devolver_valor("posicion_x_descifrar_cesar"),y=devolver_valor("posicion_y_descifrar_cesar"))

    botonDecifradoAtbash = Button(raiz,text=devolver_valor("descifrar_atbash"), command= lambda: cifrado_atbash(cuadroUsuario))
    botonDecifradoAtbash.place(x=devolver_valor("posicion_x_descifrar_atbash"),y=devolver_valor("posicion_y_descifrar_atbash"))

    

    raiz.mainloop()

def cifrado_cesar(cuadroUsuario,cuadroClave):
#HECHO POR ARMANDO AGOSTINA BELEN
    """
    >>> cifrado_cesar('hola mundo', '3')
    'krod pxqgr'
    >>> cifrado_cesar("CASA", "2")
    'ECUC'
    >>> cifrado_cesar("BIENVENIDOS", "4")
    'FMIRZIRMHSW'
    >>> cifrado_cesar("argentina vota", "1")
    'bshfoujob wpub'
    """    
    texto = cuadroUsuario.get()
    clave = cuadroClave.get()

    if not texto or not clave: 
        messagebox.showwarning("", "Debe ingresar un mensaje y una clave")
    else:
        
        desplazamiento = int(clave)
        cifrado= ""
    
        for caracter in texto:
            if caracter.isalpha():
                # Cifrar letras
                mayuscula = caracter.isupper()
                caracter = caracter.lower()
                desplazamientoLetra = (ord(caracter) - ord('a') + desplazamiento) % 26
                letraCifrada = chr(ord('a') + desplazamientoLetra)
                if mayuscula:
                    letraCifrada = letraCifrada.upper()
                cifrado += letraCifrada
            elif caracter.isnumeric():
                # Cifrar dígitos numéricos
                caracterNumerico = int(caracter)
                caracterNumericoCifrado = (caracterNumerico + desplazamiento) % 10
                cifrado += str(caracterNumericoCifrado)
            else:
                # Mantener otros caracteres sin cifrar
                cifrado += caracter
            
    return messagebox.showinfo("El mensaje cifrado es:",cifrado )

def cifrado_atbash(cuadroUsuario):
#HECHO POR ESCOBAR SELENA KATHERINE 
    """
    >>> cifrado_atbash("HOLA MUNDO")
    'sloz nfmwl'
    >>> cifrado_atbash("mov2 0234$%%")
    'NLE7 9765$%%'
    >>> cifrado_atbash("234rY( hy")
    '765Ib( SB'
    """
    texto = cuadroUsuario.get()
    cifrado = []
    cifrado = list(texto) #conversion a lista para acceso a elementos
    contador = 0
    
    if not texto: 
        messagebox.showwarning("", "Debe ingresar un mensaje")
    else:
        for contador in range(len(cifrado)): 
            elemento = cifrado[contador] 
            if elemento.isnumeric(): 
                cifrado[contador] = str(9 - int(elemento))

            elif elemento.isalpha(): 
                if elemento.isupper():
                    minuscula = chr(90 - (ord(elemento)-65)) #pasaje de letra mayuscula a minuscula
                    cifrado[contador] = minuscula.lower()
                else:
                    mayuscula = chr(122 - (ord(elemento)-97)) #pasaje de letra minuscula a mayuscula
                    cifrado[contador] = mayuscula.upper()
            else:
                cifrado[contador] = elemento  #el elemento no es caracter ni numero, se deja igual 
            contador +=1 #aumento del indice de la lista para acceder y reemplazar al elemento siguiente
        cifrado = "".join(cifrado) 
              
        return messagebox.showinfo("El mensaje cifrado es:",cifrado)

crear_ventana_principal()

#-----------pruebas con doctest ------------#



print(doctest.testmod())



ventana_principal()
>>>>>>> parent of 53f51c7 (Revert "Revert "Revert "Update and rename Obj3_PROTOTIPO_FINAL.py to Obj3_PROTOTIPO.py""")
