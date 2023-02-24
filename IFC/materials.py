import ifcopenshell
import pandas as pd



def get_material_properties(ifc_material_properties:list) -> dict:
    """holt alle Materialien aus dem ifc file und fügt deren Eigenschaften einem dictionary hinzu.

    Args:
        ifc_material_properties (list): Liste der ifcMaterialProperties des ifc files.

    Returns:
        dict: Dictionary der Materialien und ihren Eigenschaften
    """
    materials = {}
    material_propertie = {}
    for properties in ifc_material_properties:
        materials[properties[3][0]] = {}
        for mat in properties[2]:
            # print(mat[2][0])
            material_propertie[mat[0]] = mat[2][0]
            materials[properties[3][0]].update(material_propertie)
    return materials
    

if __name__ == '__main__':
    path = r"P:\2 ENG\BG\BG19-00 EnVis\4 Modelle Analyse\0 EFHeinfach\# Aktuell\2023 02 10 EFHeinfach 14 Spaces kombiniert\EFHeinfach14_2023 02 18 - Kombination.ifc"
    file = ifcopenshell.open(path)
    ifc_material_properties = file.by_type('ifcMaterialProperties')
    materials = get_material_properties(ifc_material_properties)
    
    print(pd.DataFrame.from_dict(materials).transpose())
    # print('---------------------------------------')
    # print(materials['XPS']['SpecificHeatCapacity'])