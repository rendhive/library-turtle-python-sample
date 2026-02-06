import turtle

def draw_spiral():
    for i in range(100):
        turtle.forward(i * 10)  # Panjang garis bertambah
        turtle.right(144)  # Sudut spiral
    turtle.done()

draw_spiral()
# Fungsi: Menggambar pola spiral dengan panjang garis yang bertambah.
# Kondisi: Ketika Anda ingin membuat pergerakan grafis yang dinamis.