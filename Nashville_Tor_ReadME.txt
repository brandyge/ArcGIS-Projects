conda clone environment

open python command prompt as administrator and enter the below information


conda create --name AWS_imagery --clone arcgispro-py3

conda env list       #this will show all active environments 

activate myenvironment

conda list will show you all the packages in that clone

conda install -c anaconda boto3

cd..
cd AWS_imagery

to pull down data off AWS buckets
open cmd after aws install. 

aws s3 ls s3://noaa-eri-pds/2020_Nashville_Tornado/20200307a_RGB/ --no-sign-request

In ArcGIS pro 
make a mosaic datset inside of a geo database
add a test rester and coordinate system.  Used WGS84 GCS

Run Nashville Script
#Test rasters
key:  /vsis3/noaa-eri-pds/2020_Nashville_Tornado/20200307a_RGB/20200307aC0870000w361030n.tif
     /vsis3/noaa-eri-pds/2020_Nashville_Tornado/20200307a_RGB/20200307aC0870130w361200n.tif
arcGIS pro needs the vsis because of Gdal
/vsis3/   