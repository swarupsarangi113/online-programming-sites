-- https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true

-- Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge.
-- Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
-- If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

SELECT H.HACKER_ID,H.NAME
FROM HACKERS H
INNER JOIN SUBMISSIONS S ON S.HACKER_ID = H.HACKER_ID
INNER JOIN CHALLENGES C ON C.CHALLENGE_ID = S.CHALLENGE_ID
INNER JOIN DIFFICULTY D ON D.DIFFICULTY_LEVEL = C.DIFFICULTY_LEVEL
WHERE D.SCORE = S.SCORE
GROUP BY H.HACKER_ID,H.NAME
HAVING COUNT(S.CHALLENGE_ID) > 1
ORDER BY COUNT(S.CHALLENGE_ID) DESC,H.HACKER_ID ASC;
