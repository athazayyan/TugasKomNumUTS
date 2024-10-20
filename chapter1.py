import streamlit as st
import time
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

N = st.number_input("masukkan Maks Iterasi", min_value=1, max_value=10, value=10)
bawah = st.number_input("masukkan batas bawah", value=0.0)
atas = st.number_input("masukkan batas atas", value=0.1)
h = float((atas - bawah) / N)
i = 0
x = sp.symbols('x')
hasil = None
x_array = []
fx1_array= []
fx2_array= []
fx3_array= []
fx1_array1= []
fx2_array1 = []
fx3_array1 = []
st.write("batas bawah adalah", bawah, "dan batas atas adalah", atas, "batas maksimum iterasi adalah", N)
st.write("H", h)
input_string = st.text_input("Masukkan fungsi f(x): ")
exp = sp.sympify(input_string)

def f(xA):
    f_sympy = sp.lambdify(x, exp)
    return f_sympy(xA)

'Memulai Metode Tabel...'
latest_iteration = st.empty()
bar = st.progress(1)
for i in range(N):
    latest_iteration.text(f'Iteration {i+1}')
    x_val = bawah + (i * h)
    fx1 = f(x_val)
    fx2 = f(bawah + ((i + 1) * h))
    fx3 = fx1 * fx2
    x_array.append(x_val)
    fx1_array.append(fx1)
    fx2_array.append(fx2)
    fx3_array.append(fx3)
    fx1_array1.append(abs(fx1))
    fx2_array1.append(abs(fx2))
    fx3_array1.append(abs(fx3))
    if fx1 == 0:
        hasil = x_val
    elif fx1 * fx2 < 0:
        if abs(fx1) < abs(fx2):
            hasil = x_val
        else:
            hasil = x_val + h
    st.write("iterasi", i,"akar", x_val, "fx1 ", fx1, "fx(i+1)", fx2, "fx(i) * fx(i+1)", fx3)
    bar.progress((i + 1) / N)
    time.sleep(0.5)


if hasil is not None:
    st.write("Akar ditemukan pada x =", hasil)
else:
    st.write("Akar tidak ditemukan dalam batas iterasi yang diberikan.")

    

'...Selesai..'

x_range = [-10, 10]  
plot_formula(fx1, x_range)


# Fungsi untuk plotting rumus matematika
def plot_formula(formula, x_range):
    # Mengubah rumus menjadi fungsi python menggunakan eval
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = eval(formula)
    
    # Plotting hasilnya
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {formula}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Plot of y = {formula}")
    plt.grid(True)
    plt.legend()
    plt.show()



