SELECT * FROM actor;

SELECT 
	first_name
    ,last_name
FROM actor
WHERE first_name LIKE 'A%'
ORDER BY last_name DESC
LIMIT 5;

-- HAVING

SELECT *FROM film;

SELECT
	rating
    ,rental_rate
    ,COUNT(film_id) as kiekis
    ,SUM(replacement_cost) as suma
    ,AVG(replacement_cost) as pakeitimo_kaina
FROM film
GROUP BY rating, rental_rate
HAVING kiekis > 60
ORDER BY kiekis;

SELECT *  FROM customer;

SELECT
	first_name
    ,last_name
    ,address_id
FROM customer
HAVING adress_id = 6;

-- CASE
SELECT
	actor_id
    ,first_name
    ,CASE
		WHEN first_name LIKE 'A%' THEN 'Vardas prasideda raide A'
        WHEN first_name LIKE 'B%' THEN 'Vardas prasideda raide B'
        WHEN first_name LIKE 'C%' THEN 'Vardas prasideda raide C'
        ELSE 'Vardas neprasideda raide A, B arba C'
	END AS prasideda_raide
FROM actor
-- HAVING prasideda_raide IS NOT NULL
ORDER BY first_name ASC;

SELECT
    title
    ,rental_duration
    ,rental_rate
    ,CASE 
		WHEN rental_duration > 5 THEN rental_rate *  0.75
        ELSE rental_rate
	END as nuolaida
FROM film
ORDER BY rental_duration;

SELECT
	rental_rate
FROM film
WHERE rental_duration = 5;

SELECT
	rental_duration
    ,SUM(replacement_cost)
FROM film
GROUP BY  rental_duration;

SELECT
	ilgiai
	,COUNT(ilgiai) AS kiekis
FROM (SELECT
	title
    ,length
    ,CASE
		WHEN length <  50 THEN 'Filmas trumpesnis nei 50 min'
        WHEN length = 50 THEN 'Filmo trukme yra 50 minuciu'
        WHEN length > 50 THEN 'Filmas ilgesnis nei  50 minuciu'
	END AS ilgiai
FROM film) AS filmai
GROUP BY ilgiai
ORDER BY kiekis DESC;

-- Koks  yra vardas ir pavarde, zmogaus, kuris mums sumokejo daugiausiai?

SELECT MAX(amount) FROM payment;

SELECT
	customer_id
FROM payment
WHERE amount = (SELECT MAX(amount) FROM payment);

SELECT
	first_name
    ,last_name
FROM customer
WHERE customer_id IN (SELECT
	customer_id
FROM payment
WHERE amount = (SELECT MAX(amount) FROM payment));

SELECT
	first_name
    ,last_name
FROM customer
WHERE customer_id IN (27,45,62);

-- UNION

SELECT * FROM customer;
SELECT * FROM actor;

SELECT
	first_name
    ,last_name
    ,'klientas' AS tipas
    ,email 
FROM customer
UNION ALL
SELECT 
	first_name
	,last_name
   ,'aktorius' AS tipas
   ,NULL AS email
   -- ,'Nera vertes'
   -- ,''
FROM actor;

SELECT
	email
FROM customer
UNION
SELECT
	first_name
FROM actor;

-- UZDUOTYS

--  1. Parašykite SQL užklausą, kuri pateiktų visą informaciją apie filmus, 
--  kurių nuomos trukmė (rental_duration) yra tarp 4 ir 6 dienų. Lentelė: film

SELECT * FROM film
WHERE rental_duration BETWEEN 4 AND 6;

--   2. Parašykite SQL užklausą, kuri pateiktų filmo pavadinimą (title), aprašymą (description),
-- išleidimo metus (release_year), reitingą (rating), kai reitingas yra PG-13. Lentelė: film

SELECT
	title
    ,description
    ,release_year
    ,rating
FROM film
WHERE rating = 'PG-13';

