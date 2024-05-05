-- 코드를 입력하세요
SELECT
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS	
FROM FOOD_FACTORY 
WHERE ADDRESS LIKE ('강원도%')
ORDER BY FACTORY_ID;

-- 정규식을 이용한 방법, ^ : 문자열로 시작한다는 의미
-- REGEXP_LIKE가 LIKE보다 매칭패턴은 유연하지만, 성능은 더 안좋은 경우가 많을 수 있음
 REGEXP_LIKE(ADDRESS, '^강원도')
