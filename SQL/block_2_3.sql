"45. Выберете информацию о пользователях, получивших письма (хотя бы одно) после
своего последнего посещения сайта."


SELECT users.*
FROM users 
inner JOIN messages ON users.username=messages.rlogin 
WHERE users.lasttime<messages.mtime 
GROUP by users.username