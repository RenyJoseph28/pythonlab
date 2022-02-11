import csv 
with open(D:\reny'iris.data','rb')as csvfile:
    lines=cs.reader(csvfile)
    for row in lines:
        print','.join(row)