def sum_avg(l):
    tot,ag=0,0
    for i in l:
        tot+=i
    ag=tot/len(l)
    print("Total -->",tot)
    print("Average -->",ag)

li=[23,43,56,74,34,100]
n=int(input("Enter range of lists: "))
for k in range(n+1):
    ele=input("Enter element")
    l1.append(ele)
sum_avg(li)