# (Postgre)SQL

### Combining Queries

- `UNION [ALL]` appends the result of *query2* to the result of *query1* (although there is no guarantee that this is the order in which the rows are actually returned), `ALL` includes the duplicates
- `INTERSECT [ALL]` returns all rows that are both in the result of *query1* and in the result of *query2*, `ALL` includes the duplicates
- `EXCEPT [ALL]` returns all rows that are in the result of *query1* but not in the result of *query2*, `ALL` includes the duplicates
Set operations can be combined.

### `SIMILAR TO`

The `SIMILAR TO` operator returns true or false depending on whether ist regex pattern matches the given string.

In addition to the symbols borrowed from `LIKE` (`_` and `%`), `SIMILAR TO` supports these pattern-matching metacharacters borrowed from regex:

- `|` either of two alternatives
- `*` zero or more repetitions
- `+` one or more repetitions
- `?` zero or one repetition
- `{m}` exactly *m* repetitions
- `{m,}`  *m* or more repetitions
- `{m,n}` at least *m* and not more than *n* repetitions
- parentheses `()` can be used to group items into a single logical item
- `[...]` either of the characters in the brackets

### Resources

- [Combining Queries](https://www.postgresql.org/docs/current/queries-union.html) from PostgreSQL documentation
- [SIMILAR TO regex](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-SIMILARTO-REGEXP) from PostgreSQL documentation