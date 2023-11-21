def squares_bw_2_naturalno(m,n):
    plst=[]
    for i in range (m,n+1):
        sq=i**2
        plst.append(sq)
    
    return plst

m=int(input("enter lower limit:"))        
n=int(input("enter upper limit:"))        
sq_lst=squares_bw_2_naturalno(m,n)
print(sq_lst)

