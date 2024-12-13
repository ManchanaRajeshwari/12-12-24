basic_salary=int(input("enter basic salary"))
if(basic_salary<10000):
    hra=(67*basic_salary)/100
    da=(73*basic_salary)/100
elif(10000<=basic_salary<=20000):
    hra = (69*basic_salary)/100
    da=(76*basic_salary)/100
else:
    hra = (73*basic_salary)/100
    da=(89*basic_salary)/100
gs=hra+da+basic_salary
print("The gross_salary is",gs)