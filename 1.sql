USE sakila;

-- SELECT * FROM actor;

-- SELECT * FROM city;

-- SELECT * FROM film;

-- SELECT title, length FROM film;

SELECT title, length FROM film ORDER BY length;

-- Rezultatu rikiavimas

SELECT * FROM film ORDER BY length DESC; -- rikiuos nuo didziausio iki maziausio

SELECT * FROM film ORDER BY length ASC;

-- Unikaliu reiksmiu paieska:

SELECT DISTINCT first_name FROM actor;

SELECT DISTINCT district  FROM address;

SELECT
	first_name AS vardas
--    ,last_name AS pavarde
FROM 
	actor;

SELECT
	release_year AS 'isleidimo metai'
    ,rental_duration AS 'nuomos trukme'
FROM film;

describe actor;

/*Išrinkti visus vardus aktorių lentelėje (actor)
Kokios yra galimos filmų kategorijos? (category)
Kokie filmai yra mūsų duomenų bazėje? (film)*/

SELECT first_name FROM actor;

SELECT name FROM category;

SELECT title FROM film;

SELECT 5+2 AS rezultatas;

SELECT 6+8*2/4 AS rezultatas;

SELECT
	customer_id
    ,payment_id
    ,amount
    ,amount * 10 + 1000  AS  new_amount
FROM payment;

-- count
SELECT 
	COUNT(*)
FROM film;

SELECT
	COUNT(film_id)
FROM film;

SELECT
	COUNT(original_language_id)
FROM film;

SELECT
	DISTINCT rental_rate
FROM film;

SELECT
	COUNT(DISTINCT rental_rate)
FROM film;

/*Pateikite visus duomenis iš rental lentelės, rezultatą išrikiuokite pagal rental_date nuo
naujausio įrašo. (rental)
Surūšiuoti filmus nuo brangiausio iki pigiausio (film)*/

SELECT * FROM rental ORDER BY rental_date DESC;

SELECT * FROM film ORDER BY rental_rate DESC;

/*Išrinkti skirtingos trukmės filmų ilgius (film), išrikiuoti nuo ilgiausiai trunkančio filmo.
Išrinkti visus nepasikartojančius vardus aktorių lentelėje (actor)
Išrinkti nepasikartojančias nuomos kainas (film)*/

SELECT DISTINCT length FROM film ORDER BY length DESC;

SELECT DISTINCT first_name FROM actor;

SELECT DISTINCT rental_rate FROM film;

/* Pažymėti filmo title ir description stulpelius ir juos pavadinti filmo pavadinimas, filmo
aprašymas (film) */

SELECT 
title AS 'filmo pavadinimas'
,description AS 'filmo aprasymas'
FROM
	film;

/*Pateikite visų filmų pavadinimus (title), filmo išleidimo metus (release_year), nuomos kainą (rental_rate) ir dvi naujas kainas: 
	a) nuomos kaina padidinta 10%, 
	b) nuomos kaina padidinta 15%. 
Pavadinkite naujus stulpelius `nauja kaina 10` ir `nauja kaina 15`.
Taip pat paskaičiuokite skirtumą tarp `nauja kaina 15` ir senosios nuomos kainos (rental_rate). Pavadinkite `kainų skirtumas`.
Išrikiuokite rezultatus pagal filmo išleidimo metus nuo naujausio ir pagal filmo pavadinimą abecėlės tvarka.
Naudoti FILM lentelę.*/

SELECT
	title
    ,release_year
    ,rental_rate
    ,rental_rate * 1.10 AS 'nauja kaina 10'
    ,rental_rate * 1.15 AS 'nauja kaina 15'
    ,(rental_rate * 1.15) - rental_rate AS 'kainu skirtumas'
FROM film ORDER BY release_year DESC, title;

/*1. Suskaičiuoti kiek aktorių turime aktorių lentelėje (actor)
2. Suskaičiuoti kiek turime unikalių aktorių vardų (first_name) 
(stulpelį pavadinti `Unikalių vardų skaičius`) ir kiek turime unikalių aktorių pavardžių 
(last_name) (stulpelį pavadinti `Unikalių pavardžių skaičius`).*/

