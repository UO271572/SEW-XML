""""
Procesamiento genérico de archivos XML transformacion a SVG

@version 
@author: Sergio Buenaga
"""
import math
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
    f = open("redsocial.svg","w")
    raiz = arbol.getroot()
    f.write("<?xml version=\"1.0\" standalone=\"no\"?>\n<svg style=\"overflow:visible\" xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" width=\"auto\" height=\"auto\">\n")
    x=200
    y=200
    nivel = 1
    size = 600
    lv1gap=size/1
    lv2gap=size/math.pow(3,1)
    lv3gap=size/math.pow(3,2)
    lastxlv2=0
    lastxlv3=0
    f.write("<rect x=\"{}\" y=\"{}\" width=\"150\" height=\"50\" fill=\"yellow\" stroke=\"navy\" stroke-width=\"5\" />\n".format(lv1gap/(1.2)-30,y-30))
    f.write("<text x = \"{}\" y = \"{}\" fill = \"{}\" font-size = \"{}em\">{}</text>\n"
            .format(lv1gap/(1.2),y,"black","1",raiz.get("nombre")))

    contador = 1
    nivel = 2
    for persona in raiz.findall(".//persona"):
        if(persona.tag == "persona"):
            if nivel == 2:
                f.write("<line x1=\"{}\" y1=\"{}\" stroke=\"blue\" ".format(lv1gap/(1.2),y+20))
                cx=lastxlv2+lv2gap+50
                cy=y+200
                f.write("x2=\"{}\" y2=\"{}\" stroke-width=\"5\"></line>\n".format(cx,cy))
            elif nivel == 3:
                f.write("<line x1=\"{}\" y1=\"{}\" stroke=\"blue\" ".format(lastxlv2,y+220))
                cx=lastxlv3+lv3gap+40
                cy=y+500
                f.write("x2=\"{}\" y2=\"{}\" stroke-width=\"5\"></line>\n".format(cx,cy))
            
            f.write("<rect x=\"{}\" y=\"{}\" width=\"100\" height=\"50\" fill=\"yellow\" stroke=\"navy\" stroke-width=\"5\" />\n".format(cx-30,cy-30))
            f.write("<text x = \"{}\" y = \"{}\" fill = \"{}\" font-size = \"{}\" >{}</text>\n".format(cx,cy,"black","1em",persona.get("nombre")))
            if nivel == 2:
                lastxlv2 = cx
            elif nivel == 3:
                lastxlv3 = cx
            if(len(persona.getchildren())>1):#hay nodos persona hijos
                nivel+=1
            if(len(persona.getchildren())==1):
                if(contador==3):
                    nivel-=1
                    contador=1
                else:
                    contador+=1
    f.write("</svg>\n")
    f.close()

def main():
    """Prueba de la función verXML()"""
    print(verXML.__doc__)
    file = open("redsocial.xml","r")
    verXML(file)

if __name__ == "__main__":
    main()    