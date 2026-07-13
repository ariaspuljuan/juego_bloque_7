<<<<<<< HEAD
# Demo de juego con Pygame

Este proyecto es un demo simple de un juego en Python usando `pygame`.

## Estructura

- `main.py`: archivo principal del juego.
- `images/`: carpeta donde puedes poner las imágenes del juego.
- `requirements.txt`: dependencias del proyecto.
- `venv/`: entorno virtual (no debe subirse al repositorio).

## Buenas prácticas

No es buena práctica subir el entorno virtual al repositorio. El directorio `venv/` puede ser grande, contiene archivos específicos del sistema y se puede regenerar fácilmente.

Por eso se usa `.gitignore` para excluir `venv/` y otros archivos temporales.

## Instalación

1. Clona el repositorio:

```powershell
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>
```

2. Crea el entorno virtual:

```powershell
python -m venv venv
```

3. Activa el entorno virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

4. Instala dependencias:

```powershell
pip install -r requirements.txt
```

5. Ejecuta el juego:

```powershell
python main.py
```

## Subir a GitHub

Si ya creaste el repositorio en GitHub, usa estos comandos:

```powershell
git init
git add .
git commit -m "Inicializa demo de juego con Pygame"
git remote add origin https://github.com/<tu-usuario>/<tu-repo>.git
git push -u origin main
```

Cambia `main` por la rama principal que uses en tu repositorio si es necesario.

## Nota

El archivo `requirements.txt` usa `pygame-ce`, que instala correctamente en Windows con Python 3.14.

