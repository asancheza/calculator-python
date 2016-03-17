# Calculator using Python

Basic calculator in Python without using eval and yacc.

## Testing
```
python calculator.py
```

## Lambda
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

## Dictionaries
>>>>>>> 1e7ef3d08518a99b21c589e9d57bb48d45d0ca6e

Using dictionaries you can have the following structure:

```
Ex: 3 * 4 + 1 + 3
 ["*"] = [ 3, 4 ]
 ["+"] = [ 1, 3 ]
```

Returns: 3 * 4 + 1 + 3 = 16. For order operation you should remove the last element added in the list and add in the current operator if the priority is higher.
