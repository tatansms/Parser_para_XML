#codigo Hecho con:
#DIEGO DE LA OHZ BALLENA
#SEBASTIAN MARTINEZ

import xml.etree.ElementTree as ET
class PARSERXML:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None

    def load_xml(self):
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()

    def parse_xml(self):
        if self.root is None:
            self.load_xml()

        self.parse_element(self.root)


    # En este punto (def parse_element) fue donde usamos el polimorfismo para manejar diferentes tipos de elementos XML.
    # ya que dependiendo del tipo de elemento toma una acción diferente
    def parse_element(self, element, level=0):
        if element.attrib:
            print("")
            print("  " * level + " Los Atributos:")
            for key, value in element.attrib.items():
                print("  " * level + f"    {key}: {value}")
        if element.text and element.text.strip():
            print("  " * level + f"  Texto: {element.text.strip()}")

        for child in element:
            self.parse_element(child, level )
try:
    if __name__ == "__main__":
     file_path = "ejemplo.xml"
     parser = PARSERXML(file_path)
     parser.parse_xml()  
except :   
    raise ("No se encontro el archivo xml")
