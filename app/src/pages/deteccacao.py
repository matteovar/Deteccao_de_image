import os
import gdown
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


def deteccacao():
    # Caminho para salvar o modelo localmente
    model_path = "meu_modelo.h5"

    # Baixar o modelo do Google Drive se ainda não estiver salvo
    with st.spinner("Baixando o modelo... Isso pode demorar um pouco."):
        if not os.path.exists(model_path):
            url = "https://drive.google.com/uc?id=11SDM_KTSeNfTZxHoWz-lWsS1AH2F3xON"
            gdown.download(url, model_path, quiet=False, use_cookies=False)

            # Verifica se o arquivo baixado parece válido
            if os.path.getsize(model_path) < 10000:
                st.error(
                    "❌ Erro: o arquivo do modelo não foi baixado corretamente. Verifique o link do Google Drive e as permissões de compartilhamento."
                )
                st.stop()

    # Carregar o modelo
    model = load_model(model_path)

    # Função para pré-processar a imagem
    def carregar_imagem(caminho_img):
        img = image.load_img(caminho_img, target_size=(128, 128))
        img_array = image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    # Função de predição
    def predizer(imagem):
        img_array = carregar_imagem(imagem)
        pred = model.predict(img_array)[0][0]
        print(pred)
        return 1 - pred, pred  # , com_chapeu, sem_chapeu

    # Título do app
    st.title("🎩 Classificador de Chapéu")

    # Upload da imagem
    uploaded_file = st.file_uploader(
        "Faça upload de uma imagem", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Imagem enviada", width=300)

        # Predição
        with st.spinner("Realizando a predição..."):
            prob_com_chapeu, prob_sem_chapeu = predizer(uploaded_file)

        # Gráfico
        categorias = ["Com chapéu", "Sem chapéu"]
        probabilidades = [prob_com_chapeu, prob_sem_chapeu]
        cores = ["#4CAF50", "#F44336"]

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        img_plot = image.load_img(uploaded_file, target_size=(128, 128))
        axs[0].imshow(img_plot)
        axs[0].axis("off")
        axs[0].set_title("Imagem")

        axs[1].bar(categorias, probabilidades, color=cores)
        axs[1].set_ylim(0, 1)
        axs[1].set_ylabel("Probabilidade")
        axs[1].set_title("Predição")
        for i, v in enumerate(probabilidades):
            axs[1].text(i, v + 0.02, f"{v*100:.1f}%", ha="center")

        st.pyplot(fig)


deteccacao()
