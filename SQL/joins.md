## SQL Basic Join

We have two connected tables:

**T1**<br>
ID      serial int<br>
NAME    varchar<br>
T2_ID   int<br>

**T2**<br>
ID      serial int<br>
NAME    varchar<br>

We want to get the NAME column from both tables where T2_ID corresponds to ID from T2. And we want to use JOIN for that.

This is what the JOIN syntax looks like:

```sql {"id":"01J6SMJXA2DE0TSCEJD5YXXZTM"}
SELECT T1.NAME, T2.NAME FROM T1
JOIN T2 ON T1.T2_ID = T2.ID;
```

Let's break it down:
1. We need the column NAME from table 1 so we select NAME from T1
```sql
SELECT T1.NAME FROM T1;
```
2. We also need NAME from table 2 so we select NAME from T2
```sql
SELECT T1.NAME, T2.NAME FROM T1, T2;
```
3. But how do we tell SQL that we want the two tables to be joined and not a list of T2.NAME after the list of T1.NAME?
```sql
SELECT T1.NAME, T2.NAME FROM T1
JOIN T2 ON T1.T2_ID = T2.ID;
```

### Exercises

- Our solution for [Asian Population](https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true) challenge from HackerRank:

```sql {"id":"01J6SNYNEX23JZ1A376YP35JKX"}
SELECT SUM(CITY.POPULATION) FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia';
```

- Our solution for [African Cities](https://www.hackerrank.com/challenges/african-cities/problem) from HackerRank:

```sql {"id":"01J6SP375WGWEQ1VNEJ3V60WR4"}
SELECT CITY.NAME FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa';
```

- Our solution for [Average Population of Each Continent](https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true) form HackerRank:

```sql {"id":"01J6SP7EE0T0KR3ZV0JDM3NG4G"}
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION)) FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY CONTINENT;
```