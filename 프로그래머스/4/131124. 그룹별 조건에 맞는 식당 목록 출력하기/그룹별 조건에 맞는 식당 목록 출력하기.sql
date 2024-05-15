--  리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
--  회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고, 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬

-- 리뷰수가 MAX인 회원의 ID를 찾자
-- 메인쿼리의 WHERE절에 MEMBER_ID를 넘겨주기
    SELECT  P.MEMBER_NAME, R.REVIEW_TEXT, TO_CHAR(R.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
    FROM REST_REVIEW R
    INNER JOIN MEMBER_PROFILE P ON R.MEMBER_ID = P.MEMBER_ID
    WHERE R.MEMBER_ID IN (
            SELECT MEMBER_ID
            FROM REST_REVIEW 
            GROUP BY MEMBER_ID
            HAVING COUNT(*) = (
                                SELECT MAX(COUNT(1))
                                FROM REST_REVIEW
                                GROUP BY MEMBER_ID
                                )
         )
    ORDER BY REVIEW_DATE, R.REVIEW_TEXT;