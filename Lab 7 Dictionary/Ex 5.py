m={'apple':5,'vinegar':90,'bread':70,'toothpaste':120}
b={'vinegar':2,'toothpaste':1,'apple':20,'bread':3}
print(m.items())

bill=0
for i in m.items():
    for j in b.items():
        if i[0]==j[0]:
            bill+=i[1]*j[1]

print("Payable amount",bill)