# Koding Contoh MK Kalkulus Semester Ganjil 2022/2023 Filkom UB
# Rencana Pembelajaran MK Kalkulus Semester Ganjil 2022/2023 Kelas DEF
# Fakultas Ilmu Komputer (Filkom), Universitas Brawijaya (UB) 2022.

# Dosen Pengampu:
# 1. Imam Cholissodin, S.Si., M.Kom. | email: imamcs@ub.ac.id | Filkom UB

from flask import Flask,render_template, Response, redirect,url_for,session,request,jsonify
from flask import render_template_string
import sqlite3
from flask_cors import CORS

from flask import send_file
from flask_qrcode import QRcode

from io import BytesIO
import os

import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
# from bokeh.util.string import encode_utf8

app = Flask(__name__, static_folder='static')
qrcode = QRcode(app)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "static/qr_app/db/qrdata.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# DB untuk qr_app
db_qr = SQLAlchemy(app)
migrate = Migrate(app, db_qr)

# Operasi untuk migrate
# flask db_qr init
# flask db_qr migrate
# flask db_qr upgrade

from static.qr_app.model.StudentModel import Student
from static.qr_app.model.AttendanceModel import Attendance
from static.qr_app.module.Camera import Scanner
# import pyqrcode
import uuid

CORS(app, resources=r'/api/*')

app.secret_key = 'filkomub2223^&&*(&^(filkom#DEF#G#VB#Kalkulus99nDataPyICS_ap938255bnUB'

# keterangan:
# "#" adalah untuk comment
# <br> adalah new line
# &nbsp; adalah spasi
# <!-- --> atau <!--- ---> adalah untuk comment

# FrameWeb_atas & FrameWeb_bawah untuk dekorasi web
# agar menjadi Web yang Responsif

FrameWeb_atas = """
{% extends "extends/base.html" %}
{% block title %}
    <title>Web App Kalkulus Dgn Python</title>
{% endblock title %}
{{ self.title() }}
    Home
{{ self.title() }}
<button onclick="window.location.href='/'" class="btn btn-outline btn-rounded btn-info">
    <i class="ti-arrow-left m-l-5"></i>
    <span>Back Home</span>
</button> Project 1

{{ self.title() }}
    Project 1

{% block content %}
"""
A_a = FrameWeb_atas

FrameWeb_bawah = """
{% endblock content %}
"""
Z_z = FrameWeb_bawah

# @app.route('/')
# def hello_kalkulus():
#    return 'Hello Students | Koding Kalkulus pada Teknologi Cloud :D'

@app.route("/testView_dari_project2_sbg_fp", methods=['GET', 'POST'])
def testView_dari_project2_sbg_fp():

    template_view = '''
        <script type="text/javascript" src="{{ url_for('static', filename = 'js/jquery.min.js') }}"></script>
        <div class="row">
                <div class="col-md-6">
                    <div class="white-box">
                        <h3 class="box-title m-b-0">Prediksi Hasil Pengujian (misal ambil contoh dari topik Project 2 Kel. Anda): </h3>
                        <p class="text-muted m-b-30 font-13"> masukkan nilai parameter Anda </p>
                        <form action="/testView_dari_project2_sbg_fp" method="post" class="form-horizontal">
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x1 = Suhu badan*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var1" {% if var1 is defined and var1 %} value="{{var1}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x2 = Intensitas batuk*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var2" {% if var2 is defined and var2 %} value="{{var2}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x3 = Intensitas interaksi dgn lingkungan*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var3" {% if var3 is defined and var3 %} value="{{var3}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">

                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x4 = Pola nafas (sesak atau tidak)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var4" {% if var4 is defined and var4 %} value="{{var4}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">

                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x5 = Kondisi kesadaran (sadar atau tidak)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var5" {% if var5 is defined and var5 %} value="{{var5}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">

                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x6 = warna cairan hidung (hijau = 100, kuning = 67, bening = 33)*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var6" {% if var6 is defined and var6 %} value="{{var6}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="exampleInputuname" class="col-sm-9 control-label">x7 = frekuensi buang air kecil*</label>
                                <div class="col-sm-2">
                                    <div class="input-group">
                                        <input type="text" name="var7" {% if var7 is defined and var7 %} value="{{var7}}" {% else %} value="" {% endif %} class="form-control" id="exampleInputuname" placeholder="Skor" required="required">
                                    </div>
                                </div>
                            </div>
                            <div class="form-group m-b-0">
                                <div class="col-sm-offset-3 col-sm-9 text-right">
                                    <button type="submit" class="btn btn-info waves-effect waves-light m-t-10">Hitung Hasil Prediksi</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="white-box row">
                        <h3 class="box-title m-b-0">Estimasi hasil prediksinya adalah </h3>
                        {% if c_save is defined and c_save %}
                        <p class="text-5xl font-bold"> nama Cov-19 & Var. baru (y1) = {{'%0.4f'|format(c_save[0][0]|float)}} (hasil pembulatannya =  {{ c_save_round[0][0]}}) </p>
                        <p class="text-5xl font-bold"> imunitas tubuh (y2) = {{'%0.4f'|format(c_save[0][1]|float)}} (hasil pembulatannya =  {{ c_save_round[0][1]}}) </p>
                        {% endif %}
                    </div>
                </div>
                <div class="col-md-6">
                <div class="white-box mt-8 row">
                <div class="justify-around bg-white rounded-lg">
                        <img class="col-md-3 col-xs-12" src="{{ url_for('static', filename = 'img/filkom.png') }}" alt="logo-filkom">
                        <img class="col-md-3 col-xs-12" src="{{ url_for('static', filename = 'img/conan.jpg') }}" alt="kartun-conan">
                </div>
                 </div>
                </div>
            </div>
    '''

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /testView_dari_project2_sbg_fp

        import numpy as np

        def persamaan_beta (x,y):
            hasilbeta = np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.matmul(np.transpose(x),y))
            return hasilbeta

        def y_bar(x_uji,beta):
            hasil_y_bar = np.matmul(x_uji, beta)
            return hasil_y_bar


        x = np.array ([
            [4, 4, 3, 3, 6, 3, 3],
            [6, 6, 9, 7, 8, 7, 6],
            [4, 7, 9, 7, 3, 6, 4],
            [7, 6, 5, 3, 4, 7, 8],
            [4, 3, 6, 6, 5, 7, 3],
            [6, 4, 5, 6, 2, 7, 3],
            [3, 4, 6, 3, 3, 3, 4]
        ])

        y = np.array ([
            [5, 2],
            [8, 3],
            [10, 4],
            [5, 2],
            [5, 2],
            [8, 3],
            [5, 2]
        ])

        var1_in = float(request.form['var1'])
        var2_in = float(request.form['var2'])
        var3_in = float(request.form['var3'])
        var4_in = float(request.form['var4'])
        var5_in = float(request.form['var5'])
        var6_in = float(request.form['var6'])
        var7_in = float(request.form['var7'])

        beta = persamaan_beta(x,y)

        # Memasukkan data uji (x_uji)
        x_uji = np.array([
           [var1_in,var2_in,var3_in,var4_in,var5_in,var6_in,var7_in]
           ])
        hitung_y_bar = y_bar(x_uji,beta)

        hitung_y_bar_round = hitung_y_bar.copy()

        # Agar angkanya menjadi bulat, maka dibulatkan ke atas
        hitung_y_bar_round = np.ceil(hitung_y_bar_round)

        # yang nilainya < 0, set = 0
        hitung_y_bar_round[hitung_y_bar_round < 0] = 0

        return render_template_string(A_a+template_view+Z_z, var1 = var1_in,
        var2 = var2_in, var3 = var3_in, var4 = var4_in, var5 = var5_in,
        var6 = var6_in, var7 = var7_in, c_save = list(hitung_y_bar), c_save_round = list(hitung_y_bar_round))

    else: # untuk yang 'GET' data awal untuk di send ke /testView_dari_project2_sbg_fp
        return render_template_string(A_a+template_view+Z_z)

