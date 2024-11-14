from datetime import datetime

print("Name: Dev Mehta\nRoll No: 22BCP282")

log1 = open("log1.txt","r")
log2 = open("log2.txt","r")
log3 = open("log3.txt","r")
summary = open("summary.txt","w")

result1 = log1.readlines()
result2 = log2.readlines()
result3 = log3.readlines()
valid = 0
invalid = 0 
count = 0

output = {}
avg_rates = {}

for i in result1:
    r1 = i.split()
    count +=1
    if len(r1) == 5 and len(r1[0])==10 and len(r1[1])==6:
        try:
            datetime.strptime(r1[2],"%Y-%m-%d")
            valid+=1
            if r1[0] not in output:
                output[r1[0]] = {"productcount":0,"total":0}
            output[r1[0]]["total"]+=int(r1[3])
            output[r1[0]]["productcount"]+=1
        except ValueError:
            print(r1," is an invalid entry")
            invalid+=1
        
    else:
        print(r1," is an invalid entry")
        invalid+=1
        
for i in result2:
    count +=1
    r2 = i.split()
    if len(r2) == 5 and len(r2[0])==10 and len(r2[1])==6:
        try:
            datetime.strptime(r2[2],"%Y-%m-%d")
            valid+=1
            if r2[0] not in output:
                output[r2[0]] = {"productcount":0,"total":0}
            output[r2[0]]["total"]+=int(r2[3])
            output[r2[0]]["productcount"]+=1
        except ValueError:
            print(r2," is an invalid entry")
            invalid+=1
    else:
        print(r2," is an invalid entry")
        invalid+=1

for i in result3:
    count +=1
    r3 = i.split()
    if len(r3) == 5 and len(r3[0])==10 and len(r3[1])==6:
        try:
            datetime.strptime(r3[2],"%Y-%m-%d")
            valid+=1
            if r3[0] not in output:
                output[r3[0]] = {"productcount":0,"total":0}
            output[r3[0]]["total"]+=int(r3[3])
            output[r3[0]]["productcount"]+=1
        except ValueError:
            print(r3," is an invalid entry")
            invalid+=1
    else:
        print(r3," is an invalid entry")
        invalid+=1
        
print(output)

for j in output:
    avg_ratings = output[j]['total']/output[j]['productcount']
    avg_rates[j]=avg_ratings

sorted_rates=sorted(avg_rates.items(),key = lambda s:s[1],reverse = True)
print(sorted_rates)
dictionary = dict(sorted_rates[:3])

summary.write("Total count:"+str(count)+"\nvalid entries:"+str(valid)+"\nInvalid entries:"+str(invalid)+"\n"+str(dictionary))

log1.close()
log2.close()
log3.close()
summary.close()
    
        
            
        
        
    

   
    