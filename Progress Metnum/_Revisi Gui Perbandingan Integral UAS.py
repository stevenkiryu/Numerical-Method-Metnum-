#!/usr/bin/env python
# coding: utf-8



import tkinter as tk
import numpy as np
import scipy.integrate as integral
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dapat memanggil Lambda disini
fx = lambda x : 1/(1 + x)

# Fungsi Algoritma Trapesium
def trapesium(fx , a , b , n):
    delta_X = (b - a)/(n+1) # Hasil h

    arangeplusforlooping = [a]
    g = a
    for i in range(1,n+1):
        g += delta_X
        arangeplusforlooping.append(g)

    fx_2kalitrapezoidal = []
    for i in range(1,n+1):
        trapezoidal2kali = 2 * fx(arangeplusforlooping[i])
        fx_2kalitrapezoidal.append(trapezoidal2kali)
    
    #Hasil operasi Dengan metode Trapesium
    Trapezoidal = (delta_X/2) * (fx(a) + sum(fx_2kalitrapezoidal) + fx(b))
    return Trapezoidal

# Fungsi algoritma Simpson 1/3 
def simpson_1per3(fx , a , b , n):
    delta_X = (b - a)/(n+1) # Hasil h 

    arangeplusforlooping = [a] 
    g = a
    for i in range(1,n+1):
        g += delta_X
        arangeplusforlooping.append(g)

    fx_4dan2kalisimpson = []
    
    for i in range(1,n+1):
        if i % 2 != 0:
            d = 4
            simpsonsepertiga_empat = d * fx(arangeplusforlooping[i])
            fx_4dan2kalisimpson.append(simpsonsepertiga_empat)
                
        elif i % 2 == 0:
            d = 2
            simpsonsepertiga_dua = d * fx(arangeplusforlooping[i])
            fx_4dan2kalisimpson.append(simpsonsepertiga_dua)
        
    # Hasil pengoperasian dengan metode Simpson 1/3
    simpson_sepertiga = (delta_X/3) * (fx(a) + sum(fx_4dan2kalisimpson) + fx(b))
    return simpson_sepertiga

# Lambda Error (fungsi error)
error = lambda integral_eksak , integral_approk : abs((integral_eksak - integral_approk)/integral_eksak) * 100

