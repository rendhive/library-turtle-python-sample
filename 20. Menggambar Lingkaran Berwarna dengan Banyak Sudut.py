import turtle

def draw_multi_colored_circle():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle.speed(0)
    for color in colors:
        turtle.color(color)
        turtle.circle(100)
        turtle.right(360 / len(colors))  # Rotasi untuk mengubah sudut
    turtle.done()

draw_multi_colored_circle()
# Fungsi: Menggambar lingkaran berwarna yang berputar dengan banyak sudut.
# Kondisi: Ketika Anda ingin membuat pola warna yang menarik.