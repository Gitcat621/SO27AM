import hashlib
import subprocess

def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

while True:
    points = 0
    try:
        user_input = input("Jail Scape")
    except KeyboardInterrupt:
        print("\n¡Abandonas la fuga!")
        break

    if user_input.strip() == "ls":
        print("¿COMENZAR? (S/N)")
        try:
            response = input("Respuesta: ").strip().lower()
        except KeyboardInterrupt:
            print("\n¡BYE!")
            break
        
        if response == "s":
            try:
                print("1-¿Cuál es el comando para listar todos los archivos en el directorio actual en Linux?")
                response = input("Respuesta: ").strip().lower()
                if response == "ls":
                    print("¡Correcto!")
                    points += 1
                else:
                    print("Incorrecto :(.")
                
                print("2-¿Cómo puedes conocer tu ubicación actual en la estructura de directorios en Linux?")
                response = input("Respuesta: ").strip().lower()
                if response == "pwd":
                    print("¡Correcto!")
                    points += 1
                else:
                    print("Incorrecto")
            except KeyboardInterrupt:
                print("\nRetirada")
                break
        elif response == "n":
            print("¿Mas opciones?")
        else:
            print("Responde 'S' o 'N'.")
            
    elif user_input.strip() == "d3598d9fa1f79559db82ef3ecf536f28ef7264f5492953cd883f94a46b7a3989":
        print("¡Has logrado escapar!")
        break
    else:
        print("¡ERROR! No puedes escapar")

    print(f"Puntos acumulados: ({points}/2)\nContinúa hacia adelante")

    if points == 2:
        print("(2/2) Has completado tu escape exitosamente")
      
        key = "llave"
        encrypted_key = hashlib.sha256(key.encode()).hexdigest()
        print("Llave:", encrypted_key)