SELECT
	COUNT(actor_id)
FROM actor;

SELECT
	COUNT(DISTINCT first_name) AS 'Unikaliu vardu skaicius'
    ,COUNT(DISTINCT last_name) AS 'Unikaliu pavardziu skaicius'
FROM actor;

SELECT *  FROM film;

SELECT
	SUM(length)
FROM film;

SELECT
	AVG(length)
    ,FORMAT(AVG(length), 1)
    ,TRUNCATE(AVG(length), 1)
FROM film;

SELECT
	MAX(length)
    ,MIN(length)
FROM film;

SELECT
	MIN(length)
FROM film;

SELECT
	COUNT(title)
FROM film; 

SELECT
	COUNT(DISTINCT length)
FROM film;


-- concat - skirtas tekstų sujungimui

SELECT
	first_name
    ,last_name
	,CONCAT(first_name, ' ', last_name) AS 'vardas pavarde'
FROM customer;

SELECT
	first_name
    ,last_name
	,LOWER(CONCAT(first_name, ' ', last_name)) AS 'vardas pavarde'
FROM customer;

-- upper/lower

SELECT
	LOWER(first_name)
    ,first_name
FROM customer;

SELECT 
	UPPER(description)
FROM film;

SELECT COUNT(password)
FROM staff;

SELECT
	store_id
    ,COUNT(customer_id) AS kiekis
FROM customer
GROUP BY store_id;

/*Kiek yra kokių vardų (first_name) aktorių lentelėje? (actor) 
Išrikiuokite nuo didžiausio kiekio mažėjančia tvarka. 
Jei yra besikartojančių vardų su tuo pačiu kiekiu, tuomet vardai turi būti išrikiuoti 
nuo Z iki A rikiavimo tvarka.*/

SELECT
	special_features
    ,COUNT(*)
FROM film GROUP BY special_features;

SELECT
	DISTINCT first_name
    ,COUNT(*)
FROM actor 
GROUP BY first_name
ORDER BY COUNT(first_name) DESC, first_name DESC;

SELECT
	DISTINCT first_name
    ,COUNT(*)
FROM actor 
GROUP BY first_name
ORDER BY COUNT(*) DESC, first_name DESC;

SELECT
	DISTINCT first_name
    ,COUNT(*) AS kiekis
FROM actor 
GROUP BY first_name
ORDER BY kiekis DESC, first_name DESC;

SELECT
	DISTINCT first_name
    ,COUNT(*) AS kiekis
FROM actor 
GROUP BY first_name
ORDER BY 2 DESC, 1 DESC;  --  2 ir 1 atspindi stulpeliu numeracija

/*1. Išrinkite visus aktorių pavardes ir vardus. (actor). Taip pat sujunkite concat 
pagalba stulpelį, kurio reikšmė vaizduotų tokią elektroninio pašto struktūrą: 
vardas.pavardė@gmail.com. Šis stulpelis turėtų būti parašytas mažosiomis raidėmis.
Rezultatus išrikiuoti pagal vardą (first_name) nuo Z iki A.*/

SELECT
	first_name
    ,last_name
	-- ,CONCAT(first_name, ' ', last_name) AS 'vardas pavarde'
    ,LOWER(CONCAT(first_name,'.',last_name, '@gmail.com'))  AS 'el. pastas'
FROM actor ORDER BY first_name;

/*2. Parašykite SQL užklausą, kuri ištrauktų visas nuomos trukmes (rental_duration) iš lentelės 
„film, suskaičiuokite kiek trukmių skirtingų pasikartoja lentelėje. Surūšiuokite rezultatus 
nuo dažniausiai pasikartojančios nuomos trukmės.*/

SELECT
	rental_duration
    ,COUNT(*)
FROM film GROUP BY rental_duration
ORDER BY COUNT(rental_duration) DESC;

