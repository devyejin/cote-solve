-- 코드를 입력하세요
SELECT
      PRODUCT_ID
    , PRODUCT_NAME
    , PRODUCT_CD
    , CATEGORY
    , PRICE
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT
                MAX(PRICE)
               FROM FOOD_PRODUCT);

--  매 레코드마다 서브쿼리가 실행되서 비효율적이지 않을까했지만, DB엔진에서 캐싱을 하기때문에 그건 아니라고 함
-- 더 나은 쿼리를 짜고싶다면 WITH절을 이용

WITH MaxPrice AS (
SELECT MAX(PRICE) AS MAX_PRICE FROM FOOD_PRODUT
)
SELECT
      PRODUCT_ID
    , PRODUCT_NAME
    , PRODUCT_CD
    , CATEGORY
    , PRICE
FROM FOOD_PRODUCT
WHERE PRICE = SELECT MAX_PRICE WHERE MaxPrice