--   3. Parašykite SQL užklausą, kuri ištrauktų filmo pavadinimą (title), nuomos trukmę (rental_duration), 
-- nuomos kainą (rental_rate), kai nuomos kaina yra 0.99 arba daugiau, o 
-- nuomos trukmė 6 ir 7 dienos. Lentelė: film

SELECT
	title
    ,rental_duration
    ,rental_rate
FROM film
WHERE rental_rate >= 0.99 AND rental_duration = 6 OR rental_duration = 7;

-- 4. Parašykite užklausą, kuri ištraukia visus filmų pavadinimus (title), 
--  kurie prasideda raide „z. Lentelė: film

SELECT
	title
FROM film
WHERE title LIKE 'z%';

--  5. Parašykite užklausą, kuri ištraukia filmo pavadinimą (title), nuomos kainą 
-- (rental_rate), fillmo ypatybes (special_features), kurių viena iš ypatybių yra Trailers. 
--  Pirmiausia surūšiuojant nuo trumpiausių iki ilgiausių nuomos terminų (rental_duration), 
-- paskui pagal nuomos kainą nuo brangiausių iki pigiausių.

SELECT
	title
    ,rental_rate
    ,special_features
    ,rental_duration
FROM film
WHERE special_features LIKE '%TRAILERS%'
ORDER BY rental_duration, rental_rate DESC;

/*Pateikite dešinėje esančią lentelę, kur no_films yra filmų skaičius, o Cost yra replacement_cost
suma. Tuomet pateikite tik tuos reitingus (rating) ir rental_rate, kurie turi daugiau nei 60 
filmų. Rezultatą surikiuokite pagal rental_rate didėjimo tvarka; lentelė: film.*/

SELECT * from film;

SELECT
	rating
    ,rental_rate
    ,COUNT(film_id) AS no_films
    ,SUM(replacement_cost) AS suma
FROM film
GROUP BY rating, rental_rate
HAVING no_films > 60
ORDER BY rental_rate;

/*Pateikite dešinėje esančią lentelę, kur no_films yra filmų
skaičius, o Cost yra replacement_cost suma. Tuomet pateikite
tik tuos reitingus ir rental_rate, kurie turi daugiau nei 60 filmų.
Rezultatą surikiuokite pagal rental_rate didėjimo tvarka.
Skaičiavimus naudokite tik įrašus, kurių reitingas (rating) yra „R“;
Lentelė: film. */

SELECT
	rating
    ,rental_rate
    ,COUNT(film_id) AS no_films
    ,SUM(replacement_cost) AS suma
FROM film
GROUP BY rating, rental_rate
HAVING no_films > 60 AND rating = 'R'
ORDER BY rental_rate;

/* Sukurkite tokią lentelę naudojant subqueries: */

SELECT
	ilgiai
	,COUNT(ilgiai) AS kiekis
FROM (SELECT
	title
    ,length
    ,CASE
		WHEN length <  50 THEN 'Filmas trumpesnis nei 50 min'
        WHEN length = 50 THEN 'Filmo trukme yra 50 minuciu'
        WHEN length > 50 THEN 'Filmas ilgesnis nei  50 minuciu'
	END AS ilgiai
FROM film) AS filmai
GROUP BY ilgiai
ORDER BY kiekis DESC;

/*Suraskite filmų nuomos laikotarpius: paėmimo (rental_date) ir grąžinimo datas 
(return_date) kliento, kurio pavardė yra LEE. Naudokite SUBQUERY rašydami užklausą; 
lentelės: rental, customer. */

SELECT
	customer_id
FROM customer
WHERE last_name = 'LEE';

SELECT
	rental_date
    ,return_date
FROM rental
WHERE customer_id IN (SELECT
	customer_id
FROM customer
WHERE last_name = 'LEE');

/*Kiek mažiausiai ir kiek daugiausiai už filmo nuomą yra sumokėjusi klientė Sarah Lewis? 
Naudokite SUBQUERY rašydami užklausą; lenteles: payment, customer.*/

SELECT
	MIN(amount)
    ,MAX(amount)
