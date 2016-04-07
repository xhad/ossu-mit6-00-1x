# MIT 6.00.1x
## Introduction to Computer Science with Python
---
### Week One

**Branching Programs**

Conditional
  - A test that evaluates to TRUE or FALSE
  - A block of code to evaluate if the test is TRUE
  - Optional block of code to evaluate FALSE

```Python
x = int(raw_input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with Conditional')
```

  - x%2 == 0 evaluates to True when the remainder of x divided by 2 = 0
  - == is used for comparison, since = is used for assignment
  - Indentation is important - each indented set of expressions denotes a block of instructions

```Python
if x%2 == 0:
  if x%3 == 0:
    print('Divisible by 2 and 3')
  else:
    print('Divisible by 2 and not by 3')
elif x%3 == 0:
  print('Divisible by 3 and not by 2')
```

Compound Booleans

```Python
if x < y and x < z:
  print('x is least')
elif y < z:
  print('y is least')
else :
  print('z is least')
```

Check for string

```Python
varA = 'test'
varB = 0
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print ('bigger')
elif varA == varB:
    print ('equal')
elif varA < varB:
    print ('smaller')
```

---
### Week Two

**Iteration**

  - start with a test
  - if True, execute loop body once, and go back to reeval
  - Repeat until test evals False to finish computation

  ```Python
  x = 3
  ans = 0
  itersLeft = x
  while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
  print (str(x) + '*' + str(x) + '=' + str(ans))
  ```

  This code squares the value of x by repetitive addition.
