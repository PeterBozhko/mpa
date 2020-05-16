SELECT "ID"
	FROM public."Anamnesis";

SELECT * FROM public."Patient";
SELECT "ID" ,"Disease_id", "Medicine_id"
    FROM public."Patient", public."disease_anamnesis", public."medicine_anamnesis"
	WHERE "Disease_id" = "ID" AND "Medicine_id" = "ID";

SELECT "Name", "Active_substance"
FROM public."Medicine"
WHERE "ID" = 0;

SELECT "Name"
FROM public."Disease"
WHERE "ID" = 0;