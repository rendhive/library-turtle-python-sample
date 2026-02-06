import turtle

def draw_rectangle():
    for _ in range(2):
        turtle.forward(100)  # Panjang 100
        turtle.right(90)     # Sudut 90 derajat
        turtle.forward(50)   # Lebar 50
        turtle.right(90)
    turtle.done()

draw_rectangle()
# Fungsi: Menggambar persegi panjang menggunakan loop.
# Kondisi: Ketika Anda ingin membuat bentuk persegi panjang dalam grafik.