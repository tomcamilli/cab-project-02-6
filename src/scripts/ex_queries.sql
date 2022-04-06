
SELECT Cost, Usage
FROM meters NATURAL JOIN costs
WHERE MeterType = 'Electric - Grid' AND StartDate >= '2018-03-01' AND StartDate <= '2018-03-31';

SELECT Cost, Usage
FROM meters NATURAL JOIN costs
WHERE MeterType = 'Natural Gas' AND StartDate >= '2018-03-01' AND StartDate <= '2018-03-31';

SELECT BuildingName, YearBuilt, PropertyType, GrossFloorArea, OperationalHours, NumComputerLabs
FROM buildings
WHERE PortfolioManagerID = '6610023';
