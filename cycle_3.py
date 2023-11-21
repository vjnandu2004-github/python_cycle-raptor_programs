def salary(basic_pay,   EMPNAME,empid):
    if basic_pay>10000:
        da=basic_pay*(0.05)
        hra=basic_pay*(0.025)
        net_sal=basic_pay+da+hra+500-(20+(basic_pay*0.08))


    elif basic_pay>30000:
        da=basic_pay*(0.075)
        hra=basic_pay*(0.05)
        net_sal=basic_pay+da+hra+2500-((basic_pay*0.08)+60)

    elif basic_pay>50000:
        da=basic_pay*(0.11)
        hra=basic_pay*(0.075)
        net_sal=basic_pay+da+hra+5000-((basic_pay*0.11)+60+(basic_pay*0.11))

    else:
        da=basic_pay*(0.25)
        hra=basic_pay*(0.11)
        net_sal=basic_pay+da+hra+7000-(80+(basic_pay*0.20)+60+(basic_pay*0.12))
    
    print("********PAY SLIP******")
    print("EMPLOYEE NAME      :",EMPNAME)
    print("EMPLOYEE ID        :",empid)
    print("EMPLOYEE BASIC PAY :",basic_pay)
    print("EMPLOYEE NET SALARY:",net_sal)




emp_name=input("enter the name of the empolyee:")
emp_id=int(input("enter the emp id            :"))
basic_pay=int(input("enter the basic pay      :"))

salary(basic_pay,emp_name,emp_id)



#payslip make it inside fn