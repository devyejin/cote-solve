-- PRODUCT_CODE :UNIQUE, 앞2자리 카테고리
-- 상품코드 별 매출액(판매가 * 판매량) 합계
-- 상품코드, 매출액 => 상품코드 별 매출액
WITH TEMP (PRODUCT_CODE, TOTAL)
AS
(
SELECT   
      P.PRODUCT_CODE AS PRODUCT_CODE
    , S.SALES_AMOUNT * P.PRICE AS TOTAL
FROM OFFLINE_SALE S
INNER JOIN PRODUCT P ON S.PRODUCT_ID = P.PRODUCT_ID
)
SELECT
      PRODUCT_CODE
    , SUM(TOTAL) AS SALES
FROM TEMP 
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE;



-- 굳이 CTE사용하지 않고, 바로 조인에서 처리하는게 더 가독성, 성능이 좋음
SELECT   
        P.PRODUCT_CODE
      , SUM(P.PRICE * S.SALES_AMOUNT) AS SALES
FROM OFFLINE_SALE S
INNER JOIN PRODUCT P ON S.PRODUCT_ID = P.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, P.PRODUCT_CODE;
