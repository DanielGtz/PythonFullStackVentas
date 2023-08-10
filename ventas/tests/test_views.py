from urllib import response
from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase, Client
from ventas.views import ProductosView
from ventas.models import Producto
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.models import Libro
from api.serializers import LibroSerializer
import os

class TestIntegracion(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="admin",password="admin")
        self.client.force_authenticate(user=self.user)

    def test_get_libros(self):
        Libro.objects.create(nombre_libro="Libro 1", autor="Autor 1", editorial="Editorial 1")
        Libro.objects.create(nombre_libro="Libro 2", autor="Autor 2", editorial="Editorial 2")

        response = self.client.get('/libros/')


        self.assertEqual(response.status_code, 200)

        libros = Libro.objects.filter(activo=True)
        serializer = LibroSerializer(libros, many=True)
        
        self.assertEqual(serializer.data, response.data)

    def test_post_libro(self):
        data = {
            "nombre_libro": "Libro 3", 
            "autor": "Autor 3",
            "editorial": "Editorial 3",
            "activo": False
        }
        
        #Pruebas internas del endpoint /libros/ POST
        response = self.client.post("/libros/", data, format="json")
        self.assertEqual(response.status_code, 201)
        data.pop("activo")
        self.assertEqual(response.data, data)

        #Prueba de integración con base de datos
        libro_creado = Libro.objects.get(nombre_libro="Libro 3")
        self.assertEqual(libro_creado.autor, data['autor'])
        self.assertEqual(libro_creado.editorial, data['editorial'])

        #Prueba de integración con /libros/ GET
        libro_nuevo = self.client.get('/libros/')
        self.assertNotIn(response.data, libro_nuevo.data)
        

class FunctionalTest(TestCase):
    def test_login_wrong_data(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/login")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)
        time.sleep(2)
        

        input_user = driver.find_element(By.ID,"id_usuario")
        input_password = driver.find_element(By.ID,"id_password")

        input_user.send_keys('a')
        time.sleep(2)
        input_password.send_keys('a')
        time.sleep(2)
        boton_iniciar_sesion = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[6]/button')))
        boton_iniciar_sesion.click()
        time.sleep(2)

        danger_alert = driver.find_element(By.XPATH,"/html/body/div/div/div/form/div[4]/small")
        time.sleep(2)

        self.assertEqual(danger_alert.text, "Usuario inválido")

        

    def test_open_local_project(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/")
        driver.maximize_window()
        driver.implicitly_wait(5)

        wait = WebDriverWait(driver, 10)
        time.sleep(2)
        nav_iniciar_sesion = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a')))
        nav_iniciar_sesion.click()

        input_user = driver.find_element(By.ID,"id_usuario")
        input_password = driver.find_element(By.ID,"id_password")

        input_user.send_keys('Daniel')
        time.sleep(2)
        input_password.send_keys('admin')
        time.sleep(2)
        boton_iniciar_sesion = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/form/div[6]/button')))
        boton_iniciar_sesion.click()
        
        nav_iniciar_sesion = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a')))
        nav_iniciar_sesion.click()

        nav_productos = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[2]/a')))
        nav_productos.click()
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        time.sleep(2)
        input_nombre = driver.find_element(By.ID,"id_nombre")
        input_descripcion = driver.find_element(By.ID,"id_descripcion")
        input_precio = driver.find_element(By.ID,"id_precio")
        input_archivo = driver.find_element(By.ID,"id_archivos")

        tbody = driver.find_element(By.XPATH,'//*[@id="tabla"]/tbody')
        filas = tbody.find_elements(By.TAG_NAME,'tr')
        print(len(filas))

        time.sleep(2)
        input_nombre.send_keys("Celular Samsung Galaxy")
        time.sleep(2)
        input_descripcion.send_keys("Más pantalla, más espacio para jugar. Disfruta cualquier detalle con su pantalla de 6.6” 90Hz. La batería te durará casi 2 días (dependiendo el uso del dispositivo) y tiene una recarga ultra rápida de 25W. Toma selfies 1.6 x más claras y captura cada detalle con su triple cámara de 50MP. Navega rápidamente con la red 5G y el poderoso procesador 4.0 x Single y 1.8 x Multi. Comparte lo que necesites con Quick Share y obtén")
        time.sleep(2)
        input_precio.send_keys("2799")
        time.sleep(2)
        input_archivo.send_keys(os.path.abspath('test.txt'))
        time.sleep(2)
        guardar_producto = wait.until(EC.presence_of_element_located((By.ID,"boton_guardar")))
        guardar_producto.click()
        time.sleep(2)
        tbody = driver.find_element(By.XPATH,'//*[@id="tabla"]/tbody')
        filas_despues = tbody.find_elements(By.TAG_NAME,'tr')
        print(len(filas_despues))
        time.sleep(6)
        self.assertNotEqual(len(filas), len(filas_despues))


def suma(a, b):
    return a + b



class TestUnitarioVentas(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre = "Microfono",
            descripcion = "Negro",
            precio=2000,
            activo=False
        )
        self.producto2 = Producto.objects.create(
            nombre = "Microfono 2",
            descripcion = "Negro",
            precio=2000
        )
        self.url_productos = reverse("productos")
        self.client = Client()


    def test_suma(self):
        self.assertEqual(suma(3, 9), 12)
        
    def test_productos_url(self):
        self.assertEqual(resolve(self.url_productos).func.view_class, ProductosView)
    
    def test_productos_creados(self):
        
        self.assertEqual(self.producto.nombre, "Microfono")

    def test_productos_get_status_code(self):
        response = self.client.get(self.url_productos)
        self.assertEqual(response.status_code, 200)

    def test_productos_get_context_products_inactivos(self):
        response = self.client.get(self.url_productos)
        self.assertNotIn(self.producto, response.context['productos'])

    def test_productos_get_context_products_activos(self):
        response = self.client.get(self.url_productos)
        self.assertIn(self.producto2, response.context['productos'])

