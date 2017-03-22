# Full path and name to your csv file
import os
pth = os.path.dirname(os.path.realpath(__file__))
csv_filepathname = os.path.join(pth,"Devon.csv")
# Full path to your django project directory
your_djangoproject_home = pth

import sys,django
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'csapi.settings'
django.setup()
#from django.conf import settings



from traffic.models import AADF
#from cityscience.trafficcounts.models import AADF

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'AADFYear': # Ignore the header row, import everything else
        aadf = AADF()
        aadf.AADFYEAR = row[0]
        aadf.CP = row[1]
        aadf.Estimation_method = row[2]
        aadf.Estimation_method_detailed = row[3]
        aadf.Region = row[4]
        aadf.LocalAuthority = row[5]
        aadf.Road= row[6]
        aadf.RoadCategory = row[7]
        aadf.Easting = row[8]
        aadf.Northing = row[9]
        aadf.StartJunction = row[10]
        aadf.EndJunction = row[11]
        aadf.LinkLength_km = row[12]
        aadf.LinkLength_miles = row[13]
        aadf.PedalCycles = row[14]
        aadf.Motorcycles = row[15]
        aadf.CarsTaxis = row[16]
        aadf.BusesCoaches = row[17]
        aadf.LightGoodsVehicles = row[18]
        aadf.V2AxleRigidHGV = row[19]
        aadf.V3AxleRigidHGV = row[20]
        aadf.V4or5AxleRigidHGV = row[21]
        aadf.V3or4AxleArticHGV = row[22]
        aadf.V5AxleArticHGV = row[23]
        aadf.V6orMoreAxleArticHGV = row[24]
        aadf.AllHGVs = row[25]
        aadf.AllMotorVehicles = row[26]
        aadf.save()