FROM payment
WHERE customer_id IN (SELECT
	customer_id
FROM customer
WHERE first_name = 'SARAH' AND last_name = 'LEWIS');

/*Kiek nuomos užsakymų įvykdė darbuotojas Mike Hillyer per 2005 metų liepos mėnesį?
Lentelės: rental, staff.*/

SELECT
	COUNT(rental_id) as Uzsakymai
FROM rental
WHERE rental_date LIKE '2005-07%' AND staff_id IN (SELECT
	staff_id
FROM staff
WHERE first_name = 'MIKE' AND last_name = 'HILLYER');

/*Parašykite SQL užklausą, pateikiančią pirkėjų id (customer_id), sumokamą mokestį už nuomą 
(amount). Tuos klientus, kurie sumoka už nuomą vienu kartu virš 10, pažymėkite kaip „Virš 10, 
o išleidžiančius iki 10, pažymėkite „Iki 10. Surūšiuokite pagal nuomos mokestį mažėjimo tvarka; 
lentelė: payment.*/

SELECT
	customer_id
    ,amount
	,CASE
		WHEN amount > 10 THEN 'Virs 10'
		WHEN amount < 10 THEN 'Iki 10'
    END AS 'Sumoka iki/virs 10'
FROM payment
ORDER BY amount DESC;
    

SELECT
	order_id
    ,first_name
    ,last_name
FROM orders
INNER JOIN customers
ON orders.customer_id =  customers.customer_id;

SELECT
	order_id
    ,t2.first_name
    ,t2.last_name
    ,t1.status
FROM orders AS t1  -- table1
JOIN customers AS t2
ON t1.customer_id = t2.customer_id;

SELECT
	order_id
    ,order_date
    ,first_name
    ,last_name
    ,name
FROM orders AS t1
JOIN customers AS t2
ON  t1.customer_id =  t2.customer_id
JOIN order_statuses AS t3
ON t3.order_status_id = t1.status;

SELECT
	t1.first_name
    ,t1.last_name
    ,t2.name
FROM sql_store.customers AS t1
JOIN sql_inventory.products AS t2
ON t1.customer_id = t2.product_id;

/*Sujunkite `order_items` lentelę su `products` lentele SQL_STORE duombazėje. Užklausos 
rezultate pateikite užsakymo id (order_id), produkto pavadinimą (name), pardavimo kiekį 
(order_items. quantity), pardavimo kainą (order_items.unit_price), bei pardavimo maržą 
(pardavimo kaina minus savikainą). Savikaina – products.unit_price Išrikiuokite rezultatą 
pagal produkto pavadinimą įprasta abecėlės tvarka ir pagal kiekį mažėjančia tvarka nuo 
didžiausio; lentelės: order_items, products.*/

SELECT 
	t2.order_id
    ,t1.name
    ,t2.quantity
    ,t2.unit_price
	,t2.unit_price -  t1.unit_price AS pardavimo_marza
FROM  sql_inventory.products AS t1
JOIN order_items AS t2
ON t1.product_id = t2.product_id
ORDER BY name, quantity DESC;

/*`sql_invoicing` duombazėje pateikite mokėjimų datų (`payments` lentelė), sąskaitų 
faktūrų id (‘invoice_id’), mokėjimų sumas (‘amount’), klientų vardus (‘name’) ir 
mokėjimų metodų pavadinimą (‘name’).
Naudokite: payments, clients, payment_methods lenteles.*/

SELECT
	t1.date 
    ,t1.invoice_id
    ,t1.amount suma
    ,t2.name pirkejas
    ,t3.name atsiskaitymas
FROM payments AS t1
JOIN clients AS t2
ON  t1.client_id =  t2.client_id
JOIN payment_methods AS t3
ON t3.payment_method_id = t1.payment_method;


-- 1.	Išrinkite miestų (city) pavadinimus ir šalių id (country_id). 
-- Išrikiuokite rezultatus pagal šalių id mažėjančia tvarka. 
-- Jei yra besikartojančių  šalių id, miestų pavadinimai turi būti rikiuojami 
-- abacėlės tvarka; lentelė – sakila.city 

