Data file descriptions for Cook Farm sensor network data set (CAF_Sensor_Dataset). 

Data set compiled by Caley Gasch, under supervision of David Brown, Department of Crop and Soil Sciences, Washington State University, 
Pullman, WA.
Updated: 04/01/2017

Tabular data:
CAF_sensors: folder with Daily and Hourly subfolders, each containing 42 '.txt' files of water content and temperature sensor readings. 
Each file represents readings from a single location, indicated in the file name (i.e. CAF003.txt) and in the 'Location' field of the table. 
Readings are organized by 'Date' (4/20/2007 - 6/16/2016), ‘Time’ (24 hr clock, only in hourly files), and with property (VW or T) and sensor 
'Depth' as follows:
VW_30cm: volumetric water readings at 30 cm depth (m^3/m^3)
VW_60cm: volumetric water readings at 60 cm depth (m^3/m^3)
VW_90cm: volumetric water readings at 90 cm depth (m^3/m^3)
VW_120cm: volumetric water readings at 120 cm depth (m^3/m^3)
VW_150cm: volumetric water readings at 150 cm depth (m^3/m^3)
T_30cm: temperature readings at 30 cm depth (C)
T_60cm: temperature readings at 60 cm depth (C)
T_90cm: temperature readings at 90 cm depth (C)
T_120cm: temperature readings at 120 cm depth (C)
T_150cm: temperature readings at 150 cm depth (C)
Volumetric water content readings are calibrated according to:
Gasch, CK, DJ Brown, ES Brooks, M Yourek, M Poggio, DR Cobos, CS Campbell. 2017. A pragmatic, automated approach for retroactive calibration
of soil moisture sensors using a two-step, soil specific correction. Computers and Electronics in Agriculture, 137: 29-40.
Temperature readings are factory calibrated.

CAF_BulkDensity.txt: file containing bulk density values ('BulkDensity' in g/cm^3) for sensor depths at each of the 42 instrumented 
locations at Cook Farm. Location is indicated in 'Location' field, and sample depths are defined (in cm) by the ’Depth’ field.

CAF_CropID.txt: file containing crop codes for each sub-field (A, B and C) and strip (1-6 for A and B, 1-8 for C) at Cook Farm for 2007-2016.
This is also part of the attribute table for 'CAF_strips.shp'

CAF_CropCodes.txt: file containing crop code names and crop identities, used in 'CAF_CropID.txt' and 'CAF_strips.shp'

CAF_ParticleSize.txt: file containing particle size fractions ('Sand', 'Silt', and 'Clay' as percent) for each 'Location' at sensor depths 
('Depth', in cm).

Spatial data: all spatial data have spatial reference NAD83, UTM11N
CAF_sensors.shp: file containing locations of each of the 42 monitoring locations, the 'Location' field contains the location name, 
which coincides with locations in tabular files.

CAF_strips.shp: file containing areal extents of each sub-field, stip, and crop identities for 2007-2016. Crop identity codes are listed
in 'CAF_CropCodes.txt'

CAF_DEM.tif: file containing a 10 x 10 m elevation (in m) grid for Cook Farm.

CAF_Spring_ECa.tif, CAF_Fall_ECa.tif: files containing 10 x 10 m apparent electrical conductivity (dS/m) grids to 1.5 m depth for spring 
and fall at Cook Farm.

CAF_Bt_30cm.tif, CAF_Bt_60cm.tif, CAF_Bt_90cm.tif, CAF_Bt_120cm.tif, CAF_Bt_150cm.tif: files containing 10 x 10 m predictive surfaces for 
probability (0-1) of Bt horizon at the five sensor depths.