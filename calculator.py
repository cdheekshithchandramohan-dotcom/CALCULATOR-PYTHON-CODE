while True:
  try:
    a=float(input(" Enter a value for a : "))
    b=float(input(" Enter a value for b : "))
    operation=input(" Add/Sub/Mul/Div : ").lower()
    while True:
      if operation not in ["add","sub","mul","div"]:
        print(" INVALID OPERATION! TRY AGAIN")
        continue
      else:
        pass
    if (operation=="add"):
      print(a+b)
    elif (operation=="sub"):
      print(a-b)
    elif (operation=="mul"):
      print(a*b)
    elif (operation=="div"):
      if b!=0:
        print(a/b)
      else:
        print(" Cannot divide by zero")
    else:
      print(" INVALID INPUT! TRY AGAIN")
  except ValueError:
    print(" INVALID INPUT! ENTER A PROPER NUMBER")
