diff a/Obj3_PROTOTIPO.py b/Obj3_PROTOTIPO.py	(rejected hunks)
@@ -1,72 +0,137 @@
-from tkinter import*
-from tkinter import messagebox
-
-
+from tkinter import Tk, Frame, Label, Entry, Button, messagebox
+import doctest
+
+def devolver_valor(clave):
+    valores_fijos = {
+        # VENTANA PRINCIPAL - VALORES FIJOS NO HARDCODEADOS
+        "icono_vppal": "uba.ico",
+        "titulo_vppal": "TP Grupal Parte 1 - Grupo: PROTOTIPO",
+        "color_vppal": "grey",
+        
+        "ancho_frame_vppal": 430,
+        "alto_frame_vppal": 200,
+        "color_frame_vppal": "grey",
+        
+        "color_etiqueta_vppal": "grey", 
+        "texto_etiqueta_1_vppal": "Construido por:\n Gustavo Alfredo Maita\n Agostina Armando\n Selena Escobar\n Guido Tiscornia\n",
+        "posicion_etiqueta_1_x_vppal": 140,
+        "posicion_etiqueta_1_y_vppal": 95,
+        "texto_etiqueta_2_vppal": "Bienvenido a la aplicación de mensajes secretos del grupo PROTOTIPO.\n Para continuar presione continuar, de lo contrario cierre la ventana",
+        "posicion_etiqueta_2_x_vppal": 20,
+        "posicion_etiqueta_2_y_vppal": 20,
+        
+        "texto_boton_continuar_vppal": "Continuar",
+        "posicion_boton_continuar_x_vppal": 170,
+        "posicion_boton_continuar_y_vppal": 65,
 
-def ventana_principal():
 
+        # VENTANA CONTINUAR - VALORES FIJOS NO HARDCODEADOS
+        "icono_vcont": "uba.ico",
+        "titulo_vcont": "TP Grupal Parte 1 - Grupo: PROTOTIPO",
+        
+        "ancho_frame_vcont": 430,
+        "alto_frame_vcont": 150,
+        
+        "texto_ingrese_msj_vcont": "Ingrese mensaje:",
+        "posicion_ingrese_msj_x_vcont": 20,
+        "posicion_ingrese_msj_y_vcont": 20,
+        "posicion_cuadrousuario_x_vcont": 160,
+        "posicion_cuadrousuario_y_vcont": 20,
+        
+        "texto_clave_vcont": "Clave:",
+        "posicion_clave_x_vcont:": 20,
+        "posicion_clave_y_vcont": 40,
+        "posicion_cuadroclave_x_vcont": 160,
+        "posicion_cuadroclave_y_vcont": 40,
+        
+        
+        # BOTONES - VENTANA CONTINUAR  - VALORES FIJOS NO HARDCODEADOS
+        "cifrar_cesar": "Cifrar mensaje\n César",
+        "posicion_x_cifrar_cesar": 8,
+        "posicion_y_cifrar_cesar": 62,
+        
+        "descifrar_cesar": "Descifrar mensaje\n César",
+        "posicion_x_descifrar_cesar": 206,
+        "posicion_y_descifrar_cesar": 62,
+        
+        "cifrar_atbash": "Cifrar mensaje\n Atbash",
+        "posicion_x_cifrar_atbash": 106,
+        "posicion_y_cifrar_atbash": 62,
+        
+        "descifrar_atbash": "Descifrar mensaje\n Atbash",
+        "posicion_x_descifrar_atbash": 320,
+        "posicion_y_descifrar_atbash": 62,
+    }
+    return valores_fijos[clave]
+
+def crear_ventana_principal():
+#HECHO POR TISCORNIA GUIDO JUAN
     
     raiz = Tk()
-    raiz.iconbitmap("uba.ico")
-    raiz.title("TP Grupal Parte 1 - Grupo: PROTOTIPO")
+    raiz.iconbitmap(devolver_valor("icono_vppal"))
+    raiz.title(devolver_valor("titulo_vppal"))
     raiz.resizable(0,0)
-    raiz.config(bg="grey")
+    raiz.config(bg=devolver_valor("color_vppal"))
 
-    miFrame = Frame(raiz,width=430, height=200,bg="grey")
+    miFrame = Frame(raiz,width=devolver_valor("ancho_frame_vppal"), height=devolver_valor("alto_frame_vppal"),bg=devolver_valor("color_frame_vppal"))
     miFrame.pack()
     
-    Label(miFrame, bg="grey", text = ("Construido por:\n Gustavo Alfredo Maita\n Agostina Armando\n Selena Escobar\n Guido Tiscornia\n")).place(x=140, y=95)
-    Label(miFrame, text = ("Bienvenido a la aplicación de mensajes secretos del grupo PROTOTIPO.\n Para continuar presione continuar, de lo contrario cierre la ventana")).place(x=20,y=20)
+    Label(miFrame, bg=devolver_valor("color_etiqueta_vppal"), text = (devolver_valor("texto_etiqueta_1_vppal"))).place(x=devolver_valor("posicion_etiqueta_1_x_vppal"), y=devolver_valor("posicion_etiqueta_1_y_vppal"))
+    Label(miFrame, text = (devolver_valor("texto_etiqueta_2_vppal"))).place(x=devolver_valor("posicion_etiqueta_2_x_vppal"),y=devolver_valor("posicion_etiqueta_2_y_vppal"))
     
