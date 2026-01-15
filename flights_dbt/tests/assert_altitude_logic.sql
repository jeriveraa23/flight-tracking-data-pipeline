-- This query looks for the error: planes landed at impossible altitudes
SELECT
    flight_id,
    aircraft_id,
    flight_status
FROM {{ ref('fct_flights') }}
WHERE flight_status = 'Landed'
AND barometric_altitude_meters > 500