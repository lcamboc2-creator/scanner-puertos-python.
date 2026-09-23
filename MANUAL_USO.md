# MANUAL DE USO

## Escáner de Puertos TCP Básico

El escáner de puertos permite auditar la superficie de exposición de un host o red que forma parte del objeto de auditoría, ejecutando conexiones TCP sobre una dirección y un intervalo de puertos definidos por el usuario. Su objetivo es apoyar la evaluación de seguridad, la auditoría de red y el reconocimiento de activos. fileciteturn0file1L93-L101

## Requisitos

- Python 3.6 o superior.
- Visual Studio Code.
- No requiere librerías adicionales, debido a que utiliza el módulo nativo `socket`. fileciteturn0file1L102-L105

## Guía de Uso

### Paso 1: Ejecutar la aplicación

Abrir la terminal de Visual Studio Code y ejecutar el programa con el comando:

```bash
python scanner_puertos.py
```

### Paso 2: Ingresar los parámetros requeridos

El programa solicita de manera secuencial tres datos:

1. Dirección IP a escanear.
2. Puerto de inicio.
3. Puerto de fin.

Estos parámetros permiten establecer el objetivo y el rango de puertos que será analizado. fileciteturn0file1L107-L113

### Paso 3: Visualización de resultados

Después de ingresar los datos requeridos, el programa inicia la prueba e informa los resultados obtenidos. Los puertos identificados como abiertos se muestran durante la ejecución. fileciteturn0file1L114-L116

### Paso 4: Informe final

Al finalizar el análisis, el programa muestra un resumen con los resultados obtenidos. fileciteturn0file1L117-L119

## Ejemplo de prueba documentada

En la prueba realizada sobre el equipo propio se utilizó la dirección IP `127.0.0.1` (localhost) y el rango de puertos `1 - 1024`. Se identificaron los puertos abiertos `135`, asociado a RPC, y `445`, asociado a SMB. fileciteturn0file1L121-L134

### Resultados registrados

| Elemento | Resultado |
|---|---|
| IP utilizada | 127.0.0.1 (localhost - equipo propio) |
| Rango de puertos | 1 - 1024 |
| Puertos abiertos | 135 (RPC), 445 (SMB) |
| Tiempo total de escaneo | 0:06:54 |
| Observaciones | El equipo local presentó dos puertos abiertos correspondientes a servicios propios del sistema operativo Windows. No se identificaron puertos adicionales en el rango analizado. |

Los resultados anteriores corresponden a la prueba registrada en el informe del proyecto. fileciteturn0file1L138-L154

## Consideración de seguridad

Las pruebas de escaneo deben realizarse únicamente dentro de un entorno propio o autorizado. El proyecto establece como parte de sus objetivos fomentar la práctica de auditoría de redes dentro de un marco ético y controlado. fileciteturn0file1L49-L52
