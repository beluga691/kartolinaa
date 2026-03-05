import streamlit as st

# Konfigurimi i faqes
st.set_page_config(
    page_title="Dita e Mësuesit - 7 Mars 2026",
    page_icon="🎓",
    layout="centered"
)

# CSS Stili
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Pinyon+Script&display=swap');

.stApp {
    background-color: #FDFCF8;
}

.header-date {
    font-size: 0.8rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #D4AF37;
    text-align: center;
}

.header-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 600;
    color: #1A1A1A;
    text-align: center;
}

.header-subtitle {
    color: #525252;
    text-align: center;
    margin-bottom: 2rem;
}

.teacher-name {
    font-family: 'Pinyon Script', cursive;
    font-size: 3.5rem;
    color: #D4AF37;
    text-align: center;
}

.subject {
    font-size: 0.8rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #525252;
    text-align: center;
    margin-bottom: 1.5rem;
}

.message {
    font-size: 1.1rem;
    line-height: 1.9;
    color: #333;
    text-align: center;
    margin-bottom: 2rem;
}

.signature {
    font-family: 'Pinyon Script', cursive;
    font-size: 1.75rem;
    color: #4A5D4F;
    text-align: center;
}

.signature-from {
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #525252;
    text-align: center;
}

.divider {
    width: 80px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #D4AF37, transparent);
    margin: 1rem auto;
}

