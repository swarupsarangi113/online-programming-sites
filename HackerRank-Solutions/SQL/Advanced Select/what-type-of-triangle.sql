-- https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true

SELECT
CASE
    WHEN A + B > C AND B + C > A AND A + C > B THEN
    CASE
        WHEN A=B AND B=C THEN "Equilateral"
        WHEN A=B OR B=C OR A = C THEN "Isosceles"
        WHEN A != B AND A != C THEN "Scalene"
    END
    ELSE "Not A Triangle"
END
FROM TRIANGLES;
