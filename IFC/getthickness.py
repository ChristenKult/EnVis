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
    path = r"P:\2 ENG\BG\BG19-00 EnVis\4 Modelle Analyse\0 EFHeinfach\# Aktuell\2023 02 10 EFHeinfach 14 Spaces kombiniert\EFHeinfach14_2023 02 21 .duc03 0,158 0,308 .fb01 0,031 0,068 0,051.ifc"
    file = ifcopenshell.open(path)
    coverings = file.by_type('ifccovering')
    print(get_thickness_by_coverings_multilayer(coverings))
