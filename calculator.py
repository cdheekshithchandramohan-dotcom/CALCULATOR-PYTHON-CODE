while True:
  a=input(" Enter a value for a : ")
  b=input(" Enter a value for b : ")
  if (a,b == int[a],int[b]):
    break
  else:
    print("INVALID INPUT! ENTER A PROPER VALUE")
    continue
operation=input(" Add/Sub/Mul/Div : ").lower()
if (operation=="add"):
  print(a+b)
if (operation=="sub"):
  print(a-b)
if (operation=="mul"):
  print(a*b)
if (operation=="div"):
  print(a÷b)
while True:
  if operation not in ["add","sub","mul","div"]:
    print(" INVALID INPUT! TRY AGAIN")
    continue