@app.route('/pert_9_lat', methods=["POST", "GET"])
def pert_9_lat():

    # Koding ini Berdasarkan Materi "Penggunaan Turunan Matrik" utk Generative Modelling
    import numpy as np

    # Mengisi data pada Matriks X
    X = np.array([
           [ 2.,  3.,  1., 0.5],
           [ 3.,  3.,  5., 2.],
           [ 5.,  6.,  4., 40.],
           [ 7.,  8.,  10., 80.],
           [ 9.,  10.,  12., 150.]
           ])

    # Mengisi data pada Matriks Y
    Y = np.array([
           [ 4.,  5.],
           [ 5.,  4.],
           [ 7.,  3.],
           [ 10.,  2.],
           [ 15.,  1.]
           ])

    # Hitung Matrik Beta (B)
    B = np.linalg.inv(np.transpose(X).dot(X)).dot(np.transpose(X)).dot(Y)

    # Memasukkan data uji (Xuji)
    Xuji = np.array([
           [ 10.,  10.,  10., 1000.]
           ])

    # Menghitung Hasil Output Ytopi dari inputan Xuji
    Ytopi = Xuji.dot(B)

    Ytopi_awal = Ytopi.copy()

    # Agar angkanya menjadi bulat, maka dibulatkan ke atas
    Ytopi = np.ceil(Ytopi)


    # yang nilainya < 0, set = 0
    Ytopi[Ytopi < 0] = 0


    return render_template_string(A_a+str(Ytopi_awal)+" <br> Hasil setelah diset yg kurang dari nol = 0" + str(Ytopi) +Z_z)

@app.route('/pert_9_1', methods=["POST", "GET"])
def pert_9_1():

    # Koding ini Berdasarkan Materi "Penggunaan Turunan Matrik" utk Generative Modelling
    import numpy as np

    # Ket. X
    # misal menyatakan berapa jam waktu belajar dlm 3 hari,
    # Kolom ke-1 adalah hari ke-1 (x1), .., Kolom ke-3 adalah hari ke-3 (x3)

    # Mengisi data pada Matriks X
    X = np.array([
           [ 2.,  3.,  1.],
           [ 3.,  3.,  5.],
           [ 5.,  6.,  4.],
           [ 7.,  8.,  10.],
           [ 9.,  10.,  12.]
           ])

    # Dan Y
    # Kolom ke-1 menyatakan banyaknya materi kalkulus yg berhasil dipahami
    # Kolom ke-2 menyatakan rangking di kelas
    # Mengisi data pada Matriks Y
    Y = np.array([
           [ 4.,  1.],
           [ 5.,  2.],
           [ 7.,  3.],
           [ 10.,  4.],
           [ 15.,  5.]
           ])

    # Menampilkan X dan Y
    # print("Menampilkan X sbg Input:")
    # print(X)
    # print()
    # print("Menampilkan Y sbg Output:")
    # print(Y)

    # Hitung Matrik Beta (B)
    B = np.linalg.inv(np.transpose(X).dot(X)).dot(np.transpose(X)).dot(Y)
    # print("Hitung Matrik Beta (B)")
    # print(B)
    # B[:,0]=np.clip(B[:,0], 1, 15)
    # B[:,1]=np.clip(B[:,1], 1, 10)

    # print()
    # print("Hitung Matrik Beta (B) dgn clip")
    # print(B)

    # Memasukkan data uji (Xuji)
    Xuji = np.array([
           [ 2.,  3.,  1.],
           [ 3.,  3.,  5.]
           ])
    # print(Xuji)

    # Menghitung Hasil Output Ytopi dari inputan Xuji
    # Kolom ke-1 menyatakan banyaknya materi kalkulus yg berhasil dipahami
    # Kolom ke-2 menyatakan rangking di kelas
    Ytopi = Xuji.dot(B)

    # Agar angkanya menjadi bulat, maka dibulatkan ke atas
    Ytopi = np.ceil(Ytopi)
    # [[4. 1.]
    #  [5. 2.]]


    return render_template_string(A_a+str(Ytopi)+Z_z)

