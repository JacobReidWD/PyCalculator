import os.path
os.system("clear")
`
def add(a, b):
   return a + b # adds variables a and b.
def div(c, d):
   return c / d # divides variables c and d.
def multi(e, f):
   return e * f # multiplies variables e and f.
def sub(g, h):
   return g - h # subtracts variables g and h.

query = str(input('what would you like to do? '))
if query == 'add':
  add1 = int(input('first number: '))
  if add1 == int:
    add2 = int(input('second number: '))
    if add2 == int:
      print('answer', ":", add(add1, add2))
elif query == 'subtract':
  sub1 = int(input('first number: '))
  if sub1 == int:
    sub2 = int(input('second number: '))
    if sub2 == int:
      print('answer', ":", sub(sub1, sub2))
elif query == 'divide':
  div1 = int(input('first number: '))
  if div1 == int:
    div2 = int(input('second number: '))
    if div2 == int:
      print('answer', ":", div(div1, div2))
elif query == 'multiply':
  multi1 = int(input('first number: '))
  if multi1 == int:
    multi2 = int(input('second number: '))
    if multi2 == int:
      print('answer', ":", multi(multi1, multi2))
else:
  print('sorry, that is not a function.')

    