/*3. Viename stulpelyje pateikite filmo pavadinimą (title) ir filmo ypatybes (special_features). 
Stulpelius atskirkite: tarpas, brūkšnelis, tarpas. Rezultatą pateikite mažosiomis raidėmis. 
(film)*/

SELECT
    LOWER(CONCAT(title, ' - ', special_features)) AS 'filmo pavadinimas ir ypatybes'
FROM film;

/*4. Kurių aktorių pavardės pasikartoja dažniausiai ir kiek kartų?*/

SELECT
	last_name
	,COUNT(*)
FROM actor GROUP BY last_name
ORDER BY COUNT(last_name) DESC;

/*5. Kiek ilgiausiai trunka filmas, saugomas lentoje film?*/

SELECT
	MAX(length)
FROM film;

-- filtravimas

SELECT * FROM customer;

SELECT
	active
    ,COUNT(1)
FROM customer
GROUP BY active
ORDER BY COUNT(1) DESC;

SELECT
	customer_id
    ,active
    ,first_name
    ,last_name
FROM customer
WHERE active = 0;


SELECT
	title
    ,rental_duration
    ,rental_rate
FROM film
WHERE rental_duration = 6;

SELECT
	title
    ,rental_duration
    ,rental_rate
FROM film
WHERE rental_duration >= 6;

SELECT
	title
    ,rental_duration
    ,rental_rate
FROM film
WHERE rental_duration != 6;

SELECT
	title
    ,rental_duration
    ,rental_rate
FROM film
WHERE rental_duration <> 6;

SELECT
	rental_duration
    ,COUNT(*)
FROM film
WHERE rental_duration = 6
GROUP BY rental_duration
ORDER BY COUNT(*);

SELECT
	store_id
    ,COUNT(*)
FROM customer
WHERE store_id = 1
GROUP BY store_id;

SELECT * FROM film WHERE title  = 'agent truman';

/*Užduotys:
Ištraukti visus filmus, kurie trunka (length) daugiau (>) negu 100 minučių (film)*/

SELECT
	title
    ,length
FROM film
WHERE length > 100
ORDER BY length ASC;

/*Ištraukti adresą, kuris(-ie) yra rajone (district) Ahal (address)*/

SELECT
	address
    ,district
FROM address
WHERE district  = 'Ahal';

/*Parašykite užklausą, kuri pateiktų visą informaciją apie filmus, kurių nuomos trukmė
(rental_duration) yra 3 dienos (lentelė: film)*/

SELECT  * FROM film
WHERE rental_duration =  3;

/*Pateikite filmo pavadinimą (title), aprašymą (description), išleidimo metus (release_year), reitingą
(rating), kur reitingas yra G (lentelė: film)*/

SELECT
	title
    ,description
    ,release_year
    ,rating
FROM film
WHERE rating = 'G';

/*Ištraukti visus adresus (address), kurie neturi pašto kodo (postal_code) ir telefono numerio (phone); lentelė: address*/

SELECT address FROM address
WHERE postal_code = '' AND phone = '';

/*Ištraukti filmų pavadinimus (title), nuomos laikotarpį (rental_duration), 
pakeitimo kainą (replacement_cost), kurių nuomos laikotarpis ilgesnis nei 5 dienos 
ir pakeitimo kaina mažesnė arba lygu 20; lentelė: film*/

SELECT
	title
    ,rental_duration
    ,replacement_cost
FROM film
WHERE rental_duration > 5 AND replacement_cost <= 20;

/*Ištraukti visą informaciją apie filmus, kurių nuomos kaina (rental_rate) 
daugiau už 3 dolerius ir reitingas lygus R; lentelė: film*/

SELECT * FROM film
WHERE rental_rate > 3 AND rating  = 'R';

describe address;

SELECT
	title
    ,description
    ,length
FROM film
WHERE length > 30 and length <20;

-- OR

/*Ištraukti visus filmų pavadinimus (title) ir jų filmų trukmes (length), kurių trukmė yra trumpesnė nei
50 min arba ilgesnė nei 140 min. Išrikiuokite nuo mažiausios trukmės; lentelė: film*/

SELECT
	title
    ,length
