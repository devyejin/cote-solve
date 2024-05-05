-- 코드를 입력하세요
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE 1 = 1
AND EXTRACT(MONTH FROM DATE_OF_BIRTH) = '03'
AND GENDER = 'W'
AND TLNO IS NOT NULL
ORDER BY MEMBER_ID;

-- 특정 월만 추출하는거라, 좌변 가공이 불가피해 고민이었음
-- TO_CHAR의 경우 인덱스가 있는 경우 안타지만, EXTRACT( ) 의 경우 탄다고 함.
-- TO_CHAR보다는 EXTRACT 사용하기!, 대신 EXTRACT의 경우 시간단위에 대해서는 불가
