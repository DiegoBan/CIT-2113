# Laboratorio 1

En esta carpeta se encuentra el desarrollo realizado para el laboratorio 1, el cual cuenta con 3 actividades distintas (pero interconectadas entre sí), lo siguiente descrito en este README será referente a los códigos, lo necesario para ejecutarse y cómo hacerlo, el resto de información respecto a cualquier análisis se puede encontrar en el informe realizado.
> [!WARNING]
> Todos los códigos y ejecuciones fueron realizados en una computadora Macbook Air M1 con sistema operativo macOS, en caso de estar en otro OS, los reslutados podrían varíar.

## Actividad 1: Algoritmo de Cifrado

Se pide un algoritmo que reciba un texto o String y un número, con estos realizar un cifrado cesar, realizando el corrimiento e imprimiendo en pantalla. Este código es [cesar.py](./cesar.py), la librería _argparse_ utilizada, viene en la instalación base de _python3_. Este código se ejecuta de la siguiente manera:

```
python3 cesar.py "criptografia y seguridad en redes" 9
```
En donde:
- "criptografia y seguridad en redes" es el String o texto a encriptar.
* 9 es el corrimiento a aplicar.
+ Salida correspondiente a ejemplo: _larycxpajorj h bnpdarmjm nw anmnb_

## Actividad 2: Modo Stealth

Se pide código en _python3_ que envíe carácteres de encriptado anterior en variados paquetes ICMP, enviando 1 byte del mensaje a la vez y completando el resto en de los 47 con lo que comúnmente se envía en un paquete de este tipo, con el objetivo de pasar desapercibido ante análisis de red y no levantar sospechas.

Este código se realiza en [pingv4.py](./pingv4.py), para ejecutarlo se debe instalar primero la librería _scapy_ para python a través de:
```
pip3 install scapy
```
Para ejecutar el código, se realiza de la siguiente manera:
```
sudo python3 pingv4.py "larycxpajorj h bnpdarmjm nw anmnb"
```

__Explicación de código:__ Este código envía en cada paquete ICMP un byte del mensaje encriptado, el resto del mensaje en su sección de _Data_ se completa con bytes que típicamente se encuentran en este tipo de mensajes, de esta manera se completan los 48 bytes de _Data_, por otro lado estos mensajes se envían a la IP _8.8.8.8_, la cual es el DNS público de google útil para pruebas.