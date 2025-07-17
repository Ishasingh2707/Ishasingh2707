t=int(input("Enter total water bottels:->"))
p=int(input("Enter bottles that you drink per today:->"))
days=1
while t > 0:
    if (t>p):
        print(f"day {days}: Drank {p} Bottles. {t-p}left..")
        t-=p
    else:
        print(f"day {days}:Drank {t} Bottle{'s' if t>1 else ''}.0 left")
        t=0
    days+=1
print("no bottles left")