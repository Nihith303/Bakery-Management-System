from python_sql_connector import data_entry
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta

DE = data_entry()

def calculate_price(flavor, weight):
    cake_cost = { 'Vanilla' : 300,
                  'Chocolate' : 450,
                  'Red Velvet' : 500,
                  'Strawberry' : 400}
    return cake_cost[flavor] * (weight/0.5)

def insert_pending(master, data):
    pass

def index_return(master, data):
    # print(data)
    data = (int(data[0]), data[1], int(data[2]), data[3], data[4], float(data[5]), data[6], int(data[7]), data[8], data[9])
    # print(data)
    price = calculate_price(data[4], data[5])
    if DE.insert_Orders(data, price):
        with open('orderid.txt', 'w') as f:
            orderid = data[0]
            orderid += 1
            f.write(str(orderid))
            f.close()
        # master.destroy()
        # index_Page()
        pending(data[0], price//2)
    

def index(master):
    master.destroy()
    index_Page()


def calulate(master, price, discount):
    if discount > price:
        CashIn(master, price, discount, "Discount > Price")
    else:
        CashIn(master, price, discount, price-discount)


def pending(orderid, in_pay):

    pending = tk.Tk()
    pending.title('Intital Payemnt')
    pending.config(padx=20, pady=20, highlightbackground="red", highlightcolor="red", highlightthickness=1)


    label1 = tk.Label(pending, text="Order Id : ", bg='violet', fg='white', width=20)
    label1.config(font=("Courier", "15", "bold"))
    label1.grid(row=0, column=0, padx=5, pady=5)
    entry1 = tk.Entry(pending, width=25, font=("Courier", "15"))
    entry1.grid(row=0, column=1, padx=5, pady=5)
    entry1.insert(0, orderid)

    label2 = tk.Label(pending, text="Cake Completed : ", bg='violet', fg='white', width=20)
    label2.config(font=("Courier", "15", "bold"))
    label2.grid(row=1, column=0, padx=5, pady=5)
    entry2 = tk.Entry(pending, width=25, font=("Courier", "15"))
    entry2.grid(row=1, column=1, padx=5, pady=5)
    entry2.insert(0, 'No')

    label3 = tk.Label(pending, text="Delivery Completed : ", bg='violet', fg='white', width=20)
    label3.config(font=("Courier", "15", "bold"))
    label3.grid(row=2, column=0, padx=5, pady=5)
    entry3 = tk.Entry(pending, width=25, font=("Courier", "15"))
    entry3.grid(row=2, column=1, padx=5, pady=5)
    entry3.insert(0, 'No')

    label4 = tk.Label(pending, text="Advance : ", bg='violet', fg='white', width=20)
    label4.config(font=("Courier", "15", "bold"))
    label4.grid(row=0, column=0, padx=5, pady=5)
    entry4 = tk.Entry(pending, width=25, font=("Courier", "15"))
    entry4.grid(row=0, column=1, padx=5, pady=5)
    entry4.insert(0, str(in_pay))


    submit = tk.Button(pending, text='Submit', bg='Blue', fg='Black', width=20, command=lambda: insert_pending(pending, (orderid, entry2.get(), entry3.get(), entry4.get())))
    submit.config(font=('Courier', 15, 'bold'))
    submit.grid(pady=10, row=6, column=0, columnspan=2)




def CashIn(master, price=None, discount=None, amt=None):
    master.destroy()

    cash_in = tk.Tk()
    cash_in.title('Entry the Cash In Details ')
    cash_in.config(padx=20, pady=20, highlightbackground="red", highlightcolor="red", highlightthickness=1)

    label1 = tk.Label(cash_in, text="Order Id : ", bg='violet', fg='white', width=20)
    label1.config(font=("Courier", "15", "bold"))
    label1.grid(row=0, column=0, padx=5, pady=5)
    entry1 = tk.Entry(cash_in, width=25, font=("Courier", "15"))
    entry1.grid(row=0, column=1, padx=5, pady=5)

    search = tk.Button(cash_in, text='Search', bg='Blue', fg='Black', width=20) #command=search)
    search.config(font=('Courier', 15, 'bold'))
    search.grid(pady=10, row=1, column=0, columnspan=2)

    label2 = tk.Label(cash_in, text="Price :", bg='violet', fg='white', width=20)
    label2.config(font=("Courier", "15", "bold"))
    label2.grid(row=2, column=0, padx=5, pady=5)
    entry2 = tk.Entry(cash_in, width=25, font=("Courier", "15"))
    entry2.grid(row=2, column=1, padx=5, pady=5)
    if price != None:
        entry2.insert(0, price)

    label3 = tk.Label(cash_in, text="Discount : ", bg='violet', fg='white', width=20)
    label3.config(font=("Courier", "15", "bold"))
    label3.grid(row=3, column=0, padx=5, pady=5)
    entry3 = tk.Entry(cash_in, width=25, font=("Courier", "15"))
    entry3.grid(row=3, column=1, padx=5, pady=5)
    if discount != None:
        entry3.insert(0, discount)
    
    cal = tk.Button(cash_in, text='Calulate', bg='Blue', fg='Black', width=20, command=lambda : calulate(cash_in, int(entry2.get()), int(entry3.get()))) #command=search)
    cal.config(font=('Courier', 15, 'bold'))
    cal.grid(pady=10, row=4, column=0, columnspan=2)

    label4 = tk.Label(cash_in, text="Total Amount : ", bg='violet', fg='white', width=20)
    label4.config(font=("Courier", "15", "bold"))
    label4.grid(row=5, column=0, padx=5, pady=5)
    entry4 = tk.Entry(cash_in, width=25, font=("Courier", "15"))
    entry4.grid(row=5, column=1, padx=5, pady=5)
    if amt != None:
        entry4.insert(0, amt)

    submit = tk.Button(cash_in, text='Submit', bg='Blue', fg='Black', width=20, command=lambda: index(cash_in))
    submit.config(font=('Courier', 15, 'bold'))
    submit.grid(pady=10, row=6, column=0, columnspan=2)

    cash_in.mainloop()



    

def CashOut(master):
    master.destroy()

    cash_out = tk.Tk()
    cash_out.title("Entry the Cash Out Details ")
    cash_out.config(padx=20, pady=20, highlightbackground="red", highlightcolor="red", highlightthickness=1)

    label1 = tk.Label(cash_out, text="Bought Date : ", bg='violet', fg='white', width=20)
    label1.config(font=("Courier", "15", "bold"))
    label1.grid(row=0, column=0, padx=5, pady=5)
    entry1 = tk.Entry(cash_out, width=25, font=("Courier", "15"))
    entry1.grid(row=0, column=1, padx=5, pady=5)
    Cur_day = datetime.now().date().strftime('%Y-%m-%d')
    entry1.insert(0, Cur_day)

    item_choice = ['Wheat', 'Sugar', 'Eggs', 'Milk', 'Baking Soda', 'Vanilla Essence', 'Chocolate', 'Red Velvet Essence', 'Strawberry Essence']
    label2 = tk.Label(cash_out, text="Item : ", bg='violet', fg='white', width=20)
    label2.config(font=("Courier", "15", "bold"))
    label2.grid(row=1, column=0, padx=5, pady=5)
    entry2 = ttk.Combobox(cash_out, values=item_choice, width=24, font=("Courier", "15"))
    entry2.grid(row=1, column=1, padx=5, pady=5)

    label3 = tk.Label(cash_out, text="Quantity : ", bg='violet', fg='white', width=20)
    label3.config(font=("Courier", "15", "bold"))
    label3.grid(row=2, column=0, padx=5, pady=5)
    entry3 = tk.Entry(cash_out, width=25, font=("Courier", "15"))
    entry3.grid(row=2, column=1, padx=5, pady=5)

    label4 = tk.Label(cash_out, text="Price : ", bg='violet', fg='white', width=20)
    label4.config(font=("Courier", "15", "bold"))
    label4.grid(row=3, column=0, padx=5, pady=5)
    entry4 = tk.Entry(cash_out, width=25, font=("Courier", "15"))
    entry4.grid(row=3, column=1, padx=5, pady=5)

    submit = tk.Button(cash_out, text='Submit', bg='Blue', fg='Black', width=20, command=lambda: index(cash_out))
    submit.config(font=('Courier', 15, 'bold'))
    submit.grid(pady=10, row=4, column=0, columnspan=2)
    cash_out.mainloop()



def orders(master):
    with open('orderid.txt', 'r') as f:
        orderid = int(f.read().strip())
        f.close()

    master.destroy()
    orderWindow = tk.Tk()
    orderWindow.title("Place The Order For the Cakes")
    orderWindow.config(padx=20, pady=20, highlightbackground="red", highlightcolor="red", highlightthickness=1)

    label = tk.Label(orderWindow, text="Order Id : ", bg='violet', fg='white', width=20)
    label.config(font=("Courier", "15", "bold"))
    label.grid(row=0, column=0, padx=5, pady=5)
    entry = tk.Entry(orderWindow, width=25, font=("Courier", "15"))
    entry.grid(row=0, column=1, padx=5, pady=5)
    entry.insert(0, orderid)
    
    label1 = tk.Label(orderWindow, text="Name : ", bg='violet', fg='white', width=20)
    label1.config(font=("Courier", "15", "bold"))
    label1.grid(row=1, column=0, padx=5, pady=5)
    entry1 = tk.Entry(orderWindow, width=25, font=("Courier", "15"))
    entry1.grid(row=1, column=1, padx=5, pady=5)
    entry1.focus()

    label2 = tk.Label(orderWindow, text="Phone : ", bg='violet', fg='white', width=20)
    label2.config(font=("Courier", "15", "bold"))
    label2.grid(row=2, column=0, padx=5, pady=5)
    entry2 = tk.Entry(orderWindow, width=25, font=("Courier", "15"))
    entry2.grid(row=2, column=1, padx=5, pady=5)

    label3 = tk.Label(orderWindow, text="Email : ", bg='violet', fg='white', width=20)
    label3.config(font=("Courier", "15", "bold"))
    label3.grid(row=3, column=0, padx=5, pady=5)
    entry3 = tk.Entry(orderWindow, width=25, font=("Courier", "15"))
    entry3.grid(row=3, column=1, padx=5, pady=5)
    entry3.insert(0, '@gmail.com')
    

    cake_choice = ['Vanilla', 'Chocolate', 'Red Velvet', 'Strawberry']
    label4 = tk.Label(orderWindow, text="Cakes Flavour : ", bg='violet', fg='white', width=20)
    label4.config(font=("Courier", "15", "bold"))
    label4.grid(row=4, column=0, padx=5, pady=5)
    entry4 = ttk.Combobox(orderWindow, values=cake_choice, width=24, font=("Courier", "15"))
    entry4.grid(row=4, column=1, padx=5, pady=5)

    label5 = tk.Label(orderWindow, text="Name on Cake : ", bg='violet', fg='white', width=20)
    label5.config(font=("Courier", "15", "bold"))
    label5.grid(row=5, column=0, padx=5, pady=5)
    entry5 = tk.Entry(orderWindow, width=25, font=("Courier", "15"))
    entry5.grid(row=5, column=1, padx=5, pady=5)

    label6 = tk.Label(orderWindow, text="Year on Cake : ", bg='violet', fg='white', width=20)
    label6.config(font=("Courier", "15", "bold"))
    label6.grid(row=6, column=0, padx=5, pady=5)
    entry6 = tk.Entry(orderWindow, width=25, font=("Courier", "15"))
    entry6.grid(row=6, column=1, padx=5, pady=5)

    occuation_choice = ['Birth day', 'Wedding day', 'Valentine day', 'Christmas', 'New Year']
    label7 = tk.Label(orderWindow, text="Occuation : ", bg='violet', fg='white', width=20)
    label7.config(font=("Courier", "15", "bold"))
    label7.grid(row=7, column=0, padx=5, pady=5)
    entry7 = ttk.Combobox(orderWindow, values=occuation_choice, width=24, font=("Courier", "15"))
    entry7.grid(row=7, column=1, padx=5, pady=5)

    weight_choice = ['0.5', '1', '1.5', '2', '2.5']
    label8 = tk.Label(orderWindow, text="Weight of Cake : ", bg='violet', fg='white', width=20)
    label8.config(font=("Courier", "15", "bold"))
    label8.grid(row=8, column=0, padx=5, pady=5)
    entry8 = ttk.Combobox(orderWindow, values=weight_choice, width=24, font=("Courier", "15"))
    entry8.grid(row=8, column=1, padx=5, pady=5)

    next_day = datetime.now().date() + timedelta(days=1)
    nexxt_day = next_day + timedelta(days=1)
    delivery_choice = [next_day.strftime('%Y-%m-%d'), nexxt_day.strftime('%Y-%m-%d')]
    label9 = tk.Label(orderWindow, text="Delivery date : ", bg='violet', fg='white', width=20)
    label9.config(font=("Courier", "15", "bold"))
    label9.grid(row=9, column=0, padx=5, pady=5)
    entry9 = ttk.Combobox(orderWindow, values=delivery_choice, width=24, font=("Courier", "15"))
    entry9.grid(row=9, column=1, padx=5, pady=5)
    
    submit = tk.Button(orderWindow, text='Submit', bg='Blue', fg='Black', width=20, command=lambda: index_return(orderWindow, (orderid, entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry8.get(), entry5.get(), entry6.get(), entry7.get(), entry9.get())))
    submit.config(font=('Courier', 15, 'bold'))
    submit.grid(pady=10, row=10, column=0, columnspan=2)

    orderWindow.mainloop()


def index_Page():
    mainWindow = tk.Tk()
    mainWindow.title('Bakery Managemnet System')
    mainWindow.config(padx=10, pady=10, highlightbackground="red", highlightcolor="red", highlightthickness=1)
    # Main Image of bakery
    image = Image.open("images/bakery-and-cake-shop.webp")
    image = image.resize((900, 500), Image.LANCZOS)
    bakery_img = ImageTk.PhotoImage(image)
    img = tk.Label(mainWindow, image=bakery_img)
    img.image = image
    img.grid(row=0, column=0, columnspan=3)
    # Place Order image 
    shop_image = Image.open("images/shopping_cart.jpg")
    shop_image = shop_image.resize((90, 90), Image.LANCZOS)
    shopping_img = ImageTk.PhotoImage(shop_image)
    # Cash in Image
    cash_In_image = Image.open("images/Cash in.jpg")
    cash_In_image = cash_In_image.resize((90, 90), Image.LANCZOS)
    cash_In_Img = ImageTk.PhotoImage(cash_In_image)
    # Cash Out Image
    cash_Out_image = Image.open("images/Cash out.jpeg")
    cash_Out_image = cash_Out_image.resize((90, 90), Image.LANCZOS)
    cash_Out_img = ImageTk.PhotoImage(cash_Out_image)
     
    button1 = tk.Button(mainWindow,text="Place Order", image=shopping_img, compound=tk.BOTTOM, command=lambda: orders(mainWindow))
    button1.image = shop_image
    button1.grid(row=1, column=0)


    button2 = tk.Button(mainWindow, text="Cash In", image=cash_In_Img, compound=tk.BOTTOM, command=lambda: CashIn(mainWindow))
    button2.image = cash_In_image
    button2.grid(row=1, column=1)

    button3 = tk.Button(mainWindow, text="Cash Out", image=cash_Out_img,  compound=tk.BOTTOM, command=lambda : CashOut(mainWindow))
    button3.image = cash_Out_image
    button3.grid(row=1, column=2)

    mainWindow.mainloop()

index_Page()