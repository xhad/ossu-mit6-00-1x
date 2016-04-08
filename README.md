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
###Week Two

####Lecture 3

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

####Lecture 4

**Classes of Algorithms**

  - Iterative Algorithms allow us to more complex things than simple arithmetic
  - We can repeat a sequence of steps multiple times based on some decision; leads to new classes of algorithms

  1. Guess and Check

  **Finding a cube root of an integer**
  ```Python
  x = int(raw_input('Enter an integer: '))
  ans = 0
  while ans**3 < x:
      ans = ans + 1
  if ans **3 !=x:
      print(str(x) + ' is not a perfect cube')
  else:
      print('Cube root of ' + str(x) + ' = ' + str(ans))
```
  - only works for positive integers
  - look for positive classes

  ```Python
  x = int(raw_input('Enter and integer: '))
  ans = 0
  while ans**3 < abs(x):
    ans = ans + 1
  if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
  else:
    if x < 0:
      ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
  ```
    **Loop Characteristics**

    - Need loop variable
      ~ initialized outside of Loop
      ~ Changes within Loop
      ~ Test for termination depends on variable
    - Useful to think about a **decrementing function**
      ~ Maps set of program variables into an integer
      ~ when loop is entered, value is non-negative
      ~ When value is <=0, loop terminates, and
      ~ Value is decreased every time through loop
    - Here we use abs(x) - ans**3

    **Exhaustive enumeration**

    - Guess and check methods can work on problems with a finite number of possibilities
    - Exhaustive enumeration is a good way to generate guesses in an organized manner
