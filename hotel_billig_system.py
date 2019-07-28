#================= RESTAURANT MANAGEMENT SYSTEM ===================

from tkinter import*
import random
import time;


root = Tk()  #setting root as the name of the app...
root.geometry("1200x800+0+0") #defining the size of the app..
root.title("Resturant")




# Creating 3 frames for the app
Tops = Frame(root, width = 1200, height = 80, bg = "powder blue", relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700, relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700, relief = SUNKEN)
f2.pack(side = RIGHT)


#function fot time....
localtime = time.asctime(time.localtime(time.time()))


#======================  system information   ===============

lblInfo = Label(Tops, font = ('universe',50, 'bold'), text = "Restaurant Management System", fg = "#9E9E9E", bd = 10, anchor = 'w')

#entering location for the object...
lblInfo.grid(row = 0, column = 0)

#setting up date and time...
lblInfo = Label(Tops, font = ('arial',20, 'bold'), text = localtime, fg = "steel blue", bd = 10, anchor = 'w')
lblInfo.grid(row = 1, column = 0)

#==================================  Calculator   ==========================================

#declaring variable for text_Input
text_Input = Variable()
operator = ""

#declaring function for btnClick
def btnClick (numbers):
    global operator
    operator = operator + str (numbers)
    text_Input.set(operator)


#declaring btnClear variable for calculator...
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


#declaring btnEquals....
def btnEqualsInput():
    global operator
    sumup = str (eval (operator))
    text_Input.set(sumup)
    operator = ""

# declaring Ref function
def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)



    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChicBurger = float(Chicken_Burger.get())
    CoCheese_Burger = float(Cheese_Burger.get())

    CostofFries = CoF * 300.00
    CostofDrinks = CoD * 100.00
    CostofFilet = CoFilet * 450.00
    CostofBurger = CoBurger * 250.00
    CostChicken_Burger = CoChicBurger * 300.00
    CostCheese_Burger = CoCheese_Burger * 320.00

    CostofMeal = "Ksh", str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostChicken_Burger + CostCheese_Burger))

    
    payTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostChicken_Burger + CostCheese_Burger) * 0.2)


    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostChicken_Burger + CostCheese_Burger)
    ser_charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostChicken_Burger + CostCheese_Burger) /99)

    service = "Ksh", str('%.2f' % ser_charge)

    overalCost  = "Ksh", str('%.2f' % (payTax + TotalCost +  ser_charge))

    paidTax = "Ksh", str('%.2f' % payTax)

    Cost.set(CostofMeal)
    Tax.set(paidTax)
    subTotal.set(CostofMeal)
    Total.set(overalCost)                  
                          
                          
#declaration for qExit function
def qExit():
    root.destroy()

#declaration for Reset function
def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    subTotal.set("")
    Total.set("")
    service.set("")
    Drinks.set("")
    
##Ta.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
     
        

txtDisplay = Entry(f2, font = ('arial', 20, 'bold'), textvariable = text_Input, bd = 30, insertwidth = 4,
                   bg = "cyan", justify = 'right')
txtDisplay.grid(columnspan = 4)

#adding buttons for calculator...row 1...
btn7 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "7", bg = "powder blue", command = lambda: btnClick(7)).grid(row = 2, column = 0)

btn8 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "8", bg = "powder blue", command = lambda: btnClick(8)).grid(row = 2, column = 1)


btn9 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "9", bg = "powder blue", command = lambda: btnClick(9)).grid(row = 2, column = 2)


Addition = Button (f2, padx = 16, pady = 16, bd = 8, fg = "green", font = ('arial', 20, 'bold'),
               text = "+", bg = "light green", command = lambda:btnClick("+")).grid(row = 2, column = 3)


#adding buttons for calculator...row 2...
btn4 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "4", bg = "powder blue", command = lambda: btnClick(4)).grid(row = 3, column = 0)

btn5 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "5", bg = "powder blue", command = lambda: btnClick(5)).grid(row = 3, column = 1)


