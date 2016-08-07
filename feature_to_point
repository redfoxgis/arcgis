import arcpy

def feature_to_point(in_shp, out_shp):
    """
    Replicates the Feature to Point (Data Management) tool using basic license
    Creates points at feature vertices
    -input may be polygon or line
    """
    sr = arcpy.Describe(in_shp).spatialReference

    # Create NumPy array from input feature class
    array = arcpy.da.FeatureClassToNumPyArray(in_shp,["SHAPE@XY"], spatial_reference=sr, explode_to_points=True)

    # Create a new points feature class
    arcpy.da.NumPyArrayToFeatureClass(array, out_shp, ['SHAPE@XY'], sr)

if __name__ == "__main__":
    in_shp = r'C:\path\to\input\in_shp.shp'
    out_shp = r'C:\path\to\output\points.shp'
    feature_to_point(in_shp, out_shp)
