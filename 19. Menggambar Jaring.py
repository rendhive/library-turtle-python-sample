import turtle

def draw_grid():
    for i in range(-200, 201, 20):  # Menggambar baris horizontal
        turtle.penup()
        turtle.goto(-200, i)
        turtle.pendown()
        turtle.goto(200, i)

    turtle.setheading(180)  # Ubah arah untuk menggambar kolom
    for i in range(-200, 201, 20):
        turtle.penup()
        turtle.goto(i, 200)
        turtle.pendown()
        turtle.goto(i, -200)

    turtle.done()

draw_grid()
# Fungsi: Menggambar jaring dengan garis horizontal dan vertikal.
# Kondisi: Ketika Anda ingin membuat struktur koordinat.