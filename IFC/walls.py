import ifcopenshell

#--------------------------------------------------------------------------------------------------------------
def get_material_by_walls_einschichtig(walls:list) -> dict:
    """Fügt die Materialien aus denen die einschichtigen Wände aus der Wandliste bestehen einem dictionary hinzu.

    Args:
        walls (list): Liste mit ifcWalls.

    Returns:
        dict: Dictionary:   key = GlobalId der einschichtigen Wände
                            value = Material
    """
    material_by_walls = {}
    for wall in walls:
        try:
            for Association in wall.HasAssociations:
                if Association.is_a('IfcRelAssociatesMaterial'):
                    material_by_walls[wall.GlobalId] = Association[5][2][0][0]

        except:
            continue
    return material_by_walls

#--------------------------------------------------------------------------------------------------------------

def get_materials_by_walls_mehrschichtig(walls:list) -> dict:
    """Fügt die Materialien aus denen die mehrschichtigen Wände aus der Wandliste bestehen einem dictionary hinzu.

    Args:
        walls (list): Liste mit ifcWalls

    Returns:
        dict: Dictionary:   key = GlobalId der mehrschichtigen Wände
                            value = Materialien
    """
    materials_by_walls_dict = {}

    for wall in walls:
        for rel in wall.IsDecomposedBy:
            if rel.is_a("IfcRelAggregates"):
                for related_object in rel.RelatedObjects:
                    if related_object.is_a("IfcBuildingElementPart"):
                        if wall.GlobalId not in materials_by_walls_dict:
                            materials_by_walls_dict[wall.GlobalId] = []
                        materials_by_walls_dict[wall.GlobalId].append(related_object[2])
    return materials_by_walls_dict

#--------------------------------------------------------------------------------------------------------------

def get_materials_by_walls_mehrschichtig_Einschichtwand(walls:list) -> dict:
    pass
    




#--------------------------------------------------------------------------------------------------------------

def get_materials_by_walls(walls:list) -> dict:
    """Fügt die Materialien aus denen die Wände bestehen einem dictionary hinzu

    Args:
        walls (list): Liste mit ifcWalls

    Returns:
        dict: Dictionary:   key = GlobalId der Wände
                            value = Materialien
    """
    materials_by_walls = get_material_by_walls_einschichtig(walls)
    materials_by_walls.update(get_materials_by_walls_mehrschichtig(walls))
    # materials_by_walls.update(get_materials_by_walls_mehrschichtig_Einschichtwand(walls))
    return materials_by_walls

#--------------------------------------------------------------------------------------------------------------





###############################################################################################################
if __name__ == '__main__':
    path = r"P:\2 ENG\BG\BG19-00 EnVis\4 Modelle Analyse\0 EFHeinfach\# Aktuell\2023 02 10 EFHeinfach 14 Spaces kombiniert\EFHeinfach14_2023 02 22 - Schichten Wall Wand-045 IPL Holz.ifc"
    file = ifcopenshell.open(path)
    walls = file.by_type('ifcWall')

    # count = 0
    # for key in get_materials_by_walls(walls):
    #     count+=1
    #     print(count)
    print(len(walls))
    print(len(get_materials_by_walls(walls)))
    if len(walls) == len(get_materials_by_walls(walls)):
        print('Dürfte alles passen')
    else:
        print('Da passt was nicht')