SELECT
	city
    ,country_id
FROM city
ORDER BY country_id  DESC, city;

-- 2.	Suskaičiuokite kiek yra unikalių aktorių id numerių (actor_id). 
-- 		Rezultato stulpelį pavadinkite „Unikalių aktorių kiekis“; lentelė – sakila.film_actor

SELECT 
	COUNT(DISTINCT actor_id) AS 'Unikaliu aktoriu kiekis'
FROM actor;

-- 3.	Pateikite unikalius aktorių id (actor_id) ir suskaičiuokite kiek filmų yra suvaidinę aktoriai. 
-- Išrikiuokite rezultatą pagal aktoriaus id, kuris suvaidino mažiausiai filmų. Jei yra aktorių,
-- kurie yra suvaidinę vienodą kiekį filmų, 
-- tuomet eiliškume pirmutinę vietą turėtų turėti mažesnės reikšmės aktoriaus id numeris. 
-- Stulpelį, kuriame pateikiamas filmų kiekis pavadinkite “Filmų kiekis”; lentelė – sakila.film_actor

SELECT
	DISTINCT actor_id
    ,(film_id) AS 'Filmu kiekis'
FROM  film_actor
ORDER BY film_id, actor_id ;

-- 4.	Viename stulpelyje pateikite filmo id (film_id) ir kategorijos id (category_id). 
-- Stulpelį pavadinkite “Kombinacija”. Išrikiuokite rezultatą nuo didžiausios reikšmės
-- mažėjančia tvarka; lentelė sakila.film_category

SELECT
	CONCAT(film_id, ' ',category_id) AS Kombinacija
FROM  film_category
ORDER BY Kombinacija DESC;

-- 5.	Pateikite unikalius darbuotojus (staff_id), šalia pateikite bendrą mokėjimų sumą 
-- (amount) – pavadinkite tai “Mokėjimų suma”,
-- taip pat pateikite mokėjimų vidurkį – pavadinkite tai “Mokėjimų vidurkis”, ir 
-- mokėjimų kiekį – pavadinkite “Mokėjimų kiekis”
-- Rezultatai turi būti suapvalinti iki dviejų skaičių po kablelio; lentelė – sakila.payment

SELECT
	staff_id
    ,SUM(amount) AS 'Mokejimu suma'
    ,FORMAT(AVG(amount),2) AS 'Mokejimu vidurkis'
    ,COUNT(amount) AS 'Mokejimu kiekis'
FROM payment
GROUP BY staff_id;

-- 6.	Pateikite visus įrašus iš rental lentelės, kurie priklauso pirkėjui (customer_id), 
-- kurio id yra 408. 
-- Išrikiuokite rezultatą nuo vėliausios nuomos datos (rental_date); lentelė – sakila.rental

SELECT * 
FROM rental
WHERE customer_id = '408'
ORDER BY rental_date DESC;


-- 7.	Suskaičiuokite kiek yra aktorių, kurių vardas (first_name) yra „DAN“; lentelė - sakila.actor

SELECT
	COUNT(first_name)
FROM  actor
WHERE first_name LIKE 'DAN';

-- 8.	Kiek aktyvių (active) pirkėjų yra priskirtų parduotuvei, kurios id yra 2; lentelė – sakila.customer

SELECT
	COUNT(active)
FROM customer
WHERE active = '1' AND store_id = '2';

-- 9.	Paskaičiuokita kiek kartų pirkėjai (customer_id) nuomojosi filmus per šiuos laikotarpius:
-- 		a) 2005 metų pirmą pusmetį
-- 		b) per visą laikotarpį išskyrus 2006 metų pirmą pusmetį
-- 		Abejais atvejais stulpelį, kuris skaičiuoja kiekį pavadinkite Kiekis, taip pat
-- 		išrikiuokite rezultatą nuo didžiausio kiekio mažėjančia tvarka
-- 		lentelė – sakila.rental
-- A

