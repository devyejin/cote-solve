-- 코드를 입력하세요
-- 보호시작일 > 입양일 => 잘못된 데이터
-- EXISTS 이용
SELECT 
        ANIMAL_ID 
      , NAME
FROM ANIMAL_INS A
WHERE EXISTS (SELECT 1 FROM ANIMAL_OUTS 
                WHERE ANIMAL_ID = A.ANIMAL_ID 
                  AND DATETIME < A.DATETIME)
ORDER BY A.DATETIME;
