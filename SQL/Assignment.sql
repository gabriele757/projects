-- 1. 
/*
Naudoti: sql_invoicing.invoices;
Pateikti 'client_id', 'invoice_total', 'number' stulpelius. Surūšiuokite duomenis pagal 'client_id'
nuo mažiausios reikšmės ir pagal 'invoice_total' nuo didžiausios reikšmės (1t);
*/

SELECT
	client_id
    ,invoice_total
    ,number
FROM sql_invoicing.invoices
ORDER BY client_id, invoice_total DESC;

-- 2. 
/*
Naudoti: sql_invoicing.invoices; 
Pateikite visus unikalias 'client_id' reikšmes ir jas išrikiuokit
nuo didžiausios mažėjančia reikšme. (1t);
*/

SELECT
	DISTINCT client_id
FROM sql_invoicing.invoices
ORDER BY client_id DESC;

-- 3.
/*
Naudoti: sql_invoicing.payments;
Parašykite SQL užklausą, kuri paskaičiuoja bendrą visų mokėjimų ('amount') sumą.
Rezultatą pateikite stulpelyje 'iš viso'. Taip pat paskaičiuokite mokėjimų vidurkį - 
pavadinkite stulpelį 'mokėjimų vidurkis'. Paskaičiuokite mažiausią ir didžiausią mokėjimą.
Šiuos stulpelius pavadinkite savo parinktais pavadinimais.
Taip pat paskaičiuokite unikalių pirkėjų ('client_id') skaičių, bei unikalių sąskaitų faktūrų kiekį ('invoice_id').
Šiuos stulpelius taip pat pavadinkite savo parinktais pavadinimais. (2t);
*/

SELECT
	SUM(amount) AS 'iš viso'
    ,AVG(amount) AS  'mokėjimų vidurkis'
    ,MIN(amount) AS 'mažiausias mokėjimas'
    ,MAX(amount) AS 'didžiausias mokėjimas'
    ,COUNT(DISTINCT client_id)  AS 'Unikalių pirkėjų skaičius'
    ,COUNT(DISTINCT invoice_id) AS 'Unikalių sąskaitų-faktūrų kiekis'
FROM sql_invoicing.payments;

-- 4.
/*
Naudoti: sql_hr.employees; 
Parašykite SQL užklausą, kuri ištrauktų visus įrašus, kur stulpelio 'salary' 
reikšmė yra mažesnė už 40 000. Išrikiuokite įrašus nuo dižiausios algos ('salary') mažėjančia tvarka.
Prie šitų išfiltruotų įrašu pateikite papildomą stulpelį (užvadinkite jį 'new_salary'), kur 
alga būtų padidinta 15 procentų. (2t);
*/

SELECT
	*
    ,salary*1.15  AS new_salary
FROM sql_hr.employees
WHERE salary < 40000
ORDER BY salary DESC;

-- 5. 
/*
Naudoti: sql_store.products;
Ištirkite produkto pavadinimo ('name') stulpelį. Kelinta raidė yra 'e'. 
Išrikiuokite rezultatą nuo toliausiai esančios 'e' raidės. (1t);
*/

SELECT
	name
    ,LOCATE('e', name) AS 'raidės e indeksas'
FROM sql_store.products
WHERE (name LIKE '%e%') AND (LOCATE('e',name) > 0)
ORDER BY LOCATE('e', name) DESC;

-- 6. 
/*
Naudoti: sql_store.customers; 
Parašykite SQL užklausą, kuri ištrauktų visus įrašus, kurių miestas ('city') yra Vilnius, 
Klaipėda ir Alytus,
o lojalumo taškų ('points') pirkėjas yra surinkęs mažiau nei 1000.
Išrikiuoti rezultatus pagal lojalumo taškus didėjančia tvarka. (1t);
*/

SELECT
	*
FROM sql_store.customers
WHERE (city IN ('Vilnius', 'Klaipėda', 'Alytus')) AND (points < 1000)
ORDER BY points;

-- 7.
/*
Naudoti: sql_hr.employees;
Parašykite SQL užklausą, kuri suskaičiuotų algų sumą darbuotojų, 
kurių 'job_title' stulpelyje yra reikšmė 'Operacijų'.
Stulpelį pavadinkite `sum_salary` (1t);
*/

SELECT
	SUM(salary)
FROM sql_hr.employees
WHERE job_title LIKE '%Operacijų%';

-- 8.
/*
Naudoti: sql_store.shippers,
         sql_store.orders,
         sql_store.order_items;
Parašykite užklausą, kuri pateiktų tiekėjų (SHIPPERS lentelė) pavadinimus, 
kiekį skirtingų prekių ('product_id') ir kiekį skirtingų užsakymų ('order_id') tiekėjas yra tiekęs.
Stulpelius pavadinkite atitinkamai 'Cnt_unique_products', 'Cnt_unique_orders'.
Išrikiuokite rezultatą pagal tiekėjo pavadinimą abacėlės tvarka. (3t);
*/

SELECT
	t1.name 'Shipper_name'
    ,COUNT(DISTINCT t3.product_id) AS 'Cnt_unique_products'
    ,COUNT(DISTINCT t2.order_id) AS 'Cnt_unique_orders'
FROM sql_store.shippers t1
LEFT JOIN sql_store.orders t2
ON t1.shipper_id = t2.shipper_id
LEFT JOIN sql_store.order_items t3
ON t2.order_id = t3.order_id
GROUP BY t1.name
ORDER BY t1.name;

