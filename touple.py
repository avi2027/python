myGadget = 'Laptap', 'Phone','Watch', 'Airpods','Charger','Router'
print(myGadget)

find = input("Enter my gadget name : ")
if find in myGadget:
    print('exists')
else:
    print("Not exists")

# print the gadget name
print()
for iteam in myGadget:
    print(iteam)