from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()
root.title("Encapsulation")
root.geometry("800x600")
root.config(bg="orange2")
label_heading=Label(root,text="Juice Center",bg="orange2",font=("Sylfaen",18,"bold","italic"))
label_heading.place(relx=0.05,rely=0.1,anchor=W)
juice=ImageTk.PhotoImage(Image.open("logo.png"))
juice_image=Label(root,image=juice,bg="orange2")
juice_image.place(relx=0.2,rely=0.4,anchor=CENTER)
apple=ImageTk.PhotoImage(Image.open("apple_img.png"))
mango=ImageTk.PhotoImage(Image.open("mango_img.png"))
orange=ImageTk.PhotoImage(Image.open("orange.png"))
fruit_image=Label(root,bg="orange2")
fruit_image.place(relx=0.75,rely=0.8,anchor=CENTER)
label_name=Label(root,text="Select Fruit",bg="orange2",font=("Redressed",15))
label_name.place(relx=0.96,rely=0.2,anchor=E)
fruit_list=["Apple","Mango","Orange"]
fruit_dropdown=ttk.Combobox(root,state="readonly",value=fruit_list,justify="right")
fruit_dropdown.place(relx=0.95,rely=0.25,anchor=E)
label_quantity=Label(root,text="Enter Quantity",bg="orange2",font=("Redressed",15))
label_quantity.place(relx=0.96,rely=0.35,anchor=E)
input_quantity=Entry(root)
input_quantity.place(relx=0.95,rely=0.4,anchor=E)
label_show_amount=Label(root,bg="orange2",font=("Redressed",12))
label_show_amount.place(relx=0.95,rely=0.7,anchor=E)
label_show_quantity=Label(root,bg="orange2",font=("Redressed",12))
label_show_quantity.place(relx=0.95,rely=0.8,anchor=E)
class Juice:
    def __init__(self,fruit_name,quantity):
        self.fruit=fruit_name
        self.quantity=int(quantity)
        self.__cost=25
    def __calculateCost(self):
        total_cost=self.quantity*self.__cost
        label_show_amount["text"]=("You have to pay : "+str(total_cost)+" USD")
        if(self.fruit=="Apple"):
            calorie=self.quantity*52
            fruit_image["image"]=apple
        elif(self.fruit=="Mango"):
            calorie=self.quantity*60
            fruit_image["image"]=mango
        elif(self.fruit=="Orange"):
            fruit_image["image"]=orange
            calorie=self.quantity*47
        label_show_quantity["text"]=("x"+str(self.quantity)+" = "+str(calorie)+" calories")
    def getCost(self):
        self.__calculateCost()
def orderJuice():
    fruit=fruit_dropdown.get()
    quantity=input_quantity.get()
    obj1=Juice(fruit,quantity)
    obj1.getCost()
btn=Button(root,text="TOTAL",command=orderJuice)
btn.place(relx=0.95,rely=0.5,anchor=E)
root.mainloop()
