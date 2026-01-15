{{ config(materialized='table') }}

SELECT
    TO_TIMESTAMP(time::DOUBLE PRECISION)                                        AS capture_time,
    TO_TIMESTAMP(time_position::DOUBLE PRECISION)                               AS last_position_at,
    TO_TIMESTAMP(last_contact::DOUBLE PRECISION)                                AS last_contact_at,
    icao24                                                                      AS aircraft_id,
    callsign                                                                    AS flight_id,
    origin_country                                                              AS country_aircraft_registration,
    longitude,                              
    latitude,
    baro_altitude::FLOAT                                                        AS barometric_altitude_meters,
    geo_altitude::FLOAT                                                         AS geometric_altitude_meters,
    CASE 
        WHEN on_ground::BOOLEAN THEN 'Landed'
        ELSE 'In Flight'
    END                                                                         AS flight_status,
    (velocity::FLOAT * 3.6)::DECIMAL(10,2)                                      AS speed_kmh,
    CASE
        WHEN true_track::FLOAT >= 315 OR true_track::FLOAT < 45 THEN CONCAT('North: ', true_track, '°')
        WHEN true_track::FLOAT >= 225 THEN CONCAT('West: ', true_track, '°')
        WHEN true_track::FLOAT >= 135 THEN CONCAT('South: ', true_track, '°')
        WHEN true_track::FLOAT >= 45  THEN CONCAT('East: ', true_track, '°')
        ELSE CONCAT('North: ', true_track, '°')
    END                                                                         AS cardinal_direction,
    CASE
        WHEN vertical_rate::FLOAT > 0.5  THEN 'Ascending'
        WHEN vertical_rate::FLOAT < -0.5 THEN 'Descending'
        ELSE 'Level Flight'
    END                                                                         AS vertical_status,
    CASE
        WHEN sensors IS NULL OR sensors = '' THEN 'Low Coverage'
        ELSE 'Active Coverage'
    END                                                                         AS coverage_status,
    CASE 
        WHEN position_source = 0 THEN 'ADS-B'
        WHEN position_source = 1 THEN 'ASTERIX'
        WHEN position_source = 2 THEN 'FLARM'
        WHEN position_source = 3 THEN 'MLAT'
        ELSE 'Unknown'
    END                                                                         AS source_position,
    CASE 
        WHEN squawk IS NULL THEN 'No Squawk Assigned'
        WHEN squawk = '7700' THEN 'EMERGENCY'
        ELSE 'Active/Normal'
    END                                                                         AS squawk_status,
    CASE 
        WHEN spi::BOOLEAN THEN 'Pilot Pressing IDENT'
        ELSE 'Normal'
    END                                                                         AS ident_status
    
FROM {{ source('api_data', 'flights_history')}}
