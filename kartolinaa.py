import streamlit as st
from datetime import datetime

# Konfigurimi i faqes
st.set_page_config(
    page_title="Kartolinë për Mësues - 7 Marsi",
    page_icon="🎨",
    layout="centered"
)

# Stilimi i kartolinës me CSS
st.markdown("""
    <style>
    .main {
        background-color: #fdf2f2;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #e53e3e;
        color: white;
    }
    .postcard-container {
        background: white;
        padding: 40px;
        border-radius: 10px;
        border-left: 15px solid #e53e3e;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        font-family: 'Georgia', serif;
        min-height: 350px;
        position: relative;
    }
    .stamp {
        position: absolute;
        top: 20px;
        right: 20px;
        width: 80px;
        height: 80px;
        border: 4px double #e53e3e;
        color: #e53e3e;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        transform: rotate(10deg);
        opacity: 0.6;
    }
    </style>
""", unsafe_allow_html=True)

# UI e aplikacionit
st.title("🍎 Kartolina e 7 Marsit")
st.subheader("Krijo një kujtim të bukur për mësuesin/en tënd")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### Plotëso detajet")
    emri_mesuesit = st.text_input("Emri i Mësuesit/es:", "Znj. Bardha")
    emri_nxenesit = st.text_input("Nga kush vjen:", "Nxënësi juaj")
    
    opsioni = st.selectbox("Lloji i urimit:", 
                          ["Mirënjohje", "Tradicional", "Për mësuesin e matematikës", "Për mësuesin e gjuhës"])
    
    # Logjika e mesazheve automatike
    mesazhet = {
        "Mirënjohje": "Faleminderit që ndriçuat rrugën tim me dije dhe durim. Jeni një frymëzim i vërtetë!",
        "Tradicional": "Gëzuar 7 Marsin! Paçit shëndet dhe mbarësi në misionin tuaj fisnik të mësuesisë.",
        "Për mësuesin e matematikës": "Faleminderit që na mësuat se çdo problem ka një zgjidhje dhe se dituria shumëfishohet kur ndahet!",
        "Për mësuesin e gjuhës": "Ju na mësuat bukurinë e fjalës dhe fuqinë e shkronjave. Gëzuar festën!"
    }
    
    mesazhi_final = st.text_area("Mesazhi juaj personal:", mesazhet[opsioni])

with col2:
    st.markdown("### Pamja e Kartolinës")
    
    # Struktura HTML e kartolinës
    st.markdown(f"""
        <div class="postcard-container">
            <div class="stamp">7 MARS<br>2026</div>
            <p style="color: #666; font-size: 0.9em;">Data: {datetime.now().strftime('%d.%m.%2026')}</p>
            <h2 style="color: #2d3748;">I/E dashur {emri_mesuesit},</h2>
            <p style="font-size: 1.2em; line-height: 1.6; color: #4a5568; font-style: italic; margin-top: 30px;">
                "{mesazhi_final}"
            </p>
            <div style="margin-top: 50px; text-align: right; border-top: 1px dashed #cbd5e0; pt-2;">
                <p style="margin-bottom: 0;">Me shumë respekt,</p>
                <h3 style="margin-top: 5px; color: #e53e3e;">{emri_nxenesit}</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Butoni i festimit
if st.button("🎉 Konfirmo dhe Shpërndaj"):
    st.balloons()
    st.success("Kartolina është gati! Mund të bësh 'Screenshot' dhe t'ia dërgosh mësuesit në WhatsApp ose Email.")
