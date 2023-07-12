-- Lists all bands with Glam Rock as their main style
-- deisplays columns band_name and Lifespan
SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE  "%Glam rock%" ORDER BY lifespan DESC;