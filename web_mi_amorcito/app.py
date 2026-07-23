import streamlit as st
from datetime import datetime
import random

# Configuración de la página
st.set_page_config(
    page_title="Para mi esposa ❤️",
    page_icon="💖",
    layout="centered"
)

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #007bff 0%, #00b8e6 100%);
        }

        [data-testid="stHeader"] {
            background: rgba(0, 123, 255, 0.86);
        }

        [data-testid="stMainBlockContainer"] {
            background: rgba(248, 252, 255, 0.94);
            border: 1px solid rgba(0, 77, 153, 0.28);
            border-radius: 12px;
            padding: 2rem 2.5rem;
            box-shadow: 0 12px 30px rgba(0, 46, 115, 0.24);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Efecto de globos al abrir
st.balloons()

# --- CABECERA ---
st.title("💖 Para la persona más especial")
st.write("Creé esta pequeña página para recordar lo mucho que te amo.")

st.divider()

# --- 1. CONTADOR DE TIEMPO JUNTOS ---
st.subheader("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️Siempre y más alla del siempre Mi amorcito ❤️❤️❤️❤️❤️❤️❤️")

# ⚠️ Cambia esta fecha: (Año, Mes, Día, Hora, Minuto)
fecha_inicio = datetime(2024, 10, 26, 19, 34) 
ahora = datetime.now()

diferencia = ahora - fecha_inicio
dias = diferencia.days
horas, rem = divmod(diferencia.seconds, 3600)
minutos, _ = divmod(rem, 60)

col1, col2, col3 = st.columns(3)
col1.metric("Días", f"{dias}")
col2.metric("Horas", f"{horas}")
col3.metric("Minutos", f"{minutos}")

st.caption("¡Y cada segundo a tu lado vale la pena! ❤️")

st.divider()

# --- 2. GENERADOR DE RAZONES ---
st.subheader("💌 Razones por las que te amo")

razones = [
    "❤️❤️❤️✨✨Por la forma en que me sonríes todos los días.❤️❤️❤️✨✨",
    "❤️💖❤️💖 Por ser la mujer que me motiva con todo y mi gran compañera de vida.❤️💖❤️💖",
    "❤️✨❤️✨ Por cómo haces que los días difíciles sean más ligeros.❤️✨❤️✨",
    "❤️🥰❤️🥰 Por tu sentido del humor y tu ternura.❤️🥰❤️🥰",
    "❤️🗺️🗺️❤️ Por todo lo que construimos y soñamos juntos.❤️🗺️🗺️❤️",
    "❤️🌟❤️🌟 Eres mi luz que motiva a ser mejor.❤️🌟❤️🌟",
    "❤️🍀❤️🍀 Supe que la suerte es real porque te conozco.❤️🍀❤️🍀",
    "❤️🌸❤️🌸 Mi tonota hermosa.❤️🌸❤️🌸",
    "❤️💋❤️💋 ESOS besos son para mi MI AMORCITO ERES MIA .❤️💋❤️💋",
    "❤️💭❤️💭 Simplemente por ser tú.❤️💭❤️💭"
    "🏆🌟🏆🌟Como tu no hay mi amorcito mi razon de que mis dias sean mejores.🏆🌟🏆🌟"
    "🧿🧿🏆🌟Eres mi todo contigo lo voy a logar todo para que no te falte nada.🏆🌟🧿🧿"
]

if st.button("Ver otra razón 💘", use_container_width=True):
    razon_elegida = random.choice(razones)
    st.success(f"✨ {razon_elegida}")
else:
    st.info(f"✨ {razones[0]}")

st.divider()

# --- 3. CUPONES DE AMOR INTERACTIVOS ---
st.subheader("🎟️ Cupones especiales para ti")
st.write("Toca un cupón para canjearlo cuando quieras:")

col_a, col_b = st.columns(2)

with col_a:
    if st.button("✨✨Escuchar podcast ✨✨ ", use_container_width=True):
        st.toast("¡Cupón canjeado! Lo escucharemos juntos y comentaremos cada detalle 🎧💬")
    
    if st.button("💆‍♂️ Masaje relajante", use_container_width=True):
        st.toast("¡Cupón canjeado! Válido para esta noche ✨")

with col_b:
    if st.button(" 🍿Maratón de películas a tu elección🍿", use_container_width=True):
        st.toast("¡Cupón canjeado! Tú eliges las películas y los snacks 🍿")
    
    if st.button("🏟️Maratón de Age of Empires🏟️ ", use_container_width=True):
        st.toast("¡Cupón canjeado! Vamos por la victoria Mi amorcito tonota con tu tonoto lo vas a logar todo juntos 💎🏆")

st.divider()

# Mensaje final
st.markdown("<h3 style='text-align: center; color: #E91E63;'>💕✨✨¡Te amo muchísimo!✨✨ 💕</h3>", unsafe_allow_html=True)