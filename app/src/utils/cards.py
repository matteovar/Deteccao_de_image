import streamlit as st


def create_title(title: str):
    st.html(
        f"""
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Inter:wght@700&display=swap');
          .title {{
            font-family: 'Inter', sans-serif;
            font-size: 3.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 8%;
            background: linear-gradient(90deg, #00AFFF, #005F99);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 1.2px;
            user-select: none;
          }}
          @media (max-width: 480px) {{
            .title {{
              font-size: 2.5rem;
              margin-bottom: 15%;
            }}
          }}
        </style>
        <div class="title">{title}</div>
        """
    )


def create_cards(title: str, value: str):
    st.html(
        f"""
    
    <style>
    .card{{
        position: relative;
        background: linear-gradient(145deg, #181818, #101010);
        border-radius: 12px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.7);
        padding: 20px 25px 20px 25px;
        width: 280px;
        min-height: 120px;
        margin-bottom: 50px;
        cursor: default;
        transition: box-shadow 0.3s ease, transform 0.3s ease;
    }}
    .card:hover {{
        box-shadow: 0 12px 25px rgba(0,150,255,0.6);
        transform: translateY(-4px);
    }}
    .card::before {{       
        content: '';
        position: absolute;
        top: 20px;
        left: 0;
        height: calc(100% - 40px);
        width: 6px;
        background: #0096FF;
        border-radius: 6px 0 0 6px;
    }}
    .card-title {{
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 6px;
        color: #89CFF0;
        user-select: none;
    }}
    .card-value {{
        font-size: 36px;
        font-weight: 700;
        color: #E0E0E0;
        user-select: none;
    }}
    </style>
    <div class="card">
        <div class='card-title'>{title}</div>
        <div class = 'card-value'>{value}</div>
    </div>
    
    """
    )


def model(title: str, title1: str, value1: str, title2: str, value2: str):
    st.html(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
            .card {{
                border: 2px solid #3c4044;
                border-radius: 15px;
                padding: 20px;
                font-family: 'Inter', sans-serif;
                color: #fff;
                background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
                transition: transform 0.3s, box-shadow 0.3s;
                width: 100%;
            }}
            .card:hover {{
                transform: translateY(-4px);
                box-shadow: 0 8px 30px rgba(0, 150, 255, 0.5);
            }}
            .title {{
                text-align: center;
                color: #00AFFF;
                margin-top: 0;
                font-size: 50px;  /* Tamanho do título aumentado */
                font-weight: 600;  /* Opcional: deixa o título mais grosso */
            }}
            .section {{
                flex: 1;
                text-align: center;
                margin: 0 10px;
            }}
            .divider {{
                border-left: 2px solid #fff;
                margin: 0 10px;
            }}
            .value {{
                font-size: 28px;
                font-weight: bold;
                color: #E0E0E0;
            }}
        </style>
        <div class="card">
            <h2 class="title" >{title}</h2>
            <div style="display: flex; justify-content: space-around;">
                <div class="section">
                    <h4 style="color: #fff;">{title1}</h4>
                    <p class="value">{value1}</p>
                </div>
                <div class="divider"></div>
                <div class="section">
                    <h4 style="color: #fff;">{title2}</h4>
                    <p class="value">{value2}</p>
                </div>
            </div>
        </div>
        """
    )
