productos = [
    ("Audífonos inalámbricos", 150000),
    ("Teclado mecánico", 280000),
    ("Mouse gamer", 90000),
    ("Monitor 24 pulgadas", 650000),
]

descuentos_a_aplicar = [
    ("Audífonos inalámbricos", 150000, 20),   # 20% de descuento
    ("Teclado mecánico", 280000, 15),
    ("Mouse gamer", 90000, 50),
    ("Monitor 24 pulgadas", 650000, 10),
]

porcentajes_para_validar = [
    50,     # válido
    100,    # válido (límite superior)
    0,      # válido (límite inferior)
    150,    # inválido — mayor a 100
    -10,    # inválido — negativo
]