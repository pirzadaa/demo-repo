print("Hello from CLI")
weight_of_person = float(input("Enter Your Weight: "))
type_of_weight = str(input("Enter K for kg and L for Lbs: "))
if type_of_weight == "K" or "k":
    inLBS = weight_of_person * 0.453
    print("Weight of person in lbs is " + str(inLBS))
elif type_of_weight == "L" or "l":
    inKG = weight_of_person / 0.453
    print("Weight of person in kg is " + str(inKG))
else:
    print("please check what you entered, See ya Bye")