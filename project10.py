import tkinter as tk

#function to exit the window by clicking on an exit button
def exit():
    window.destroy()    

#temperature conversion function with management of invalid inputs   
def fahrenheit_to_celsius():
    try:
        f= float (ent_temperature.get()) 
        if f > 200:
            lbl_result.config(text="Erreur")
            
        else:
            c=(f- 32 )*( 5 / 9 ) 
            c = round(c, 2)
            t1.config(state='normal')
            t1.delete('1.0', tk.END)
            t1.insert(tk.END,c)
            t1.config(state='disabled')
            lbl_result.config(text= "\N{DEGREE CELSIUS}")
        
    except ValueError:
        lbl_result.config(text="Erreur")
    



#window creation
window = tk.Tk()

window.geometry("330x250")
window.config(bg="#A569BD")

window.title('Temperature Converter') 
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)

#input widget to accept temperature in Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w") 

#creation of conversion and exit buttons
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}",command=fahrenheit_to_celsius)
btn_exit = tk.Button(master=window,text="Exit application",font=("Arial", 10),command=exit)



    
t1=tk.Text(window,state="disabled",width=10,height=0)
t1.grid(row=0, column=2, sticky="w") 


lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=1, padx=10), btn_convert.grid(row=0, column=1, pady=10) 

lbl_result.grid(row=0, column=3, padx= 10)

frm_entry.grid(row=0, column=0, padx=10), btn_exit.grid(row=1, column=1, pady=10) 


    
window.mainloop()   