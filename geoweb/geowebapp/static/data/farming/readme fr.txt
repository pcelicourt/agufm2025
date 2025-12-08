Description des fichiers de données pour le réseau de capteurs de la ferme Cook (CAF_Sensor_Dataset). 



Ensemble de données compilées par Caley Gasch, sous la supervision de David Brown, Department of Crop and Soil Sciences, Washington State University, 
Pullman, WA.
Mise à jour : 04/01/2017



Données tabulaires :
CAF_sensors : dossier avec des sous-dossiers quotidiens et horaires, chacun contenant 42 fichiers '.txt' de la teneur en eau et des relevés des capteurs de température. 
Chaque fichier représente les relevés d'un seul emplacement, indiqué dans le nom du fichier (par exemple CAF003.txt) et dans le champ "Emplacement" du tableau. 
Les relevés sont organisés par "date" (20/04/2007 - 16/06/2016), "heure" (horloge 24 heures, uniquement dans les fichiers horaires), et par propriété (VW ou T) et capteur. 
Profondeur' comme suit :
VW_30cm : relevés volumétriques de l'eau à 30 cm de profondeur (m^3/m^3)
VW_60cm : relevés volumétriques de l'eau à 60 cm de profondeur (m^3/m^3)
VW_90cm : relevés volumétriques de l'eau à 90 cm de profondeur (m^3/m^3)
VW_120cm : relevés volumétriques de l'eau à 120 cm de profondeur (m^3/m^3)
VW_150cm : relevés volumétriques de l'eau à 150 cm de profondeur (m^3/m^3)
T_30cm : relevés de température à 30 cm de profondeur (C)
T_60cm : relevés de température à 60 cm de profondeur (C)
T_90cm : relevés de température à 90 cm de profondeur (C)
T_120cm : relevés de température à 120 cm de profondeur (C)
T_150cm : relevés de température à 150 cm de profondeur (C)
Les lectures de la teneur en eau volumétrique sont calibrées selon :
Gasch, CK, DJ Brown, ES Brooks, M Yourek, M Poggio, DR Cobos, CS Campbell. 2017. Une approche pragmatique et automatisée pour l'étalonnage rétroactif
des capteurs d'humidité du sol à l'aide d'une correction spécifique au sol en deux étapes. Computers and Electronics in Agriculture, 137 : 29-40.
Les relevés de température sont étalonnés en usine. (Methodes de calibration)



CAF_BulkDensity.txt : fichier contenant les valeurs de densité apparente ("BulkDensity" en g/cm^3) pour les profondeurs des capteurs à chacun des 42 emplacements instrumentés à la ferme Cook. 
instrumentés à la ferme Cook. L'emplacement est indiqué dans le champ "Location" et la profondeur des échantillons est définie (en cm) par le champ "Depth".



CAF_CropID.txt : fichier contenant les codes de culture pour chaque sous-champ (A, B et C) et bande (1-6 pour A et B, 1-8 pour C) à la ferme Cook pour la période 2007-2016.
Ce fichier fait également partie de la table attributaire de "CAF_strips.shp".



CAF_CropCodes.txt : fichier contenant les noms des codes des cultures et les identités des cultures, utilisé dans "CAF_CropID.txt" et "CAF_strips.shp".



CAF_ParticleSize.txt : fichier contenant les fractions granulométriques ("Sand", "Silt" et "Clay" en pourcentage) pour chaque "Location" aux profondeurs des capteurs 
("Profondeur", en cm).



Données spatiales : toutes les données spatiales ont une référence spatiale NAD83, UTM11N
CAF_sensors.shp : fichier contenant les emplacements de chacun des 42 sites de surveillance, le champ "Location" contient le nom de l'emplacement, 
Le champ "Emplacement" contient le nom de l'emplacement, qui coïncide avec les emplacements dans les fichiers tabulaires.



CAF_strips.shp : fichier contenant les superficies de chaque sous-champ, parcelles, et les identités de culture pour 2007-2016. Les codes d'identité des cultures sont répertoriés
dans "CAF_CropCodes.txt".



CAF_DEM.tif : fichier contenant une grille d'élévation de 10 x 10 m (en m) pour la ferme Cook.



CAF_Spring_ECa.tif, CAF_Fall_ECa.tif : fichiers contenant des grilles de conductivité électrique apparente de 10 x 10 m (dS/m) à 1,5 m de profondeur pour le printemps et l'automne à la ferme Cook. 
et l'automne à la ferme Cook.

CAF_Bt_30cm.tif, CAF_Bt_60cm.tif, CAF_Bt_90cm.tif, CAF_Bt_120cm.tif, CAF_Bt_150cm.tif : fichiers contenant des surfaces prédictives de 10 x 10 m pour la probabilité (0-1) de l'horizon Bt aux cinq profondeurs du capteur. 
probabilité (0-1) de l'horizon Bt aux cinq profondeurs du capteur.