-    botonContinuar =Button(raiz,text="Continuar", command= lambda: ventana_continuar())
-    botonContinuar.place(x=170 , y=65)
+    botonContinuar =Button(raiz,text=devolver_valor("texto_boton_continuar_vppal"), command= lambda: crear_ventana_continuar())
+    botonContinuar.place(x=devolver_valor("posicion_boton_continuar_x_vppal") , y=devolver_valor("posicion_boton_continuar_y_vppal"))
     
     raiz.mainloop()
 
-
-
-    
-    
-def ventana_continuar():
-    
+   
+def crear_ventana_continuar():
+#HECHO POR MAITA GUSTAVO ALFREDO    
 
     raiz = Tk()
-    raiz.iconbitmap("uba.ico")
-    raiz.title("TP Grupal Parte 1 - Grupo: PROTOTIPO")
-    miFrame = Frame(raiz,width=430, height=150)
+    raiz.iconbitmap(devolver_valor("icono_vcont"))
+    raiz.title(devolver_valor("titulo_vcont"))
+    miFrame = Frame(raiz,width=devolver_valor("ancho_frame_vcont"), height=devolver_valor("alto_frame_vcont"))
 
     miFrame.pack()
 
-    Label(raiz, text = ("Ingrese mensaje:")).place(x=20,y=20)
+    Label(raiz, text = (devolver_valor("texto_ingrese_msj_vcont"))).place(x=devolver_valor("posicion_ingrese_msj_x_vcont"),y=devolver_valor("posicion_ingrese_msj_y_vcont"))
     cuadroUsuario = Entry(miFrame)
-    cuadroUsuario.place(x=160, y=20)
+    cuadroUsuario.place(x=devolver_valor("posicion_cuadrousuario_x_vcont"), y=devolver_valor("posicion_cuadrousuario_y_vcont"))
 
-    Label(miFrame, text = ("Clave:")).place(x=20,y=40)
+    Label(miFrame, text = (devolver_valor("texto_clave_vcont"))).place(x=20,y=40)
     cuadroClave = Entry(miFrame)
-    cuadroClave.place(x=160, y=40)
+    cuadroClave.place(x=devolver_valor("posicion_cuadroclave_x_vcont"), y=devolver_valor("posicion_cuadroclave_y_vcont"))
     cuadroClave.config()
 
-    botonAgregar = Button(raiz,text="Cifrar mensaje\n César", command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
-    botonAgregar.place(x=8,y=62)
+    botonCifradoCesar = Button(raiz,text=devolver_valor("cifrar_cesar"), command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
+    botonCifradoCesar.place(x=devolver_valor("posicion_x_cifrar_cesar"),y=devolver_valor("posicion_y_cifrar_cesar"))
 
-    botonAgregar = Button(raiz,text="Cifrar mensaje\n Atbash", command= lambda: cifrado_atbash(cuadroUsuario))
-    botonAgregar.place(x=106,y=62)
+    botonCifradoAtbash = Button(raiz,text=devolver_valor("cifrar_atbash"), command= lambda: cifrado_atbash(cuadroUsuario))
+    botonCifradoAtbash.place(x=devolver_valor("posicion_x_cifrar_atbash"),y=devolver_valor("posicion_y_cifrar_atbash"))
 
-    botonAgregar = Button(raiz,text="Descifrar mensaje\n César", command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
-    botonAgregar.place(x=206,y=62)
+    botonDecifradoCesar = Button(raiz,text=devolver_valor("descifrar_cesar"), command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
+    botonDecifradoCesar.place(x=devolver_valor("posicion_x_descifrar_cesar"),y=devolver_valor("posicion_y_descifrar_cesar"))
 
-    botonAgregar = Button(raiz,text="Descifrar mensaje\n Atbash", command= lambda: cifrado_atbash(cuadroUsuario))
-    botonAgregar.place(x=320,y=62)
+    botonDecifradoAtbash = Button(raiz,text=devolver_valor("descifrar_atbash"), command= lambda: cifrado_atbash(cuadroUsuario))
+    botonDecifradoAtbash.place(x=devolver_valor("posicion_x_descifrar_atbash"),y=devolver_valor("posicion_y_descifrar_atbash"))
 
     
 
     raiz.mainloop()
 
-
-
-
 def cifrado_cesar(cuadroUsuario,cuadroClave):
-    
+#HECHO POR ARMANDO AGOSTINA BELEN
+    """
+    >>> cifrado_cesar('hola mundo', '3')
+    'krod pxqgr'
+    >>> cifrado_cesar("CASA", "2")
+    'ECUC'
+    >>> cifrado_cesar("BIENVENIDOS", "4")
+    'FMIRZIRMHSW'
+    >>> cifrado_cesar("argentina vota", "1")
+    'bshfoujob wpub'
+    """    
     texto = cuadroUsuario.get()
     clave = cuadroClave.get()
 
