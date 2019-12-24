'15. Описание сайта знакомств. Включает в себя: пользователей, анкеты
пользователей, оплату услуг пользователями, переписку пользователей. 
Описание пользователя включает в себя: 
логин, пароль, имя, пол, дата рождения, страна, город, электронная почта, время последнего посещения сайта, место в рейтинге.

Анкета пользователя включает в себя:
описание пользователя (текстом), перечень увлечений (текстом), перечень вредных привычек (выбираются из списка), тип
проживания (выбирается из списка: своя квартира, живу с родителями и т.д.), 
цели знакомства (выбираются из списка: дружба, серьезные отношения и т.д.). 

Оплата услуг включает в себя:
указание пользователя, совершившего оплату, тип оплаченной услуги (выбирается из списка), стоимость, время оплаты, 
срок действия услуги в часах (0 для единовременных услуг). 

Переписка пользователей
содержит информацию о получателе, отправителе, времени отправления письма,
тексте письма и статусе письма (новое или прочитанное).

b. У одного пользователя может быть только одна анкета.'




CREATE TABLE users(
    username VARCHAR(20),
    pswd VARCHAR(20),
    first_name VARCHAR(30),
    sex ENUM('m','f'),
    birthday DATE,
    country VARCHAR(20),
    city VARCHAR(20),
    email VARCHAR(30),
    lasttime DATETIME,
    rating INT,
    pr_id INT,
    UNIQUE (`pr_id`),
    PRIMARY KEY (username)
);

INSERT INTO `users`(`username`, `pswd`, `first_name`, `sex`, `birthday`, `country`, `city`, `email`, `lasttime`, `rating`, "pr_id") 
VALUES ('Steper','1111','Иерусалим','m','2000-06-21',"Русь","Киев","w@bk.ru",'2019-12-30 12:11:34',10, 1),
('iera','112','Иера','f','2001-02-01',"Русь","Киев","r@bk.ru",'2019-12-30 12:12:50',13, 2),
('lox','123','Вангог','m','1988-04-13',"Колумбия","Дыра","y@bk.ru",'2018-10-16 00:23:23',60, 3),
('emae','1132','Тихон','m','2004-06-01',"Русь","Магадан","v@bk.ru",'2019-10-10 03:20:06',16, 4),
('lox2','123','Вангогиня','f','1988-04-13',"Колумбия","Дыра","p@bk.ru",'2018-10-16 00:23:40',40, 5);


CREATE TABLE profiles (
    id INT,
    about TEXT,
    hobbies TEXT,
    bad  ENUM('курю', "пью", "-"),
    live ENUM('с родителями','один', "в общежитии"),
    targ ENUM('общение','серьёзные отношения', "ничего серьёзного"),
    PRIMARY KEY (id)
);

INSERT INTO `profiles`(`id`, `about`, `hobbies`, `bad`, `live`, `targ`) 
VALUES (1,"Im the best",'Love girls)))','-','один',"серьёзные отношения"),
(5,"Im the man with prekol",'Love boys','-','в общежитии',"серьёзные отношения"),
(2,"I hate men ",'Love girls)))','-','один',"ничего серьёзного"),
(3,"Im the black",'Love KFS','-','с родителями',"общение"),
(4,"Im the silver",'Love MAC','-','один',"общение");

ALTER TABLE `users` ADD FOREIGN KEY (`pr_id`) 
REFERENCES `profiles`(`id`) 
ON DELETE RESTRICT 
ON UPDATE RESTRICT;

CREATE TABLE services (
    id INT,
    plogin VARCHAR(20),
    pservice  ENUM('раскрутка', "неограниченные лайки", "всё", "невидимость"),
    price INT,
    ptime DATETIME,
    term INT,
    PRIMARY KEY (`id`)
);

INSERT INTO `services`(`plogin`, `pservice`, `price`, `ptime`, `term`) 
VALUES (1, "iera","всё", 10000,"2018-09-11 15:00:03", 12),
(2, "lox","неограниченные лайки", 2000,"2011-05-21 16:40:43", 48),
(3, 'emae', "раскрутка", 5000,"2019-04-15 16:40:43", 5),
(4, 'emae', "раскрутка", 5500,"2013-04-15 16:40:43", 5),
(5, 'Steper', "раскрутка", 3000,"2013-04-15 16:40:43", 5)
(6, "lox","неограниченные лайки", 2000,"2013-05-21 16:40:43", 48),
(7, "iera","неограниченные лайки", 2000,"2013-05-21 10:40:43", 48),
(8, "lox","неограниченные лайки", 2000,"2016-05-26 16:30:43", 48)
(9, "lox2","всё", 10000,"2013-10-02 16:30:43", 48),
(10, "lox2","невидимость", 10000,"2015-10-02 16:30:43", 48),
(11, 'Steper', "раскрутка", 3000,"2013-07-15 16:40:43", 5);

ALTER TABLE `services` ADD FOREIGN KEY (`plogin`) 
REFERENCES `lusers`(`username`) 
ON DELETE RESTRICT 
ON UPDATE RESTRICT;


CREATE TABLE messages (
    id INT,
    slogin VARCHAR(20),
    rlogin VARCHAR(20),
    mtext TEXT,
    mtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stat ENUM('прочитано', "не прочитано"),
    PRIMARY KEY (`id`)
);

INSERT INTO `messages`(`slogin`, `rlogin`, `mtext`, `mtime` `stat`) 
VALUES (1,'Steper','iera',"привет","2019-12-30 12:09:30",'прочитано'),
(2, 'iera','Steper',"привет)", "2019-12-30 12:10:30", 'прочитано'),
(3, 'Steper','iera',"Лю тя","2019-12-30 12:11:30",'прочитано'),
(4, 'iera','Steper',"я тож))","2019-12-30 12:12:30",'не прочитано'),
(5, 'lox','lox2',"хочу арбуз","2018-10-16 00:18:40", 'прочитано'),
(6, 'lox2','lox',"ты больной?","2018-10-16 00:19:40", 'прочитано'),
(7, 'lox','lox2',"да ладно тебе","2018-10-16 00:20:40", 'прочитано'),
(8, 'lox2','lox',"у меня диабет","2018-10-16 00:23:33", 'не прочитано'),
(9, 'iera','Steper',"не игнорь!!","2019-12-30 12:12:30",'не прочитано');


ALTER TABLE `messages` ADD FOREIGN KEY (`rlogin`) 
REFERENCES `users`(`username`) 
ON DELETE RESTRICT 
ON UPDATE RESTRICT;

ALTER TABLE `messages` ADD FOREIGN KEY (`slogin`) 
REFERENCES `users`(`username`) 
ON DELETE RESTRICT 
ON UPDATE RESTRICT;