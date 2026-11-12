
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def get_app_info():
    return "Nueva funcionalidad de consulta de datos"

