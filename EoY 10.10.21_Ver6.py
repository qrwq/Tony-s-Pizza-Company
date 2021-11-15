from tkinter import *
from datetime import date, timedelta
from tkinter import messagebox
 
#Constants
regularPizza = ["Cheese", "Vegan", "Pepperoni",  "Meat Lovers", "Margherita",  "BBQ Chicken", "Hawaiian"]
gourmetPizza = ["Ham & Cheese", "Beef & Onion", "Cheesy Garlic", "Chicken Cranberry", "Buffalo Chicken"]
regularPrice = 8.50
gourmetPrice = 13.50
deliveryCharge = 3
 
 
#Creating window
root = Tk()
root.geometry("620x650+15+10")
root.configure(bg='white')
icon = PhotoImage(file="C:\\Users\\64212\\Documents\\EoY Project\\pizza.png")
root.iconphoto(False,icon)
root.title("Tony's Pizza Company Order Form")
   
#Clear entries
def Clear():    
    Cheese.set('0')
    Vegan.set('0')  
    Pepperoni.set('0')
    MeatLovers.set('0')
    Margherita.set('0')
    BBQChicken.set('0')
    Hawaiian.set('0')
    HamCheese.set('0')
    BeefOnion.set('0')
    CheesyGarlic.set('0')
    ChickenCranberry.set('0')
    BuffaloChicken.set('0')  
    nameEntry.delete(0, "end")
    addressEntry.delete(0, "end")
    phNumberEntry.delete(0, "end")
    shipmentMethod.set("")
   