class App():
    def __init__(self):
        window = tk.Tk()
        window.title("Metode Numerik Praktek Python/MATLAB") # Judul di tab windows form
        self.app_utama = window
        
        # Membuat Label di window
        # Grid = posisi letak nya  
        tk.Label(window, text = "Perbandingan Metode Trapesium dengan Metode Simpson 1/3").grid(row= 0, column = 2, sticky = "e")
        
        # Entry = Textbox
        # Label = Label sebuah tulisan saja
        tk.Label(window, text="a :").grid(row=4, column=2, sticky='e')
        self.a = tk.Entry(window)
        self.a.grid(row=4, column=3)

        tk.Label(window, text="b :").grid(row=5, column=2, sticky='e')
        self.b = tk.Entry(window)
        self.b.grid(row=5, column=3)

        tk.Label(window, text="error :").grid(row=6, column=2, sticky='e')
        self.error = tk.Entry(window)
        self.error.grid(row=6, column=3)
        
        # Hasil Akhir Trapesium
        tk.Label(window , text="Trapesium :").grid(row = 31 , column=0 , sticky='e')
        self.hasil_akhir_trape = tk.Label(window)
        self.hasil_akhir_trape.grid(row=31 , column=1 , sticky='e')
        
        tk.Label(window , text="Segmen :").grid(row = 32 , column=0 , sticky='e')
        self.segmen_akhir_trape = tk.Label(window)
        self.segmen_akhir_trape.grid(row=32 , column=1 , sticky='e')
        
        # Hasil Akhir Simpson 1/3
        tk.Label(window , text="Simpson 1/3 :").grid(row = 31 , column=4 , sticky='e')
        self.hasil_akhir_simpson = tk.Label(window)
        self.hasil_akhir_simpson.grid(row=31 , column=5 , sticky='e')
        
        tk.Label(window , text="Segmen :").grid(row = 32 , column=4 , sticky='e')
        self.segmen_akhir_simpson = tk.Label(window)
        self.segmen_akhir_simpson.grid(row=32 , column=5 , sticky='e')
        
        # Plotting Matlplotlib figure (Untuk menampilkan figurenya)
        self.figure = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        self.plot_value = self.figure.add_subplot(211)
        self.plot_value.set_xlabel("Segmen N")
        self.plot_value.set_ylabel("Hasil Integral ")
        self.plot_error = self.figure.add_subplot(212)
        self.plot_error.set_xlabel("Segmen N")
        self.plot_error.set_ylabel("Error N")
        
        # Membuat matplotlib GUI di tkinter dengan posisi gambarnya
        self.canvas_plot = FigureCanvasTkAgg(self.figure, window)
        self.canvas_plot.get_tk_widget().grid(row=12,column=2,rowspan=12,columnspan=2)

        # Membuat Button yang akan muncul sesuai fungsi di bawah
        tk.Button(window, text="Calculate" , command = self.Calculate_Integral_Gabungan).grid(row = 7 , column = 2)

        window.mainloop()
    
    # Untuk memanggil button Calculate Gabungan Trapesium dan simpson 1/3
    def Calculate_Integral_Gabungan(self):
        try :
            a = float(self.a.get())
            b = float(self.b.get())
            Error = float(self.error.get())
            
        except ValueError:
            tk.messagebox.showinfo(title = "Calculate Error" , message = "Maaf , anda perlu menginput semua angka di dalam textbox")
        
        cobatestintegral , error_scipy = integral.quad(fx, a , b)
    
        n = 0
        error_rate_trape = 100
        error_rate_simpson = 100
        
        segmen_N_trape = [n]
        error_N_trape = [error_rate_trape]
        hasil_Int_trape = [0]
        
        segmen_N_simpson_sepertiga = [n]
        error_N_simpson_sepertiga = [error_rate_simpson]
        hasil_integrate_simpson_sepertiga = [0]
        
        
        # Dilakukan looping 2 kali selama error Trapesium dan error simpson sepertiga sesuai error inputnya masing-masing
        while error_N_trape[len(error_N_trape) - 1] > Error and error_N_simpson_sepertiga[len(error_N_simpson_sepertiga) - 1] > Error:
            # While kedua Trapesium
            while error_N_trape[len(error_N_trape) - 1] > Error:
                Trapezoidal = trapesium(fx,a,b,n)
                error_rate_trape = error(cobatestintegral , Trapezoidal)
                n = n + 1
            
                segmen_N_trape.append(n)
                error_N_trape.append(error_rate_trape)
                hasil_Int_trape.append(Trapezoidal)
                
            n = 0
            # While kedua Simpson 1/3
            while error_N_simpson_sepertiga[len(error_N_simpson_sepertiga) - 1] > Error:
                if n % 2 != 0:
                
                    simpson_sepertiga = simpson_1per3(fx,a,b , n)
                    error_rate_simpson = error(cobatestintegral , simpson_sepertiga)
                    n = n + 1
                
                    segmen_N_simpson_sepertiga.append(n)
                    error_N_simpson_sepertiga.append(error_rate_simpson)
                    hasil_integrate_simpson_sepertiga.append(simpson_sepertiga)
                    
                else:
                    n = n + 1
            
            self.plot_value.clear()
            self.plot_error.clear()
            
            # Plotting gabungan
            self.plot_error.plot(segmen_N_trape, error_N_trape , "g--d" , color = "red" , marker = "o" , label = "Trapesium")
            self.plot_value.plot(segmen_N_trape, hasil_Int_trape  , color = "red" , marker = "o" , label = "Trapesium")
            
            self.plot_error.plot(segmen_N_simpson_sepertiga, error_N_simpson_sepertiga , "g--d" , color = "blue" , marker = "o" , label = "Simpson 1/3")
            self.plot_value.plot(segmen_N_simpson_sepertiga, hasil_integrate_simpson_sepertiga  , color = "blue" , marker = "o" , label = "Simpson 1/3")
        
            
            self.plot_error.set_xlabel("Segmen N")
            self.plot_error.set_ylabel("Error Rate")
            
            self.plot_value.set_xlabel("Segmen N")
            self.plot_value.set_ylabel("Perbandingan Integral")
            
            self.plot_error.legend()
            self.plot_value.legend()
            
            old = self.canvas_plot
            self.canvas_plot = FigureCanvasTkAgg(self.figure, self.app_utama)
            self.canvas_plot.get_tk_widget().grid(row=12,column=2,rowspan=12,columnspan=2)
            old.get_tk_widget().destroy()    
            
        ## Untuk Hasil akhir Trapesium dan Simpson dalam Label 
        masukin_hasil_akhir_trape = hasil_Int_trape[len(hasil_Int_trape) - 1]
        masukin_segmen_akhir_trape = segmen_N_trape[len(segmen_N_trape) - 1]
        masukin_hasil_akhir_simpson = hasil_integrate_simpson_sepertiga[len(hasil_integrate_simpson_sepertiga) - 1]
        masukin_segmen_akhir_simpson = segmen_N_simpson_sepertiga[len(segmen_N_simpson_sepertiga) - 1]
        
        ## Untuk Dimasukkan ke Label
        self.hasil_akhir_trape.config(text = masukin_hasil_akhir_trape)
        self.segmen_akhir_trape.config(text = masukin_segmen_akhir_trape)
        self.hasil_akhir_simpson.config(text = masukin_hasil_akhir_simpson)
        self.segmen_akhir_simpson.config(text = masukin_segmen_akhir_simpson)
                    
App()