SELECT
	COUNT(customer_id)
    ,COUNT(rental_date) AS Kiekis
FROM rental
WHERE rental_date BETWEEN '2005-01-01 00:00:00' AND '2005-07-01 00:00:00'
ORDER BY customer_id;

-- B
SELECT
	COUNT(customer_id)
    ,COUNT(rental_date) AS Kiekis
FROM rental
WHERE rental_date NOT BETWEEN '2006-01-01 00:00:00' AND '2006-07-01 00:00:00'
ORDER BY customer_id;

-- 10.	Kiek yra filmų/inventoriaus (inventory_id), kurie yra negrąžinti (return_date)?
-- 		lentelė – sakila.rental

SELECT
	COUNT(inventory_id)
FROM rental
WHERE return_date IS NULL;


-- 11. 	Pateikite visus įrašus, kurių nuomos data (rental_date) yra ankstesnė nei 2005 
-- gegužės 25 diena arba nuomos data vėlesnė arba lygi
-- 	2006 metų sausio 1 diena ir kurių inventoriaus id (inventory_id) yra mažesnis arba 
--  lygus 600 arba didesnis nei 1500.
-- 	Išrikiuokite pagal nuomos datą nuo anksčiausios ir pagal inventoriaus id didėjančia seka.
-- 	lentelė – sakila.rental

SELECT *
FROM rental
WHERE (rental_date NOT BETWEEN '2005-05-25 00:00:00' AND '2006-01-01 00:00:00') AND (inventory_id <= 600 OR inventory_id >1500)
ORDER BY rental_date DESC, inventory_id;

-- 12.
/*
Naudoti: sql_invoicing.invoices lentelę. 
Pateikite visus stulpelius iš `invoices` lentelės, išfiltruokite tik tuos įrašus, 
kurie turi `payment_date` ir surūšiuokite pagal `invoice_date` pateikiant naujausią datą viršuje.
*/

SELECT *
FROM sql_invoicing.invoices
WHERE payment_date IS NOT NULL
ORDER BY invoice_date DESC;

-- 13.
/*
Naudoti: sql_invoicing.invoices lentelę. 
Pateikite `invoice_id`, `invoice_total`, `payment_total` ir suskaičiuokite, 
kiek klientui yra likę sumokėti (pavadinkite šį atributą `left_to_pay`). 
Taip pat pateikite atskirą stulpelį, kuriame parodysit kiek procentaliai jau 
yra sumokėta nuo `invoice_total`. Pavadinkite šį stulpelį `percentage_of_paid_amount`.
Taip pat išrikiuokite rezultatą pagal daugiausiai likusius sumokėti invoice'u (`left_to_pay`)
*/

SELECT
	invoice_id
    ,invoice_total
    ,payment_total
    ,invoice_total - payment_total  AS left_to_pay
    ,(payment_total/invoice_total)*100 AS percentage_of_paid_amount
FROM sql_invoicing.invoices
ORDER BY left_to_pay DESC;

-- 14.
/*
Naudoti: sql_invoicing.invoices lentelę. 
Pateikite `invoice_id`, `payment_total`.
Pateikite TOP 5 įrašus išrikiuojant rezultatus pagal `payment_total`.
*/

SELECT
	invoice_id
    ,payment_total
FROM sql_invoicing.invoices 
ORDER BY payment_total DESC LIMIT 5;

-- 15.
/*
Naudoti: sql_invoicing.payments lentelę. 
Parašykite SQL užklausą, kuri paskaičiuoja kiek yra atliktų mokėjimų ir kiek yra unikalių klientų (client_id). Mokėjimų kiekį užvadinkite`count_payments`, klientų kiekį pavadinkite `count_unique_clients`. 
Trečiam stulpelyje pateikite didžiausią mokėjimų sumą (amount) - pavadinkite `maximum_amount`.
Ketvirtame stulpelyje pateikite mažiausią mokėjimų sumą (amount) - pavadinkite `minimum_amount`.
Penktame stulpelyje paskaičiuokite unikalių `payment_method` kiekį.Pavadinkite stulpelį `count_unique_payment_methods`.
Paskutiniamme stulpelyje pateikite skirtumą tarp didžiausios ir mažiausios mokėjimų sumos.Šį stulpelį pavadinkite `min_max_amount_range`.
*/