#Creates output window
def Order():
    #Creates Headings, Logo, and Icon
    new_window = Toplevel(root)
    new_window.geometry("620x650+15+10")
    new_window.configure(bg='white')
    icon = PhotoImage(file="C:\\Users\\64212\\Documents\\EoY Project\\pizza.png")
    new_window.iconphoto(False,icon)
    new_window.title("Tony's Pizza Company Processed Order")
    logo2 = PhotoImage(file="C:\\Users\\64212\\Documents\\EoY Project\\pizza_resized.png")
    logo2Place = Label(new_window, image=logo, bg='white').place(height=150,width=150,x=440,y=0)
 
    #Headings
    outputHeader = Label(new_window,text="Tony's Pizza Company", font="Georgia 18 bold", bg="white").place(x=160,y=50)
    outputHeader2 = Label(new_window,text="Processed Order", font="Georgia 18 bold", bg="white").place(x=200,y=80)
 
    #Subheadings and embellishments
    dateofOrder = Label(new_window,text="Date of Order:", font="arial 12",  bg="white").place(x=45,y=130)
    current_dt = date.today().strftime("%d/%m/%y")
    date_label = Label(new_window, text=current_dt, font="arial 12", bg='white',).place(x=150,y=130)
    name_outputLabel=Label(new_window,text="Customer Name:", font="arial 12",  bg="white").place(x=45, y=150)
    shipmentmethod_outputLabel = Label(new_window,text="Shipping Method:", font="arial 12", bg="white").place(x=45, y=172)
    customeraddress_outputLabel = Label(new_window,text="Customer Address:", font="arial 12", bg="white").place(x=45,y=194)
    phNumber_outputLabel = Label(new_window,text="Phone Number:", font="arial 12",bg="white").place(x=45,y=216)
    my_canvas = Canvas(new_window, width=565,height=1, bg='black', highlightthickness=0.5,highlightbackground='black').place(x=25,y=255)
    item = Label(new_window, text="Item", font="arial 12", bg='white').place(x=45, y=272)
    quantity = Label(new_window, text="Quantity", font="arial 12", bg='white').place(x=210, y=272)
    unitprice = Label(new_window, text="Unit Price", font="arial 12", bg="white").place(x=350,y=272)
    amount = Label(new_window, text="Amount", font="arial 12", bg="white").place(x=490,y=272)
    my_canvas = Canvas(new_window, width=565,height=1, bg='black', highlightthickness=0.5,highlightbackground='black').place(x=25,y=492)
    total = Label(new_window, text="Total Price (incl shipping)", font="arial 12", bg="white").place(x=45, y=512)
 
 
    #New order function
    def newOrder():
        Cheese.set('0')
        Vegan.set('0')  
        Pepperoni.set('0')
        MeatLovers.set('0')
        Margherita.set('0')
        BBQChicken.set('0')
        Hawaiian.set('0')
        HamCheese.set('0')
        BeefOnion.set('0')
        CheesyGarlic.set('0')
        ChickenCranberry.set('0')
        BuffaloChicken.set('0')
        nameEntry.delete(0, "end")
        addressEntry.delete(0, "end")
        phNumberEntry.delete(0, "end")
        shipmentMethod.set("")
        new_window.withdraw()
 
 
    #Creating Exit and New Order Buttons
    exitButton = Button(new_window, text="Exit", font="arial 14", bg="white", relief="solid", borderwidth=1, command=new_window.quit).place(x=105, y=572, width=200, height=40)
    new_orderButton = Button(new_window, text="New Order", font="arial 14", bg="white", relief="solid", borderwidth=1, command=newOrder).place(x=335, y=572, width=200, height=40)
 
    #Retrieves customer info and shipping method
    cusName = nameEntry.get()
    address = addressEntry.get()
    phNumber = phNumberEntry.get()
    shipmentmethodOption = shipmentMethod.get()
 
    #Checks for invalid customer name entry
    if cusName == "":
        messagebox.showerror("Error Message", "You must enter a valid name for this order.")
        new_window.withdraw()
        return
   
    #Checks for empty shipment method entry
    if shipmentmethodOption == "":
        messagebox.showerror("Error Message", "You must not leave the shipment method option empty for this order.")
        new_window.withdraw()
        return
    #Checks for invalid phNumber and address entry if customer has selected delivery as their preferred shipment method
    if shipmentmethodOption == "Delivery" and address == "":
        messagebox.showerror("Error Message", "You must enter a valid address for this order.")
        new_window.withdraw()
        return
    elif shipmentmethodOption == "Delivery" and phNumber == "":
        messagebox.showerror("Error Message", "You must enter a valid phone number for this order.")
        new_window.withdraw()
        return
    else:
        pass
 
    #Checks for pizza values that arent integers
    if Cheese.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return  
    elif Vegan.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif Pepperoni.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif MeatLovers.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif Margherita.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif BBQChicken.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif Hawaiian.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif HamCheese.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif BeefOnion.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif CheesyGarlic.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif ChickenCranberry.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    elif BuffaloChicken.get().isdigit() == FALSE:
        messagebox.showerror("Error Message", "You must only enter positive integers in the pizza entry fields.")
        new_window.withdraw()
        return
    else:
        pass
 
    #Retrieves pizza values and calculates total
    item1 = int(Cheese.get())
    item2 = int(Vegan.get())
    item3 = int(Pepperoni.get())
    item4 = int(MeatLovers.get())
    item5 = int(Margherita.get())
    item6 = int(BBQChicken.get())
    item7 = int(Hawaiian.get())
    item8 = int(HamCheese.get())
    item9 = int(BeefOnion.get())
    item10 = int(CheesyGarlic.get())
    item11 = int(ChickenCranberry.get())
    item12 = int(BuffaloChicken.get())
 
    totalcost_Pickup=(item1*regularPrice)+(item2*regularPrice)+(item3*regularPrice)+(item4*regularPrice)+(item5*regularPrice)+(item6*regularPrice)+(item7*regularPrice)+(item8*gourmetPrice)+(item9*gourmetPrice)+(item10*gourmetPrice)+(item11*gourmetPrice)+(item12*gourmetPrice)
    totalcost_Delivery = float(totalcost_Pickup) + int(deliveryCharge)
 
    #Checks for pizza values that exceed 5 or are less than 1
    totalPizzas=(item1+item2+item3+item4+item5+item6+item7+item8+item9+item10+item11+item12)
    if totalPizzas > 5:
        messagebox.showerror("Error Message", "You may only order a maximum of 5 pizzas for this order.")
        new_window.withdraw()
        return
    elif totalPizzas <= 0:
        messagebox.showerror("Error Message", "You must order a minimum of 1 pizzas for this order.")
        new_window.withdraw()
        return
    else:
        pass
 
    #Displays total cost
    if shipmentmethodOption == "Pickup":
        totalpriceAll_outputLabel = Label(new_window, text="$" + str('{:.2f}'.format(totalcost_Pickup)), font="arial 12", bg="white").place(x=490, y=512)
    else:
        totalpriceAll_outputLabel = Label(new_window, text="$" + str('{:.2f}'.format(totalcost_Delivery)), font="arial 12", bg="white").place(x=490, y=512)
 
    #Adding pizza entries and unit prices to list
    order=[]
    orderPrices=[]
    if item1 !=0:
        order.append(regularPizza[0])
        orderPrices.append(regularPrice)    
    if item2 !=0:
        order.append(regularPizza[1])
        orderPrices.append(regularPrice)
    if item3 !=0:
        order.append(regularPizza[2])
        orderPrices.append(regularPrice)
    if item4 !=0:
        order.append(regularPizza[3])  
        orderPrices.append(regularPrice)
    if item5 !=0:
        order.append(regularPizza[4])
        orderPrices.append(regularPrice)
    if item6 !=0:
        order.append(regularPizza[5])
        orderPrices.append(regularPrice)
    if item7 !=0:
        order.append(regularPizza[6])
        orderPrices.append(regularPrice)
    if item8 !=0:
        order.append(gourmetPizza[0])
        orderPrices.append(gourmetPrice)
    if item9 !=0:
        order.append(gourmetPizza[1])
        orderPrices.append(gourmetPrice)
    if item10 !=0:
        order.append(gourmetPizza[2])
        orderPrices.append(gourmetPrice)
    if item11 !=0:
        order.append(gourmetPizza[3])
        orderPrices.append(gourmetPrice)
    if item12 !=0:
        order.append(gourmetPizza[4])
        orderPrices.append(gourmetPrice)
    else:
        pass
 
    #Creating pizza output labels
    if len(order) >=1:
        pizza_outputLabel=Label(new_window, text=order[0], font="arial 12", bg="white").place(x=45, y=305)
    if len(order) >=2:
        pizza_outputLabel2=Label(new_window, text=order[1], font="arial 12", bg="white").place(x=45, y=345)
    if len(order) >=3:
        pizza_outputLabel3=Label(new_window, text=order[2], font="arial 12", bg="white").place(x=45, y=385)
    if len(order) >=4:
        pizza_outputLabel4=Label(new_window, text=order[3], font="arial 12", bg="white").place(x=45, y=425)
    if len(order) >=5:
        pizza_outputLabel5=Label(new_window, text=order[4], font="arial 12", bg="white").place(x=45, y=465)
    else:
        pass
 
    #Creating unit price labels
    if len(orderPrices) >=1:
        pizza_priceLabel=Label(new_window, text=(orderPrices[0]), font="arial 12", bg="white").place(x=350, y=305)
    if len(orderPrices) >=2:
        pizza_priceLabel2=Label(new_window, text=(orderPrices[1]), font="arial 12", bg="white").place(x=350, y=345)
    if len(orderPrices) >=3:
        pizza_priceLabel3=Label(new_window, text=(orderPrices[2]), font="arial 12", bg="white").place(x=350, y=385)
    if len(orderPrices) >=4:
        pizza_priceLabel4=Label(new_window, text=(orderPrices[3]), font="arial 12", bg="white").place(x=350, y=425)
    if len(orderPrices) >=5:
        pizza_priceLabel5=Label(new_window, text=(orderPrices[4]), font="arial 12", bg="white").place(x=350, y=465)
    else:
        pass
 
    #Adding quantity of pizza to list
    quantity=[]
    if item1 != 0:
        quantity.append(item1)
    if item2 != 0:
        quantity.append(item2)
    if item3 != 0:
        quantity.append(item3)
    if item4 != 0:
        quantity.append(item4)
    if item5 != 0:
        quantity.append(item5)
    if item6 != 0:
        quantity.append(item6)
    if item7 != 0:
        quantity.append(item7)
    if item8 != 0:
        quantity.append(item8)
    if item9 != 0:
        quantity.append(item9)
    if item10 != 0:
        quantity.append(item10)
    if item11 != 0:
        quantity.append(item11)
    if item12 != 0:
        quantity.append(item12)
    else:
        pass
 
    #Creating quantity labels
    if len(quantity) >=1:
        pizza_quantityLabel=Label(new_window, text=quantity[0], font="arial 12", bg="white").place(x=210, y=305)
    if len(quantity) >=2:
        pizza_quantityLabel=Label(new_window, text=quantity[1], font="arial 12", bg="white").place(x=210, y=345)
    if len(quantity) >=3:
        pizza_quantityLabel=Label(new_window, text=quantity[2], font="arial 12", bg="white").place(x=210, y=385)
    if len(quantity) >=4:
        pizza_quantityLabel=Label(new_window, text=quantity[3], font="arial 12", bg="white").place(x=210, y=425)
    if len(quantity) >=5:
        pizza_quantityLabel=Label(new_window, text=quantity[4], font="arial 12", bg="white").place(x=210, y=465)
    else:
        pass
 
    #Calculating price amount for each selection of pizza
    if len(order) >=1:
        amount1 = orderPrices[0] * quantity[0]
    if len(order) >=2:
        amount2 = orderPrices[1] * quantity[1]
    if len(order) >=3:
        amount3 = orderPrices[2] * quantity[2]
    if len(order) >=4:
        amount4 = orderPrices[3] * quantity[3]
    if len(order) >=5:
        amount5 = orderPrices[4] * quantity[4]
    else:
        pass
 
    #Creating amount labels
    if len(order) >=1:
        pizza_amountLabel = Label(new_window, text=(amount1), font="arial 12", bg="white").place(x=490, y=305)
    if len(order) >=2:
        pizza_amountLabel2 = Label(new_window, text=(amount2), font="arial 12", bg="white").place(x=490, y=345)
    if len(order) >=3:
        pizza_amountLabel3 = Label(new_window, text=(amount3), font="arial 12", bg="white").place(x=490, y=385)
    if len(order) >=4:
        pizza_amountLabel4 = Label(new_window, text=(amount4), font="arial 12", bg="white").place(x=490, y=425)
    if len(order) >=5:
        pizza_amountLabel5 = Label(new_window, text=(amount5), font="arial 12", bg="white").place(x=490, y=465)
   
    #Displays cusName, address, and ph Number
    cusName_output = Label(new_window, text=cusName, font="arial 12", bg="white").place(x=167, y=150)
    address_output = Label(new_window, text=address, font="arial 12", bg="white").place(x=185, y=192)
    phNumber_output = Label(new_window, text=phNumber, font="arial 12", bg="white").place(x=157, y=216)
    shipmentMethod_output = Label(new_window, text=shipmentmethodOption, font="arial 12", bg="white").place(x=170, y=172)
 
