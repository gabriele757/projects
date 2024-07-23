SELECT 
    t1.first_name,
    t1.last_name,
    t2.order_id
FROM customers AS t1
INNER JOIN orders AS t2
ON t2.customer_id = t1.customer_id;


SELECT
	t1.*
    ,t2.note
FROM order_items AS t1
JOIN order_item_notes AS t2
ON  t1.order_id  =  t2.order_Id AND t1.product_id = t2.product_id;

-- implicit join 

SELECT *
FROM orders AS t1
JOIN customers AS t2
ON t1.customer_id = t2.customer_id;

SELECT  *
FROM orders t1, customers t2
WHERE t1.customer_id = t2.customer_id;

SELECT 
    t1.first_name,
    t1.last_name,
    t2.order_id
FROM customers AS t1
INNER JOIN orders AS t2
ON t2.customer_id = t1.customer_id;


SELECT 
    t1.first_name,
    t1.last_name,
    t2.order_id
FROM customers AS t1
LEFT JOIN orders AS t2
ON t2.customer_id = t1.customer_id;


-- 1. Pateikite visų esančių produktų id (product_id), pavadinimus (name) bei
--   produktų kiekį (quantity) iš `order_items` lentelės.
-- Kokio produkto nėra užsakymo krepšeliuose?
-- Naudokite products ir order_items lenteles. DB: SQL_STORE

SELECT
	t1.product_id
    ,t2.name
    ,t1.quantity
FROM order_items AS t1
LEFT JOIN products AS t2
ON t1.product_id = t2.product_id;

-- 2. Parašius JOIN užklausą, pabandykite panaudoti ją SUBQUERY konstrukte pateikiant
-- atsakymą dėl produkto, kurio nėra užsakymo krepšeliuose. COUNT() produktų, kurių nebuvo.

SELECT *
FROM products, order_items
WHERE (SELECT
	t1.product_id
    ,t2.name
    ,t1.quantity
FROM order_items AS t1
LEFT JOIN products AS t2
ON t1.product_id = t2.product_id);

--  1) Pateikite visas užsakymų datas (order_date), užsakymų id (order_id), pirkėjų vardą
-- (first_name), pavardę (last_name), siuntėjo pavadinimą (shippers.name), užsakymo būklę 
-- (order_statuses.name).
-- 2) Sugrupuokite pirmos užduoties duomenis pateikdami užsakymo būkles ir jų kiekį.
-- Naudokite orders, customers, shippers, order_statuses lenteles.

SELECT
	t1.order_date
    ,t1.order_id
    ,t2.first_name
    ,t2.last_name
    ,t3.name as 'shipper'
    ,t4.name as 'bukle'
FROM orders AS t1
LEFT JOIN customers AS t2 ON t1.customer_id = t2.customer_id
LEFT JOIN shippers AS t3 ON t1.shipper_id = t3.shipper_id
LEFT JOIN order_statuses AS t4 ON t1.status = t4.order_status_id;

SELECT
	bukle
	,count(bukle) as 'kiekis'
FROM (SELECT
	t1.order_date
    ,t1.order_id
    ,t2.first_name
    ,t2.last_name
    ,t3.name as 'shipper'
    ,t4.name as 'bukle'
FROM orders AS t1
LEFT JOIN customers AS t2 ON t1.customer_id = t2.customer_id
LEFT JOIN shippers AS t3 ON t1.shipper_id = t3.shipper_id
LEFT JOIN order_statuses AS t4 ON t1.status = t4.order_status_id) as l
group by bukle;
SELECT
	t1.product_id
    ,t1.name
    ,t2.quantity
FROM products AS t1
LEFT JOIN order_items AS t2
ON t1.product_id = t2.product_id;


SELECT *
FROM(
SELECT
	t1.product_id
    ,t1.name
    ,t2.quantity
FROM products AS t1
LEFT JOIN order_items AS t2
ON t1.product_id = t2.product_id) as l
WHERE quantity IS NULL;

SELECT 
	t1.first_name
    ,t1.last_name
    ,t2.order_id
FROM customers AS t1
INNER JOIN orders AS t2
ON t1.customer_id = t2.customer_id;

--
SELECT
	t1.*
    ,t2.note
