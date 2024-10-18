-- A script that lists all bands with Glam rock
SELECT band_name,
     CASE
	 WHEN split IS NOT NULL THEN split - formed
	 ELSE 2024 - formed
     END AS lifespan
FROM
     metal_bands
WHERE
     style = 'Glam rock'
ORDER BY 
     lifespan DESC;