#Open Image
logo = PhotoImage(file="C:\\Users\\64212\\Documents\\EoY Project\\pizza_resized.png")
logoPlace = Label(root, image=logo, bg='white').place(height=150,width=150,x=0,y=0)
 
#Pizza Menu Labels
header_label = Label(root,text="Tony's Pizza Company", font="Georgia 18 bold",bg='white')
header2_label = Label(root,text="Order Form", font="Georgia 18 bold",bg='white')
pizza_menu_label = Label(root, text="Pizza Menu", font="arial 14", bg="white")
quantity_label = Label(root, text="Quantity", font="arial 12", bg="white")
quantity_label2 = Label(root, text="Quantity", font="arial 12", bg="white")
max5_label = Label(root, text="(Max 5)", font="arial 12", bg="white")
max5_label2 = Label(root, text="(Max 5)", font="arial 12", bg="white")
 
#Pizza Labels
pizza_label1 = Label(root, text="1."+ regularPizza[0], font="arial 12", bg="white")
pizza_label2 = Label(root, text="2."+ regularPizza[1], font="arial 12", bg="white")
pizza_label3 = Label(root, text="3."+ regularPizza[2], font="arial 12", bg="white")
pizza_label4 = Label(root, text="4."+ regularPizza[3], font="arial 12", bg="white")
pizza_label5 = Label(root, text="5."+ regularPizza[4], font="arial 12", bg="white")
pizza_label6 = Label(root, text="6."+ regularPizza[5], font="arial 12", bg="white")
pizza_label7 = Label(root, text="7."+ regularPizza[6], font="arial 12", bg="white")
pizza_label8 = Label(root, text="8."+ gourmetPizza[0], font="arial 12", bg="white")
pizza_label9 = Label(root, text="9."+ gourmetPizza[1], font="arial 12", bg="white")
pizza_label10 = Label(root, text="10."+ gourmetPizza[2], font="arial 12", bg="white")
pizza_label11 = Label(root, text="11."+ gourmetPizza[3], font="arial 12", bg="white")
pizza_label12 = Label(root, text="12."+ gourmetPizza[4], font="arial 12", bg="white")
 