FROM order_items AS t1
JOIN order_item_notes AS t2
ON t1.order_id = t2.order_id AND t1.product_id = t2.product_id;

-- implicit join

SELECT * 
FROM orders AS t1
JOIN customers AS t2
ON t1.customer_id = t2.customer_id;

SELECT * 
FROM orders t1, customers t2
WHERE t1.customer_id = t2.customer_id;

-- Right Join

-- kairio pvz
SELECT * FROM customers;
SELECT * FROM orders;

SELECT 
	t1.customer_id
    ,t1.first_name
    ,t2.order_id
FROM customers t1
LEFT JOIN orders t2
ON t1.customer_id = t2.customer_id;


-- desinio
SELECT 
	t1.customer_id
    ,t1.first_name
    ,t2.order_id
FROM customers t1
RIGHT JOIN orders t2
ON t1.customer_id = t2.customer_id;

-- FULL OUTER JOIN

-- SELECT 
-- 	t1. *
--     ,t2. *
-- FROM custoemr t1
-- FULL JOIN orders t2;
-- -- MYSQL nepalaiko tokio full join


SELECT
	t1.*
    ,t2.*
FROM customers t1
LEFT JOIN orders t2
ON t1.customer_id = t2.customer_id
UNION
SELECT
	t1.*
    ,t2.*
FROM customers t1
RIGHT JOIN orders t2
ON t1.customer_id = t2.customer_id;

-- USING

SELECT
	t1.order_id
    ,t2.first_name
FROM orders t1
JOIN customers t2
-- ON t1.customer_id = t2.customer_id;
USING(customer_id); -- ON analogas

-- NATURAL JOINS - pats SQL nusprendzia kaip sujungti

SELECT
	t1.order_id
    ,t2.first_name
FROM orders t1
NATURAL JOIN customers t2;

SELECT 
	t1.name
FROM shippers t1
NATURAL JOIN products t2;

SELECT
	t1.first_name
    ,t2.name
FROM customers t1
CROSS JOIN products t2;

SELECT
	t1.*
    ,t2.note
FROM order_items AS t1
JOIN order_item_notes AS t2
ON t1.order_id = t2.order_id AND t1.product_id = t2.product_id;

SELECT
	t1.employee_id
    ,t1.first_name
    ,t2.first_name AS vadovo_vardas
FROM  employees t1
LEFT JOIN  employees t2
ON t1.reports_to = t2.employee_id;

DESCRIBE customers;

DESCRIBE orders;

-- metodai, skirti dirbti su tekstu
-- SUBSTRING

SELECT
	first_name
    ,SUBSTRING(first_name, 1,5) AS teksto_iskarpa
FROM customer;

SELECT
	payment_date
    ,SUBSTRING(payment_date, 6,2) AS menuo
FROM payment;

-- DESCRIBE payment;


-- TRIM

SELECT TRIM(LEADING 'S' FROM 'SSSSSSSSSSSSSSSABASSSS');

SELECT TRIM(TRAILING 'S' FROM 'SSSSSSSSSSSSSSSABASSSS');

SELECT TRIM(BOTH 'S' FROM 'SSSSSSSSSSSSSSSABASSSS');

SELECT TRIM('S' FROM 'SSSSSSSSSSSSSSSABSASSSS');

SELECT TRIM('       Labas       ');

-- REPLACE

SELECT REPLACE ('aBC aBC aBC',  'a', 'A') AS pakeistas_tekstas;

SELECT SUM(new_amount)
FROM 
(SELECT
	amount
    ,REPLACE(amount,  '.', ',') AS  new_amount
FROM payment) dt;

-- LENGTH

SELECT
	first_name
    ,LENGTH(first_name) AS vardo_ilgis
    ,customer_id
    ,LENGTH(customer_id) AS id_ilgis
FROM customer;


SELECT
	phone
    ,REPLACE(phone, NULL, 'NERA')
FROM customers;

-- LOCATE

SELECT
	email
    -- ,LEFT(email, 3) AS pvz
    ,RIGHT(email, 3) AS pvz
    ,LOCATE('@', email) AS email_index
FROM customer;


