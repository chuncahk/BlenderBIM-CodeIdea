import mathutils

def closestPointToSegment(pt,curve_pt1,curve_pt2):
    p4 = mathutils.geometry.intersect_point_line(pt,curve_pt1,curve_pt2)[0]
    curveLength = (curve_pt1-curve_pt2).length
    if ((p4-curve_pt1).length > curveLength) or ((p4-curve_pt2).length > curveLength):
        if ((p4-curve_pt1).length) > ((p4-curve_pt2).length):
            return(curve_pt2)
        else:
            return(curve_pt1)
    else:
        return(p4)