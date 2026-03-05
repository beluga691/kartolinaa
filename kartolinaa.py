import streamlit as st

# Konfigurimi i faqes
st.set_page_config(
    page_title="Gëzuar 7 Marsin 2026",
    page_icon="🎓",
    layout="centered"
)

# CSS Stili i përditësuar
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Pinyon+Script&display=swap');

.stApp {
    background-color: #FDFCF8;
}

/* Animacion për hyrjen e tekstit */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fadeIn 1.5s ease-out;
}

.header-date {
    font-size: 0.9rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #D4AF37;
    text-align: center;
    font-weight: bold;
    margin-top: 2rem;
}

.header-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 600;
    color: #1A1A1A;
    text-align: center;
    margin-bottom: 0.5rem;
}

.header-subtitle {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: #525252;
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

.teacher-name {
    font-family: 'Pinyon Script', cursive;
    font-size: 4.5rem;
    color: #D4AF37;
    text-align: center;
    margin-top: 1rem;
}

.subject {
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #525252;
    text-align: center;
    margin-bottom: 2rem;
    border-bottom: 1px solid #D4AF37;
    display: inline-block;
    padding-bottom: 5px;
}

.message {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    line-height: 2;
    color: #222;
    text-align: center;
    margin: 2rem auto;
    max-width: 600px;
    font-style: italic;
}

.signature {
    font-family: 'Pinyon Script', cursive;
    font-size: 2.2rem;
    color: #4A5D4F;
    text-align: center;
    margin-top: 2rem;
}

.signature-from {
    font-size: 0.8rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #525252;
    text-align: center;
    margin-bottom: 3rem;
}

.divider {
    width: 120px;
    height: 1px;
    background: #D4AF37;
    margin: 2rem auto;
}

.footer {
    font-size: 0.75rem;
    color: #999;
    text-align: center;
    margin-top: 5rem;
    letter-spacing: 0.1em;
}

/* Fshehja e elementeve te default te Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Stilimi i Input-it */
div[data-baseweb="input"] {
    border-radius: 0px;
    border-bottom: 1px solid #D4AF37;
}
</style>
""", unsafe_allow_html=True)

# Të dhënat e mësuesve (Data e përditësuar në mesazhe)
TEACHERS = {
    "yllka": {
        "name": "Yllka",
        "subject": "Biologji • Mësuese Kujdestare",
        "message": "Në librin e rritjes sonë, ju jeni kapitulli që na mësoi se jeta nuk është thjesht një bashkësi qelizash që lëvizin, por një mrekulli që duhet mbrojtur me dashuri. Si mësuese kujdestare, ju ishit dora që na mbajti kur u rrezikuam të rrëzoheshim dhe zëri që na dha kurajo kur heshtëm. Në këtë 7 Mars 2026, duam t'ju themi se jeni 'shkenca' më njerëzore që kemi njohur ndonjëherë."
    },
    "egla": {
        "name": "Egla",
        "subject": "Gjuhë Shqipe",
        "message": "Ju na mësuat se gjuha jonë nuk është thjesht mjet komunikimi, por një kështjellë ku rri e fshehur shpirti i kombit. Me durimin e një shkrimtareje, ju i dhashë ngjyrë çdo fjalie tonë dhe na treguat se si ta duam veten përmes vargut e rreshtit. Faleminderit që na bëtë personazhe të bukur në faqet e kësaj shkolle."
    },
    "loreta": {
        "name": "Loreta",
        "subject": "Gjeografi • Qytetari",
        "message": "Harta e botës në sytë tanë do të ishte e zbrazët pa shpjegimet tuaja që i dhanë jetë çdo mali e lumi. Por mbi të gjitha, ju vizatuat te ne hartën e vlerave, duke na treguar se përpara se të bëhemi udhëtarë të botës, duhet të mësojmë të jemi njerëz me integritet. Mirënjohje për çdo horizont që na hapët."
    },
    "sava": {
        "name": "Sava",
        "subject": "Histori",
        "message": "Përmes zërit tuaj, pluhuri i shekujve u shndërrua në dritë. Ju na treguat se ne nuk jemi thjesht kalimtarë, por pasardhës të një historie që duhet ta nderojmë. Faleminderit që na mësuat se e ardhmja shkruhet më mirë kur nuk e harrojmë kurrë të shkuarën tonë."
    },
    "irvena": {
        "name": "Irvena",
        "subject": "Italisht",
        "message": "Orët tuaja ishin si një dritare e hapur nga ku hynte aroma e detit dhe melodia e një gjuhe që fluturon. Me ju, ne nuk mësuam thjesht fjalë të reja, por mësuam stilin dhe hijeshinë e një kulture që na bëri t'i shohim gjërat me më shumë ëmbëlsi. Grazie di cuore për çdo buzëqeshje."
    },
    "gladiola": {
        "name": "Gladiola",
        "subject": "Anglisht",
        "message": "Në botën e madhe që na pret jashtë këtyre mureve, ju na dhatë çelësin më të rëndësishëm. Anglishtja juaj ishte më shumë se mësim; ishte premtimi se asnjë ëndërr nuk do të jetë e paarritshme sepse tani ne dimë të flasim gjuhën e mundësive."
    },
    "liza": {
        "name": "Liza",
        "subject": "Matematikë",
        "message": "Në labirintin e numrave dhe formulave, ju ishit drita që na udhëhoqi drejt logjikës së pastër. Na mësuat se edhe ekuacioni më i ndërlikuar ka një zgjidhje nëse ke durim e vullnet. Faleminderit që nuk hoqët dorë nga ne deri sa çdo 'X' i panjohur u bë i qartë në mendjet tona."
    },
    "xheni": {
        "name": "Xheni",
        "subject": "Informatikë",
        "message": "Ju na treguat se e ardhmja nuk është një mister, por një kod që ne mund ta shkruajmë vetë. Faleminderit që na përgatitët për epokën e re me profesionalizëm dhe që na mësuat se pas çdo ekrani, njeriu mbetet programi më i rëndësishëm."
    },
    "andi": {
        "name": "Andi",
        "subject": "Muzikë",
        "message": "Nëse shkolla jonë do të ishte një simfoni, ju do të ishit dirigjenti që i dha kuptim çdo note. Faleminderit që na mësuat se jeta ka ritmin e saj dhe se sekreti i vërtetë qëndron te harmonia që krijojmë me njëri-tjetrin."
    },
    "andoni": {
        "name": "Andoni",
        "subject": "Vizatim",
        "message": "Ju na mësuat se bota nuk është vetëm ashtu siç duket, por ashtu siç ne zgjedhim ta pikturojmë. Faleminderit që na dhatë guximin të përdorim ngjyrat tona më të forta dhe që e kthyet klasën tonë në një galeri shpresash."
    },
    "aveniri": {
        "name": "Aveniri",
        "subject": "Fiskulturë",
        "message": "Ju ishit forca që na nxiti të vrapojmë më shpejt se dyshimet tona. Në çdo garë e në çdo stërvitje, na mësuat se fitorja e vërtetë nuk është trofeu, por disiplina për t'u ngritur sërish pas çdo rrëzimi. Mirënjohje për energjinë tuaj!"
    },
    "zeni": {
        "name": "Zeni",
        "subject": "Fiskulturë",
        "message": "Me ju, palestra nuk ishte thjesht një hapësirë fizike, por një shkollë e karakterit. Na mësuat se trupi i fortë duhet të shoqërohet nga një mendje e fortë dhe se me vullnet, çdo pengesë kthehet në një trampolinë drejt suksesit."
    }
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

# LOGJIKA E FAQES
if not st.session_state.show_message:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown('<p class="header-date">7 Mars 2026</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="header-title">Dita e Mësuesit</h1>', unsafe_allow_html=True)
    st.markdown('<p class="header-subtitle">Një udhëtim mirënjohjeje në çdo rresht</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name = st.text_input("Shkruani emrin për të hapur kartolinën", placeholder="Emri i mësuesit (psh. Yllka)...")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Hap Kartolinën", use_container_width=True):
            teacher = find_teacher(name)
            if teacher:
                st.session_state.teacher = teacher
                st.session_state.show_message = True
                st.rerun()
            else:
                st.error("Kërkojmë ndjesë, kjo kartolinë nuk u gjet. Ju lutem kontrolloni emrin.")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    teacher = st.session_state.teacher
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown('<p class="header-date">7 Mars 2026</p>', unsafe_allow_html=True)
    st.markdown(f'<h2 class="teacher-name">{teacher["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<center><p class="subject">{teacher["subject"]}</p></center>', unsafe_allow_html=True)
    st.markdown(f'<p class="message">"{teacher["message"]}"</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<p class="signature">Me dashuri dhe mirënjohje të pafundme,</p>', unsafe_allow_html=True)
    st.markdown('<p class="signature-from">Dioni, Rudolfi dhe Ema</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Kthehu Mbrapa", use_container_width=True):
            reset()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p class="footer">Krijuar me përkushtim nga Dioni, Rudolfi dhe Ema • 2026</p>', unsafe_allow_html=True)
