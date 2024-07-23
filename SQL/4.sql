-- 1. Naudokite customer lentelę ir atvaizduokite du stulpelius - first_name ir pirmas tris vardo raides

SELECT 
	first_name
    ,LEFT (first_name, 3) AS vardo_iskarpa
FROM customer;

-- 2. Naudokite film lentelę ir atvaizduokite du stulpelius - filmo title ir pirmus 10 simbolių  iš film title 

SELECT
	title
    ,LEFT(title, 10) AS simboliai
FROM film;

-- 3. Naudokite staff lentelę ir atvaizduokite du stulpelius - darbuotojo email ir paskutinius 10 email simbolius

SELECT
	email
    ,RIGHT(email, 10) email_simb
FROM staff;

-- 4. Naudokite rental lentelę ir atvaizduokite du stulpelius - nuomos datą (pilną) ir nuomos metus

SELECT
	rental_date
    ,SUBSTRING(rental_date, 1,4) AS Metai
FROM rental;

-- 5. Naudodami substring ir papildomą konvertavimo funkciją atvaizduokite tris stulpelius - rental_id, rental_date ir 
-- savaites diena (Mon, Tue, Wed)

SELECT
	rental_id
    ,rental_date
    ,SUBSTRING(DATE_FORMAT(rental_date, '%a'), 1,3) AS 'Savaites diena'
FROM rental;

-- 6. Naudodami film lentelę atvaizduokite du stulpelius - title ir trimmed_title, kuriame turėtų būti atvaizduojami duomenys
-- be tarpų priekyje ir gale

SELECT
	title
    ,TRIM(title) AS trimmed_title
FROM film;

-- 7. Atvaizduokite visus duomenis iš film lentelės, tačiau rezultatų lentelėje turi būti papildomas stulpelis, kuriame
-- vietoje PG matytume "Parental Guidance"

SELECT 
	*
    ,REPLACE(rating, 'PG', 'Parental Guidance') AS new_rating
FROM film;

-- 8.  atvaizudokite filmų pavadinimą ir stulpelyje šalia to pavadinimo raidžių kiekį
-- lentelė film

SELECT
	title
    ,LENGTH(title) AS 'raidziu kiekis pavadinime'
FROM film;


-- 9. atvaizudokite klientų email ir stulpelyje  to email raidžių kiekį
-- lentelė customer

SELECT
	email
    ,LENGTH(email) AS 'email raidziu kiekis'
FROM customer;

-- 10. naudokite locate ir suraskite @ poziciją klientų email'e, rezultate turime matyti 
-- customer_id, first_name, last_name, email ir email_poziciją
-- lentelė customer

SELECT
	customer_id
    ,first_name
    ,last_name
    ,email
	,LOCATE('@', email) AS email_pozicija
FROM customer;

-- 11. Suraskite žodžio "action" poziciją title stulpelyje, rezultate mes turime matyti tik 
-- tuos filmus, kurių title viduje yra žodis "Action"
-- pateikite film_id, title, ir action poziciją
-- lentelė film

SELECT
	film_id
    ,title
    ,LOCATE('Action',title) AS 'action pozicija'
FROM film
WHERE title like '%action%';


/*
 Išvesti iš lentelės film:
• Vidutinę nuomos trukmę
• Vidutinę nuomos kainą
• Vidutinę filmo trukmę
• Vidutinę pakeitimo kainą */

SELECT
	AVG(rental_duration)
    ,AVG(rental_rate)
    ,AVG(length)
    ,AVG(replacement_cost)
FROM film;

/*
• Bendrą visų filmų trukmę
• Bendrą visų filmų nuomos laiką */

SELECT
	SUM(length)
    ,SUM(rental_duration)
FROM film;

/*
• Kokia trumpiausia nuomos trukmė? */

SELECT
	MIN(rental_duration) AS 'trumpiausia nuomos trukme'
FROM film;

/*
• Kokie filmai buvo išsinuomoti ilgiausiai, trumpiausiai, kiek jų buvo kiek­
vienoje grupėje? */ -- ???

SELECT
    rental_duration,
    MIN(title) AS issinuomoti_trumpiausiai,
    MAX(title) AS issinuomoti_ilgiausiai,
    COUNT(*) AS film_count
FROM film
GROUP BY rental_duration
ORDER BY rental_duration;

/*
• Kokie ir kiek filmų buvo išsinuomoti vidutiniam nuomos laikui?
*/

SELECT
	COUNT(*) 
FROM film
WHERE rental_duration = (SELECT AVG(rental_duration) FROM film);

/*
• Ties kiek filmų jų apraše buvo pavartotas žodis ’boring’?
 */

SELECT
	COUNT(*)
FROM film
WHERE description LIKE '%boring%';

-- • Kiek filmų buvo minimalios trukmės, vidutinės, maksimalios?

SELECT
    'minimalios trukmės' AS 'Filmų trukmė',
    COUNT(*) AS 'Kiekis'
FROM
    film
WHERE
    length = (SELECT MIN(length) FROM film)
UNION
SELECT
    'vidutinės trukmės' AS 'Filmų trukmė',
    COUNT(*) AS 'Kiekis'
FROM
    film
WHERE
    length = (SELECT AVG(length) FROM film)
