#!/usr/bin/env python
# coding: utf-8


import tkinter as tk
import scipy.integrate as integral
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dapat memanggil Lambda disini
fx = lambda x : 1 / (1 + x)

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
        tk.Label(window, text = "Metode Trapesium" , font=("Times New Roman" , 12)).grid(row= 2, column= 1, sticky = "e")
        tk.Label(window, text = "Metode Simpson 1/3" , font=("Times New Roman" , 12)).grid(row= 2, column = 5, sticky = "e")
        
        # Entry = Textbox
        # Label = Label sebuah tulisan saja
        tk.Label(window, text="a :").grid(row=4, column=0, sticky='e')
        self.a_trapesium = tk.Entry(window)
        self.a_trapesium.grid(row=4, column=1)

        tk.Label(window, text="b :").grid(row=5, column=0, sticky='e')
        self.b_trapesium = tk.Entry(window)
        self.b_trapesium.grid(row=5, column=1)

        tk.Label(window, text="error :").grid(row=6, column=0, sticky='e')
        self.error_trapesium = tk.Entry(window)
        self.error_trapesium.grid(row=6, column=1)
        
        tk.Label(window, text="a :").grid(row=4, column=4, sticky='e')
        self.a_simpson = tk.Entry(window)
        self.a_simpson.grid(row=4, column=5)

        tk.Label(window, text="b :").grid(row=5, column=4, sticky='e')
        self.b_simpson = tk.Entry(window)
        self.b_simpson.grid(row=5, column=5)

        tk.Label(window, text="error :").grid(row=6, column=4, sticky='e')
        self.error_simpson = tk.Entry(window)
        self.error_simpson.grid(row=6, column=5)
        
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
        tk.Button(window, text="Calculate Trapesium" , command = self.Integral_trapesium).grid(row=7, column=1)
        tk.Button(window, text="Calculate Simpson 1/3" , command = self.Integral_Simpson_sepertiga).grid(row = 7 , column=5)
        tk.Button(window, text="Calculate Both" , command = self.Calculate_Integral_Gabungan).grid(row = 7 , column = 2)

        window.mainloop()
    
    # Untuk memanggil button Calculate Trapesium
    def Integral_trapesium(self):
        try:
        # Dipanggil dari Entry menggunakan get dan conversi float karena method get merupakan string 
            a_trape = float(self.a_trapesium.get())
            b_trape = float(self.b_trapesium.get())
            error_trape = float(self.error_trapesium.get())
        except ValueError:
            tk.messagebox.showinfo(title = "Calculate Error" , message = "Maaf , mohon masukkan angka terlebih dahulu")
        
        
        # Hanya bisa dilakukan di fungsi bukan di Textbox nya
        cobatestintegral , error_scipy = integral.quad(fx, a_trape , b_trape)
        
        n = 0
        error_rate = 100
    
        segmen_N_trape = [n]
        error_N_trape = [error_rate]
        hasil_Int_trape = [0]
        
        while error_N_trape[len(error_N_trape) - 1] > error_trape:
            Trapezoidal = trapesium(fx,a_trape,b_trape,n)
            error_rate = error(cobatestintegral , Trapezoidal)
            n = n + 1
            
            segmen_N_trape.append(n)
            error_N_trape.append(error_rate)
            hasil_Int_trape.append(Trapezoidal)
            
            # Untuk mereset Plotting jika melakukan plotting baru
            self.plot_value.clear()
            self.plot_error.clear()
            
            self.plot_error.plot(segmen_N_trape, error_N_trape , "g--d", color = "red" , marker = "o" , label = "Trapesium")
            self.plot_error.set_xlabel("Segmen N")
            self.plot_error.set_ylabel("Error Rate")
            
            self.plot_value.plot(segmen_N_trape, hasil_Int_trape , color = "red" , marker = "o" , label = "Trapesium")
            self.plot_value.set_xlabel("Segmen N")
            self.plot_value.set_ylabel("Integral Trapesium")
            
            # Perlu taruh dibawah 
            self.plot_error.legend()
            self.plot_value.legend()
            
            old = self.canvas_plot
            self.canvas_plot = FigureCanvasTkAgg(self.figure, self.app_utama)
            self.canvas_plot.get_tk_widget().grid(row=12,column=2,rowspan=12,columnspan=2)
            old.get_tk_widget().destroy()
        
        masukin_hasil_akhir = hasil_Int_trape[len(hasil_Int_trape) - 1]
        masukin_segmen_akhir = segmen_N_trape[len(segmen_N_trape) - 1]
        self.hasil_akhir_trape.config(text = masukin_hasil_akhir)
        self.segmen_akhir_trape.config(text = masukin_segmen_akhir)
    
    # Untuk memanggil button Calculate simpson 1/3
    def Integral_Simpson_sepertiga(self):
        try:
            a_simpson_sepertiga = float(self.a_simpson.get())
            b_simpson_sepertiga = float(self.b_simpson.get())
            error_simpson_sepertiga = float(self.error_simpson.get())
        except ValueError:
            tk.messagebox.showinfo(title = "Calculate Error" , message = "Maaf , anda belom menginput semua variable di salah satu metode")
        
        cobatestintegral , error_scipy = integral.quad(fx, a_simpson_sepertiga , b_simpson_sepertiga)
        
        n = 0
        error_rate = 100

        segmen_N_simpson_sepertiga = [n]
        error_N_simpson_sepertiga = [error_rate]
        hasil_integrate_simpson_sepertiga = [0]
        
        while error_N_simpson_sepertiga[len(error_N_simpson_sepertiga) - 1] > error_simpson_sepertiga:
            
            if n % 2 != 0:
                
                simpson_sepertiga = simpson_1per3(fx,a_simpson_sepertiga,b_simpson_sepertiga , n)
                error_rate = error(cobatestintegral , simpson_sepertiga)
                n = n + 1
                
                segmen_N_simpson_sepertiga.append(n)
                error_N_simpson_sepertiga.append(error_rate)
                hasil_integrate_simpson_sepertiga.append(simpson_sepertiga)
                
                self.plot_value.clear()
                self.plot_error.clear()
                
            
                self.plot_error.plot(segmen_N_simpson_sepertiga, error_N_simpson_sepertiga , "g--d" , color = "blue" , marker = "o" , label = "Simpson 1/3")
                self.plot_error.set_xlabel("Segmen N")
                self.plot_error.set_ylabel("Error Rate")
                
                self.plot_value.plot(segmen_N_simpson_sepertiga, hasil_integrate_simpson_sepertiga , color = "blue" , marker = "o" , label = "Simpson 1/3")
                self.plot_value.set_xlabel("Segmen N")
                self.plot_value.set_ylabel("Integral Simpson 1/3")
                self.plot_error.legend()
                self.plot_value.legend()

            
                old = self.canvas_plot
                self.canvas_plot = FigureCanvasTkAgg(self.figure, self.app_utama)
                self.canvas_plot.get_tk_widget().grid(row=12,column=2,rowspan=12,columnspan=2)
                old.get_tk_widget().destroy()
                
                
            else:
                n = n + 1
        
        masukin_hasil_akhir = hasil_integrate_simpson_sepertiga[len(hasil_integrate_simpson_sepertiga) - 1]
        masukin_segmen_akhir = segmen_N_simpson_sepertiga[len(segmen_N_simpson_sepertiga) - 1]
        self.hasil_akhir_simpson.config(text = masukin_hasil_akhir)
        self.segmen_akhir_simpson.config(text = masukin_segmen_akhir)
    
    # Untuk memanggil button Calculate Gabungan Trapesium dan simpson 1/3
    def Calculate_Integral_Gabungan(self):
        try :
            a_trape = float(self.a_trapesium.get())
            b_trape = float(self.b_trapesium.get())
            error_trape = float(self.error_trapesium.get())
        
            a_simpson_sepertiga = float(self.a_simpson.get())
            b_simpson_sepertiga = float(self.b_simpson.get())
            error_simpson_sepertiga = float(self.error_simpson.get())
        except ValueError:
            tk.messagebox.showinfo(title = "Calculate Error" , message = "Maaf , anda belom menginput semua variable di salah satu metode")
        
        cobatestintegral_trape , error_scipy = integral.quad(fx, a_trape , b_trape)
        cobatestintegral_simpson , error_scipy = integral.quad(fx, a_simpson_sepertiga , b_simpson_sepertiga)
        
        n = 0
        error_rate_trape = 100
        error_rate_simpson = 100
        
        segmen_N_trape = [n]
        error_N_trape = [error_rate_trape]
        hasil_Int_trape = [0]
        
        segmen_N_simpson_sepertiga = [n]
        error_N_simpson_sepertiga = [error_rate_simpson]
        hasil_integrate_simpson_sepertiga = [0]
        
        lanjut_hitung_trapesium = True
        lanjut_hitung_simpson_1per3 = True
        
        # Dilakukan looping 2 kali selama error Trapesium dan error simpson sepertiga sesuai error inputnya masing-masing
        while error_N_trape[len(error_N_trape) - 1] > error_trape and error_N_simpson_sepertiga[len(error_N_simpson_sepertiga) - 1] > error_simpson_sepertiga:
            # While kedua Trapesium
            while error_N_trape[len(error_N_trape) - 1] > error_trape:
                Trapezoidal = trapesium(fx,a_trape,b_trape,n)
                error_rate = error(cobatestintegral_trape , Trapezoidal)
                n = n + 1
            
                segmen_N_trape.append(n)
                error_N_trape.append(error_rate)
                hasil_Int_trape.append(Trapezoidal)
                
            n = 0
            # While kedua Simpson 1/3
            while error_N_simpson_sepertiga[len(error_N_simpson_sepertiga) - 1] > error_simpson_sepertiga:
                if n % 2 != 0:
                
                    simpson_sepertiga = simpson_1per3(fx,a_simpson_sepertiga,b_simpson_sepertiga , n)
                    error_rate = error(cobatestintegral_simpson , simpson_sepertiga)
                    n = n + 1
                
                    segmen_N_simpson_sepertiga.append(n)
                    error_N_simpson_sepertiga.append(error_rate)
                    hasil_integrate_simpson_sepertiga.append(simpson_sepertiga)
                    
                else:
                    n = n +1
            
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





