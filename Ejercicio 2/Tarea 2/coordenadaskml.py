""""
Procesamiento genérico de archivos XML transformacion a KML

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
    f = open("redsocial.kml","w")
    raiz = arbol.getroot()
    
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?><kml xmlns=\"http://www.opengis.net/kml/2.2\">\n<Document>\n")
    for persona in raiz.findall(".//"):
        if(persona.tag == "persona"):
            createPlacement(f,persona)
    f.write("</Document></kml>")
    f.close()

def createPlacement(f,persona):
    for i in range(2):
        f.write("<Placemark>\n")
        f.write("<name>{}</name>\n".format(persona.attrib.get("nombre")))
        if i==0:
            f.write("<description>Nacimiento: {}</description>\n".format(persona.find("datos/nacimiento/lugarNacimiento").text))
        else:
            f.write("<description>Reside: {}</description>\n".format(persona.find("datos/residencia").get("lugarResidencia")))
        createPoint(f,persona,i)
        f.write("</Placemark>\n")

def createPoint(f,persona,i):
    if i==0:
        latitud = "datos/nacimiento/coordenadasNacimiento/latitud"
        longitud = "datos/nacimiento/coordenadasNacimiento/longitud"
        altitud = "datos/nacimiento/coordenadasNacimiento/altitud"
    else:
        latitud = "datos/residencia/coordenadasResidencia/latitud"
        longitud = "datos/residencia/coordenadasResidencia/longitud"
        altitud = "datos/residencia/coordenadasResidencia/altitud"
    f.write("<Point>\n")
    f.write("<coordinates>{},{},{}</coordinates>\n".format(persona.find(longitud).text,
                                                        persona.find(latitud).text,
                                                        persona.find(altitud).text))
    f.write("</Point>\n")
    f.write("<altitudeMode>absoluto</altitudeMode>\n")

def main():
    """Prueba de la función verXML()"""
    print(verXML.__doc__)
    file = open("redsocial.xml","r")
    verXML(file)

if __name__ == "__main__":
    main()    