-- This query looks for the error: planes flying nut no latitud reported
SELECT
    flight_id,
    flight_status,
    barometric_altitude_meters
FROM {{ ref('fct_flights') }}
WHERE flight_status = 'In Flight'
AND barometric_altitude_meters IS NULL