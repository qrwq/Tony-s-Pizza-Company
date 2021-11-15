from tkinter import *
from datetime import date, timedelta
 
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
clear_button = Button(root, text="Clear", font="arial 14", bg="white", relief="solid", borderwidth=1)
order_button = Button(root, text="Order", font="arial 14", bg="white", relief="solid", borderwidth=1)
 
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