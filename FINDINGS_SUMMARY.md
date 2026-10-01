# Business Analytics Internship – Findings Summary
Dataset: 40 respondents, 24 columns, no missing values.

## Level 1 – Beginner
- **Task 1:** 40 rows x 24 columns (8 numeric, 16 text), no nulls.
- **Task 2:** 25 Male (62.5%), 15 Female (37.5%).

## Level 2 – Intermediate
- **Task 3:** Mean age 27.8 (median 27, SD 3.56). The other numeric columns are preference *ranks* (1-7), so their mean/median/SD are given in `task3_descriptive_statistics.csv`.
- **Task 4:** Mutual Funds are the most preferred avenue, chosen by 18 of 40 (45%), then Equity 25%, Fixed Deposits 22.5%, PPF 7.5%.

## Level 3 – Advanced
- **Task 5:** Equity -> Capital Appreciation (75%). Mutual Funds -> Better Returns (60%). Bonds -> Assured Returns (65%). Fixed Deposits -> Risk Free (47.5%) and Fixed Returns (45%).
- **Task 6:** Retirement Plan 60%, Health Care 32.5%, Education 7.5%.

## Level 4 – Expert
- **Task 7:** Financial Consultants 40%, Newspapers & Magazines 35%, Television 15%, Internet 10%.
- **Task 8:** Most respondents invest for 1-3 years (18) or 3-5 years (19). Average duration is about 2.98 years, using band midpoints (0.5, 2, 4, 6 years).
- **Task 9:** 80% expect 20%-30% returns, 12.5% expect 30%-40%, 7.5% expect 10%-20%.
- **Task 10:** Age vs duration r = 0.05, age vs expected return r = -0.09, duration vs expected return r = 0.26. All are weak; with n=40 none are strong evidence of a relationship.

## Notes / assumptions
- Duration and expected return are text bands, so midpoints were used for averages and correlation.
- Preference rank columns (Mutual_Funds ... Gold) use 1 = most preferred, so lower means "more preferred".