@app.route('/contoh_utk_uts_kalkulus_no_4', methods=["POST", "GET"])
def contoh_utk_uts_kalkulus_no_4():

    # Hitung Lambert w function atau omega function atau productlog
    # x*(e^x) = a, maka, W(x*(e^x)) = W(a), shg, x = W(a)
    import numpy as np

    def fn_utk_fn_lambert(x,a):
        return x*(np.e**x) - a

    def D_fn_utk_fn_lambert(x):
        # f(x) = x*(e^x) - a
        # u = x, v=e^x
        # f'(x) = u'v + v'u
        # = e^x + x*e^x
        return np.e**x + x*(np.e**x)

    # Membuat lambert w function / omega function /
    # productlog base Other function above like Stirling's approximation function
    def fn_lambert(a): # masih dibatasi untuk a >=0
        if a ==0:
            return 0
        else:
            # if a > 0:
            #misal menggunakan newton's method:
            # init x_n = 1
            x_n = 1.0
            epsilon = 0.0001 #utk pembandingan tingkat tolerasi error
            IterMax = 1000
            is_ok = True
            counter = 0
            while(is_ok):
                x_n_plus_1 = x_n - (fn_utk_fn_lambert(x_n,a)/D_fn_utk_fn_lambert(x_n))
                x_n = x_n_plus_1
                if (abs(fn_utk_fn_lambert(x_n,a))<=epsilon) or counter==IterMax:
                    is_ok = False
                # x_n = float(x_n) counter+=1
            return x_n

        # else:
            #return 'Masukkan nilai a >=0, karena sbg pembatasan dari koding yg dibuat :D'
        # return

    def fn_invers_fact(from_n_fact_get_n):
        val_fn_lambert = \
        float(fn_lambert((1/(np.e))*(np.log(from_n_fact_get_n/(np.sqrt(2*np.pi))))))
        val_fn_lambert = float(val_fn_lambert)
        n_init = np.e*(np.e**( val_fn_lambert ))-0.5
        n = 0 if np.isnan(n_init) else n_init

        if(fac(int(np.ceil(n)))==from_n_fact_get_n):
            n = int(np.ceil(n))
        return n

    def fac(n):
        if n == 0 or n == 1:
            return 1
        else:
            hasil_fac=1
            for _ in range(n):
                hasil_fac *=(_+1)

            return hasil_fac

    hasil_x_for_x_e_pow_x_minus_2_equal_zero = fn_lambert(2)
    # Output 0.8526055263689221
    hasil_n_for_n_faktorial_equal_x = fn_invers_fact(22/7)
    # Output 2.4359820320554704

    # return str(hasil_x_for_x_e_pow_x_minus_2_equal_zero)+'<br>'+str(hasil_n_for_n_faktorial_equal_x)
    # <br> untuk new line
    return render_template_string(A_a+'Hasil x untuk x*(e^x) = 2, x = '+str(hasil_x_for_x_e_pow_x_minus_2_equal_zero)+'<br><br>'+\
    'Hasil n untuk n! = 22/7, n = '+str(hasil_n_for_n_faktorial_equal_x)+Z_z)

    # petunjuk untuk LIATE, yaitu  L = Log, I = Inverse Trig, A = Algebraic, T = Trigonometric, E = Exponential,
    # misal untuk yang trigonometri sin dan cos, dan lainnya
    # import numpy as np
    # #
    # # Kepanjangan dari LIATE, yaitu Log, Invers-Trigonometri, Aljabar, Trigonometri dan Exponential
    # #
    # # hitung log_e(0) atau setara dengan logaritma natural ln(0)
    # print(np.log(0))

    # # hitung log_2(8)
    # print(np.log(8)/np.log(2))

    # # hitung log_10(100)
    # print(np.log(100)/np.log(10))

    # x = 0.8526055263689221
    # hasil = x*np.exp(x)
    # print(hasil)

    # # contoh hitung Invers-Trigonometri
    # print(np.arcsin(np.arccos(0.7)))

    # # hitung aljabar linear
    # from sympy import *
    # x,y=symbols('x,y')

    # eq1 = 2*x + 5*y - 6
    # eq2 = 3*x + 7*y - 12


    # res = solve((eq1, eq2), dict=True)
    # print(res)

    # # hitung aljabar untuk hasil akar persaman kuadrat
    # from sympy import symbols, Eq, solve
    # y = symbols('x')
    # eq1 = Eq(x**2 - 5*x + 6, 0)

    # sol = solve(eq1)
    # # cara akses nilai hasilnya
    # print('[ ',float(sol[0]),' , ', float(sol[1]), ' ]')

    # # hitung Trigonometri
    # print(np.sin(np.deg2rad(180)))
    # print(np.sin(np.pi))
    # print(np.rad2deg(22/7))
    # print(np.sin(np.cos(0.7)))

    # # hitung Exponential
    # print(2*np.exp(5))