/* Ištraukite iš customer lentelės elektroninius pašto adresus, atskirame stulpelyje iš elektroninių
pašto adresų ištraukite vardus ir pavardes bei dar viename stulpelyje atvaizduokite internetinių
 puslapių tinklapius.*/
-- el pastas | vardas  pavarde | web (www.sakilacustomer.org)

SELECT
	email AS 'el pastas'
    ,REPLACE(TRIM('@sakilacustomer.org' FROM email), '.', ' ') AS 'vardas pavarde'
    -- ,REPLACE(LEFT(email, LOCATE('@', email) -1), '.', ' ') AS 'vardas pavarde'
    ,RIGHT(email, 19) AS web
FROM customer;

SELECT round(4.563, 2);

SELECT round(344.563, -2); -- apvalina simtaisiais

SELECT round(344.563, 0); -- apvalina iki sveiku skaiciu


-- 1.
/*
Naudoti: sql_hr.employees
		 sql_hr.offices
Pateikite `first_name`, `last_name` iš EMPLOYEES lentelės, bei miesto pavadinimą (`city`) iš
OFFICES lentelės. Išrikiuokite rezultą pagal `city` nuo atvirkštine abecėles rikiuote (Z -> A) 
ir pagal pavardę nuo abecėlės tvarka (A -> Z)
*/ 

SELECT
	t1.first_name
    ,t1.last_name
    ,t2.city
FROM employees t1
JOIN offices t2
ON t1.office_id = t2.office_id
ORDER BY city DESC, last_name;

-- 2.
/*
Naudoti: sql_hr.employees
		 sql_hr.offices
Parašykite užklausą, kuri pateiktų visus `job_title`, kurie savo pavadime turi žodį `specialistas`,
taip pat pridėkite `address` ir `city` duomenis. Surikiuokite rezultatą pagal adresą abecėlės tvarka.
*/

SELECT
	t1.job_title
    ,t2.address
    ,t2.city
FROM employees t1
JOIN offices t2
ON t1.office_id = t2.office_id
WHERE job_title LIKE '%specialistas%' 
ORDER BY address;

-- 3.
/*
Naudoti: sql_hr.employees
		 sql_hr.offices
Parašykite užklausą, kuri pateiktų `state` ir susumuotas darbuotojų algas `state` lygmenyje.
Naudokite GROUP BY apskaičiuojant agreguotą sumą. Surikiuokite rezultatą pagal agreguotas algas
 nuo didžiausios reikšmės.        
*/

SELECT
	t2.state
    ,SUM(t1.salary) 'Darbuotoju algu suma'
FROM employees t1
JOIN offices t2
ON t1.office_id = t2.office_id
GROUP BY state
ORDER BY 'Darbuotoju algu suma' DESC;


-- 4.
/*
Naudoti: sql_hr.employees
		 sql_hr.offices
Parašykite užklausą, kuri pateiktų `city`, `first_name` ir `last_name`. Pateikite tik Vilniaus miesto darbuotojus. 
Duomenis išrikiuokite pagal darbuotojo pavardę abecėlės tvarka.       
*/

SELECT
	t2.city
    ,t1.first_name
    ,t1.last_name
FROM employees t1
JOIN offices t2
ON t1.office_id = t2.office_id
WHERE city = 'Vilnius'
ORDER BY last_name;

-- 5.
/*
Naudoti: sql_invoicing.invoices
		 sql_invoicing.payment_methods
         sql_invoicing.payments
Parašykite užklausą, kuri pateiktų `invoice_id`, `invoice_total`, `invoice_date`, `payment_id`. 
Pateikite tik tuos įrašus, kurie buvo apmokėti elektronine bankininkyste.
Išrikiuokite rezultatą pagal `invoice_date` nuo seniausio.
*/

SELECT
	t1.invoice_id
    ,t1.invoice_total
    ,t1.invoice_date
    ,t2.payment_id
FROM invoices t1
JOIN payments t2
ON t1.invoice_id = t2.invoice_id
JOIN payment_methods t3
ON t3.payment_method_id = t2.payment_method
WHERE t3.name  = 'Elektroninė bankininkystė'
ORDER BY invoice_date;
    
