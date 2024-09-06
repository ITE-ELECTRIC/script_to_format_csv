import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox


def convert_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        rows = list(reader)

    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerows(rows)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                ruta_input = os.path.join(root, file)
                ruta_output = os.path.join(root, f'formatted_{file}')
                convert_csv(ruta_input, ruta_output)
                print(f"Archivo convertido: {ruta_output}")
    messagebox.showinfo("Éxito", "Todos los archivos CSV han sido convertidos.")


def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        process_directory(directory)


def main():
    root = tk.Tk()
    root.title("Convertidor de CSV")

    tk.Label(root, text="Seleccione el directorio que contiene los archivos CSV").pack(pady=10)

    btn_select = tk.Button(root, text="Seleccionar Directorio", command=select_directory)
    btn_select.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
