from .deteccacao import deteccacao
from .graph import mostrar_todos_os_graficos
from .main_page import main_page

page = {
    "Desempenho do Modelo": main_page,
    "Classificador de Chapeu": deteccacao,
    "Grafico": mostrar_todos_os_graficos,
}
