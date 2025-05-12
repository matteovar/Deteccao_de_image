import streamlit as st


def create_title(title: str):
    st.html(
        f"""
        <div class="title">{title}</div>
        <style>
            .title {{
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 8%;
            }}
        </style>
        """
    )


def create_cards(title: str, value: str):
    st.html(
        f"""
    
    <style>
    
        .card {{
           border: 1px solid #373739 ;
           border-radius: 10px;
           text-align: left;
           height: 120px;
           padding-left: 10px;
           padding-top: 10px;
           background-color: #070707;
           margin-bottom: 50px;
        }}
        .card-title{{
            font-size: 16px;
        }}
        .card-value{{
            font-size: 30px;
            font-weight: 600;
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
        <div style="
            border: 2px solid #3c4044;
            border-radius: 15px;
            padding: 20px;
            font-family: Arial, sans-serif;
            color: #fff;
        ">
            <h2 style="text-align: center; color: #fff; margin-top: 0;">{title}</h2>
            <div style="display: flex; justify-content: space-around;">
                <div style="flex: 1; text-align: center; margin-right: 10px;">
                    <h4 style="color: #fff;">{title1}</h4>
                    <p style="font-size: 28px; font-weight: bold;">{value1}</p>
                </div>
                <div style="border-left: 1px solid; height: 100;"></div>
                <div style="flex: 1; text-align: center; margin-left: 10px;">
                    <h4 style="color: #fff;">{title2}</h4>
                    <p style="font-size: 28px; font-weight: bold;">{value2}</p>
                </div>
            </div>
        </div>
        """
    )
