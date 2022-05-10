import csv

# Open a SQL file to write into.
f = open("insert_data.sql", "w")

# Open the "Properties.csv" file to read from.
with open('../../csv/Properties.csv', newline='') as csvfile:
	propertyreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	# Skip the header
	next(propertyreader)
	# For each row of the csv file, write an insert statement.
	for row in propertyreader:
		f.write('INSERT INTO buildings (BuildingName, PortfolioManagerID, YearBuilt, PropertyType, GrossFloorArea, OperationalHours, NumComputerLabs) VALUES (\'%s\',\'%s\',\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');\n' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

# Write a newline
f.write('\n')

# Open the "Meters.csv" file to read from.
with open('../../csv/Meters.csv', newline='') as csvfile:
	meterreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	# Skip the header
	next(meterreader)
	# For each row of the csv file, write an insert statement.
	for row in meterreader:
		f.write('INSERT INTO meters (PortfolioManagerMeterID, MeterName, MeterType) VALUES (\'%s\',\'%s\',\'%s\');\n' % (row[0],row[1],row[2]))

# Write a newline
f.write('\n')

# Open the "Costs.csv" file to read from.
with open('../../csv/Costs.csv', newline='') as csvfile:
	costreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	# Skip the header
	next(costreader)
	# For each row of the csv file, write an insert statement.
	for row in costreader:
		f.write('INSERT INTO costs (PortfolioManagerMeterID, StartDate, EndDate, Usage, Cost) VALUES (\'%s\',\'%s\',\'%s\', \'%s\', \'%s\');\n' % (row[0],row[1],row[2],row[3],row[4]))

# Close the SQL file after we're done writing to it.
f.close()


	
