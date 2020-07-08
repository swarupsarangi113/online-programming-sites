SELECT CITY.NAME FROM CITY
JOIN COUNTRY
ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'Africa';

-- SELECT CITY.NAME FROM CITY
-- WHERE CITY.COUNTRYCODE IN (
--                         SELECT COUNTRY.CODE
--                         FROM COUNTRY
--                         WHERE CONTINENT = 'Africa'
--                     );