#Creating text variables for entry boxes
Cheese = StringVar()
Vegan = StringVar()
Pepperoni = StringVar()
MeatLovers = StringVar()
Margherita = StringVar()
BBQChicken = StringVar()
Hawaiian = StringVar()
HamCheese = StringVar()
BeefOnion = StringVar()
CheesyGarlic = StringVar()
ChickenCranberry = StringVar()
BuffaloChicken = StringVar()
 
#Creating entries
pizza_label1_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=Cheese)
pizza_label2_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=Vegan)
pizza_label3_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=Pepperoni)
pizza_label4_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=MeatLovers)
pizza_label5_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=Margherita)
pizza_label6_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=BBQChicken)
pizza_label7_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=Hawaiian)
pizza_label8_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=HamCheese)
pizza_label9_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=BeefOnion)
pizza_label10_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=CheesyGarlic)
pizza_label11_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=ChickenCranberry)
pizza_label12_entry = Entry(root, relief="solid", highlightthickness=1, textvariable=BuffaloChicken)
 
#Sets entry boxes to 0 on click
def handle_click(event):
    Cheese.set('0')
    return None
 
pizza_label1_entry.bind("<1>", handle_click)
 
def handle_click2(event):
    Vegan.set('0')
    return None
 
pizza_label2_entry.bind("<1>", handle_click2)
 
