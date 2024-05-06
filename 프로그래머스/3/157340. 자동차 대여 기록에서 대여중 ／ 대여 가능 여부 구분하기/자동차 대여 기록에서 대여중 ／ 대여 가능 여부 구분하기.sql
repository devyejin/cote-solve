-- 코드를 입력하세요
-- CAR_ID별로 여러 대여 기록이 존재, 가장 최근 상태로 표시 -> 서브쿼리
SELECT
    CAR_ID,
    MAX(
        CASE
            WHEN TO_DATE('2022-10-16', 'YYYY-MM-DD') BETWEEN START_DATE AND END_DATE THEN '대여중'
            ELSE '대여 가능'
        END
    ) AS AVAILABILITY  
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;