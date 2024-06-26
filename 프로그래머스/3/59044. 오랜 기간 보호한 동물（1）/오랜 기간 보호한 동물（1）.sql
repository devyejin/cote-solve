-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회
SELECT NAME, DATETIME
FROM (
    SELECT 
          I.NAME
        , I.DATETIME
        , ROW_NUMBER() OVER(ORDER BY I.DATETIME) AS RN
    FROM ANIMAL_INS I
    WHERE NOT EXISTS(SELECT 1 FROM ANIMAL_OUTS O WHERE I.ANIMAL_ID = O.ANIMAL_ID)
    ORDER BY I.DATETIME
)
WHERE RN <= 3;
