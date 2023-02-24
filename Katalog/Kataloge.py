import requests
import xml.etree.ElementTree as ET
import pandas as pd

def load_Katalog_XML(url:str,name:str) -> None:
    """Lädt die XML eines bestimmten Kataloges herunter und legt ihn unter /Data/ ab.

    Args:
        url (str): URL des herunterzuladenden Katalogs.
        name (str): Name des Katalogs. Wird unter /Data/Name.xml abgelegt.
    """

    resp = requests.get(url)

	# xml file speichern
    with open(f'Data/{name}.xml', 'wb') as f:
        f.write(resp.content)
		


def get_XML_id_by_Kataloge() -> dict:
    """Durchläuft den Katalog der Baustoff-Kataloge und gibt ein dictionary mit den Namen der Baustoffkatalogen und deren id's aus.

    Returns:
        dict: dictionary mit Namen und zugehörigen id's der Baustoffkataloge.
    """
    dic_Kataloge = {}

    xmlfile = 'Data/Grundlage/Kataloge.xml'
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    for catalog in root.findall('catalog'):
        name = catalog.find('name').text
        id = catalog.get('id')
        dic_Kataloge[name] = id

    return dic_Kataloge


def update_Katalog_XML(Katalog:str) -> None:
    """Lädt den ausgewählten Katalog neu herunter und legt ihn unter /Data/ ab.

    Args:
        Katalog (str): Name des Katalogs.
    """

    id_Kataloge = get_XML_id_by_Kataloge()
    id = id_Kataloge[Katalog]

    url_Katalog = f'http://bphdb.com/catalog/asXML/{id}'

    load_Katalog_XML(url_Katalog, Katalog)


def get_Katalog_XML(Katalog:str) -> dict:
    """Gibt den gewählten Katalog als dictionary aus.

    Args:
        Katalog (str): Name des Katalogs.

    Returns:
        dict: dictionary mit allen Daten des gewählten Katalogs.
    """
    xmlfile = f'Data/{Katalog}.xml'
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    dic = {'Material':[], 
            'Gruppe':[], 
            'Anwendung':[], 
            'Beschreibung':[], 
            'dimension':[], 
            'density':[], 
            'compressiveStrength':[], 
            'thermCond':[], 
            'heatSpecCap':[], 
            'waterDiffRes':[], 
            'waterDiffResWet':[], 
            'acousticEDyn':[], 
            'lifeTime':[], 
            'peiNotRenewable':[], 
            'peiRenewable':[], 
            'gwp100':[],
            'ap':[]
            }

    for material in root.findall('material'):
        dic['Gruppe'].append(material.find('groupName').text)
        dic['Material'].append(material.find('name').text)
        dic['Anwendung'].append(material.find('application').text)
        dic['Beschreibung'].append(material.find('description').text)

        for param in material.iter('param'):
            dic[param.attrib['sym']].append(param.attrib['val'])

    return dic

	
if __name__ == "__main__":

    Katalog = 'Basic Europe'
    print(pd.DataFrame.from_dict(get_Katalog_XML(Katalog)))