def handle_click3(event):
    Pepperoni.set('0')
    return None
 
pizza_label3_entry.bind("<1>", handle_click3)
 
def handle_click4(event):
    MeatLovers.set('0')
    return None
 
pizza_label4_entry.bind("<1>", handle_click4)
 
def handle_click5(event):
    Margherita.set('0')
    return None
 
pizza_label5_entry.bind("<1>", handle_click5)
 
def handle_click6(event):
    BBQChicken.set('0')
    return None
 
pizza_label6_entry.bind("<1>", handle_click6)
 
def handle_click7(event):
    Hawaiian.set('0')
    return None
 
pizza_label7_entry.bind("<1>", handle_click7)
 
def handle_click8(event):
    HamCheese.set('0')
    return None
 
pizza_label8_entry.bind("<1>", handle_click8)
 
def handle_click9(event):
    BeefOnion.set('0')
    return None
 
pizza_label9_entry.bind("<1>", handle_click9)
 
def handle_click10(event):
    CheesyGarlic.set('0')
    return None
 
pizza_label10_entry.bind("<1>", handle_click10)
 
def handle_click11(event):
    ChickenCranberry.set('0')
    return None
 
pizza_label12_entry.bind("<1>", handle_click11)
 
def handle_click12(event):
    BuffaloChicken.set('0')
    return None
 
pizza_label12_entry.bind("<1>", handle_click12)
 
