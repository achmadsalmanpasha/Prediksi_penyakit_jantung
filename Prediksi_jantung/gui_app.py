import tkinter as tk
from tkinter import messagebox
from decision_tree_model import predict_heart_disease
from fuzzy_module import fuzzy_risk_level

def predict():
    try:
        age = int(age_entry.get())
        chol = int(chol_entry.get())
        bp = int(bp_entry.get())
        hr = int(hr_entry.get())

        fuzzy_result = fuzzy_risk_level(chol, bp, hr)
        pred = predict_heart_disease(age, chol, bp, hr)

        messagebox.showinfo("Hasil", f"Fuzzy Risk: {fuzzy_result}\nPrediksi Model: {'Risiko' if pred == 1 else 'Sehat'}")
    except:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

app = tk.Tk()
app.title("Prediksi Penyakit Jantung")

tk.Label(app, text="Usia:").grid(row=0, column=0)
tk.Label(app, text="Kolesterol:").grid(row=1, column=0)
tk.Label(app, text="Tekanan Darah:").grid(row=2, column=0)
tk.Label(app, text="Detak Jantung:").grid(row=3, column=0)

age_entry = tk.Entry(app)
chol_entry = tk.Entry(app)
bp_entry = tk.Entry(app)
hr_entry = tk.Entry(app)

age_entry.grid(row=0, column=1)
chol_entry.grid(row=1, column=1)
bp_entry.grid(row=2, column=1)
hr_entry.grid(row=3, column=1)

tk.Button(app, text="Prediksi", command=predict).grid(row=4, columnspan=2)

app.mainloop()
