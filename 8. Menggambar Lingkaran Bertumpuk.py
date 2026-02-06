import turtle

def draw_concentric_circles():
    for i in range(5):
        turtle.circle(50 + i * 20)  # Lingkaran bertumpuk dengan jarak bertambah
        turtle.penup()
        turtle.sety(turtle.ycor() - 20)  # Menurunkan posisi untuk lingkaran berikutnya
        turtle.pendown()
    turtle.done()

draw_concentric_circles()
# Fungsi: Menggambar lingkaran bertumpuk.
# Kondisi: Ketika Anda ingin membuat pola lingkaran yang terpusat.