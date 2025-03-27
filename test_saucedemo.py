from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del WebDriver
service = Service("chromedriver.exe")  # Asegúrate de que el driver está en tu PATH
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# URL del sitio web de prueba
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

try:
    # Escenario 1: Prueba de Inicio de Sesión
    print("Ejecutando prueba de inicio de sesión...")
    usuario = driver.find_element(By.ID, "user-name")
    contraseña = driver.find_element(By.ID, "password")
    boton_login = driver.find_element(By.ID, "login-button")
    
    usuario.send_keys("standard_user")
    contraseña.send_keys("secret_sauce")
    boton_login.click()
    
    # Espera hasta que el usuario sea redirigido
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    print("Inicio de sesión exitoso.")
    
    # Escenario 2: Navegación y selección de producto
    print("Ejecutando prueba de navegación y selección de producto...")
    producto = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    producto.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_name")))
    print("Navegación y selección de producto exitosa.")
    
    # Escenario 3: Añadir producto al carrito y realizar checkout
    print("Ejecutando prueba de compra...")
    boton_add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    boton_add_cart.click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    carrito.click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
    boton_checkout = driver.find_element(By.ID, "checkout")
    boton_checkout.click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name")))
    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Pérez")
    driver.find_element(By.ID, "postal-code").send_keys("10101")
    driver.find_element(By.ID, "continue").click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "finish")))
    driver.find_element(By.ID, "finish").click()
    print("Compra realizada exitosamente.")
    
except Exception as e:
    print(f"Error en la prueba: {e}")

finally:
    time.sleep(3)
    driver.quit()
    print("Pruebas finalizadas.")