btn6 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "6", bg = "powder blue", command = lambda: btnClick(6)).grid(row = 3, column = 2)


Subtraction = Button (f2, padx = 16, pady = 16, bd = 8, fg = "green", font = ('arial', 20, 'bold'),
               text = "-", bg = "light green", command = lambda:btnClick("-")).grid(row = 3, column = 3)


#adding buttons for calculator...row 3...
btn1 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "1", bg = "powder blue", command = lambda: btnClick(1)).grid(row = 4, column = 0)

btn2 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "2", bg = "powder blue", command = lambda: btnClick(2)).grid(row = 4, column = 1)


btn3 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "3", bg = "powder blue", command = lambda: btnClick(3)).grid(row = 4, column = 2)


Multiplication = Button (f2, padx = 16, pady = 16, bd = 8, fg = "green", font = ('arial', 20, 'bold'),
               text = "*", bg = "light green", command = lambda:btnClick("*")).grid(row = 4, column = 3)


#adding buttons for calculator...row 4...
btn0 = Button (f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
               text = "0", bg = "powder blue", command = lambda: btnClick(0)).grid(row = 5, column = 0)

btnClear = Button (f2, padx = 16, pady = 16, bd = 8, fg = "firebrick", font = ('arial', 20, 'bold'),
               text = "C", bg = "#FF0000", command = btnClearDisplay).grid(row = 5, column = 1)


btnEquals = Button (f2, padx = 16, pady = 16, bd = 8, fg = "peru", font = ('arial', 20, 'bold'),
               text = "=", bg = "saddlebrown", command = btnEqualsInput).grid(row = 5, column = 2)


Division = Button (f2, padx = 16, pady = 16, bd = 8, fg = "green", font = ('arial', 20, 'bold'),
               text = "/", bg = "light green", command = lambda:btnClick("/")).grid(row = 5, column = 3)

#=====================================================row 5=======================================================================


btnDot = Button(f2, padx= 16, pady= 16, bd = 8, fg = "black", font= ('arial', 20, 'bold'),
              text = ".", bg = "powder blue", command = lambda :btnClick(".")).grid(row = 6, column = 0)


#================== RESTAURANT INFO 1 START FROM HERE ====================================

#====Declaration of rand variable
rand = StringVar()

#====Declaration of Fries variable
Fries = StringVar()

#====Declaration of Burger variable
Burger = StringVar()

#====Declaration of Filet variable
Filet = StringVar()

#====Declaration of subTotal variable
subTotal = StringVar()

#====Declaration of Total variable
Total = StringVar()

#====Declaration of services variable
service = StringVar()

#====Declaration of Drinks variable
Drinks = StringVar()

#====Declaration of Drinks variable
Tax =  StringVar()

#====Declaration of Cost variable
Cost = StringVar()

#====Declaration of Chicken_Burger variable
Chicken_Burger = StringVar()

#====Declaration of Cheese_Burger variable
Cheese_Burger = StringVar()


#=============     Reference   ===========

lblReference = Label(f1, font = ('arial', 16, 'bold'), text = "Reference", bd =16, anchor = 'w')
lblReference.grid(row = 0, column = 0)

txtReference = Entry (f1, font = ('arial', 16, 'bold'), textvariable = rand, bd =10, insertwidth = 4,
                    bg = "#b6b6b4", justify = 'right')

txtReference.grid(row = 0, column = 1)

#============  Fries   ================

lblFries = Label(f1, font = ('arial', 16, 'bold'), text = "Large Fries", bd =16, anchor = 'w')
lblFries.grid(row = 1, column = 0)

txtFries = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Fries, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtFries.grid(row = 1, column = 1)

#============ Burger  =============

lblBurger = Label(f1, font = ('arial', 16, 'bold'), text = "Burger Meal", bd =16, anchor = 'w')
lblBurger.grid(row = 2, column = 0)

txtBurger = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Burger, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtBurger.grid(row = 2, column = 1)


#============   Filet  ================

