from pathlib import Path

# Carpeta donde están las imágenes
carpeta = Path("datos/raw")

# Extensiones de imagen permitidas
extensiones = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".bmp"
}

# Buscar imágenes
imagenes = [
    archivo for archivo in carpeta.iterdir()
    if archivo.is_file()
    and archivo.suffix.lower() in extensiones
]

cantidad = len(imagenes)
minimo = 100
faltantes = max(0, minimo - cantidad)

print("=" * 50)
print("       REVISIÓN DEL DATASET")
print("=" * 50)

print(f"Carpeta: {carpeta}")
print(f"Imágenes encontradas: {cantidad}")
print(f"Mínimo requerido: {minimo}")

if faltantes > 0:
    print(f"Faltan: {faltantes} imágenes")
else:
    print("¡Ya tienes las 100 imágenes requeridas!")

print("=" * 50)