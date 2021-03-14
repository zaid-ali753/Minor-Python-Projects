from tkinter import Tk , Button , Label , DoubleVar , Entry

window = Tk()
window.title("Feet-->Meter Conversion App")
window.configure(background="grey")
window.geometry("250x200")
window.resizable(width=False, height=False)

def convert():
    value = float(ft_entry1.get())
    meter = value * 0.3048
    ft_value2.set("%.4f" % meter)
def clear():
    ft_value1.set(" ")
    ft_value2.set(" ")

ft_label1 = Label(window,text="FEET" , bg="magenta" , fg="black" , width=13)
ft_label1.grid(column=0,row=0,padx=14,pady=14)

ft_value1= DoubleVar()
ft_entry1= Entry(window,textvariable=ft_value1,width=13)
ft_entry1.grid(column=1,row=0)
ft_entry1.delete(0,'end')

ft_label= Label(window,text="METER" , bg="green" , fg="black" , width=13)
ft_label.grid(column=0,row=1,padx=14,pady=14)

ft_value2 = DoubleVar()
ft_entry2=Entry(window,textvariable=ft_value2,width=13)
ft_entry2.grid(column=1,row=1,pady=27)
ft_entry2.delete(0,'end')

convert_btn=Button(window,text="CHANGE", bg="white",fg="red",width=13,command=convert)
convert_btn.grid(column=0,row=3,padx=14)

clear_btn=Button(window,text="CLEAR", bg="purple",fg="white",width=13,command=clear)
clear_btn.grid(column=1,row=3,padx=14)

window.mainloop()
