# Regex

Regex = REGular EXpression

### Non-comprehensive regex symbols list

| Symbol | Explanation |
| --- | --- |
| . | matches any character except new line `\n` |
| ^ | beginning of the string |
| $ | end of the string |
| * | matches 0 or more occurences of the char that comes before |
| + | matches 1 or more occurrences of the char that comes before |
| () | matches whatever expression is in parentheses |
| ? | matches 0 or 1 occurrences of char that comes before |
| | *?=* only matches if what follows the parentheses matches what's inside |
| {m,n} | matches between m and n occurrences of the character before |

### Our complicated experiment

ChatGPT told us that this expression should check for a valid password:

`^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$`

- `^`: start of the string
- `(?=.*[A-Z])`: checks for uppercase letters
- `(?=.*[a-z])`: checks for lowercase letters
- `(?=.*\d)`: checks for digits
- `(?=.*[@$!%*?&])`: checks for any special symbol
- `[A-Za-z\d@$!%*?&]{8,}`: checks for any uppercase letter, lowercase letter, digit or special symbol for a length of at least 8 characters
- `$`: end of the string

### Resources

- https://regex101.com/
- https://docs.python.org/2/library/re.html
- my notes :)