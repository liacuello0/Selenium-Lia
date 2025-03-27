# Selenium Tests - SauceDemo

Este proyecto contiene pruebas automatizadas en **Python** utilizando **Selenium WebDriver** para el sitio web [SauceDemo](https://www.saucedemo.com/).  
Las pruebas incluyen inicio de sesión, navegación, selección de productos y proceso de compra.

## 🚀 Requisitos

Antes de ejecutar las pruebas, asegúrate de tener lo siguiente:

- **Python 3.x** instalado ([Descargar](https://www.python.org/downloads/))
- **Google Chrome** instalado
- **Chromedriver** compatible con tu versión de Chrome ([Descargar aquí](https://chromedriver.chromium.org/downloads))
- **Instalar dependencias** con:

  ```bash
  pip install selenium
  ```

## 📌 Configuración y Ejecución

1. Clona este repositorio:

   ```bash
   git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git
   cd NOMBRE_DEL_REPOSITORIO
   ```

2. Asegúrate de que `chromedriver.exe` está en el directorio del proyecto o en el **PATH** del sistema.

3. Ejecuta el script:

   ```bash
   python test_saucedemo.py
   ```

## 📝 Escenarios de Prueba

✔ **Inicio de sesión exitoso**  
✔ **Navegación a la página de productos**  
✔ **Selección de un producto**  
✔ **Añadir producto al carrito**  
✔ **Realizar checkout exitosamente** 
