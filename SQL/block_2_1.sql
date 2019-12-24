"43. Выберете всех пользователей, оплативших различные услуги в 2013 году более
чем на 5000 рублей."

SELECT plogin, sum(price) as sprice FROM `services` 
WHERE ptime BETWEEN '2013-01-01' and '2013-12-31 23:59:59' 
GROUP BY plogin 
HAVING SUM(price) > 5000