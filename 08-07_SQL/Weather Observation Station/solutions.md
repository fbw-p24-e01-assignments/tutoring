## Solutions for the SQL exercises

### Task 1

```sql {"id":"01J265M8T9HKE6D7HYC677TSBC"}
SELECT DISTINCT city
FROM location
WHERE id % 2 = 0;
```

### Task 2

```sql {"id":"01J265M8T9HKE6D7HYC72Y8S5D"}
SELECT COUNT(city) - COUNT(DISTINCT city) AS difference
FROM location;
```

### Task 3

Solution 1:

```sql {"id":"01J267S81DQ9NQ2R8W3B9FDV64"}
SELECT city, country FROM location
WHERE city ILIKE 'a%'
    OR city ILIKE 'e%'
    OR city ILIKE 'i%'
    OR city ILIKE 'o%'
    OR city ILIKE 'u%';
```

Solution 2:

```sql {"id":"01J269N7METJ8STF77EP34X3K0"}
SELECT city, country FROM location
WHERE city
SIMILAR TO '[AaEeIiOoUu]%';
```

### Task 4

```sql {"id":"01J26ANGQ210M9KB89TRKPN8WM"}
SELECT DISTINCT city FROM location
WHERE city
SIMILAR TO '[AaEeIiOoUu]%[aeiou]';
```

### Task 5

```sql {"id":"01J26BKR0XWBH50BNJDATM280P"}
SELECT DISTINCT city FROM location
EXCEPT
SELECT DISTINCT city FROM location
WHERE city SIMILAR TO '[AaEeIiOoUu]%';
```

### Task 6

```sql {"id":"01J265M8T9HKE6D7HYCAJJKXM5"}
SELECT city, LENGTH(city) AS len
FROM (SELECT city, LENGTH(city) AS len
FROM location
ORDER BY LENGTH(city) ASC, city ASC
LIMIT 1) AS shortest
UNION ALL
SELECT city, LENGTH(city) AS len
FROM (SELECT city, LENGTH(city) AS len
FROM location
ORDER BY LENGTH(city) DESC, city ASC
LIMIT 1) AS longest;
```