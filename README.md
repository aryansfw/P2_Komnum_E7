# Romberg Integration Method
### Kelompok 7
#### Anggota
Nama | NRP
:---: | :---:
Aryan Shafa Wardana | 5025211031
Muhammad Daffa Harits | 5025211005
Syukra Wahyu Ramadhan | 5025211037

## How to Run?
#### 1. Clone
Download dan extract zip repository ini atau clone menggunakan
```bash
$ git clone
```
#### 2. Install libraries
Install library yang diperlukan dengan
```bash
$ pip install pandas numpy
```
#### 3. Edit f(x)
Dalam file `romberg.py` pada line 60 terdapat fungsi
```py
def f(x):
    return 1/(1+x)
```
Ubah return value dari fungsi tersebut menjadi fungsi yang diinginkan. Pada source code disediakan library numpy dan math untuk digunakan dalam fungsi f(x).
#### 4. Running the program
Jalankan program menggunakan
```bash
$ python romberg.py
```