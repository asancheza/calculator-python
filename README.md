# Calculator using Python

Basic calculator in Python without using eval and yacc.

## Testing

```
python calculator.py
```

## Alternative using lambda

```
python lambda.py
```

## Other possible solution

Using dictionaries you can have the following structure:

```
Ex: 3 * 4 + 1 + 3
 ["*"] = [ 3, 4 ]
 ["+"] = [ 1, 3 ]
```

Returns: 3 * 4 + 1 + 3 = 16. For order operation you should remove the last element added in the list and add in the current operator if the priority is higher.
