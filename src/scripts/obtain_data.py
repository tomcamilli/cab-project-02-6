import csv

f = open("insert_data.sql", "w")

with open('../../csv/Properties.csv', newline='') as csvfile:
	propertyreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(propertyreader)
	for row in propertyreader:
		f.write('INSERT INTO buildings (BuildingName, PortfolioManagerID, YearBuilt, PropertyType, GrossFloorArea, OperationalHours, NumComputerLabs) VALUES (\'%s\',\'%s\',\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');\n' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

f.write('\n')

with open('../../csv/Meters.csv', newline='') as csvfile:
	meterreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(meterreader)
	for row in meterreader:
		f.write('INSERT INTO meters (PortfolioManagerMeterID, MeterName, MeterType) VALUES (\'%s\',\'%s\',\'%s\');\n' % (row[0],row[1],row[2]))


f.write('\n')
		
with open('../../csv/Costs.csv', newline='') as csvfile:
	costreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(costreader)
	for row in costreader:
		f.write('INSERT INTO costs (PortfolioManagerMeterID, StartDate, EndDate, Usage, Cost) VALUES (\'%s\',\'%s\',\'%s\', \'%s\', \'%s\');\n' % (row[0],row[1],row[2],row[3],row[4]))

f.close()


	
