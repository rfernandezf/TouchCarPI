# TouchCarPI
## by Rafael Fernández Flores (@Plata17).

![alt text](http://i.imgur.com/gz1Aroh.png)
![alt text](http://i.imgur.com/2SY80AY.png)

## Description

This is my end of degree project. It's a touchscreen based system with autoradio functions using a Raspberry Pi, focused on be implemented into real cars.

## Installation instructions

All has been tested over Raspbian distribution. Could change between distributions.

First of all we have to satisfy the dependencies:

```
sudo apt-get install python3-pyqt5

sudo apt-get install python3-lxml
```

Then, we should enter into the directory of the project and execute it:

```
python3 __main__py
```

If all went well, you should be watching the main menu of the app.

## Other stuff

To use the radio you need the SI4703 IC connected to the Raspberry's GPIO ports.

There's a diagram of the connections:

![alt text](http://i.imgur.com/2uApq7e.png)

The music is read from the directory "/home/user/Music".

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Descripción

Mi proyecto final de grado (TFG). Se basa en un sistema táctil con función de autoradio sobre Raspberry Pi, enfocado a implantarse en vehículos reales.

## Instrucciones de instalación

Todo ha sido probado sobre la distribución Raspbian. Podría cambiar entre distribuciones.

Primero tenemos que satisfacer las dependencias:

```
sudo apt-get install python3-pyqt5

sudo apt-get install python3-lxml
```

Una vez instaladas, vamos al directorio donde hayamos descomprimido el proyecto y ejecutamos:

```
python3 __main__py
```

Si todo ha ido bien, deberíamos de estar viendo el menú principal de la aplicación.

## Otros apuntes

Para la función de radio hay que disponer del módulo SI4703, y conectarlo a los GPIO de la Raspberry Pi.

Aquí se puede ver un esquema de su instalación:

![alt text](http://i.imgur.com/2uApq7e.png)

La música es leída desde el directorio "/home/user/Music".

