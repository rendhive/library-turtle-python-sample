import turtle

def draw_polygon(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)  # Menghitung sudut untuk poligon
    turtle.done()

draw_polygon(6, 70)  # Menggambar heksagon
# Fungsi: Menggambar poligon berdasarkan jumlah sisi dan panjang.
# Kondisi: Ketika Anda ingin menggambar bentuk geometris lainnya.