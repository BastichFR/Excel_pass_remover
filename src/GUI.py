import tkinter as tk
from tkinter import filedialog

listbox = None

def get_selected_files():
    if listbox:
        return [item for item in listbox.get(0, tk.END)]
    return []

def add_files():
    filenames = filedialog.askopenfilenames(title="Sélectionner des fichiers", filetypes=[("Fichiers Excel", "*.xlsx")])
    for filename in filenames:
        if filename not in listbox.get(0, tk.END):
            listbox.insert(tk.END, filename)

def remove_selected():
    selection = listbox.curselection()
    for index in reversed(selection):
        listbox.delete(index)

def clear_selection():
    listbox.delete(0, tk.END)


def on_closing(root):
    if tk.messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        root.quit()


def run_gui():
    global listbox
    root = tk.Tk()
    root.title("Sélection de fichiers et de dossiers")
    root.geometry("800x400")

    # Left frame
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

    button_files = tk.Button(button_frame, text="Sélectionner des fichiers", command=add_files)
    button_files.pack(side=tk.TOP, pady=5, fill=tk.X)

    button_remove = tk.Button(button_frame, text="Retirer la sélection", command=remove_selected)
    button_remove.pack(side=tk.TOP, pady=5, fill=tk.X)

    button_clear = tk.Button(button_frame, text="Vider la sélection", command=clear_selection)
    button_clear.pack(side=tk.TOP, pady=5, fill=tk.X)

    # Bottom frame
    button_bottom_frame = tk.Frame(root)
    button_bottom_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

    button_cancel = tk.Button(button_bottom_frame, text="Annuler", command=root.quit)
    button_cancel.pack(side=tk.LEFT, padx=10)

    button_extract = tk.Button(button_bottom_frame, text="Valider", command=root.quit)
    button_extract.pack(side=tk.LEFT, padx=10)

    # Right frame
    list_frame = tk.Frame(root)
    list_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Listbox pour afficher les fichiers sélectionnés
    listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Lier la scrollbar à la listbox
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()

