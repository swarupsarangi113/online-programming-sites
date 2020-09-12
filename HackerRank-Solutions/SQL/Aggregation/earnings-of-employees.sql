-- https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true

SELECT (SALARY*MONTHS) AS EARNINGS,COUNT(NAME) FROM EMPLOYEE
GROUP BY EARNINGS
ORDER BY EARNINGS DESC LIMIT 1;
