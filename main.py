from lib import cuadrado, triangulo, rectangulo, circunferencia
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado = 4
print(f"El área de un {cuadrado.get_identificador()} de lado {lado} es {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")
base_triangulo = 4
altura_triangulo = 2
lado_a=4
lado_b=8
lado_c=8
print(triangulo.get_identificador())
print(f"El área de un {triangulo.get_identificador()} de base {base_triangulo} y altura {altura_triangulo} es {triangulo.get_area(base_triangulo, altura_triangulo)} y el perímetro es {triangulo.get_perimetro(lado_a, lado_b, lado_c)}")
base_rectangulo = 4
altura_rectangulo = 2
print(rectangulo.get_identificador())
print(f"El área de un {rectangulo.get_identificador()} de base {base_rectangulo} y altura {altura_rectangulo} es {rectangulo.get_area(base_rectangulo, altura_rectangulo)} y el perímetro es {rectangulo.get_perimetro(base_rectangulo, altura_rectangulo)}")
radio=5
print(f"El área de la circunferencia es {circunferencia.get_area(radio)}")