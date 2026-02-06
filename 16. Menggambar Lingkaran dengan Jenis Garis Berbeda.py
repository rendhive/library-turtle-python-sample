import turtle

def draw_dashed_circle():
    for _ in range(36):  # Mengubah untuk jalur putus-putus
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
    turtle.done()

draw_dashed_circle()
# Fungsi: Menggambar lingkaran putus-putus menggunakan turtle.
# Kondisi: Ketika Anda ingin menambahkan efek visual khusus untuk lingkaran.