SELECT
	COUNT(payment_id) AS count_payments
    ,COUNT(DISTINCT client_id) AS count_unique_clients
    ,MAX(amount) AS maximum_amount
    ,MIN(amount) AS minimum_amount
    ,COUNT(DISTINCT payment_method) AS count_unique_payment_methods
    ,MAX(amount) - MIN(amount) AS min_max_amount_range
FROM sql_invoicing.payments;

-- 16.
/*
Naudoti: sql_hr.employees lentelę. 
Parašykite SQL užklausą, kuri ištrauktų visus stulpelius, kurių `office_id` reikšmės yra 2 ir 3
o `first_name` prasideda pirmąja `S` arba `A` raide.
Išrikiuoti rezultatus pagal `last_name` abecėlės tvarka.
*/

SELECT *
FROM sql_hr.employees
WHERE office_id BETWEEN 2 AND 3 AND  first_name LIKE 'S%' OR first_name LIKE 'A%';

-- 17.
/*
Naudoti: sql_hr.employees lentelę. 
Parašykite SQL užklausą, kuri pateiktų `job_title` reikšmes,
kurių pabaiga pasibaigia `kas`. 
Išrikiuokite `job_title` atvirkštine abecėles tvarka - nuo Z iki A.
*/

SELECT
	job_title
FROM sql_hr.employees
WHERE job_title LIKE '%KAS'
ORDER BY job_title DESC;


-- 18.
/*
Naudoti: sql_hr.employees lentelę. 
Parašykite SQL užklausą, kuri pateiktų visų darbuotojų, kurie 
yra atskaitingi Daliai Pargienei, atlyginimų vidurkį, aukščiausią ir mažiausią atlygius.
WHERE sakinyje panaudokite SUBQUERY konstruktą.
*/

SELECT
	AVG(salary)
    ,MAX(salary)
    ,MIN(salary)
FROM sql_hr.employees
WHERE (SELECT
	employee_id
FROM sql_hr.employees
WHERE first_name = 'Dalia' AND last_name = 'Pargienė');


-- 19.
/*
Naudoti: sql_store.products lentelę. 
Parašykite SQL užklausą, kuri paskaičiuotų productų esančių sandėlyje vertę. 
Pateikite produkto pavadinimą (užvadinkite `product_name`), o vertę pavadinkite `total_value`.
Rezultate pateikite TOP 3 įrašus pagal `total_value`.
*/

SELECT
	name AS product_name
    ,unit_price * quantity_in_stock AS total_value
FROM sql_store.products
ORDER BY total_value DESC LIMIT 3;

-- 20.
/*
Naudoti: sql_store.products lentelę. 
Parašykite SQL užklausą, kuri paskaičiuotų kiekį prekių,
kurių `quantity_in_stock` yra tarp 5 ir 45. 5 ir 45 reikšmės turi patekti į intervalą.
*/

SELECT
	COUNT(quantity_in_stock)
FROM sql_store.products
WHERE quantity_in_stock BETWEEN 5 AND 45;

-- 21.
/*
Naudoti: sql_store.products lentelę. 
Parašykite SQL užklausą, kuri paskaičiuotų prekių,
kurių `product_id` nėra 3 ir 7, kiekį ir sumą `quantity_in_stock`.
*/

SELECT
	COUNT(quantity_in_stock)
    ,SUM(quantity_in_stock)
FROM sql_store.products
WHERE product_id !=3 AND product_id !=7;