lblFilet = Label(f1, font = ('arial', 16, 'bold'), text = "Filet_o_Meal", bd =16, anchor = 'w')
lblFilet.grid(row = 3, column = 0)

txtFilet = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Filet, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtFilet.grid(row = 3, column = 1)


#=============  Chicken   =========

lblChicken = Label(f1, font = ('arial', 16, 'bold'), text = "Chicken Meal", bd =16, anchor = 'w')
lblChicken.grid(row = 4, column = 0)

txtChicken = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Chicken_Burger, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtChicken.grid(row = 4, column = 1)


#===========  Cheese  ===========

lblCheese = Label(f1, font = ('arial', 16, 'bold'), text = "Cheese Meal", bd =16, anchor = 'w')
lblCheese.grid(row = 5, column = 0)

txtCheese = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Cheese_Burger, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtCheese.grid(row = 5, column = 1)


#================== RESTAURANT INFO 2 START FROM HERE ====================================

#============  Drinks   ================


lblDrinks = Label(f1, font = ('arial', 16, 'bold'), text = "Drinks", bd =16, anchor = 'w')
lblDrinks.grid(row = 0, column = 2)

txtDrinks = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Drinks, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtDrinks.grid(row = 0, column = 3 )

#============  Cost  ================

lblCost = Label(f1, font = ('arial', 16, 'bold'), text = "Cost of Meal", bd =16, anchor = 'w')
lblCost.grid(row = 1, column = 2)

txtCost = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Cost, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtCost.grid(row = 1, column = 3)

#============ service  =============

lblservice = Label(f1, font = ('arial', 16, 'bold'), text = "Burger Meal", bd =16, anchor = 'w')
lblservice.grid(row = 2, column = 2)

txtservice = Entry (f1, font = ('arial', 16, 'bold'), textvariable = service, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtservice.grid(row = 2, column = 3)


#============   StateTax  ================

lblStateTax = Label(f1, font = ('arial', 16, 'bold'), text = "Filet_o_Meal", bd =16, anchor = 'w')
lblStateTax.grid(row = 3, column = 2)

txtStateTax = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Tax, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtStateTax.grid(row = 3, column = 3)


#=============  SubTotal   =========

lblSubTotal = Label(f1, font = ('arial', 16, 'bold'), text = "Sub Total", bd =16, anchor = 'w')
lblSubTotal.grid(row = 4, column = 2)

txtSubTotal = Entry (f1, font = ('arial', 16, 'bold'), textvariable = subTotal, bd =10, insertwidth = 4,
                    bg = "#E5E4E2", justify = 'right')

txtSubTotal.grid(row = 4, column = 3)


#===========  TotalCost  ===========

lblTotalCost = Label(f1, font = ('arial', 16, 'bold'), text = "Total Cost", bd =16, anchor = 'w')
lblTotalCost.grid(row = 5, column = 2)

txtTotalCost = Entry (f1, font = ('arial', 16, 'bold'), textvariable = Total, bd =10, insertwidth = 4,
                    bg = "#b6b6b4", justify = 'right')

txtTotalCost.grid(row = 5, column = 3)



#================  End of info 2  =========================


#======== bottom button

btnTotal = Button (f1, padx = 8, pady = 8, bd = 16, fg = "#000000", font = ('arial', 16, 'bold'), width = 10,
                   text = "Total", bg = "#BBBBBB", command = Ref).grid(row = 7, column = 1)


#======== Reset

btnReset = Button (f1, padx = 8, pady = 8, bd = 16, fg = "#000000", font = ('arial', 16, 'bold'), width = 10,
                   text = "Reset", bg = "#BBBBBB", command = Reset).grid(row = 7, column = 2)



#======== botton  Exit

btnExit = Button (f1, padx = 8, pady = 8, bd = 16, fg = "#000000", font = ('arial', 16, 'bold'), width = 10,
                   text = "Exit", bg = "#BBBBBB", command = qExit).grid(row = 7, column = 3)


root.mainloop()

#================== END OF PROGRAM  ====================================
