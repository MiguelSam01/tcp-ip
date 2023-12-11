import socket

def start_client():
    # Pedir al usuario la dirección IP y el puerto
    host = input('Ingrese la dirección IP del servidor: ')

    # Manejar la entrada del puerto de manera segura
    while True:
        port_str = input('Ingrese el puerto del servidor: ')
        try:
            port = int(port_str)
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido papípra el puerto.")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f'Conectado al servidor en {host}:{port}')

        while True:
            # Obtener la entrada del usuario en formato hexadecimal
            hex_data = input('Ingrese datos hexadecimales (o "exit" para salir): ')

            if hex_data.lower() == 'exit':
                break

            # Enviar datos al servidor en formato hexadecimal
            client_socket.sendall(bytes.fromhex(hex_data))

    except ConnectionRefusedError:
        print(f'Error: No se puede conectar al servidor en {host}:{port}')
    finally:
        client_socket.close()
        print('Conexión cerrada')

if __name__ == "__main__":
    start_client()
