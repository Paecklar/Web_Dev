count=10
while(count):
    print(count)
    count -= 1
    if count<5:
        #break
        continue

    print("continue text")

print(range(4))

Bundesl=("Burgenland", "Kärnten", "Nieder")
for item in Bundesl:
#for item in range(4):
    print(item)
