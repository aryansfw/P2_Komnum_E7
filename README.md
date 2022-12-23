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
$ pip install pandas scipy
```
#### 3. Edit f(x)
Dalam file `romberg.py` pada line 60 terdapat fungsi
```py
def f(x):
    return 1/(1+x)
```
Ubah return value dari fungsi tersebut menjadi fungsi yang diinginkan. Pada source code disediakan library math untuk digunakan dalam fungsi `f(x)`.

#### 4. Running the program
Jalankan program menggunakan
```bash
$ python romberg.py
```
#### 5. Input
Program akan meminta input batasan bawah, batasan atas, serta jumlah step.
```bash
Input lower limit, upper limit, and steps (e.g, 0, 1, 5):
```
## Example
Misalnya, kita ingin mengestimasi nilai integral dari\
![image](https://user-images.githubusercontent.com/115603634/209128335-0c069e41-6e9e-45f9-aee6-c1ac1bd608f8.png)\
maka fungsi `f(x)` dalam  `romberg.py` ditulis sebagai berikut
```py
def f(x):
    return math.sin(x) * math.e**x + 1/x
```
Setelah menjalankan program, masukkan batasan bawah, batasan atas, dan jumlah step, misalnya 5 step.
```
Input lower limit, upper limit, and steps (e.g, 0, 1, 5): 1, 2, 5
```
Program akan menghasilkan aproksimasi integral tersebut.
```
Integration using Romberg Method:
          0         1         2         3         4
0  5.253102
1  5.195116  5.175787
2  5.184098  5.180425  5.180734
3  5.181542  5.180691  5.180708  5.180708
4  5.180915  5.180706  5.180708  5.180708  5.180708
Best approximation of the definite integral is 5.180708
```
Dari 5 step diperoleh approksimaksi terbaik adalah `5.180708`\
Selain itu, program juga akan menghasilkan error relatif ($E_r$) seperti berikut:
```
Relative error for each step:
      Value Relative Error
0  5.253102      1.397396%
1  5.175787      0.094980%
2  5.180734      0.000510%
3  5.180708      0.000006%
4  5.180708      0.000000%
```
