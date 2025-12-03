-- Initialize PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Create timescale extension if needed
-- CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Set up database
-- Database will be created by environment variables
-- This script runs after database creation