-- 9.
/*
Naudoti: sakila.film;
Parašykite SQL užklausą, kuri pateiktų filmų pavadinimus ('title'), reitingus ('rating'), bei 
suskirstytų filmus pagal jų reitingus ('rating') į tokias kategorijas:
Jei reitingas yra 'PG' arba 'G' tada 'PG_G'
Jei reitingas yra 'NC-17' arba „PG-13“ tada „NC-17_PG-13“
Visus kitus reitingus priskirkite kategorijai 'Nesvarbu'
Kategorijas atvaizduokite stulpelyje 'Reitingo_grupė' (2t)
*/

SELECT
	title
    ,rating
    ,CASE
        WHEN rating IN ('PG', 'G') THEN 'PG_G'
		WHEN rating IN ('NC-17', 'PG-13') THEN 'NC-17_PG-13'
        ELSE 'Nesvarbu'
	END AS Reitingo_grupė
FROM sakila.film;

-- 10.
/*
Naudoti: sakila.film;
Parašykite SQL užklausą, kuri suskaičiuotų kiek filmų priklauso reitingo grupėms, 
kurios buvo sukurtos 9-ame uždavinyje.
Rezultate pateikite tik tokias reitingo grupes, kurioms priklausantis filmų kiekis 
yra 250 - 450 intervale. 
Išrikiuokite rezultatą nuo didžiausio filmų kiekio mažėjančia tvarka. (4t)
*/

SELECT
	Reitingo_grupė
	,COUNT(*) AS kiekis
FROM (SELECT
	title
    ,rating
    ,CASE
        WHEN rating IN ('PG', 'G') THEN 'PG_G'
		WHEN rating IN ('NC-17', 'PG-13') THEN 'NC-17_PG-13'
        ELSE 'Nesvarbu'
	END AS Reitingo_grupė
FROM sakila.film) AS filmai_ir_reitingai
GROUP BY Reitingo_grupė
HAVING COUNT(*) BETWEEN 250 AND 450
ORDER BY kiekis DESC;

-- 11. 
/*
Naudoti: sakila.customer, 
		 sakila.rental, 
         sakila.inventory, 
         sakila.film;
Pateikite klientų vardus ('first_name') ir pavardes ('last_name') iš CUSTOMER lentelės, 
kurie išsinuomavo filmą 'AGENT TRUMAN'. 
Užduotį atlikite naudodami subquery konstruktus. Išrikiuokite rezultą pagal kliento vardą 
(first_name) abecėlės tvarka.
Užduotis atlikta teisingai be subquery vertinama (2t). 
P.S. teisingame subquery konsrtukte turi būti 4 x SELECT sakiniai. (4t);
*/

SELECT
	first_name
    ,last_name
FROM sakila.customer
WHERE customer_id  IN (
	SELECT 
		customer_id
	FROM sakila.rental
	WHERE inventory_id IN (
		SELECT 
			inventory_id
		FROM sakila.inventory
		WHERE film_id = (
			SELECT
				film_id
			FROM sakila.film 
			WHERE title = 'AGENT TRUMAN')))
ORDER BY first_name;
                                           
-- 12.
/*
Naudoti: sql_invoicing.clients, 
		 sql_invoicing.invoices;
Parašykite užklausą, kuri pateiktų clientų id ('client_id'), klientų pavadinimą ('name') ir kiek tie klientai 
turi neapmokėtų sąskaitų. Neapmokėtom sąskaitom ieškoti naudokite 'payment_date' stulpelį.
Išrikiuokite rezultatą pagal kliento id nuo diždiausios reikšmės mažėjančia tvarka. (3t);
*/

SELECT
	t1.client_id
    ,t1.name
    ,COUNT(t2.invoice_id) AS 'Neapmokėtos sąskaitos'
FROM sql_invoicing.clients t1
LEFT JOIN sql_invoicing.invoices t2
ON t1.client_id = t2.client_id
WHERE payment_date IS NULL
GROUP BY client_id
ORDER BY client_id DESC;

-- 13.
/*
Naudoti: sql_store.products;
Iš products lentelės pateikite produkto pavadinimą ('name').
Šalia pateikite ir kitą stulpelį, kuriame suformuotumėte naują produkto pavadinimo rašymo
 struktūrą ir pavadinkite jį 'new_name'.
Sąlyga: jei produkto pavadinimas turi tarpelį, tuomet naujoje struktūroje jį pakeiskite į 
tris žvaigždutes '***';
jei produkto pavadinimas tarpelio neturi, tuomet pridėkite prieš pavadinimą trys šauktukus '!!!'. (2t);
*/

SELECT
	name
    ,CASE
		WHEN LOCATE(' ', name) >0 THEN REPLACE(name, ' ', '***')
        ELSE CONCAT('!!!',name)
	END AS new_name
FROM sql_store.products;

-- 14.
/*
Naudoti: sql_store.customers;
Pateikite įrašus iš CUSTOMERS lentelės jei pirkėjas turi daugiau lojalumo taškų ('points') už visų  
esančių pirkėjų lojalumo taškų vidurkį. Naudokite tokiai paieškai SUBQUERY konstruktą.
Išrikiuokite įrašus nuo daugiausiai lojalumo taškų turinčio pirkėjo. (2t);
*/

SELECT
	*
FROM sql_store.customers
WHERE points > (
	SELECT
		AVG(points)
	FROM sql_store.customers)
ORDER BY points DESC;

-- 15.
/*
Parašykite SELECT užklausą, kuri atvaizduotų Jūsų vardą kaip reikšmę stulpelyje pavadinimu 'Vardas',
stulpelį 'VCS MySQL kursas' su reikšme 'Labai patiko :)' ir stulpelį 'Surinkau taškų' su taškų skaičiumi, kurį 
manote jog surinkote spręsdami šį testą. :)))
(1t);
*/

SELECT
	'Gabrielė' AS Vardas
    ,'Labai patiko :)' AS 'VCS MySQL kursas'
    ,30 AS 'Surinkau taškų';