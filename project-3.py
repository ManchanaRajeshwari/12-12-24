project=int(input("Enter project score"))
internal=int(input("Enter internal_score"))
external=int(input("Enter external score"))
if(project >=50 and internal >=50 and external >=50):
  total=(70*project)/100+(10*internal)/100+(20*external)/100
  if(total>=90):
    print("A grade")
  elif(total>80):
    print("B grade")
  else:
    print("C grade")
else:
    if(project<50):
      print("Failed in project score:",project)
    if(internal< 50):
        print("Failed in internal score:",internal)
    if(external < 50):
        print("Failed in external score:",external)

