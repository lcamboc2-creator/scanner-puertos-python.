# Desarrollo de un Escáner de Puertos de Red Utilizando Python

## Descripción

Este proyecto consiste en el desarrollo de un escáner de puertos de red utilizando el lenguaje de programación Python y la biblioteca nativa `socket`. La herramienta permite realizar conexiones TCP sobre una dirección IP y un intervalo de puertos definido por el usuario, con el propósito de identificar los puertos que se encuentran abiertos.

El escaneo de puertos constituye una etapa de reconocimiento dentro de una auditoría de seguridad o proceso de pruebas de penetración. Esta implementación permite comprender de manera práctica el funcionamiento de las conexiones de red bajo el modelo TCP/IP, mediante el uso de sockets, tiempos de espera y manejo de excepciones. fileciteturn0file1L25-L37

## Objetivo

Crear un escáner de puertos de red funcional en Python mediante el módulo `socket`, orientado a la identificación de la disponibilidad de servicios y al reconocimiento de puertos abiertos en una IP objetivo. fileciteturn0file1L39-L43

## Herramientas utilizadas

- Visual Studio Code
- GitHub
- Biblioteca `socket` de Python fileciteturn0file1L53-L56

## Requisitos

- Python 3.6 o superior.
- Visual Studio Code.
- No requiere instalar librerías externas, ya que utiliza el módulo nativo `socket`. fileciteturn0file1L102-L105

## Archivos del proyecto

```text
scanner-puertos-python/
├── scanner_puertos.py
├── README.md
└── MANUAL_USO.md
```

## Ejecución

El programa se ejecuta desde la terminal mediante Python:

```bash
python scanner_puertos.py
```

Para conocer el procedimiento completo de ejecución e ingreso de los parámetros, consulte `MANUAL_USO.md`.

## Uso autorizado

El escaneo debe realizarse dentro de un marco ético y controlado, únicamente sobre equipos propios, máquinas virtuales o laboratorios autorizados. El documento del proyecto señala la importancia de evitar actividades de reconocimiento no autorizado. fileciteturn0file1L49-L52
