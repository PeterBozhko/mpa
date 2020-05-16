SELECT "ID", "Frequency", "Medicine_id", "Side_effects_id"
	FROM public."Side_effects_of_medicine";
	
SELECT "ID", "Name"
FROM public."Medicine";
SELECT "Incompatibility"
FROM public."Medicine"
WHERE "ID" = "";