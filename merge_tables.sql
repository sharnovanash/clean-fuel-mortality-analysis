/* Merging Air Quality and Mortality Tables */
SELECT
    m.Location,
    m.Period AS Year,
    c.Continent,
    m.Value AS Mortality_Rate,
    f.Value AS Clean_Fuel_Access
FROM Air_Pollution_Mortality m
JOIN Clean_Fuel_Access f
    ON m.Location = f.Location
    AND m.Period = f.Period
LEFT JOIN Continent_Map c
    ON m.Location = c.Country
WHERE m.Value IS NOT NULL
  AND f.Value IS NOT NULL;