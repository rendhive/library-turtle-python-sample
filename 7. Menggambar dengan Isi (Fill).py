import turtle

def draw_filled_rectangle():
    turtle.begin_fill()  # Memulai pengisian
    turtle.color("green")  # Warna isi hijau
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()  # Mengakhiri pengisian
    turtle.done()

draw_filled_rectangle()
# Fungsi: Menggambarkan persegi panjang dengan pengisian warna.
# Kondisi: Ketika Anda ingin mengganti cara menggambar dengan warna isi.