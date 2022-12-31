import bpy
import ifcopenshell
import blenderbim.tool as tool

def getCommonPsets():
    elements = [tool.Ifc.get_entity(obj) for obj in bpy.context.selected_objects]
    eleCommonPsetsKeys = None
    for element in elements:
        elePsets = ifcopenshell.util.element.get_psets(element)
        if eleCommonPsetsKeys is not None:
            eleCommonPsetsKeys = eleCommonPsetsKeys & elePsets.keys()
        else:
            eleCommonPsetsKeys = elePsets.keys()
    
    eleCommonParaKeyslist = []
    for key in eleCommonPsetsKeys:
        eleCommonParaKeys = None
        for element in elements:
            paraPairs = ifcopenshell.util.element.get_psets(element)[key]
            if eleCommonParaKeys is not None:
                eleCommonParaKeys = eleCommonParaKeys & paraPairs.keys()
            else:
                eleCommonParaKeys = paraPairs.keys()
        eleCommonParaKeyslist.append(eleCommonParaKeys)
    
    eleCommonParaValuesList = []
    for n,psetsKey in enumerate(eleCommonPsetsKeys):
        eleCommonParaKeys = eleCommonParaKeyslist[n]
        eleCommonParaValues = []
        for parakey in eleCommonParaKeys:
            eleCommonValue = None
            for element in elements:
                if eleCommonValue is not None:
                    if eleCommonValue != ifcopenshell.util.element.get_psets(element)[psetsKey][parakey]:
                        eleCommonValue = "varies"
                else:
                    eleCommonValue = ifcopenshell.util.element.get_psets(element)[psetsKey][parakey]
            eleCommonParaValues.append(eleCommonValue)
        eleCommonParaValuesList.append(eleCommonParaValues)