import ifcopenshell
import pandas as pd



def get_walls_by_type(file):

    # Create a dictionary to store the walls by type
    walls_by_type = {}

    # Get all the wall types
    wall_types = file.by_type("IfcWallType")

    # Loop over the wall types
    for wall_type in wall_types:
        # Get the related walls
        related_walls = []
        for rel in file.get_inverse(wall_type):
            if rel.is_a("IfcRelDefinesByType"):
                for wall in rel.RelatedObjects:
                    if wall.is_a("IfcWall"):
                        related_walls.append(wall.Name + '|' + wall.GlobalId)

        # Add the related walls to the dictionary
        walls_by_type[wall_type.Name + '|' + wall_type.GlobalId] = related_walls

    # Return the walls by type
    return walls_by_type



#--------------------------------------------------------------------------------------------------------------

def get_roofs_by_type(file):

    # Create a dictionary to store the roofs by type
    roofs_by_type = {}

    # Get all the roof types
    roof_types = file.by_type('IfcRoofType')

    # Loop over the roof types
    for roof_type in roof_types:
        # Get the related roofs
        related_roofs = []
        for rel in file.get_inverse(roof_type):
            if rel.is_a("IfcRelDefinesByType"):
                for roof in rel.RelatedObjects:
                    if roof.is_a("Ifcroof"):
                        related_roofs.append(roof.Name + '|' + roof.GlobalId)

        # Add the related roofs to the dictionary
        roofs_by_type[roof_type.Name + '|' + roof_type.GlobalId] = related_roofs

    # Return the roofs by type
    return roofs_by_type




if __name__ == '__main__':
    
    file = ifcopenshell.open('file/EFHeinfach14_2023 02 20 - Kombination.ifc')
    roofs_by_type = get_roofs_by_type(file)
    print(roofs_by_type)