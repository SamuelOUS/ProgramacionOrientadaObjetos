class Student:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def add_grade(self, grade):
        self.notas.append(grade)

    def average_grade(self):
        if len(self.notas) == 0:
            return None
        else:
            return sum(self.notas) / len(self.notas)


informacion_estudiantes = [

    {"Nombre": "Samuel", "edad": 18, "notas": [5.0, 5.0, 5.0]},
    {"Nombre": "Anna", "edad": 18, "notas": [3.5, 5.0, 4.0]},
    {"Nombre": "Cristo", "edad": 18, "notas": [3.5, 2.5, 4.5]},
    {"Nombre": "Camilo", "edad": 20, "notas": [3.0, 3.0, 3.0]}

]

# print(informacion_estudiantes[0]["Nombre"])
# print(informacion_estudiantes[1]["Nombre"])
# print(informacion_estudiantes[2]["Nombre"])
# print(informacion_estudiantes[3]["Nombre"])

estudiantes = [Student(informacion_estudiantes[i]["Nombre"], informacion_estudiantes[i]["edad"],
                       informacion_estudiantes[i]["notas"]) for i in range(len(informacion_estudiantes))]

promedio = 4.0
estudiantes_sobre_promedio = [estudiantes[i] for i in range(len(estudiantes)) if
                              estudiantes[i].average_grade() >= promedio]

# print(estudiantes_sobre_promedio[0].nombre)
# print(estudiantes_sobre_promedio[1].nombre)
# print(len(estudiantes_sobre_promedio))


diccionario_estudiantes = {estudiantes_sobre_promedio[i].nombre: estudiantes_sobre_promedio[i] for i in
                           range(len(estudiantes_sobre_promedio))}

print(estudiantes_sobre_promedio[0])
print(diccionario_estudiantes["Samuel"].edad)




