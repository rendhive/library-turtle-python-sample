import turtle

def go_to_coordinates(x, y):
    turtle.penup()  # Mengangkat pena untuk tidak menggambar
    turtle.goto(x, y)  # Pergi ke koordinat yang ditentukan
    turtle.pendown()
    turtle.write(f"({x}, {y})")  # Menulis koordinat
    turtle.done()

go_to_coordinates(50, 50)
# Fungsi: Menggerakan turtle ke koordinat tertentu dan mencetak posisi.
# Kondisi: Ketika Anda ingin menempatkan turtle di lokasi spesifik.