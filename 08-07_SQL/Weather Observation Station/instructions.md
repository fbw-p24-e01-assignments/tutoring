## Weather Observation Station

#### from HackerRank, adapted for PostgreSQL.

Within the database `wos3` you have a `location` table which is described as follows:

`location`

| Field | Type |
| --- | --- |
| id | INTEGER |
| city | VARCHAR (50) |
| country | VARCHAR (25) |

> run `\i wos3_data.sql` before attempting the tasks

### Task 1: Even ids

Query a list of `city` names from `location` for cities that have an even `id` number. Print the results in any order, but exclude duplicates from the answer.

Original exercise [here](https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true).

### Task 2: Number of distinct cities

Find the difference between the total number of `city` entries in the table and the number of distinct `city` entries in the table.

Original exercise [here](https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true).

### Task 3: Names starting with vowels

Query the list of `city` names starting with vowels (i.e., a, e, i, o, or u) and their respective `country` from `location`. Your result cannot contain duplicates.

The result should look like this:

><pre>   city  |  country
>---------+------------
> Al Fiyay | UAE
> Anadia   | Bulgaria
> Ogusu    | Japan
> Ozhet    | Kazakhstan
>(4 rows)</pre>

Original exercise [here](https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true).

### Task 4: Distinct cities starting ending with vowels

Query the list of `city` names from `location` which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

Your result should look like this:

><pre>  city  
>--------
> Anadia
> Ogusu
>(2 rows)</pre>

Original exercise [here](https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true).

### Task 5: Cities that do not start with vowels

Query the list of `city` names from `location` that do not start with vowels. Your result cannot contain duplicates.

*Hint: research `EXCEPT`*

Original exercise [here](https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true).

### Task 6: Shortest and longest names

Query the two cities in `location` with the shortest and longest `city` names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

Your result should look like this:

><pre>     city     | len 
>--------------+-----
> Bonn          |   4
> Jebel Jelloud |  13
>(2 rows)</pre>


*Hint: research `UNION`*

Original exercise [here](https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true).