def Cek_Genap_Ganjil(bilangan):
    if(float(bilangan)%2==0):
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"

@app.route('/genap_vs_ganjil', methods=["POST", "GET"])
def genap_vs_ganjil():
    template_view_1 = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
                  <form method="post">
                    Masukkan bilangan = <input type="text" name="a" value="{{a_post}}" />
                    <input type="submit" value="Cek Tipe Bilangan"/>
                  </form>
                  <h2>Hasil Pengecekan, bilangan tersebut merupakan {{ hasil }} </h2>
            <!--- </body> --->
            <!--- </html> --->
        '''

    template_view_2 = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
                  <form action="/genap_vs_ganjil" method="post">
                    Masukkan bilangan = <input type="text" name="a" value="" />
                     <input type="submit" value="Cek Tipe Bilangan"/>
                  </form>
            <!--- </body> --->
            <!--- </html> --->
        '''

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /genap_vs_ganjil

        bil = request.form['a']
        hasil = Cek_Genap_Ganjil(bil)

        return render_template_string(A_a+template_view_1+Z_z, a_post = bil, hasil = hasil)

    else: # untuk yang 'GET' data awal untuk di send ke /genap_vs_ganjil
        return render_template_string(A_a+template_view_2+Z_z)

@app.route('/visual_cartesius_vs_polar')
def visual_cartesius_vs_polar():
    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure(plot_width=300, plot_height=300)
    fig.vbar(
        x=[1, 2, 3, 4],
        width=0.5,
        bottom=0,
        top=[1.7, 2.2, 4.6, 3.9],
        color='navy'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    template_view ='''
    <!-- <!doctype html> -->
    <!-- <html lang="en"> -->
    <!--  <head> -->
        <meta charset="utf-8">
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <title>Embed Demo</title>
        {{ js_resources|indent(4)|safe }}
        {{ css_resources|indent(4)|safe }}
        {{ plot_script|indent(4)|safe }}
    <!--  </head> -->
    <!--  <body> -->
        {{ plot_div|indent(4)|safe }}
    <!--  </body> -->
    <!-- </html> -->
    '''

    # render template
    script, div = components(fig)
    html = render_template_string(
        A_a+template_view+Z_z,
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )

    return html

# mencoba memuat fungsi untuk cek apakan
# bilangan yang dimasukkan merupakan bilangan integer (bulat) atau Float
def Cek_Int_atau_Bulat_vs_Float(bilangan):
    f = float(bilangan)
    if f == int(f):
        return "Bilangan Integer atau Bilangan Bulat"
    else:
        return "Bilangan Float"

@app.route('/int_vs_float', methods=["POST", "GET"])
def int_vs_float():

    template_view_1 = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
                  <form method="post">
                    Masukkan bilangan = <input type="text" name="a" value="{{a_post}}" />
                    <input type="submit" value="Cek Tipe Bilangan"/>
                  </form>
                  <h2>Hasil Pengecekan, bilangan tersebut merupakan {{ hasil }} </h2>
            <!--- </body> --->
            <!--- </html> --->
        '''

    template_view_2 = '''
            <!--- <html> --->
            <!--- <head> --->
            <!--- </head> --->
            <!--- <body> --->
                  <form action="/int_vs_float" method="post">
                    Masukkan bilangan = <input type="text" name="a" value="" />
                     <input type="submit" value="Cek Tipe Bilangan"/>
                  </form>
            <!--- </body> --->
            <!--- </html> --->
        '''

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /int_vs_float

        bil = request.form['a']
        hasil = Cek_Int_atau_Bulat_vs_Float(bil)

        return render_template_string(A_a+template_view_1+Z_z, a_post = bil, hasil = hasil)

    else: # untuk yang 'GET' data awal untuk di send ke /int_vs_float
        return render_template_string(A_a+template_view_2+Z_z)

@app.route('/visual_xy_polar')
def visual_xy_polar():
    # ..
    # .
    return "tempat koding visual_xy_polar"

@app.route('/db/<aksi>')
def manipulate_tabel(aksi):
    conn = connect_db()
    db = conn.cursor()

    # Aksi => Buat, Hapus

    if aksi == 'c':
        str_info = 'tabel berhasil dibuat :D'
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS data_cronjob
        (tipe_run TEXT, date_pembuatan DATETIME,
        teks_call_sintaks TEXT,
        keterangan TEXT,
        date_masa_berlaku DATETIME)
        """)
    elif aksi== 'd':
        str_info = 'tabel berhasil dihapus :D'
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS data_cronjob
        """)

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air/<aksi>')
def manipulate_tabel_CloundAI_Air(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/db/CloudAI_Air_Rev/<aksi>')
def manipulate_tabel_CloundAI_Air_Rev(aksi):
    conn = connect_db()
    db = conn.cursor()

    if aksi == 'c':
        # create tabel
        db.execute("""
        CREATE TABLE IF NOT EXISTS CloudAI_Air_Rev (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
        """)
        str_info = 'tabel berhasil dibuat :D'
    elif aksi== 'd':
        # hapus tabel
        db.execute("""
        DROP TABLE IF EXISTS CloudAI_Air_Rev
        """)

        str_info = 'tabel berhasil dihapus :D'

    conn.commit()
    db.close()
    conn.close()

    return str_info

@app.route('/user')
def data_user():
    try:
        conn = connect_db()
        db = conn.cursor()

        rs = db.execute("SELECT * FROM user order by id")
        userslist = rs.fetchall()
        return render_template('data_user.html',userslist=userslist)

    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

@app.route("/update_user",methods=["POST","GET"])
def update_user():
    try:
        conn = connect_db()
        db = conn.cursor()
        if request.method == 'POST':
            field = request.form['field']
            value = request.form['value']
            editid = request.form['id']

            if field == 'mail':
                db.execute("""UPDATE user SET Mail=? WHERE id=?""",(value,editid))
            if field == 'name':
                db.execute("""UPDATE user SET Name=? WHERE id=?""",(value,editid))
            if field == 'pwd':
                db.execute("""UPDATE user SET Password=? WHERE id=?""",(value,editid))
            if field == 'level':
                db.execute("""UPDATE user SET Level=? WHERE id=?""",(value,editid))

            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        db.close()
        conn.close()

# ================ awal - dasar ke-2 ===============
#

# buat input dari url, untuk penjumlahan misal 2 bilangan
@app.route('/add/<a>/<b>')
def add_ab(a,b):
    c = int(a) + float(b)
    return 'a + b = ' + str(c)
    # return 'a + b = %s' % c
# https://userAnda.pythonanywhere.com/add/1/2.5
# hasil => a + b = 3.5

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return kode html dalam flask python Web App
@app.route('/post_add2', methods=["POST", "GET"])
def inputkan_ab():
    # membuat penjumlahan 2 bilangan

    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return '''
        <html>
            <head>
            </head>
            <body>
              <form method="post">
                <input type="text" name="a" value="%s" />
                <input type="text" name="b" value="%s" />
                <input type="submit" value="Hitung a + b"/>

              </form>
              <h2>Hasil a + b = %s + %s = %s </h2>
            </body>
        </html>
        ''' % (a_in, b_in, a_in, b_in, c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add2
        return '''
            <html>
                <head>
                </head>
                <body>
                  <form action="/post_add2" method="post">
                    Masukkan nilai a = <input type="text" name="a" value="" />
                    <br>
                    Masukkan nilai b = <input type="text" name="b" value="" />
                    <input type="submit" value="Hitung a + b"/>
                  </form>
                </body>
            </html>
        '''

#
# buatlah halaman post sekaligus get
# nilai a dan b, lalu ditambahkan
# dengan return file "form_add3.html" dalam folder "mysite/templates", flask python Web App
@app.route('/post_add3', methods=["POST", "GET"])
def inputkan_ab3():
    # membuat penjumlahan 2 bilangan
    if request.method == 'POST': # dioperasikan dihalaman sendiri tanpa send ke route, misal /post_add2

        a_in = float(request.form['a'])
        b_in = float(request.form['b'])
        c = a_in + b_in

        return render_template('form_add3.html', a_save = a_in, b_save = b_in, c_save = c)

    else: # untuk yang 'GET' data awal untuk di send ke /post_add3
        return render_template('form_add3.html')


# ================================================================================
# Contoh koding dasar operasi CRUD pada tabel CloudAI_Air,
# mulai dari "def dasar2_create_database():" sampai sebelum "# ================ akhir - dasar ke-2 ==============="
#
# membuat render_template_string sebagai pengganti render_template
# agar semua kodenya hanya dalam 1 file, sehingga lebih mudah untuk membuat dan run kodingnya
#
def dasar2_create_database():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS CloudAI_Air (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    suhu_dlm_celcius TEXT,
                    humidity_kelembaban_dlm_persen TEXT,
                    precipitation_curah_hujan_dlm_persen TEXT,
                    wind_angin_dlm_km_per_jam TEXT,
                    durasi_air_dlm_menit TEXT
                )
                """)

    conn.commit()
    conn.close()

def dasar2_generate_data():
    """Generate sintesis atau dummy data untuk percontohan."""
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM CloudAI_Air')
    entry = cur.fetchone()

    if entry is None:
        import numpy as np
        import pandas as pd
        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))


        # Misal skema dataset-nya seperti berikut: => Silahkan dimodifikasi sesuai case Anda
        kolomFitur_X_plus_Target_Y = ['Suhu (X1)','Kelembaban (X2)', 'Curah Hujan (X3)','Angin (X4)','Durasi Air Dlm Menit (Y)']

        # set bykData = 3*np.power(10,7)
        bykData = 10
        bykFitur = len(kolomFitur_X_plus_Target_Y)-1

        # Interval atau Variasi nilai fitur
        nilaiFitur_Suhu = [17,35]
        nilaiFitur_Kelembaban = [70,90]
        nilaiFitur_Curah_Hujan = [2,95]
        nilaiFitur_Angin = [0,15]
        labelTargetY = [0.0,90.0]

        # generate isi dataset
        content_dataGenerate = np.array([np.arange(bykData)]*(bykFitur+1)).T
        df_gen = pd.DataFrame(content_dataGenerate, columns=kolomFitur_X_plus_Target_Y)

        df_gen ['Suhu (X1)'] = np.random.randint(nilaiFitur_Suhu[0], nilaiFitur_Suhu[1], df_gen.shape[0])
        df_gen ['Kelembaban (X2)'] = np.random.randint(nilaiFitur_Kelembaban[0], nilaiFitur_Kelembaban[1], df_gen.shape[0])
        df_gen ['Curah Hujan (X3)'] = np.random.randint(nilaiFitur_Curah_Hujan[0], nilaiFitur_Curah_Hujan[1], df_gen.shape[0])
        df_gen ['Angin (X4)'] = np.random.randint(nilaiFitur_Angin[0], nilaiFitur_Angin[1], df_gen.shape[0])
        df_gen ['Durasi Air Dlm Menit (Y)'] = np.round(np.random.uniform(labelTargetY[0], labelTargetY[1], df_gen.shape[0]),2)

        # save dataframe generate ke *.csv
        import os
        userhome = os.path.expanduser("~").split("/")[-1]

        path = "/home/"+userhome+"/mysite/static/data_contoh"
        if not os.path.exists(path):
            os.makedirs(path)
        # file_name_data_generate = 'static/data_contoh/Data_CloudAI_Air.csv'
        # df_gen.to_csv(file_name_data_generate, encoding='utf-8', index=False)
        url_file_name_data_generate = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")
        df_gen.to_csv(url_file_name_data_generate, encoding='utf-8', index=False)

        # read file *.csv dan tampilkan
        # data_generate = pd.read_csv(file_name_data_generate)

        url = os.path.join(BASE_DIR, "static/data_contoh/Data_CloudAI_Air.csv")

        # Importing the dataset => ganti sesuai dengan case yg anda usulkan
        dataset = pd.read_csv(url)
        # X = dataset.iloc[:, :-1].values
        # y = dataset.iloc[:, 1].values

        def pushCSVdatasetToDB(x1,x2,x3,x4,y):
            #inserting values inside the created table

            cmd = "INSERT INTO CloudAI_Air(suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES('{}','{}','{}','{}','{}')".format(x1,x2,x3,x4,y)
            cur.execute(cmd)
            conn.commit()

        # CSV_to_SQLite3 dari file dataset
        for i in range(0,len(dataset)):
            pushCSVdatasetToDB(dataset.iloc[i][0],dataset.iloc[i][1],dataset.iloc[i][2],dataset.iloc[i][3],dataset.iloc[i][4])
    else:
        ket_hasil = 'Tidak dilakukan Insert, karena Tabel tidak kosong'
        print(ket_hasil)

    conn.commit()
    cur.close()
    conn.close()

@app.route('/dasar2_crud')
def dasar2_index():
    return '<a href="/dasar2_list">Demo Menampilkan List dari Tabel + Support => Create, Read, Update, Delete (CRUD)</a>'

@app.route('/dasar2_list')
def dasar2_list():

    # buat tabel dan generate data dummy
    dasar2_create_database()
    dasar2_generate_data()

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM CloudAI_Air")
    rows = cur.fetchall()

    conn.close()

    #return render_template("list.html", rows=rows)
    return render_template_string(template_list, rows=rows)


@app.route('/dasar2_edit/<int:number>', methods=['GET', 'POST'])
def dasar2_edit(number):
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        # suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit

        cur.execute("UPDATE CloudAI_Air SET suhu_dlm_celcius = ?, humidity_kelembaban_dlm_persen = ?, precipitation_curah_hujan_dlm_persen = ?, wind_angin_dlm_km_per_jam = ?, durasi_air_dlm_menit = ? WHERE id = ?",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi, item_id))
        conn.commit()

        return redirect('/dasar2_list')

    cur.execute("SELECT * FROM CloudAI_Air WHERE id = ?", (number,))
    item = cur.fetchone()

    conn.close()

    #return render_template("edit.html", item=item)
    return render_template_string(template_edit, item=item)

@app.route('/dasar2_delete/<int:number>')
def dasar2_delete(number):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM CloudAI_Air WHERE id = ?", (number,))

    conn.commit()
    conn.close()

    return redirect('/dasar2_list')

@app.route('/dasar2_add', methods=['GET', 'POST'])
def dasar2_add():
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        # item_id      = number
        item_suhu    = request.form['suhu']
        item_kelembaban = request.form['kelembaban']
        item_hujan  = request.form['hujan']
        item_angin = request.form['angin']
        item_durasi = request.form['durasi']

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam, durasi_air_dlm_menit) VALUES (?, ?, ?, ?, ?)""",
                    (item_suhu, item_kelembaban, item_hujan, item_angin, item_durasi))
        conn.commit()

        return redirect('/dasar2_list')

    #return render_template("add.html", item=item)
    return render_template_string(template_add)

@app.route('/dasar2_add2')
def dasar2_add2():
    conn = connect_db()
    cur = conn.cursor()

    # get data dari iot API
    import requests
    # from datetime import datetime
    # import pytz
    # Date = str(datetime.today().astimezone(pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y %H:%M:%S'))

    def F2C(f_in):
        return (f_in - 32)* 5/9

    def Kelvin2C(k_in):
      return (k_in-273.15)

    # list_kota = ['Jakarta','Los Angeles','Chicago','New York City','Toronto','São Paulo', \
    #              'Lagos', 'London', 'Johannesburg', 'Kairo', 'Paris', 'Zurich', 'Istanbul', 'Moskwa', 'Dubai', \
    #             'Mumbai','Hong Kong','Shanghai','Singapura','Tokyo','Sydney']
    list_kota = ['Malang']


    for nama_kota in list_kota:
        #   each_list_link='http://api.weatherapi.com/v1/current.json?key=re2181c95fd6d746e9a1331323220104&q='+nama_kota
        each_list_link='http://api.weatherapi.com/v1/current.json?key=2181c95fd6d746e9a1331323220104&q='+nama_kota
        resp=requests.get(each_list_link)

        # print(nama_kota)

        #http_respone 200 means OK status
        if resp.status_code==200:
            resp=resp.json()
            suhu = resp['current']['temp_c']
            curah_hujan = resp['current']['precip_mm']
            lembab = resp['current']['humidity']
            angin = resp['current']['wind_mph']
        else:
            # print("Error")
            suhu = '-'
            curah_hujan = '-'
            lembab = '-'
            angin = '-'

        # print(nama_kota, 'dengan suhu = ', round(float(suhu),2),'°C', end='\n')

        cur.execute("""INSERT INTO CloudAI_Air (suhu_dlm_celcius, humidity_kelembaban_dlm_persen, precipitation_curah_hujan_dlm_persen, wind_angin_dlm_km_per_jam) VALUES (?, ?, ?, ?)""",
                (suhu, lembab, curah_hujan, angin))

        conn.commit()
        cur.close()
        conn.close()

    return redirect('/dasar2_list')

template_list = """
<h2>Menampilkan Data CloudAI Air + Support Create, Read, Update, delete (CRUD)</h2>
<a href="{{ url_for( "dasar2_add" ) }}">Tambah Data</a> |
<a href="{{ url_for( "dasar2_add2" ) }}">Tambah Data dari iot_api (tanpa nilai Durasi Waktu)</a>
{% if rows %}
<table border="1">
    <thead>
        <td>No</td>
        <td>Suhu (°C)</td>
        <td>Kelembaban (%)</td>
        <td>Curah Hujan (%)</td>
        <td>Kecepatan Angin (Km/Jam)</td>
        <td>Durasi Waktu Pengairan / Penyiraman (Menit)</td>
    </thead>

    {% for row in rows %}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>
        <td>{{row[5]}}</td>
        <td>
            <a href="{{ url_for( "dasar2_edit", number=row[0] ) }}">Edit</a> |
            <a href="{{ url_for( "dasar2_delete", number=row[0] ) }}">Hapus</a>
        </td>
    </tr>
    {% endfor %}
</table>
{% else %}
Empty</br>
{% endif %}
"""

template_add = """
<h1>Tambah Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_add" ) }}">
    Suhu: <input name="suhu" value=""/></br>
    Kelembaban: <input name="kelembaban" value=""/></br>
    Curah Hujan: <input name="hujan" value=""/></br>
    Kecepatan Angin: <input name="angin" value=""/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value=""/></br>
    <button>Simpan Data</button></br>
</form>
"""

template_edit = """
<h1>Edit Data CloudAI Air</h1>
<form method="POST" action="{{ url_for( "dasar2_edit", number=item[0] ) }}">
    Suhu: <input name="suhu" value="{{item[1]}}"/></br>
    Kelembaban: <input name="kelembaban" value="{{item[2]}}"/></br>
    Curah Hujan: <input name="hujan" value="{{item[3]}}"/></br>
    Kecepatan Angin: <input name="angin" value="{{item[4]}}"/></br>
    Durasi Waktu Pengairan / Penyiraman: <input name="durasi" value="{{item[5]}}"/></br>
    <button>Simpan Update Data</button></br>
</form>
"""

# ================ akhir - dasar ke-2 ===============

# ================ awal - dasar ke-1 ===============
# #

# @app.route('/add')
# def add():
#     # membuat penjumlahan 2 bilangan
#     a = 10
#     b = 90
#     c = a + b

#     return str(c)

# # buatlah halaman perkalian
# # antara a*b
# @app.route('/kali')
# def kali():
#     # membuat perkalian 2 bilangan
#     a = 10
#     b = 90
#     c = a * b

#     return str(c)

# # buatlah tampilan indeks looping 1..10
# @app.route('/loop')
# def loop():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '  '

#     return str(c)

# # buatlah tampilan indeks looping 1..10 dengan new line (<br> dari tag html)
# @app.route('/loop_new_line')
# def loop_new_line():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         c +=str(i+1) + '<br>'

#     return str(c)

# # buatlah tampilan indeks looping 1 sampai 10
# # yang ganjil
# @app.route('/ganjil')
# def ganjil():
#     c = ''
#     for i in range(10): # i = 0,1,..,9
#         if((i+1)%2!=0):
#             c +=str(i+1) + '  '

#     return str(c)
# # ================ akhir - dasar ke-1 ===============

# ========= untuk Tugas Ke-1 & 2 | Project =================

@app.route("/")
def index():
    # return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
  conn = connect_db()
  db = conn.cursor()
  msg = ""
  if request.method == "POST":
      mail = request.form["mail"]
      passw = request.form["passw"]

      rs = db.execute("SELECT * FROM user WHERE Mail=\'"+ mail +"\'"+" AND Password=\'"+ passw+"\'" + " LIMIT 1")

      conn.commit()

      hasil = []
      for v_login in rs:
          hasil.append(v_login)

      if hasil:
          session['name'] = v_login[3]
          return redirect(url_for("launchpad_menu"))
      else:
          msg = "Masukkan Username (Email) dan Password dgn Benar!"

  return render_template("login.html", msg = msg)

@app.route("/register", methods=["GET", "POST"])
def register():
  conn = connect_db()
  # db = conn.cursor()
  if request.method == "POST":
      mail = request.form['mail']
      uname = request.form['uname']
      passw = request.form['passw']

      cmd = "insert into user(Mail, Password,Name,Level) values('{}','{}','{}','{}')".format(mail,passw,uname,'1')
      conn.execute(cmd)
      conn.commit()

      # conn = db

      return redirect(url_for("login"))
  return render_template("register.html")

def connect_db():
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data.db")

    return sqlite3.connect(db_path)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def internal_server_error(error):
    userhome = os.path.expanduser("~").split("/")[-1]
    link_error_debug = "https://www.pythonanywhere.com/user/"+userhome+"/files/var/log/"+userhome+".pythonanywhere.com.error.log"

    return render_template("500.html", link_error_debug = link_error_debug)

@app.route('/iot', methods=["GET", "POST"])
def iot():

    if 'name' in session:
        name = session['name']
    else:
        name = 'Guest'

    # start kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv
    if request.method == "POST":

        from io import StringIO
        import csv

        # date_var = request.args.get('date_var')
        # kota_var = request.args.get('kota_var')
        conn = connect_db()
        db = conn.cursor()

        output = StringIO()
        writer = csv.writer(output)
        c = db.execute("SELECT * FROM data_suhu_dll")

        result = c.fetchall()
        writer.writerow([i[0] for i in c.description])

        for row in result:
            line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
            writer.writerow(line)

        output.seek(0)

        conn.commit()
        db.close()
        conn.close()

        return Response(output, mimetype="text/csv",
                        headers={"Content-Disposition": "attachment;filename=data_suhu_iot_all.csv"})
    # ending kode untuk download atau export semua data dari tabel data_suhu_dll menjadi file *.csv


    # menampilkan data dari tabel data_suhu_dll
    conn = connect_db()
    db = conn.cursor()

    c = db.execute(""" SELECT * FROM  data_suhu_dll """)

    mydata = c.fetchall()
    for x in c.fetchall():
        name_v=x[0]
        data_v=x[1]
        break

    hasil = []
    for v_login in c:
        hasil.append(v_login)

    conn.commit()
    db.close()
    conn.close()


    return render_template("getsuhu_dll.html", header = mydata)

@app.route('/del_iot/', methods=["GET"])
def del_iot():
    date_var = request.args.get('date_var')
    kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    db.execute("DELETE FROM data_suhu_dll WHERE date =\'"+ date_var +"\' AND  kota =\'"+ kota_var +"\'")

    conn.commit()
    db.close()
    conn.close()

    return redirect(url_for("iot"))

@app.route('/dw_iot/', methods=["GET"])
def dw_iot():

    from io import StringIO
    import csv

    date_var = request.args.get('date_var')
    # kota_var = request.args.get('kota_var')
    conn = connect_db()
    db = conn.cursor()

    output = StringIO()
    writer = csv.writer(output)
    c = db.execute("SELECT * FROM data_suhu_dll WHERE date =\'"+ date_var +"\'")

    result = c.fetchall()
    writer.writerow([i[0] for i in c.description])

    for row in result:
        line = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])]
        writer.writerow(line)

    output.seek(0)

    conn.commit()
    db.close()
    conn.close()

    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=data_suhu_iot.csv"})

@app.route('/logout')
def logout():
   # remove the name from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))


# ================
# Ergo Project

@app.route("/in")
def index_qrcode():
    return render_template("qrcode.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")

@app.route('/qr_index')
def qr_index():
    attendance = Attendance.getAll()
    return render_template("qr_scan2.html", data=enumerate(attendance, 1))


@app.route("/qr_scan", methods=["GET"])
def qr_scan():
    return Response(scanner(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/qr_student", methods=["GET", "POST"])
def qr_student():
    if request.method == "POST":
        name = request.form['name']
        nim = request.form['nim']
        UUID = str(uuid.uuid4())
        qr_code_mark = "static/img/tmp_qr/{}.png".format(UUID)
        student = Student(nim=nim, name=name, qr_code=qr_code_mark)
        student.save()

        import qrcode

        # # /qrcode
        # qrcode_img = qrcode.make(student.id)
        # # buf = io.BytesIO()
        # buf_qrcode = BytesIO()
        # qrcode_img.save(buf_qrcode)
        # buf_qrcode.seek(0)
        # # return send_file(buf_qrcode, mimetype='image/jpeg')

        qrcode_img = qrcode.make(student.id)
        # qrcode_img = qrcode(student.id)
        # canvas = Image.new('RGB', (290,290), 'white')
        # draw = ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # fname = f'qr_code_{self.name}.png'
        fname = f'static/img/tmp_qr/qr_code_{student.id}.png'.format(UUID)
        buffer = BytesIO()
        # canvas.save(buffer,'PNG')
        # qrcode_img.save(fname, File(buffer), save=False)
        # qrcode_img.save(fname, buffer, save=False)
        # qrcode_img.save(buffer)

        import os.path

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        url_file_name_qrcode = os.path.join(BASE_DIR, fname)

        qrcode_img.save(url_file_name_qrcode, format="PNG")
        # canvas.close()
        # super().save(*args, **kwargs)

        # img = pyqrcode.create(student.id, error="L", mode="binary", version=5)
        # img.png(qr_code, scale=10)
    students = Student.getAll()
    return render_template("qr_student.html", data=enumerate(students, 1))


def scanner():
    camera = Scanner()
    while True:
        frame = camera.get_video_frame()

        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            break

@app.route('/launchpad_menu')
def launchpad_menu():
   return render_template("launchpad_menu.html")