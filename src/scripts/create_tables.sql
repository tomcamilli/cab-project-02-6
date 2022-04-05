CREATE TABLE buildings(
	BuildingName text,
	PropertyType text,
	PortfolioManagerID char(7) PRIMARY KEY,
	GrossFloorArea int,
	YearBuilt smallint,
	OperationalHours text,
	NumComputerLabs int
);

CREATE TABLE meters(
	PortfolioManagerMeterID char(8) PRIMARY KEY,
	MeterName varchar(4) UNIQUE,
	MeterType text
);

CREATE TABLE costs(
	PortfolioManagerMeterID char(8),
	StartDate date,
	EndDate date,
	Cost float,
	Usage int,
	FOREIGN KEY (PortfolioManagerMeterID)
	REFERENCES meters (PortfolioManagerMeterID) MATCH FULL,
	PRIMARY KEY (PortfolioManagerMeterID, StartDate, EndDate)
);
