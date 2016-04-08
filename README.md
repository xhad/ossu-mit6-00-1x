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
**Lecture 4**

###Creating Functions
Capturing computation as a function
- idea is to encapsulate this computations within a scope such that can treat as primitive
  ~ use by simply calling name, and providing input
  ~ internal details hidden from users (blackbox)
- syntax
```Python
def <function name> (<formal parameters>)
  <function body>
```
  - **def** is a keyword
  - Name is any legal python name
  - Within parenthesis are zero or more formal parameters
    ~ each is a variable name to be used inside a function body

**Turing Complete**

####Anything that is computable can be done with software language

- but code lacks abstraction
- can't use same code in other places
- functions allow abstraction

```python
if x > y:
  z = x
else:
  z = y
```

- encapsulate this computation within a scope and use it as a primitive

```python
def max (x, y):
  if x > y:s
    return y
  else:
    return x
```

1. expressions for each parameters are evaluated, bound to formal parameters as the name of a function
2. control transfers to first expression in body of function
3. body expressions executed until return keyword reached ( returning value of next expression ) or run out of expressions (returning None)
4. Invocations is bound to the returned value

**Environments**

- formalism for tracking bindings of variables and values
- Assignments pair name and values in environment
- asking for value of name just looks up in current environment
- python shell is default (or global) environment
- definitions pair function name with details of function

```Python
x = 5
p = 3
for turn in range(p):
  print('iteration: ' + str(turn) + 'current result: ' + str(result))
  result = result * x
```

**Understanding Variable Binding**

- Each	function	call	creates	a	new	environment,
which	scopes	bindings	of	formal	parameters
and	values,	and	of	local	variables	(those
created	with	assignments	within	body)
- Scoping	often	called	static	or	lexical	because
scope	within	which	variable	has	value	is
defined	by	extent	of	code	boundaries