-- 6.
/*
Naudoti: sql_invoicing.payment_methods
         sql_invoicing.payments
         sql_invoicing.clients
Parašykite užklausą, kuri pateiktų visus mokėjimus (visą informaciją iš PAYMENTS lentelės) klientui, 
kurio pavadinimas yra 'Topinis', bei pridėti mokėjimo metodo pavadinimą iš PAYMENT_METHODS lentelės.
*/

SELECT t1.*
	-- ,t2.name
	,t3.name
FROM payments t1
JOIN clients t2
ON t1.client_id = t2.client_id
JOIN payment_methods t3
ON t3.payment_method_id = t1.payment_method
WHERE t2.name = 'Topinis';

-- 7.
/*
Naudoti: sql_store.customers
         sql_store.orders
         sql_store.order_items
         sql_store.products
Parašykite užklausą, kuri pateiktų pirkėjų vardus (`first_name`), pavardes (`last_name`), užsakymo datą (`order_date`)
ir užsakymo id (`order_id`), kurie yra pirkę 'Mikorbangų krosnelę'.
*/

SELECT
	t1.first_name
    ,t1.last_name
    ,t2.order_date
    ,t3.order_id
FROM customers t1
JOIN orders t2
ON t1.customer_id = t2.customer_id
JOIN order_items t3
ON t2.order_id = t3.order_id
JOIN products t4
ON t3.product_id = t4.product_id
WHERE t4.name = 'Mikrobangų krosnelė';

-- 8. 
/*
Naudoti: sql_hr.employees
		 sql_hr.office
Parašykite užklausą, kuri pateiktų miestą (City), vidutinį, mažiausią ir didžiausią atlyginimą 
(Salary) pagal miestus.
Rezultate neturi būti įtraukti Vilniaus miesto rezultatai. Stulpelius pervadinkite atitinkamai
 'avg_salary', 'min_salary', 'max_salary'.
Taip pat paskaičiuokite skirtumą tarp didžiausio atlyginimo ir mažiausios. Pavadinkite šį 
stulpelį - diff_min_max_salary
Rezultatą išrikiuokite nuo didžiausio vidutinio atlyginimo mažėjančia tvarka.
*/

SELECT
	t2.city
    ,AVG(t1.salary) AS avg_salary
    ,MIN(t1.salary) AS min_salary
    ,MAX(t1.salary) AS max_salary
    ,MAX(t1.salary) - MIN(t1.salary) AS diff_min_max_salary
FROM employees t1
LEFT JOIN offices t2
ON t1.office_id = t2.office_id
WHERE t2.city != 'VILNIUS'
GROUP BY city
ORDER BY avg_salary DESC;
    
-- 9. 

/*
Naudoti: sql_invoicing.clients
		 sql_invoicing.invoices
Parašykite užklausą, kuri pateiktų klientų pavadinimus (name), jų bendrą užsakymų sumą (invoice_total),
sąskaitų faktūrų kiekį.
Skaičiuokite tik tų sąskaitų faktūrų sumas, kurių išrašymo datos patenka į pirmąjį 2019 metų pusmečio intervalą.
Taip pat eliminuokite tokius klientus, kurie turi 1 ir mažiau sąskaitų faktūrų per tą laikotarpį
*/

SELECT
	t1.name
    ,SUM(t2.invoice_total) AS 'bendra uzsakymu suma'
    ,COUNT(t2.invoice_total) AS  'saskaitu fakturu kiekis'
FROM clients t1
JOIN invoices t2
ON t1.client_id = t2.client_id
WHERE t2.invoice_date BETWEEN '2019-01-01' AND '2019-07-01'
GROUP BY t1.name
HAVING COUNT(t2.invoice_id) > 1;
 
-- 10. 
/*
Naudoti: sql_invoicing.clients
		 sql_invoicing.invoices
Parašykite užklausą, kuri pateiktų 3 stulpelius. Pirmąjį pavadinsim 'Agregacija' ir jis turės dvi reikšmes:
'Klientai neturintis išrašytų sąskaitų faktūrų' ir 'Klientai, kuriems buvo išrašytos sąskaitos faktūros'.
Antras stulpelį pavadinsim 'Kiekis_unikalių_klientų' ir trečia stulpelį pavadinsim 'Kiekis_išrašytų_sąskaitų_faktūrų'.
Abejose stulpeliuose paskaičiuosim tai ko prašo pirmame stulpelyje pateiktos sąlygos.
Žiūrėti į rezultatinę lentelę.
*/