.footer {
    font-size: 0.75rem;
    color: #999;
    text-align: center;
    margin-top: 3rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Lista e zgjeruar e mësuesve (Shtuar Monika, Emiliana, Majlinda, Elena, Ajbana, Albana, Anila, Arta, Erida, Laura)
TEACHERS = {
    # Mesuesit e fillores
    "monika": {
        "name": "Monika",
        "subject": "Mësuese Fillore",
        "message": "Ju ishit dritarja jonë e parë drejt botës së dijes. Faleminderit që me ëmbëlsinë tuaj na mësuat shkronjat e para dhe na mbajtët dorën në hapat tanë më të rëndësishëm. Mirënjohje për durimin dhe dashurinë që na dhuruat!"
    },
    "emiliana": {
        "name": "Emiliana",
        "subject": "Mësuese Fillore",
        "message": "Çdo fëmijë ka nevojë për një mësuese që beson tek ai, dhe ne jemi me fat që ju patëm ju. Faleminderit që i kthyet orët e mësimit në momente magjike dhe që na rritët me vlerat më të bukura njerëzore."
    },
    "majlinda": {
        "name": "Majlinda",
        "subject": "Mësuese Fillore",
        "message": "Në kujtimet tona më të bukura të fëmijërisë, ju keni një vend të veçantë. Faleminderit që me profesionalizëm dhe buzëqeshje na treguat se si të bëhemi nxënës të mirë dhe njerëz të vlefshëm."
    },
    "elena": {
        "name": "Elena",
        "subject": "Mësuese Fillore",
        "message": "Ju na mësuat se shkolla nuk është thjesht një ndërtesë, por një shtëpi e dytë ku mësohet dashuria për librin. Mirënjohje për çdo këshillë dhe për çdo fjalë të ngrohtë që na keni dhënë."
    },
    # Lendet e tjera
    "ajbana": {
        "name": "Ajbana",
        "subject": "Frëngjisht",
        "message": "Merci beaucoup për çdo orë mësimi që na bëri të udhëtojmë drejt kulturës dhe elegancës franceze. Ju na mësuat se gjuha është një urë që na lidh me botën, dhe na e bëtë këtë udhëtim shumë të bukur."
    },
    "albana": {
        "name": "Albana",
        "subject": "Psikologji",
        "message": "Në labirintin e mendimeve dhe emocioneve tona, ju ishit udhërrëfyesja më e mirë. Faleminderit që na mësuat se si të kuptojmë veten dhe të tjerët, duke na dhënë çelësin e një mendjeje të shëndoshë."
    },
    "anila": {
        "name": "Anila",
        "subject": "Gjeografi • Histori",
        "message": "Me ju, ne udhëtuam nëpër kohë dhe nëpër kontinente pa lëvizur nga klasa. Faleminderit që na treguat se sa e pasur është bota jonë dhe sa e rëndësishme është të njohim rrënjët tona."
    },
    "arta": {
        "name": "Arta",
        "subject": "Oficere e Sigurisë",
        "message": "Përtej rregullit dhe sigurisë, ju jeni për ne një mbështetje e vazhdueshme. Faleminderit që kujdeseni për ne çdo ditë dhe që na bëni të ndihemi të mbrojtur në ambientet e shkollës sonë."
    },
    "erida": {
        "name": "Erida",
        "subject": "Gjuhë Shqipe",
        "message": "Fjala shqipe në gojën tuaj merr një tjetër vlerë. Faleminderit që na mësuat t'i shkruajmë ëndrrat tona bukur dhe që na rrënjosët dashurinë për leximin dhe korrektësinë e gjuhës sonë amtare."
    },
    "laura": {
        "name": "Laura",
        "subject": "Matematikë",
        "message": "Edhe llogaritë më të vështira duken të thjeshta kur i shpjegoni ju. Faleminderit që na stërvitët mendjen me logjikë dhe që na treguat se me përkushtim, çdo ekuacion jetësor mund të zgjidhet."
    },
    # Mesuesit e vjeter (te ruajtur ne kod)
    "yllka": {"name": "Yllka", "subject": "Biologji • Mësuese Kujdestare", "message": "Në librin e rritjes sonë, ju jeni kapitulli që na mësoi se jeta nuk është thjesht një bashkësi qelizash, por një mrekulli. Faleminderit si mësuese kujdestare!"},
    "egla": {"name": "Egla", "subject": "Gjuhë Shqipe", "message": "Ju na mësuat se gjuha jonë nuk është thjesht mjet komunikimi, por kështjellë e shpirtit të kombit. Faleminderit!"},
    "loreta": {"name": "Loreta", "subject": "Gjeografi • Qytetari", "message": "Harta e botës do të ishte e zbrazët pa shpjegimet tuaja. Ju vizatuat te ne hartën e vlerave njerëzore."},
    "sava": {"name": "Sava", "subject": "Histori", "message": "Përmes zërit tuaj, pluhuri i shekujve u shndërrua në dritë. Faleminderit që na mësuat historinë!"},
    "irvena": {"name": "Irvena", "subject": "Italisht", "message": "Orët tuaja ishin si një dritare nga ku hynte melodia e një gjuhe që fluturon. Grazie di cuore!"},
    "gladiola": {"name": "Gladiola", "subject": "Anglisht", "message": "Në botën e madhe, ju na dhatë çelësin më të rëndësishëm: gjuhën e mundësive të pafundme."},
    "liza": {"name": "Liza", "subject": "Matematikë", "message": "Në labirintin e numrave, ju ishit drita drejt logjikës së pastër. Faleminderit për durimin!"},
    "xheni": {"name": "Xheni", "subject": "Informatikë", "message": "Ju na treguat se e ardhmja nuk është mister, por një kod që mund ta shkruajmë vetë."},
    "andi": {"name": "Andi", "subject": "Muzikë", "message": "Nëse shkolla do ishte simfoni, ju do ishit dirigjenti që i dha kuptim çdo note."},
    "andoni": {"name": "Andoni", "subject": "Vizatim", "message": "Ju na mësuat se bota është ashtu siç ne zgjedhim ta pikturojmë. Faleminderit për ngjyrat!"},
    "aveniri": {"name": "Aveniri", "subject": "Fiskulturë", "message": "Ju ishit forca që na nxiti të vrapojmë më shpejt se dyshimet tona. Mirënjohje!"},
    "zeni": {"name": "Zeni", "subject": "Fiskulturë", "message": "Me ju, palestra u bë shkollë e karakterit dhe vullnetit të fortë."}
}

# State Management
if "show_message" not in st.session_state:
    st.session_state.show_message = False
if "teacher" not in st.session_state:
    st.session_state.teacher = None

def find_teacher(name):
    return TEACHERS.get(name.strip().lower())

def reset():
    st.session_state.show_message = False
    st.session_state.teacher = None

# FAQJA KRYESORE
if not st.session_state.show_message:
    st.markdown('<p class="header-date">7 Mars 2026</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="header-title">Dita e Mësuesit</h1>', unsafe_allow_html=True)
    st.markdown('<p class="header-subtitle">Një falënderim i veçantë për ju</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name = st.text_input("Shkruani emrin tuaj", placeholder="Emri...")
        
        if st.button("Zbulo Mesazhin", use_container_width=True, type="primary"):
            teacher = find_teacher(name)
            if teacher:
                st.session_state.teacher = teacher
                st.session_state.show_message = True
                st.rerun()
            else:
                st.markdown('<p class="error" style="text-align:center; color:red;">Emri nuk u gjet. Provoni psh: Monika, Laura, ose Erida.</p>', unsafe_allow_html=True)

else:
    teacher = st.session_state.teacher
    st.markdown(f'<h2 class="teacher-name">{teacher["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="subject">{teacher["subject"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="message">{teacher["message"]}</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="signature">Me dashuri dhe mirënjohje</p>', unsafe_allow_html=True)
    st.markdown('<p class="signature-from">Dioni, Rudolfi dhe Ema</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Kthehu Mbrapa", use_container_width=True):
            reset()
            st.rerun()

st.markdown('<p class="footer">Ndërtuar me dashuri nga Dioni, Rudolfi dhe Ema • 2026</p>', unsafe_allow_html=True)
