"44. Выберете наиболее востребованную услугу (по количеству обращений) в 2013
году. Таких услуг может быть несколько."

select pservice 
from services 
WHERE ptime BETWEEN "2013-01-01" and "2013-12-31 23:59:59" 
GROUP by pservice 
HAVING Count(pservice)=(SELECT  COUNT(pservice) as f 
                        FROM `services` 
                        WHERE ptime 
                        BETWEEN "2013-01-01" and "2013-12-31 23:59:59" 
                        GROUP by pservice 
                        ORDER by f desc
                        LIMIT 1)