SELECT
	CASE
		WHEN t2.client_id IS NULL THEN 'Klientai neturintis išrašytų sąskaitų faktūrų'
        ELSE 'Klientai, kuriems buvo išrašytos sąskaitos faktūros'
	END AS Agregacija
	,COUNT(DISTINCT t1.client_id) AS 'Kiekis_unikalių_klientų'
    ,COUNT(DISTINCT t2.invoice_id) AS 'Kiekis_išrašytų_sąskaitų_faktūrų'
FROM clients t1
RIGHT JOIN invoices t2
ON t1.client_id = t2.client_id
GROUP BY Agregacija;

SELECT
	CASE
		WHEN i.client_id IS NULL THEN 'Klientai neturintis išrašytų sąskaitų faktūrų'
		WHEN i.client_id IS NOT NULL THEN 'Klientai, kuriems buvo išrašytos sąskaitos faktūros' 
    END AS Agregacija
    ,COUNT(distinct c.client_id) AS 'Kiekis_unikalių_klientų'
    ,COUNT(distinct i.invoice_id) AS 'Kiekis_išrašytų_sąskaitų_faktūrų'
FROM invoices AS i
RIGHT JOIN clients AS c
ON i.client_id = c.client_id
GROUP BY
	CASE
		WHEN i.client_id IS NULL THEN 'Klientai neturintis išrašytų sąskaitų faktūrų'
		WHEN i.client_id IS NOT NULL THEN 'Klientai, kuriems buvo išrašytos sąskaitos faktūros'
	END;

-- 11.
/*
Šitai skirta MySQL gurmanams :D Reikės ir LEFT JOIN, ir SUBQUERY panaudojimo, ir CASE :)
Tokio atsiskaityme nebus :)

Naudoti: sql_store.customers
		 sql_store.orders
   		 sql_store.order_items
Parašykite užklausą, kuri pateiktų rezultatą, kuris yra prisegtas kaip nuotrauka Classworke. Rezultate turi būti segmentai:
a) Pirkėjas, kuris turėjęs užsakymą (order_id) ir yra palikęs komentarą (orders.comments)
b) Pirkėjas, kuris turėjęs užsakymą (order_id), bet nepalikęs komentaro (orders.comments)
c) Pikėjas, kuris neturėjęs užsakymo ir nepalikęs komentaro.
Šalia šių segmentų turėtų būti stulpelis Kiekis, kuris nurodytų kiek tokių pirkėjų yra.
Paskutiniame stulpelyje turi būti pateikta bendra užsakymų suma tų klientų, kurie patenka į 
šiuos segmentus.
Tai yra užsakymų bendra suma customer_id lygyje, o tam tikro produkto užsakymo suma yra lygi
 order_items.quantity ir order_items.unit_price sandaugai.       
*/

-- SELECT
--     CASE
--         WHEN (o.order_id > 0) AND (o.comments IS NOT NULL) THEN 'Pirkės ir palikęs komentarą'
--         WHEN (o.order_id > 0) AND (o.comments IS NULL) THEN 'Pirkės, bet nėra komentavęs'
--         ELSE 'Nėra pirkės ir nėra komentavęs'
--     END AS Pirkejo_segmentas,
--     COUNT(DISTINCT o.order_id) AS Kiekis,
--     SUM(oi.quantity * oi.unit_price) AS Bendra_uzsakymu_suma
-- FROM
--     sql_store.customers c
--     LEFT JOIN sql_store.orders o ON c.customer_id = o.customer_id
--     LEFT JOIN sql_store.order_items oi ON o.order_id = oi.order_id
-- GROUP BY
--     CASE
--         WHEN (o.order_id > 0) AND (o.comments IS NOT NULL) THEN 'Pirkės ir palikęs komentarą'
--         WHEN (o.order_id > 0) AND (o.comments IS NULL) THEN 'Pirkės, bet nėra komentavęs'
--         ELSE 'Nėra pirkės ir nėra komentavęs'
--     END;


-- sql_store.customers t1
-- sql_store.orders t2
-- sql_store.order_items t3
