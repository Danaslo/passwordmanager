[Ir a la sección en español](#gestor-de-contraseñas)


# **Password Manager**

**A secure and easy-to-use password manager built with Python, SQLite, and AES encryption.**

This project allows you to securely manage your accounts and passwords by storing them in an encrypted local database. With a simple graphical user interface created using `Tkinter`, you can add, delete, and view accounts without compromising your security.

---

## **Features**

- **Account Management:** Add, delete, and view your accounts and passwords.
- **Secure Encryption:** Passwords are stored encrypted using the **AES (Fernet)** algorithm.
- **Graphical Interface:** Easy-to-use GUI created with `Tkinter` for seamless user interaction.
- **Local SQLite Database:** Stores passwords in an SQLite database that works across multiple platforms.

---

## **Requirements**

Make sure you have the following installed:

- **Python 3.x**
- **Required Libraries:**
  - `cryptography`
  - `tkinter` (typically included in Python)
  - `sqlite3` (also included with Python)

Install the dependencies with:

```bash
pip install cryptography
```

## **Project structure**

```
Password_Manager/
│
├── db/
│   ├── database.py           # Database Manager
│   └── models/
│       └── account.py        # Account model
│
├── gui/
│   └── interface.py          # Graphical interface with Tkinter
│
├── Security/
│   └── Encryptor.py          # Class for password 
│   └── key_manager.py        # Key management functions
│
├── main.py                   # Main entry point of the program
├── README.md                 # This file
└── clave.key                 # Encryption key file generated with first execution
```

## **How to Use**

First you need to clone this repository:

```bash
git clone https://github.com/danaslo/Password-Manager.git
cd Password-Manager
```   
Now that you have the repository cloned and your prompt inside the correct folder, you can start the application by just writing this command:

```bash
python main.py
```

And the application should start without errors.


## **How it works**

- **Password Encryption:** The passwords are stored encrypted using the AES (Fernet) algorithm to ensure that they are secure in the database.

- **Key Management:** The encryption key is generated and saved in a file called clave.key. If this file doesn't exist, it will be automatically created on the first run of the application.

- **SQLite Database:** The project uses SQLite to store accounts and encrypted passwords. The database is set to create the necessary table if it doesn't exist.

## **License**

This project is under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) License.

You can copy, redistribute and change the code as you see fit, as long as it remains free and attribution is given.

---


# **Gestor de contraseñas**

**Una forma segura y fácil de gestionar contraseñas construída con Python, SQLite y con encriptado AES (Estándar de Encriptación Avanzada)**

Este proyecto te permite gestionar de forma segura tus cuentas y contraseñas guardándolas en una base de datos encriptada. Con una interfaz gráfica simple creada usando `Tkinter`, puedes añadir, borrar y ver cuentas sin comprometer tu seguridad.

---

## **Características**

- **Gestión de cuentas:** Agrega, borra y visualiza tus cuentas.
- **Encriptado seguro:** Las contraseñas se almacenan encriptadas utilizando el argoritmo de encriptación **AES (Fernet)**.
- **Interfaz gráfica:** Fácil de usar gracias a `Tkinter` para comodidad del usuario.
- **Base de datos Local SQLite:** Contraseñas guardadas con SQLite para una mayor compatibilidad.

---

## **Requisitos**

Asegúrate de tener instalado: 

- **Python 3.x**
- **Librerías requeridas:**
  - `cryptography`
  - `tkinter` (Suele incluírse en Python)
  - `sqlite3` (También incluída en Python)

Instala las dependencias con:

```bash
pip install cryptography
```

## **Estructura del proyecto**

```
Password_Manager/
│
├── db/
│   ├── database.py           # Gestor de base de datos
│   └── models/
│       └── account.py        # Modelo de cuenta
│
├── gui/
│   └── interface.py          # Interfaz gráfica con Tkinter
│
├── Security/
│   └── Encryptor.py          # Clase de encriptado y desencriptado de contraseñas
│   └── key_manager.py        # Gestión de la llave de encriptado
│
├── main.py                   # Punto de entrada del programa
├── README.md                 # Éste archivo
└── clave.key                 # Clave de encriptado generada con la primera ejecución
```

## **Como usar**

Primero necesitas clonar éste repositorio:

```bash
git clone https://github.com/danaslo/Password-Manager.git
cd Password-Manager
```   
Una vez clonado el repositorio basta con ejecutar el programa utilizando el siguiente comando:

```bash
python main.py
```

Y la aplicación debería ejecutarse sin errores.


## **Cómo funciona**

- **Encriptación:** Las cotnraseñas se guardan utilizando (Fernet) para asegurarse de que son seguras en la base de datos.

- **Gestión de llaves:** La clave de encriptado se guarda en un archivo llamado clave.key. Si no existe se genera automáticamente con la primera ejecución del programa.

- **BD SQLite:** El programa utiliza SQLite para guardar cuentas y contraseñas encriptadas. La base de datos está preparada para crearse con la primera ejecución si no existe.

## **Licencia**

Éste proyecto está recogido bajo la licencia Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).

Puedes copiar, redistribuir y cambiar el código como creas conveniente, siempre que permanezca libre y se de atribución al creador.