-- 22. 
-- Pateikite visą informaciją apie filmus, kurių filmo ilgis trumpiausias. 
-- Panaudokite SUBQUERY (Select'as selecte) ieškant trumpiausios filmo trukmės
-- Išrikiuokite rezultatą pagal replacement_cost mažėjimo tvarka; 
-- lentelė: sakila.film.

SELECT *
FROM film
WHERE length = (SELECT MIN(length)
    FROM film)
ORDER BY replacement_cost DESC;

-- 23. 
-- Ištraukite visą informaciją apie filmus, kurių nuomos trukmė yra 4,
-- o reitingas turi 'NC-17' arba 'PG'  reikšmę. Rezultatus išrikiuokite pagal filmo 
-- trukmę (length) didėjimo tvarka. Pateikite tik 7 įrašus, kurie turi 
-- mažiausias filmo trukmės reikšmes; lentelė sakila.film.

SELECT *
FROM sakila.film
WHERE rental_duration = 4
HAVING rating = 'NC-17' OR rating = 'PG'
ORDER BY length LIMIT 7;

-- 24. 
-- Parašykite SQL užklausą, kur susumuotumėte nuomos kainą (rental_rate), grupuojant ją pagal 
-- nuomos trukmę (rental_duration). 
-- Rezultate pateikite tik tuos atvejus, kai nuomos kainos suma yra daugiau nei 600.
-- Išrikiuokite rezultatus nuo didžiausios nuomos kainos sumos mažėjančia tvarka; lentelė: 
-- sakila.film

SELECT 
	SUM(rental_rate) AS Suma
    ,rental_duration
FROM film
GROUP BY rental_duration
HAVING SUM(rental_rate) > 600
ORDER BY SUM(rental_rate) DESC;

-- 25. 
-- Suskaičiuokite filmų ACE GOLDFINGER, ADAPTATION HOLES, AFFAIR PREJUDICE (filmų pavadinimai) bendrą filmų trukmę (length) - 
-- pavadinkite stulpelį 'Bendra filmų trukmė', paskaičiuokite šių filmų unikalių nuomos kainų 
-- (rental_rate) kiekį - 
-- pavadinkite stulpelį 'Unikalių nuomos kainų kiekis', pateikite didžiausią iš išvardintų filmų
--  nuomos sumą už nuomos laikotarpį, 
-- jei ją skaičiuotume pritaikant sąlygą: nuomos trukmę dauginant iš nuomos kainos - pavadinkite 
-- stulpelį 'Didžiausia nuomos kaina'
-- ; lentelė: sakila.film.

SELECT
    SUM(length) AS 'Bendra filmų trukmė',
    COUNT(DISTINCT rental_rate) AS 'Unikalių nuomos kainų kiekis',
    MAX(rental_rate * rental_duration) AS 'Didžiausia nuomos kaina'
FROM film
WHERE title IN ('ACE GOLDFINGER', 'ADAPTATION HOLES', 'AFFAIR PREJUDICE');
    


-- 26. 
-- Suskaičiuokite kiek yra filmų, kurie aprašyme (description) turi fragmentą „Doc“ 
-- ir kurių kaina (rental_rate) yra 2.99, gautą sulpelį pavadinkite -  Filmu_skaicius; lentelė sakila.film.

SELECT 
    COUNT(*) AS Filmu_skaicius
FROM film
WHERE (description LIKE '%Doc%') AND (rental_rate = 2.99);

-- 27. 	
-- 	Pateikite užsakymų (order_id) krepšelio vidurkį. Krepšelio kaina apskaičiuojama kaip suma 
-- parduotų produktų kiekio (quantity) 
-- 	ir vieneto kainos (unit_price) sandaugos.
-- 	Užsakymų krepšelio vidurkį skaičiuosime tik tokiems užsakymams, kurie turi daugiau nei vieną užsakymą.
-- 	Taip pat suapvalinkime atsakymą iki sveikųjų skaičių.
-- 	Lentelė: sql_store.order_items

SELECT 
    ROUND(AVG(quantity * unit_price)) AS 'Uzsakymu krepselio vidurkis'
FROM order_items
--  GROUP BY order_id
HAVING COUNT(order_id) > 1;



