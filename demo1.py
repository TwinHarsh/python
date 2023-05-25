'''n=1232465
count=0
sum=0
s=0
evensum=0
while(n!=0):
    d=n%10
    sum=sum+d
    if(d%2==0):
        s=s*10+d
    count=count+1
    n=n//10
print("count is=",count)
print("sum is=",sum)
print(s)
reversed_num = 0
while s!=0:
    d=s%10
    evensum=evensum+d
    reversed_num=reversed_num*10+d
    s//=10
print("even sum=",evensum)
print("even=",reversed_num)

'''
'''#login method using dictionary
data={"user":["abc","efg","hij"],
     "pass":[111,123,456]}
x=input("enter user:")
y=int(input("enter password:"))
if x in data["user"]and y in data["pass"]:
    print("login")
else:
    print("no")
    
#each user with its assigned password
data={"user1":[111],"user2":[123],"user3":[456]}
x=input("enter user:")
y=int(input("enter password:"))
if x in data and y in data[x]:
    print("login")
else:
    print("invalid user or pass")'''

'''def login(userlist,passlist):
    #print(userlist)
    #print(passlist)
    try:
        name=input("enter name")
        p=int(input("enter password"))

        for i in range(len(userlist)):
            if(name==userlist[i]and p==passlist[i]):
                return True
    except:
        print("")
    return False

user=["user1","admin"]
pass1=[12345,1111]
count=0
while True:
    if(login(user,pass1)):
        print("login") 

    else:
        print("not login")   
        count=count+1
        if(count>=3):
            break'''

