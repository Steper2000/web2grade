"44. Выберете наиболее востребованную услугу (по количеству обращений) в 2013
году. Таких услуг может быть несколько."

select pservice 
from services 
WHERE ptime BETWEEN "2013-01-01" and "2013-12-31" 
GROUP by pservice 
HAVING Count(pservice)=(SELECT COUNT(pservice) 
                        FROM `services`
                        WHERE ptime BETWEEN "2013-01-01" and "2013-12-31" 
                        GROUP by pservice 
                        ORDER by pservice 
                        LIMIT 1)