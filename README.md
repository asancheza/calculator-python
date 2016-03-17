# calculator-python

Basic calculator in Python without using eval and yacc.

## Testing

```
python calculator.py
```

## Alternative using lambda

```
python lambda.py
```

## Grammar

```
virtualenv env
source env/bin/activate
pip install plyplus
python grammar.py
``` 

# Other possible solution

Using dictionaries you can have the following structure:

```
Ex: 3 * 4 + 1 + 3
 ["*"] = [ 3, 4 ]
 ["+"] = [ 1, 3 ]
```

This would return 3 * 4 + 1 + 3 = 16. For order operation you should remove the last element added in the list and add in the current operator if the priority is higher.
