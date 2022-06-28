--- 29-06-2022 00:31:36
--- bd.db
/***** ERROR ******
near "NOTNULL": syntax error
 ----- 
CREATE TABLE holidays(
  id integer PRIMARY KEY,
  holiday date,
  holiname text NOTNULL UNIQUE
  );
*****/

--- 29-06-2022 00:31:41
--- bd.db
CREATE TABLE holidays(
  id integer PRIMARY KEY,
  holiday date,
  holiname text NOT NULL UNIQUE
  );

--- 29-06-2022 00:32:08
--- bd.db
/***** ERROR ******
table holidays already exists
 ----- 
CREATE TABLE holidays(
  id integer PRIMARY KEY,
  holiday date,
  holiname text NOT NULL UNIQUE
  );
*****/

--- 29-06-2022 00:33:46
--- bd.db
/***** ERROR ******
table holidays has 3 columns but 2 values were supplied
 ----- 
INSERT INTO holidays VALUES('17.06.1980', 'День Рождения Мамы');
*****/

--- 29-06-2022 00:34:05
--- bd.db
INSERT INTO holidays VALUES(1, '17.06.1980', 'День Рождения Мамы');

