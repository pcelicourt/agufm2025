The Flags folder consists of the files containing the quality control flags for the Cook Farm Sensor Dataset.

The nomenclature for the files indicates flags for either temperature (T) or water content (VW) and sensor depths. For example: 
T_30 is for the temperature data at 30cm. depth 
VW_120 is for the Volumetric water content at 120 cm. depth

Files starting with “missing” contain flags (“M”) for locations and dates (mm/dd/yyyy) with missing data (NA in original dataset).

Files starting with “range” contain flags for locations and dates (mm/dd/yyyy) with values outside acceptable ranges:
Soil moisture (0-0.6 m^3/m^3) flagged as “C”
Soil temperature (<0 deg. C) flagged as “D”

Files starting with the name “flats” contain flags (“D”) for locations, dates (mm/dd/yyyy), and times (hh:mm) with constant values (within 1%) for a 24 hour period, as in Dorigo et al. 2013.

Files starting with the name “spikes” contain flags (“D”) for locations, dates (mm/dd/yyy), and times (hh:mm) with sudden spikes in VWC readings.

Files starting with the name “breaks” contain flags (“D”) for locations, dates (mm/dd/yyy), and times (hh:mm) with sudden breaks (jumps or drops) in VWC readings.

Code (implemented in R) for the screening and flagging is included in “Code Snippet.txt”

A list of the sensor versions as of 06/16/16 at each location and depth.
