import ifcopenshell

# COVERINGS:

# Einschichtig:


#---------------------------------------------------------------------------------------------------------------

# Mehrschichtig:
def get_thickness_by_coverings_multilayer(coverings:list) -> dict:
    """Gibt ein Dictionary der mehrschichtigen Coverings mit Material und Dicke der jeweiligen Schichten aus.

    Args:
        coverings (list): Liste der Coverings

    Returns:
        dict: Dictionary der mehrschichtigen Coverings mit Material und Dicke der jeweiligen Schichten.
    """
            
    output = {}
    for covering in coverings:
        for rel_agg in covering.IsDecomposedBy:
            dic_bEP = {}
            for building_Element_Part in rel_agg[5]:
                dic_bEP[building_Element_Part.Name] = building_Element_Part.Representation[2][0][3][0].Depth
            output[covering.Name]= dic_bEP
    return output



if __name__ == '__main__':
    path = 'file/EFHeinfach14_2023 02 20 - Kombination.ifc'
    file = ifcopenshell.open(path)
    coverings = file.by_type('ifccovering')
    print(get_thickness_by_coverings_multilayer(coverings))
