from .deteccacao import deteccacao
from .graph import plot_confusion_matrix
from .main_page import main_page

page = {
    "Desempenho do Modelo": main_page,
    "Classificador de Chapeu": deteccacao,
    "Grafico": plot_confusion_matrix,
}
