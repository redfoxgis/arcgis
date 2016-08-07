import arcpy

def convex_hull(shp, outshp):
    """
    Creates a convex hull around input polygon (or point) features
    """
    sr = arcpy.Describe(shp).spatialReference

    # Create NumPy array from input feature class
    array = arcpy.da.FeatureClassToNumPyArray(shp,["SHAPE@XY"], spatial_reference=sr, explode_to_points=True)

    # Create a new points feature class
    arcpy.da.NumPyArrayToFeatureClass(array, "in_memory\points", ['SHAPE@XY'], sr)

    # Now get the convex hull of the feature vertices
    pointArray = arcpy.Array()

    #Loop through points in FC (points)
    desc = arcpy.Describe(shp)
    shapefieldname = desc.ShapeFieldName
    fields = ["SHAPE@"]
    with arcpy.da.SearchCursor("in_memory\points", fields) as cursor:
        for row in cursor:
            pnt = row[0].getPart()
            pointArray.add(pnt)

    pointMultipoint = arcpy.Multipoint(pointArray)
    pointArray.removeAll() #frees up memory
    convexPolygon = pointMultipoint.convexHull()
    arcpy.CopyFeatures_management(convexPolygon, outshp)
    arcpy.DefineProjection_management (outshp, sr)

if __name__ == "__main__":
    shp = r'C:\path\to\input\polygons.shp'
    outshp = r'C:\path\to\output\convex_hull.shp'
    convex_hull(shp, outshp)
