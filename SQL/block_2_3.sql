"45. Выберете информацию о пользователях, получивших письма (хотя бы одно) после
своего последнего посещения сайта."


SELECT lusers.username, lusers.pswd , lusers.first_name, lusers.sex, lusers.birthday, lusers.country, lusers.city, 
lusers.email, lusers.rating, lusers.lasttime, messages.mtime, messages.mtext
FROM lusers 
INNER JOIN messages ON lusers.username=messages.rlogin 
WHERE lusers.lasttime<messages.mtime 