UNION
SELECT
    'maksimalios trukmės' AS 'Filmų trukmė',
    COUNT(*) AS 'Filmu kiekis'
FROM
    film
WHERE
    length = (SELECT MAX(length) FROM film);

-- A.1. Suraskite, kiek vidutiniškai trukdavo filmai, priklausomai nuo reitingo.

SELECT
	AVG(length) AS 'vidutine filmo trukme'
    ,rating
FROM film
GROUP BY rating;

-- A.2. Suraskite vidutinį nuomos laiką filmams pagal reitingą.

SELECT
	AVG(rental_duration) AS 'vidutinis nuomos laikas'
    ,rating
FROM film
GROUP BY rating;

-- A.3. Suraskite vidutinę nuomos kainą filmams pagal reitingą.

SELECT
	AVG(rental_rate) AS 'vidutine nuomos kaina'
    ,rating
FROM film
GROUP BY rating;

/*
B. Išvesti aktorių vardus, pavardes viename stulpelyje. Vardai turi būti mažo­
siomis raidėmis, pavardės ­ didžiosiomis. */

SELECT
	CONCAT(LOWER(first_name), ' ', UPPER(last_name)) AS vardai_pavardes
FROM actor;

/*
C. Išvesti aktorių vardus, prasidedančius raidėmis ’A’, ’B’, ’E’. Suskaičiuoti,
kiek vardų prasideda raidėmis ’D’, ’E’, ’W’. Čia turima omeny, jog jei turime
Dan, Ed, Wolf, tai atsakymas bus 3. */

SELECT
	first_name
FROM actor
WHERE (first_name LIKE 'A%') OR (first_name LIKE  'B%') OR (first_name LIKE 'E%');

 SELECT
	COUNT(first_name)
FROM actor
WHERE (first_name LIKE 'D%') OR (first_name LIKE  'E%') OR (first_name LIKE 'W%');

/*
CASE sakinio treniravimuisi
1. Parašykite SQL užklausą, kuri suskirstytų nuomos mokestį į tokias grupes:
• ­ jei mokestis 2 arba mažiau, tai priskiriama grupei “Minimalus”,
• ­ jei daugiau negu 2, bet mažiau arba lygu 6.99, tai “Vidutinis”,
• ­ kitu atveju, mokestis priskiriamas grupei “Didesnis nei vidutinis”.
Naudokite lentelę ”payment”. */

SELECT
	amount
    ,CASE
		WHEN amount <= 2 THEN 'Minimalus'
        WHEN (amount > 2) AND (amount <=6.99) THEN 'Vidutinis'
        ELSE 'Didesnis nei vidutinis'
	END AS 'Nuomos mokestis'
FROM payment;

/*
2. Parašykite SQL užklausą, kuri suskirsto filmus pagal jų trukmę į tokias
kategorijas:
• ­ Jei filmo trukmė 60 arba trumpiau, tai kategorija “Iki valandos”,
• ­ Jei filmo trukmė tarp 60 ir 120, tai kategorija “Iki dviejų valandų”,
• ­ Jei filmo trukmė tarp 120 ir 180, tai kategorija “Iki trijų valandų”,
Visais kitais atvejais filmus priskirkite kategorijai “Virš trijų valandų”. Naudo­
kite lentelę “film”. */

SELECT
	title
	,CASE
		WHEN length <= 60 THEN  'Iki valandos'
        WHEN length BETWEEN 60 AND 120 THEN 'Iki dviejų valandų'
        WHEN length BETWEEN 120 AND 180 THEN  'Iki trijų valandų'
        ELSE 'Virš trijų valandų'
	END AS 'Filmo trukme'
FROM film;

/*
3. Iššūkis:
Funkcija length() ­ grąžina elementų skaičių įraše. Tai yra length('Labas')
grąžins 5, nes žodyje ’Labas’ yra 5­ki simboliai.
Išveskite visus aktorių vardus, kurie yra trumpesni nei 5­ki simboliai.
Išveskite aktorių vardus ir naują stulpelį, kuriame būtų toks tekstas:
• ”5ki ir daugiau”, jei vardas yra iš 5­kių ir daugiau simbolių
• ”Mažiau 5­kių simbolių”, jei vardas turi mažiau 5­kių simbolių.
Suksaičiuokite, kiek vardų yra iš 5­kių ir daugiau simbolių ir kiek vardų turi
mažiau 5­kių simbolių. */

SELECT
	first_name
FROM actor
WHERE LENGTH(first_name) <5;

SELECT
	first_name
	,CASE
		WHEN LENGTH(first_name) >= 5 THEN '5ki ir daugiau'
        WHEN LENGTH(first_name) < 5 THEN 'Mažiau 5­kių simbolių'
	END AS 'Vardo simboliai'
FROM actor;

SELECT
	CASE
		WHEN LENGTH(first_name) >= 5 THEN '5ki ir daugiau'
        WHEN LENGTH(first_name) < 5 THEN 'Mažiau 5­kių simbolių'
	END AS 'Vardo simboliai'
    ,COUNT(*) AS kiekis
FROM actor
GROUP BY CASE
		WHEN LENGTH(first_name) >= 5 THEN '5ki ir daugiau'
        WHEN LENGTH(first_name) < 5 THEN 'Mažiau 5­kių simbolių'
	END;