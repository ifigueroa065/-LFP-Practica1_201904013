#IMPORTANDO LIBRERIAS A UTILIZAR
import os
import tkinter.filedialog
from LISTA import lista
import webbrowser

#VARIABLES GLOBALES
contenedor= []
GENERAL=[]
NOMBRES=[]
DATOS=[]
DATOSIN=[]
INSTRUCCIONES=[]
NUMEROS=[]
MOD1=[]
MOD2=[]
POSICIONES=[]
def ordenar(entrada):
    #ORDENAMIENTO DE BURBUJA
    for posicion in range(len(entrada)-1,0,-1):
        for i in range(posicion):
            #SI POSICION ACTUAL ES > A POSICION SIGUIENTE
            if entrada[i]>entrada[i+1]:
                temporal = entrada[i]
                entrada[i] = entrada[i+1]
                #SE REALIZA CAMBIO
                entrada[i+1] = temporal

def parseo(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return(lista)

def comparar(lista,valor):
    global POSICIONES
    listemp=[]
    condicion=False
    if valor!="":
        temp=int(valor)  
        for i in range(len(lista)):
            if lista[i]==temp:
                listemp.append(i+1)
                condicion=True
            else:
                condicion=False
        if condicion==False:
            return(print("--->no encontrado"))
        else:            
            return(print(" --> encontrado en : " + str(listemp)))
    else:
        return(print(""))

def comphtml(lista,valor):
    global POSICIONES
    listemp=[]
    condicion2=False
    if valor!="":
        temp=int(valor)  
        for i in range(len(lista)):
            if lista[i]==temp:
                listemp.append(i+1)
                condicion2=True
            else:
                condicion2=False
        if condicion2==False:
            return("no encontrado")
        else:                
            return(str(listemp))
    else:
        return("")
            
def busquedas():
    global MOD1,MOD2,NOMBRES,DATOSIN,GENERAL,INSTRUCCIONES,POSICIONES
    for x in range(len(INSTRUCCIONES)):
        if INSTRUCCIONES[x]!="ORDENAR":
            respuesta=NOMBRES[x]+"="+str(DATOSIN[x])
            print(respuesta + "-- Valor buscado:" + str(NUMEROS[x]),end="")
            comparar(DATOSIN[x],NUMEROS[x])

def imprimirtodo():
    for x in range(len(INSTRUCCIONES)):
        if INSTRUCCIONES[x]!="ORDENAR":
            respuesta=NOMBRES[x]+"=" + str(DATOSIN[x])
            res2="resultado de ordenar la lista -->"+str(DATOS[x])
            print(respuesta + "-- Valor buscado: " + str(NUMEROS[x]),end="")
            comparar(DATOSIN[x],NUMEROS[x])
            print(res2)
        else:
            respuesta=NOMBRES[x]+"="+str(DATOSIN[x])
            resultado=str(DATOS[x])
            print(respuesta+"-- Resultado de ordenar lista --"+ resultado)

def Op1():
    os.system('cls')
    print("Seleccione su archivo")
    global contenedor,NUMEROS,INSTRUCCIONES,DATOS,NOMBRES,DATOSIN
    global MOD1,MOD2,GENERAL
    root= tkinter.Tk()
    root.withdraw()
    ruta=tkinter.filedialog.askopenfilename(
        initialdir="C:", 
        filetypes=(
            ("Ficheros de texto", "*.txt"),
            ("Todos los ficheros","*.*")
        ), 
        title = "ABRIR ARCHIVO"
    )
    try:
        #lectura de archivo linea*linea
        with open(ruta) as f:
            linea=f.readlines()

        #separando por espacios    
        for i in linea:
            MOD1.append(i.split())
        #imprimiendo primer modulo  
        #print("este es el modulo 1")  
        #print(MOD1)

        #separando por igual
        for i in range(len(MOD1)):
            #separando por "="
            MOD2.append(MOD1[i][0].split("="))
        #print("este es el modulo 2")
        #print(MOD2)
        for i in range(len(MOD2)):
            #obteniendo los nombres de las listas
            NOMBRES.append(MOD2[i][0])
            DATOS.append(MOD2[i][1].split(","))
            DATOSIN.append(MOD2[i][1].split(","))
        
        for i in range(len(DATOS)):
            #casteando datos
            parseo(DATOS[i])
            parseo(DATOSIN[i]) 
            #ordenar(c[i])             
        #print("los datos finales son")
        #print("nombres")
        #print(NOMBRES)
        #print("datos:")        
        #print(DATOS)
        #print("instrucciones")
        #recolectando instrucciones
        for i in range(len(MOD1)):
            if len(MOD1[i])==2:
                INSTRUCCIONES.append(MOD1[i][1])
                NUMEROS.append("")
            elif len(MOD1[i])==3:
                INSTRUCCIONES.append(MOD1[i][1])
                NUMEROS.append(MOD1[i][2])
                
            else:
                print("instrucciones invalidas")
        #print(INSTRUCCIONES)
        #print("los numeros son:")
        #print(NUMEROS)
        GENERAL.append(lista(NOMBRES,DATOS,INSTRUCCIONES,NUMEROS))
        #for i in GENERAL:
            #for j in i.getNombre():
                #print(j +",",end="")
    finally:
        os.system('cls')
        print("**************************")
        print("     Carga exitosa    ")
        print("**************************")
        
def Op2():
    global DATOS,NOMBRES
    print("************************         LISTAS ORDENADAS        ************************")
    print("")
    for i in range(len(NOMBRES)):
        ordenar(DATOS[i])
        ans=NOMBRES[i]+"=" + str(DATOSIN[i])
        resultado=str(DATOS[i])
        print(ans +"-- Resultado de ordenar lista -->"+ resultado)
        
def Op3():
    print("********************         BÚSQUEDAS        ********************")
    print("")
    busquedas()

def Op4():
    global MOD1,MOD2,NOMBRES,DATOSIN,GENERAL,INSTRUCCIONES,POSICIONES
    print("**********************       TODAS LAS LISTAS        **********************")
    print("")
    imprimirtodo()
            
def Op5():
    global NOMBRES,DATOS,DATOSIN,INSTRUCCIONES,NUMEROS
    f = open('REPORTE.html','w')

    f.write("""<!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>PRACTICA_1_201904013</title>
    <meta content="" name="description">
    <meta content="" name="keywords">

    <!-- Favicons -->
    <link href="assets/img/icon.png" rel="icon">
    <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/vendor/icofont/icofont.min.css" rel="stylesheet">
    <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="assets/vendor/venobox/venobox.css" rel="stylesheet">
    <link href="assets/vendor/owl.carousel/assets/owl.carousel.min.css" rel="stylesheet">
    <link href="assets/vendor/aos/aos.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="assets/css/style.css" rel="stylesheet">

    <!-- =======================================================
    * Template Name: iPortfolio - v1.5.1
    * Template URL: https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/
    * Author: BootstrapMade.com
    * License: https://bootstrapmade.com/license/
    ======================================================== -->
    </head>

    <body>
        <audio  id="player" src="rolita.mp3" autoplay loop></audio>
    <!-- ======= Mobile nav toggle button ======= -->
    <button type="button" class="mobile-nav-toggle d-xl-none"><i class="icofont-navigation-menu"></i></button>

    <!-- ======= Header ======= -->
    <header id="header">
        <div class="d-flex flex-column">

        <div class="profile">
            <img src="assets/img/2.webp" alt="" class="img-fluid rounded-circle">
            <h1 class="text-light"><a href="REPORTE.html">ISAI FIGUEROA</a></h1>
            
        </div>

        <nav class="nav-menu">
            <ul>
            <li class="active"><a href="REPORTE.html"><i class="bx bx-home"></i> <span>HOME</span></a></li>
            <li><a href="#services"><i class="bx bx-server"></i>RESUME</a></li>
            
            </ul>
        </nav><!-- .nav-menu -->
        <button type="button" class="mobile-nav-toggle d-xl-none"><i class="icofont-navigation-menu"></i></button>

        </div>
    </header><!-- End Header -->

    <!-- ======= Hero Section ======= -->
    <section id="hero" class="d-flex flex-column justify-content-center align-items-center">
        <div class="hero-container" data-aos="fade-in">
        <h1>ISAI FIGUEROA</h1>
        
        </div>
    </section><!-- End Hero -->

    <main id="main">

        
        <!-- ======= Services Section ======= -->
        <section id="services" class="services">
        <div class="container">

            <div class="section-title">
            <h2>RESUME</h2>
            <p></p>
            <div>
            </div>

            <div class="row">
            <table class="table table-dark table-hover">""")

    
    f.write("""
        <td><center><h4>NOMBRE DE LISTA</h4></center></td>
        <td><center><h4>SIN ORDENAR</h4></center></td>
        <td><center><h4>ORDENADA</h4></center></td>
        <td><center><h4>INSTRUCCIONES</h4></center></td>
        <td><center><h4>VALOR BUSCADO</h4></center></td>
        <td><center><h4>POSICIONES</h4></center></td>
        </tr>""") 
    for i in range(len(NOMBRES)):
        ordenar(DATOS[i])
        f.write("<tr>")
        f.write("<td><center>"+"<h4>"+NOMBRES[i]+"</h4>"+"</center></td>"+"<td>"+"<h5>"+str(DATOSIN[i])+"</h5>"+"</td>"
        +"<td>"+"<h5>"+str(DATOS[i])+"</h5>"+"</td>"
        +"<td><center>"+"<h5>"+str(INSTRUCCIONES[i])+"</h5>"
        +"</center></td>"+"<td><center>"+"<h5>"+str(NUMEROS[i])+"</h5>"+"</center></td>"
        +"<td><center>"+"<h5>"+str(comphtml(DATOSIN[i],NUMEROS[i]))+"</h5>"+"</center></td>")     
        f.write("<t/r>")
    f.write("</table>")     
    f.write("""</div>
       
        <button  class="btn btn-light" onclick="document.getElementById('player').play() ">Play</button>
        <button  class="btn btn-dark" onclick="document.getElementById('player').pause() ">Pause</button>
        </div>
        </section><!-- End Services Section -->
    </main><!-- End #main -->

    </body>

    </html>""")
    f.close()

    webbrowser.open_new_tab('REPORTE.html')

def MENU():	
    os.system('cls')
    print("********************************************************************") 
    print ("\t           1 - Cargar archivo de entrada")
    print ("\t           2 - Desplegar listas ordenadas")
    print ("\t           3 - Desplegar búsquedas")
    print ("\t           4 - Desplegar todas")
    print ("\t           5 - Desplegar todas a archivo ")
    print ("\t           6 - Salir")
    print("********************************************************************")

while True:
    MENU()
    op = input("\n ----Seleccione una Opción---- \n")
    if op=="1":
        print ("")
        Op1()
        input("\npulsa enter para volver...")
    elif op=="2":
        print ("")
        os.system('cls')
        Op2()
        input("\npulsa enter para volver...")
    elif op=="3":
        print ("")
        os.system('cls')
        Op3()
        input("\npulsa enter para volver...")
    elif op=="4":
        print ("")
        os.system('cls')
        Op4()
        input("\npulsa enter para volver...")
    elif op=="5":
        print ("")
        os.system('cls')
        Op5()
        input("\npulsa enter para volver...")
    elif op=="6":
        os.system('cls')
        print("CARNET: 201904013")
        print("NOMBRE: MARLON ISAÍ FIGUEROA FARFÁN")
        print("CORREO: isaiimiff13@gmail.com")
        print("CURSO: LENGUAJES FORMALES")
        input("\n...")
        break
    else:
        print ("***ERROR****")
        os.system('cls')
        input("No has pulsado ninguna opción correcta...\npulsa enter para volver...")

