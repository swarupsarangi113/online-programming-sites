-- https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true

-- Please note we dont have a median function in MYSQL so the below solution works for Oracle

SELECT ROUND(MEDIAN(Lat_N), 4)
FROM Station;
