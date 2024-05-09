-- 7월의 아이스크림 주문 정보를 담은 JULY 테이블
-- SHIPMENT_ID : 아이스크림 공장 -> 아이스크림가게 출하 번호 (JULY테이블 FK, PK)
-- 7월 맛 별로 총 주문량 JOIN 상반기 맛 별 총 주문량

SELECT FLAVOR
FROM (
    SELECT FLAVOR,
           ROW_NUMBER() OVER (ORDER BY TOTAL_ORDER DESC) AS rn
    FROM (
        SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
        FROM (
            SELECT * FROM JULY
            UNION ALL
            SELECT * FROM FIRST_HALF
        ) U
        GROUP BY FLAVOR
    )
)
WHERE rn <= 3;