FROM film
WHERE length <50 OR length > 140
ORDER BY length ASC;

SELECT * FROM city LIMIT 5;


-- between

SELECT
	title
    ,length
    ,description
FROM film
WHERE length BETWEEN 50 AND 70;

SELECT
	MAX(amount)
FROM payment;

SELECT
	amount
    ,customer_id
    ,rental_id
FROM payment
WHERE amount BETWEEN 5 AND 12;

SELECT
	rating
FROM film
WHERE rating BETWEEN  'G' AND 'P';


--  IN  

SELECT
	title
    ,length
FROM film
WHERE length IN (47,57,92);

SELECT
	rating
    ,title
FROM film
WHERE  rating IN ('PG','G');

SELECT *
FROM film
WHERE description LIKE '%documentary%';

SELECT *
FROM film
WHERE title LIKE '%home%'; -- %zodis% procentai reiskia, kad nesvarbu kurioje sakinio dalyje yra ieskomas zodis

SELECT *
FROM film
WHERE title LIKE 'home%';

SELECT *
FROM film
WHERE title LIKE '%home';

SELECT *
FROM actor
WHERE first_name LIKE '_a%';

SELECT *
FROM actor
WHERE first_name LIKE '_a_';

-- NOT

SELECT *
FROM actor
WHERE first_name NOT LIKE '_a%';

SELECT
	title
    ,length
FROM film
WHERE length NOT IN (47,57,92);

/*Ištraukti visus filmų pavadinimus (title) ir jų filmų trukmes (length), 
kurių trukmė yra trumpesnė nei 50 min arba ilgesnė nei 140 min.
 Išrikiuokite nuo mažiausios trukmės; lentelė: film*/
 
SELECT
	title
    ,length
FROM film
WHERE length < 50 OR length > 140
ORDER BY length ASC;

/*Ištraukti visą informaciją apie adresus, kurie neturi pašto kodo ar telefono numerio*/

SELECT * FROM address
WHERE postal_code = '' OR phone = '';

/*Pateikite 5 klientų vardus ir pavardes, kurių pirkėjo id (customer_id) yra didžiausi customer
lentelėje;*/

SELECT
	first_name
    ,last_name
    ,customer_id
FROM customer ORDER BY customer_id DESC LIMIT 5;

/*Raskite 10 trumpiausių filmų. Pateikite filmų pavadinimą (title), aprašymą (description) ir trukmę
(length); lentelė: film*/

SELECT
	title
    ,description
    ,length
FROM film ORDER BY length ASC LIMIT 5;

/*Išrinkite filmus, kurių išnuomojimo kaina (rental_rate) yra tarp 1 ir 2.99; lentelė: film*/

SELECT *
FROM film
WHERE rental_rate BETWEEN 1 AND 2.99;


/*Išrinkite filmus, kurių trukmė (length) yra tarp 47 ir 100 min. Išrikiuokite nuo ilgiausiai trunkančio
filmo mažėjimo tvarka; lentelė: film*/

SELECT *
FROM film
WHERE length BETWEEN 47 AND 100
ORDER BY length DESC;

/*Išrinkite filmų pavadinimus, aprašymus, išleidimo metus, nuomos trukmę ir kainą, kai nuomos
kaina yra 4.99 arba mažiau, o nuomos trukmė 5 arba 6 dienos.*/

SELECT
	title
    ,description
    ,release_year
    ,rental_duration
    ,rental_rate
FROM film
WHERE rental_rate >=4.99 AND rental_duration BETWEEN 5 AND 6;

/*Išrinkite filmų pavadinimus, aprašymus, kurių pavadinimas prasideda ALI
Rasti filmus, kuriu pavadinimo antra raidė yra L*/

SELECT
	title
    ,description
FROM film
WHERE title LIKE 'ALI%';

SELECT
	title
    ,description
FROM film
WHERE title LIKE '_L%';

/*Išrinkite filmus kurių nuomojimo trukmė rental_duration nėra tarp 2 ir 4.*/

SELECT *
FROM film
WHERE rental_duration NOT BETWEEN 2 AND 4;