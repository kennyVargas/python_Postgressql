import psycopg2 as pc
conexion = pc.connect(user="postgres",
                      password="123456",
                      host="127.0.0.1",
                      port="5432",
                      database="academico")
cursor = conexion.cursor()
ci= input("Ingrese ci de alumno:")
if ci.isdigit():
    print(ci.isdigit())
else:
    ci="0"


sql = "select a.* from asignatura a, inscripcion i where a.id=i.idasignatura and i.idalumno="+ci
sqlA="select * from alumnos where id="+ci

cursor.execute(sqlA)
regNombre=cursor.fetchall()

if cursor.rowcount != 0:
    for registro in regNombre:
        print("Nombre Alumno: ",registro[1]+" "+registro[2])
        
cursor.execute(sql)
registros = cursor.fetchall()

if cursor.rowcount != 0:
    for registro in registros:
        print("--------------------Materias inscritas---------- ")
        print("id:",registro[0])
        print("nombre:",registro[1])
else:
    print("NO SE REGISTRON NIGUNA MATERIA0")
cursor.close()
conexion.close()
