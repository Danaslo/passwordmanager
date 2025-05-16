import tkinter as tk
from tkinter import messagebox
from db.database import create_account, get_accounts, update_account, delete_account

def create_window():
    window = tk.Tk()
    window.title("Gestor de cuentas")
    window.geometry("1150x980")
    window.config(bg="#6BDFAF")
    add_widgets(window)
    window.mainloop() 

def add_widgets(window):
    title = tk.Label(window, text="Gestor de contraseñas", font=("Arial", 20), bg="#6BDFAF")
    title.pack(pady=10)
 
    listbox_frame = tk.Frame(window)
    listbox_frame.pack(pady=10)

    accounts_list = tk.Listbox(listbox_frame, width=97, height=20, font=("Helvetica", 14)) 
    accounts_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=accounts_list.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    accounts_list.config(yscrollcommand=scrollbar.set)

    def load_accounts():
        accounts_list.delete(0, tk.END)
        accounts = get_accounts()
        for account in accounts:
            accounts_list.insert(tk.END, f"{account.id}: {account.whatfor}: Nombre: {account.name},  Contraseña: {account.password},  Correo: {account.email},  Comentario: {account.comment}")
            accounts_list.insert(tk.END,"")
    load_accounts()

    tk.Label(window, text="Para qué es:", bg="#6BDFAF", font=("Helvetica", 12)).pack(pady=5)
    whatfor_entry = tk.Entry(window)
    whatfor_entry.pack(pady=5)

    tk.Label(window, text="Nombre:", bg="#6BDFAF",font=("Helvetica", 12)).pack(pady=5)
    name_entry = tk.Entry(window)
    name_entry.pack(pady=5)

    tk.Label(window, text="Correo:", bg="#6BDFAF",font=("Helvetica", 12)).pack(pady=5)
    email_entry = tk.Entry(window)
    email_entry.pack(pady=5)

    tk.Label(window, text="Contraseña:", bg="#6BDFAF",font=("Helvetica", 12)).pack(pady=5)
    password_entry = tk.Entry(window)
    password_entry.pack(pady=5)

    tk.Label(window, text="Comentario", bg="#6BDFAF",font=("Helvetica", 12)).pack(pady=5)
    comment_entry = tk.Entry(window)
    comment_entry.pack(pady=5)

    def add_account():
        whatfor = whatfor_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        comment = comment_entry.get()

        if not whatfor or not name or not email or not password:
            messagebox.showerror("Error", "Por favor rellena todos los campos")
            return

        create_account(whatfor, name, email, password, comment)
        load_accounts()  
        messagebox.showinfo("Success", "Cuenta agregada con éxito")

    add_button = tk.Button(window, text="Agregar cuenta", command=add_account, font=("Helvetica", 12), bg="#c0ed70")
    add_button.pack(pady=10)

    def widget_delete_account():
        try:
            selected = accounts_list.curselection()
            selected_account = accounts_list.get(selected)
            delete_account(selected_account[0])      
            messagebox.showinfo("Success", "Cuenta borrada con éxito")
            load_accounts()
        except IndexError:
            messagebox.showerror("Error", "Selecciona una cuenta a borrar")

    delete_button = tk.Button(window, text="Borrar cuenta", command=widget_delete_account, font=("Helvetica", 12), bg="#c0ed70")
    delete_button.pack(pady=10)
