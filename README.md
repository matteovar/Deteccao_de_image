# Detecção de Chapéu com Redes Neurais e Streamlit

Este projeto tem como objetivo realizar a **classificação de imagens** de indivíduos **com e sem chapéu** por meio de uma **rede neural convolucional (CNN)** implementada com as bibliotecas TensorFlow e Keras. O modelo foi integrado a uma interface web interativa utilizando o **framework Streamlit**, permitindo a análise de desempenho e a predição de novas imagens.

## Streamlit

Acesse a aplicação Streamlit desenvolvida no seguinte hyperlink: <a href="https://deteccaodechapeu.streamlit.app">website</a>

## Vídeo

Acesse o vídeo desenvolvido no seguinte hyperlink: <a href="https://youtu.be/bKGqzj-inE8">vídeo</a>

## Funcionalidades

-  Upload de imagens para predição em tempo real.
-  Visualização de métricas de desempenho do modelo:
    - Acurácia, Precisão, Recall, F1-Score
    - Matriz de confusão
    - Distribuição de erro (Loss)
    - Acurácia por classe
    -  Gráficos interativos com Plotly.
-  Organização modular com scripts separados para dados, lógica, visualização e app.

---

##  Tecnologias Utilizadas

- [Python 3.11](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
- [Pandas](https://pandas.pydata.org/)

---

##  Como Executar o Projeto

### 1. Intale Python 3.11

[Python 3.11](https://www.python.org/downloads/release/python-3110/)


### 2. Clone o repositório
```
git clone https://github.com/seu-usuario/deteccao-chapeu.git
cd deteccao-chapeu
```
### 3. Crie um ambiente virtual
```
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate     
```

### 4. Instale as dependencias

```
pip install -r requirements.txt

```

### 5. Execute o streamlit

1 - Abra o arquivo ```app.py``` no VS Code.

2 - Clique na aba "**Run and Debug**" (ícone do inseto na sidebar esquerda).

3 - Selecione a opção de rodar o arquivo ```app.py```.

4 - Clique em "**Start Debugging**" (F5) para iniciar o app.

5- O Streamlit abrirá automaticamente no navegador ou estará disponível em:

```
http://localhost:8501
```

## Dataset
- O dataset foi criado manualmente com a ferramenta Imageye, contendo:

    - 264 imagens com chapéu

    - 257 imagens sem chapéu

- As imagens foram redimensionadas para 128x128 pixels e normalizadas para valores entre 0 e 1.

## Autores
- Diogo L. Hatz – diogolourenzonhatz2@gmail.com

- Matteo D. Varnier – matvarnier@gmail.com

## Referências 

- Deep Learning Book – Capítulo de CNNs

- Chollet, F. Deep Learning with Python

- Treuille, A. et al. Streamlit Docs

- Rawat, W. & Wang, Z. (2017). Neural Computation, 29(9), 2352–2449.
