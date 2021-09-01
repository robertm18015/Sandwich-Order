import datetime
today=datetime.datetime.now()

def force_name(message,lower,upper):
    while True:
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            break
        else:
            print("Error.{}, please enter text only".format(message))
    return name

def get_phone_number(message):
    while True:
        try:
            phone_number = str(input(message))
            if len(phone_number) >= 9 and len (phone_number) <=12 and phone_number.isnumeric():
                break
            else:
                print("Cellphones numbers only contain numbers that are between 9 and 12 digits")
        except:
            print("Please enter a valid phone number")
    return phone_number


def breads():
    global breadtype,breadlist
    breadlist=["White", "Brown", "Italian", "Granary"]
    breadcount=0
    print ("We have the following breads")
    while breadcount < len(breadlist):
        print(breadcount," ", breadlist[breadcount])
        breadcount += 1
    breadyype = int(input("What number bread do you want"))

def meats():
    global meatcount, meatlist
    meatlist=["Chicken","Turkey","Tuna","Bacon"]
    meatcount= 0
    print("We have the following meats")
    while meatcount < 4:
        print(meatcount," ", meatlist[meatcount])
        meatcount+= 1
    meattype = int(inpuut("What number meat do you want"))

def cheeses():
    global cheesetypes, cheeselist
    cheeselist=["Swiss","Feta","Brie","Tasty"]
    cheesecount= 0
    print("We have the following cheeses")
    while cheesecount < 4:
        print(cheesecount," ", cheeselist[cheesecount])
        cheesecount+= 1
    cheesetype = int(inpuut("What number cheese do you want"))

def salads():
    global saladtype,saladlist,saladwanted
    saladlist = ["Lettuce", "Tomato", "Carrot", "Cucumber","Onions"]
    saladcount = 0
    print("We have the following salaads, you can have as many as you want")
    while saladcount < 5:
        print(saladcount," ",saladlist[saladcount])
        saladcount+=1
    print("Press ENTER when you have finished choosing your salads")
    saladwanted = " "
    saladtype = " "
    while saladtype != " ":
        saladtype = input("What number salad do you want? ")
        if saladtype != " "
            saladtype=int(saladtype)
            saladwanted = saladwanted + " " + saladlist[saladtype]

def dressings():
    global dressingstype,dressingslistdressingslist=["BBQ Sauce","Ranch Dressing", "Mayo", "No Sauce"]
    dressingscount=0
    print("We have the following dressings")
    while dressingscount <4:
        print(dressingscount, " ", dressingslist[dressingscount])
        dressingscount +=1
    dressingstype = int(input("What number dressings dp you want"))

def output_order():
    breadorder=[]

    breadorder.append(first_name)
    breadorder.append(cellphone)
    breadorder.append(breadlist[breadtype])
    breadorder.append(meatlist[meattype])
    breadorder.append(cheeselist[cheesetype])
    breadorder.append(saladwanted)
    breadorder.append(dressingslist[dressingtype])
    breadorder.append(today)
    outputFile = open("sams_order.txt", "a")
    print("*************** Order for {} - {} ***************".format(first_name,cellphone))
    outputFile.write("*************** Order for {} - {} ***************".format(first_name,cellphone))
    for order in breadorder:
        print(order)
        outputFile.write("{}\n".format(order))
    outputFile.write("*************** End of Order: {}.***************".format(today))
    print("*************** End of Order: {}. ****************".format(today))
    outputFile.close()

#main program
first_name = force_name("Please enter in your name",2,10)
cellphone = get_[hone_number("Please enter in your cellphone number")]
breads()
meats()
cheese()
salads()