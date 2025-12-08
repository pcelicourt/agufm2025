#!/bin/bash
# Database setup script for AGU FM 2025

DB_NAME="agufmdb"
DB_USER="agufm2025"
DB_PASSWORD="agufm2025"

echo "Installing PostgreSQL client..."
sudo apt-get update 
sudo apt-get install -y postgresql-client

echo "Starting PostgreSQL service..."
sudo service postgresql start

# Wait for PostgreSQL to be ready
sleep 2

echo "Creating database user and database..."
sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';" || echo "User already exists"
sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;" || echo "Database already exists"
sudo -u postgres psql -d $DB_NAME -c "CREATE EXTENSION IF NOT EXISTS postgis;"
sudo -u postgres psql -c "ALTER USER $DB_USER CREATEDB;"

echo ""
echo "Database setup complete!"
echo "Database: $DB_NAME"
echo "User: $DB_USER"
echo "Password: $DB_PASSWORD"
echo ""
echo "Connection string: postgresql://$DB_USER:$DB_PASSWORD@localhost:5432/$DB_NAME"
echo "Installing PostgreSQL client..."
sudo apt-get update && sudo apt-get install -y postgresql-client
echo "Creating PostGIS extension and granting CREATEDB privilege..."
sudo -u postgres psql -d agufmdb -c "CREATE EXTENSION postgis;" 
sudo -u postgres psql -c "ALTER USER agufm2025 CREATEDB;"