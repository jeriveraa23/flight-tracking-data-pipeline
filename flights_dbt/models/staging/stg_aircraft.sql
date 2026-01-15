{{ config(materialized='table') }}

SELECT
    UPPER("ModeS")                AS aircraft_id,
    "Registration"                AS registration_number,
    "RegisteredOwners"            AS owner_name,
    "Manufacturer",
    "ICAOTypeCode"                AS model_code,
    "OperatorFlagCode"            AS operator_code
FROM {{ source('api_data', 'aircraft_info')}}