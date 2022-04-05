dropdb energyDemand
createdb energyDemand
psql -d energyDemand -f create_tables.sql
python3 obtain_data.py
psql -d energyDemand -f insert_data.sql
