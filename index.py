def st(t,a,b):
    st=[]
    for i in range (a,b) :
        st.append(t[i])
    return st
t=[]
while True :
    for i in range (1,11) :
        print("Type the number N",i," :")
        n=int(input())
        t.append(n)
    a=int(input("type the first index :"))
    b=int(input("type the second index :"))
    print(st(t,a,b))
    m=input("Do you want to enter a new list ?(yes/no) :")
    if m == "no" :
        break