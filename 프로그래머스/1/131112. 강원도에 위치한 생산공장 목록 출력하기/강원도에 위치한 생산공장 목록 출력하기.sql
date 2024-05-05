-- 코드를 입력하세요
SELECT
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS	
FROM FOOD_FACTORY 
WHERE ADDRESS LIKE ('강원도%')
ORDER BY FACTORY_ID;

-- 정규식을 이용한 방법, ^ : 문자열로 시작한다는 의미
 REGEXP_LIKE(ADDRESS, '^강원도')
