# Laboratorio 4

Para este laboratorio se pidió investigar el funcionamiento de los algoritmos _DES_, _3DES_ y _AES-256_ y escribir un código que utilice la librería pycrypto para encriptar un texto ingresado con estos algoritmos (y que se ingresen los respectivos inputs necesarios para cada uno).

> [!CAUTION]
> Este laboratorio fue desarrollado en un computador Macbook Air M1 con sistema operativo MacOS, puede que algunas instrucciones de este README no funcionen en otro SO.

### Cómo instalar librería

Para la instalación de la librería pycrypto se creó primero un entorno virtual de python3 (en caso de no tener tal librería ya instalada), de esta manera se evita corromper instalación de python y librerías de estas.
Creación de entorno:
```
python3 -m venv labcripto
```
Para ingresar al entorno es a través de:
```
source labcripto/bin/activate
```



La librería pycrypto es bastante antigua y fue reemplazada por pycryptodome, sin embargo, aquí están los pasos a seguir para poder instalar la librería y ejecutar un código con tal librería en MacOS, si ya tiene la librería instalada, saltese esta parte directamente hasta la ejecución del código.

Para ejecutar los siguientes pasos es necesario tener brew, a través de brew se instalará la herramienta _pyenv_, la cual permite instalar versiones antiguas de python:
```
brew install pyenv
```
Una vez instalado, descargamos una versión de python compatible con pycrypto:
```
pyenv install 3.9.18
```
Una vez se tiene instalada la librería, te mueves a la carpeta donde está el código o proyecto y ejecutas lo siguiente:
```
cd /tu/ruta
pyenv local 3.9.18
```
Ahora se crea un entorno virtual para instalar la librería, a través de lo siguiente se crea y accede a tal entorno:
```
python3 -m venv labcripto
source labcripto/bin/activate
```
Con esto podemos pasar a la instalación de la librería, la cual se realiza primero configurando algunas variables y luego instalar y compilar la librería:
```
# Configuración de variables
export LDFLAGS="-L$(brew --prefix gmp)/lib"
export CPPFLAGS="-I$(brew --prefix gmp)/include"
# Instalación
pip install --no-binary :all: pycrypto
```
Ahora podrémos ejecutar el código fácilmente, para salir del entorno virtual se debe ejecutar:
```
deactivate
```

### Ejecución de código

Para ejecutar el código solo se debe ingresar lo siguiente en la carpeta correspondiente:
```
python3 code.py
```

Para su correcto funcionamiento solo debe ejecutarse dentro del entorno mencionado anteriormente o si ya se tiene la librería instalada no hay problema.
Luego de la ejecución se deben ingresar los parámetros para cada tipo de encriptación, en caso de no cumplir con el largo de la _key_ esta se rellenará con bytes aleatorios o si se sobrepasa, se trunca a la cantidad necesaria, luego de ingresar todo, se ejecutarán los algoritmos entregando por pantalla la encriptación y luego el mismo texto desencriptado.