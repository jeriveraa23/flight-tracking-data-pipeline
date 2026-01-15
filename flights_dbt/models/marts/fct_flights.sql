{{ config(materialized='table') }}

WITH flights AS (
    SELECT * FROM {{ ref('stg_flights') }}
),
aircrafts AS(
    SELECT * FROM {{ ref('stg_aircraft') }}
)
SELECT
    f.capture_time,
    f.aircraft_id,
    f.flight_id,
    COALESCE(a."registration_number", 'Unknown')      AS registration,
    COALESCE(a."owner_name", 'Private/Unknown')       AS airline,
    COALESCE(a."Manufacturer", 'Unknown')             AS manufacturer,
    f.last_position_at,
    f.last_contact_at,
    f.country_aircraft_registration,
    f.latitude,
    f.longitude,
    f.barometric_altitude_meters,
    f.geometric_altitude_meters,
    f.flight_status,
    f.speed_kmh,
    f.cardinal_direction,
    f.vertical_status,
    f.coverage_status,
    f.source_position,
    f.squawk_status,
    f.ident_status
FROM flights f 
LEFT JOIN aircrafts a ON f.aircraft_id = a.aircraft_id