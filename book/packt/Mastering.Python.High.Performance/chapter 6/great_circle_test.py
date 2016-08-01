from great_circle_py import great_circle #4.5 seconds
#from great_circle_cy_v1 import great_circle #3 seconds
#from great_circle_cy_v2 import great_circle #0.98 seconds
#from great_circle_cy_v3 import great_circle

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 5000000

for i in range(num):
	great_circle(lon1,lat1,lon2,lat2)
