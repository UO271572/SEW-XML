# 02000-XML.py
# # -*- coding: utf-8 -*-
""""
Procesamiento genérico de archivos XML

@version 
@author: Sergio Buenaga
"""

import xml.etree.ElementTree as ET

def verXML(archivoXML):
    try:
        
        arbol = ET.parse(archivoXML)
        
    except IOError:
        print ('No se encuentra el archivo ', archivoXML)
        exit()
        
    except ET.ParseError:
        print("Error procesando en el archivo XML = ", archivoXML)
        exit()
       
    raiz = arbol.getroot()
    
    html ="<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n<meta charset=\"UTF-8\"><title>Generacion</title>\n<meta name=\"keywords\" content=\"Generacion, persona, personas, fechas, lugares\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<meta name=\"author\" content=\"Sergio Buenaga Gutierrez\">\n<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n</head>\n<body>\n<header>\n<h2>EJERCICIO 1</h2>\n</header>\n"
        
    html = recorrePersona(raiz,html)

    html += footer()
    html += ("</body>\n</html>")
    
    f = open("index.html","w")
    f.write(html)
    f.close()
#########################################################################
def recorrePersona(raiz,html):
    html += "<section>\n"
    html += h3(raiz.attrib.get("nombre"))
    html += p("Nombre: ",raiz.attrib.get("nombre"))
    html += p("Apellidos: ",raiz.attrib.get("apellidos"))
    for nodo in raiz:
        if(nodo.tag.partition("}")[2] == "datos"):
            html = recorreDatos(nodo,html)
        elif(nodo.tag.partition("}")[2] == "persona"):
            html = recorrePersona(nodo,html)
    return html
            
def recorreDatos(nodo,html):
    for e in nodo.find("."):
        if(e.tag.partition("}")[2] == "nacimiento"):
            html = recorreNacimiento(e,html)
        elif(e.tag.partition("}")[2] == "residencia"):
            html = recorreResidencia(e,html)
        elif(e.tag.partition("}")[2] == "imagenes"):
            html = recorreImagenes(e,html)
        elif(e.tag.partition("}")[2] == "videos"):
            html = recorreVideos(e,html)
        elif(e.tag.partition("}")[2] == "comentarios"):
            html = recorreComentarios(e,html)
    return html
     
def recorreResidencia(e,html):
    html += p("Residencia: ",e.get("lugarResidencia"))
    for i in e.find("."):
        if(i.tag.partition("}")[2] == "coordenadasResidencia"):
            html += h4("Coordenadas de residencia:")
            html = recorreCoordenadas(i,html)
    return html

def recorreNacimiento(e,html):
    for i in e.find("."):
        if(i.tag.partition("}")[2] == "fechaNacimiento"):
            html += p("Nacimiento: ",i.text)
        elif(i.tag.partition("}")[2] == "lugarNacimiento"):
            html += p("Lugar de nacimiento: ",i.text)
        elif(i.tag.partition("}")[2] == "coordenadasNacimiento"):
            html += h4("Coordenadas de lugar de nacimiento:")
            html = recorreCoordenadas(i,html)
    return html
      
def recorreCoordenadas(e,html):
    html += ulOpen()
    for i in e.find("."):
        if(i.tag.partition("}")[2] == "longitud"):
            html += li("Longitud: "+i.text)
        if(i.tag.partition("}")[2] == "latitud"):
            html += li("Latitud: "+i.text)
        if(i.tag.partition("}")[2] == "altitud"):
            html += li("Altitud: "+i.text)
    html += ulClose()
    return html

def recorreImagenes(e,html):
    html += h4("Imagenes:")
    for i in e.find("."):
        html += imagen(i.text,i.text)
    return html

def recorreVideos(e,html):
    html += h4("Videos:")
    for i in e.find("."):
        html += video(i.text)
    return html
        
def recorreComentarios(e,html):
    html += h4("Comentarios:")
    for i in e.find("."):
        html += p("Comentario: ",i.text)
    html += "</section>\n"
    return html

def h3(text):
    return "<h3>"+text+"</h3>\n"

def h4(text):
    return "<h4>"+text+"</h4>\n"

def p(categoria,text):
    return "<p>"+categoria+text+"</p>\n"

def ulOpen():
    return "<ul>\n"
def ulClose():
    return "</ul>\n"
def li(txt):
    return "<li>"+txt+"</li>\n"

def listaCoordenadas(elementos):
    txt = "<ul>\n"
    for e in range(2):
        if e==0:
            txt+=("<li>Longitud: "+elementos[0]+"</li>\n")
        if e==1:
            txt+=("<li>Latitud: "+elementos[1]+"</li>\n")
        if e==2:
            txt+=("<li>Altura: "+elementos[2]+"</li>\n")
    txt+=("</ul>\n")
    return txt

def lista(elementos):
    txt = "<ul>\n"
    for e in elementos:
        txt+=("<li>"+e+"</li>\n")
    txt+=("</ul>\n")
    return txt

def imagen(rutaImagen,txAlternativo):
    return "<img src=\""+rutaImagen+"\" alt=\""+txAlternativo+"\">\n"

def video(multimedia):
    return "<video controls><source src=\""+multimedia+"\" type=\"video/mp4\"></video>\n"
  
def footer():
    return "<footer><address>Para mas informacion personalizada pincha <a href=\"mailto:UO271572@uniovi.es\">aqui</a>.</address></footer>\n"

    
def main():
    """Prueba de la función verXML()"""
    
    print(verXML.__doc__)
    
    file = open("redsocial.xml","r")
    verXML(file)

if __name__ == "__main__":
    main()    
