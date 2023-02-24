import ifcopenshell
import pandas as pd

from walls import get_materials_by_walls
from materials import get_material_properties

path = r"P:\2 ENG\BG\BG19-00 EnVis\4 Modelle Analyse\0 EFHeinfach\# Aktuell\2023 02 10 EFHeinfach 14 Spaces kombiniert\EFHeinfach14_2023 02 18 - Kombination.ifc"
file = ifcopenshell.open(path)

walls = file.by_type('ifcWall')
materials = file.by_type('ifcMaterialProperties')




# Materialien der Wände:
df_materials_by_walls = pd.DataFrame.from_dict(get_materials_by_walls(walls))
# print(df_materials_by_walls.transpose())

for column in df_materials_by_walls:
    df_materials_by_walls[file.by_guid(column).Name + ' ' +column] = df_materials_by_walls[column]
    del df_materials_by_walls[column]
print(df_materials_by_walls.transpose())


# Eigenschaften der Materialien
df_materials_properties = pd.DataFrame.from_dict(get_material_properties(materials))
# print(df_materials_properties.transpose())


