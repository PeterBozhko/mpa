SELECT "ID", "Medicine_id"
FROM public."Side_effects_of_medicine"
WHERE "ID" = 0;

SELECT "ID", "Name", "Seriousness"
FROM public."Side_effects"
WHERE "ID" BETWEEN 0 AND 4;