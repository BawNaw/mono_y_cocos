from sympy import symbols, Eq, solve

def distribucion_cocos(x):
    distribucion = []  # Lista para guardar la distribución de cocos
    cocos = x
    for i in range(5):  # Cinco personas toman cocos
        if (cocos - 1) % 5 == 0:
            tomados = (cocos - 1) // 5
            cocos = cocos - 1 - tomados
            distribucion.append(tomados)  # Guardar cuántos cocos toma cada persona
        else:
            return (False, [])
    if cocos % 5 == 0:
        distribucion.append(cocos)  # Guardar cuántos cocos quedan para el mono
        return (True, distribucion)
    else:
        return (False, [])

# Encontrar la solución y la distribución
x = 1
solucion_valida, distribucion = distribucion_cocos(x)
while not solucion_valida:
    x += 1
    solucion_valida, distribucion = distribucion_cocos(x)

print(f"La menor cantidad de cocos que satisface el problema es: {x} \n")
print("Distribución de cocos tomados por cada persona y para el mono al final:")

# Imprimir cuántos cocos toma cada persona
for i, cocos in enumerate(distribucion[:-1], start=1):
    print(f"Persona {i} tomó inicialmente: {cocos} cocos")

# Corrección en la impresión para clarificar la cantidad de cocos para repartir al final
print("\n")
print(f"Cocos para repartir entre 5 al final: {distribucion[-1]} \n")

# Calcular y agregar 204 cocos a cada persona
distribucion_final = [cocos + 204 for cocos in distribucion[:-1]]
print("Distribución final de cocos para cada persona:")
for i, cocos in enumerate(distribucion_final, start=1):
    print(f"Persona {i} obtiene al final: {cocos} cocos")

# Imprimir cuántos cocos quedan para el mono
print(f"Cocos que le tocan al mono al final: 5")
