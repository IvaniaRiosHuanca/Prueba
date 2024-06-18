#2 Dado dos gráficos cualesquiera, convierta estás en una matriz sparce



# Función para cargar una imagen y convertirla en escala de grises
def imagen_a_EscalaGrises(ruta_img):
    image = cv2.imread(ruta_img, cv2.IMREAD_GRAYSCALE)
    return image

# Función para convertir una imagen en una matriz dispersa
def imagen_a_matrizSparce(imagen):
    # Convertir la imagen en una matriz dispersa en formato CSR
    matriz = csr_matrix(imagen)
    return matriz

# Rutas de las imágenes en Google Drive
imagen_ruta1 = '/content/drive/MyDrive/inf_lic_silva/leon1.jpg'
imagen_ruta2 = '/content/drive/MyDrive/inf_lic_silva/leon2.jpg'

# Cargar las imágenes en escala de grises
image1 = imagen_a_EscalaGrises(imagen_ruta1)
image2 = imagen_a_EscalaGrises(imagen_ruta2)

# Convertir las imágenes en matrices dispersas
matriz1 = imagen_a_matrizSparce(image1)
matriz2 = imagen_a_matrizSparce(image2)

# Mostrar información sobre las matrices dispersas
print("Matriz dispersa de la imagen 1:")
print(matriz1)

print("\nMatriz dispersa de la imagen 2:")
print(matriz2)

#  Mostrar las imágenes originales
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Imagen 1')
plt.imshow(image1, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Imagen 2')
plt.imshow(image2, cmap='gray')

plt.show()