#Setting entries to 0
Cheese.set('0')
Vegan.set('0')
Pepperoni.set('0')
MeatLovers.set('0')
Margherita.set('0')
BBQChicken.set('0')
Hawaiian.set('0')
HamCheese.set('0')
BeefOnion.set('0')
CheesyGarlic.set('0')
ChickenCranberry.set('0')
BuffaloChicken.set('0')
 
 
#Creating Customer Information Labels
customerInfo_label = Label(root, text="Customer Information", font="arial 14", bg="white")
name_label = Label(root, text="Name:", font="arial 12", bg="white")
address_label = Label(root, text="Address:", font="arial 12", bg="white")
phNumber_label = Label(root, text="Phone Number:", font="arial 12", bg="white")
 
#Creating Customer Information entries
nameEntry = Entry(root, relief="solid")
addressEntry = Entry(root, relief="solid")
phNumberEntry = Entry(root, relief="solid")
 
#Creating Shipping Method Label and Clear and Order Buttons
shippingmethod_label = Label(root, text="Shipping Method", font="arial 14", bg="white")
clear_button = Button(root, text="Clear", font="arial 14", bg="white", relief="solid", borderwidth=1, command=Clear)
order_button = Button(root, text="Order", font="arial 14", bg="white", relief="solid", borderwidth=1, command=Order)
 
#Creating dropdown menu for shipment method
shipmentMethod = StringVar()
drop = OptionMenu(root, shipmentMethod, "Pickup", "Delivery")
drop.config(bg="white",highlightbackground="#231F20", highlightthickness=1)
 
#Placing Header Label and Pizza Menu Labels
header_label.place(x=190,y=50)
header2_label.place(x=240,y=80)
pizza_menu_label.place(x=20, y=145)
quantity_label.place(x=200, y=145)
max5_label.place(x=200,y=167)
quantity_label2.place(x=520, y=145)
max5_label2.place(x=520,y=167)
 
#Placing Pizza Labels
pizza_label1.place(x=15, y=195)
pizza_label2.place(x=15, y=225)
pizza_label3.place(x=15, y=255)
pizza_label4.place(x=15, y=285)
pizza_label5.place(x=15, y=315)
pizza_label6.place(x=15, y=345)
pizza_label7.place(x=15, y=375)
pizza_label8.place(x=315, y=195)
pizza_label9.place(x=315, y=225)
pizza_label10.place(x=315, y=255)
pizza_label11.place(x=315, y=285)
pizza_label12.place(x=315, y=315)
 
#Placing entries
pizza_label1_entry.place(x=213,y=195,width=37,height=25)
pizza_label2_entry.place(x=213,y=225,width=37,height=25)
pizza_label3_entry.place(x=213,y=255,width=37,height=25)
pizza_label4_entry.place(x=213,y=285,width=37,height=25)
pizza_label5_entry.place(x=213,y=315,width=37,height=25)
pizza_label6_entry.place(x=213,y=345,width=37,height=25)
pizza_label7_entry.place(x=213,y=375,width=37,height=25)
pizza_label8_entry.place(x=533,y=195,width=37,height=25)
pizza_label9_entry.place(x=533,y=225,width=37,height=25)
pizza_label10_entry.place(x=533,y=255,width=37,height=25)
pizza_label11_entry.place(x=533,y=285,width=37,height=25)
pizza_label12_entry.place(x=533,y=315,width=37,height=25)
 
#Placing Customer Information Labels
customerInfo_label.place(x=20,y=425)
name_label.place(x=20,y=455)
address_label.place(x=20,y=505)
phNumber_label.place(x=20,y=555)
 
#Placing Customer Information entries
nameEntry.place(x=20,y=480,width=250, height=25)
addressEntry.place(x=20,y=530,width=250, height=25)
phNumberEntry.place(x=20,y=580,width=250, height=25)
 
#Placing Shipping Method Label and Clear and Order Buttons
shippingmethod_label.place(x=315, y=425)
clear_button.place(x=315, y=520, width=120)
order_button.place(x=477, y=520, width=120)
 
#Placing dropdown menu
drop.place(x=315,y=480, width=285, height=30)
 
root.mainloop()