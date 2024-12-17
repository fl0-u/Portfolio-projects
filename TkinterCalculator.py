#Very fun figuring it out

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        #aqui puedes ajustar el tamano y los botones se ajustan automaticamente solo borra los # que empiezan
        #master.geometry("300x400")  # Adjust width and height as needed
        #for i in range(5):  # 5 filas (1 para la entrada y 4 para botones)
          #  master.rowconfigure(i, weight=1)
        #for j in range(4):  # 4 columnas
         #   master.columnconfigure(j, weight=1)

        # Crea la pantalla en la calculadora
        self.display = tk.Entry(master, width=25, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Recive y ejecuta presiones de boton
        master.bind("<Key>", self.handle_key_press)
        master.bind("<Return>", lambda event: self.button_click('='))
        master.bind("<BackSpace>", lambda event: self.button_click('Borrar'))
        master.bind("<Escape>", lambda event: self.button_click('C'))

        # Botones
        button_list = [
            'C', 'Borrar', '', '',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(master, text=button_text, width=5, height=2,
                               command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'C':
            self.display.delete(0, tk.END)
        elif text == 'Borrar':
            current_text = self.display.get()
            # Ultimo texto se borra
            self.display.delete(len(current_text)-1, tk.END)
        else:
            self.display.insert(tk.END, text)

    def handle_key_press(self, event):
        # Permmite los valores de las teclas
        valid_keys = "0123456789+-*/.()"
        if event.char in valid_keys:
            self.display.insert(tk.END, event.char)

# En vez the root se puede usar winodw, main etc.
root = tk.Tk()
calculator = Calculator(root)

root.mainloop()
