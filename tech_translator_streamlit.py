import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Tech Terms Translator",
    page_icon="💻"
)

def get_translations():
    """Dictionary containing all translations and definitions"""
    translations = {
        'algorithm': {
            'french': 'algorithme',
            'spanish': 'algoritmo',
            'hausa': 'algorithm',
            'igbo': 'usoro',
            'yoruba': 'ilana',
            'definition': 'A step-by-step procedure for solving a problem'
        },
        'binary': {
            'french': 'binaire',
            'spanish': 'binario',
            'hausa': 'binary',
            'igbo': 'binary',
            'yoruba': 'binary',
            'definition': 'A number system using only 0 and 1'
        },
        'cache': {
            'french': 'cache',
            'spanish': 'cache',
            'hausa': 'cache',
            'igbo': 'nchekwa',
            'yoruba': 'ipamọ',
            'definition': 'A storage component for faster data access'
        },
        'database': {
            'french': 'base de donnees',
            'spanish': 'base de datos',
            'hausa': 'rumbun bayanai',
            'igbo': 'ebe nchekwa data',
            'yoruba': 'ibi ipamọ data',
            'definition': 'An organized collection of data'
        },
        'encode': {
            'french': 'encoder',
            'spanish': 'codificar',
            'hausa': 'rufe',
            'igbo': 'tinye koodu',
            'yoruba': 'fi koodu si',
            'definition': 'To convert data into a specific format'
        },
        'function': {
            'french': 'fonction',
            'spanish': 'funcion',
            'hausa': 'aiki',
            'igbo': 'oru',
            'yoruba': 'iṣẹ',
            'definition': 'A reusable block of code'
        },
        'gateway': {
            'french': 'passerelle',
            'spanish': 'puerta de enlace',
            'hausa': 'kofar shiga',
            'igbo': 'onu uzo',
            'yoruba': 'ẹnu-ọna',
            'definition': 'A network point connecting to another network'
        },
        'hash': {
            'french': 'hachage',
            'spanish': 'hash',
            'hausa': 'hash',
            'igbo': 'hash',
            'yoruba': 'hash',
            'definition': 'A function that converts data into a fixed-size string'
        },
        'interface': {
            'french': 'interface',
            'spanish': 'interfaz',
            'hausa': 'fuskar sadarwa',
            'igbo': 'ihu mmekọrịta',
            'yoruba': 'oju isopọ',
            'definition': 'A point where two systems interact'
        },
        'keyword': {
            'french': 'mot-cle',
            'spanish': 'palabra clave',
            'hausa': 'kalmar mahimmanci',
            'igbo': 'okwu mkpa',
            'yoruba': 'ọrọ pataki',
            'definition': 'A reserved word in programming'
        },
        'loop': {
            'french': 'boucle',
            'spanish': 'bucle',
            'hausa': 'madauki',
            'igbo': 'ntughari',
            'yoruba': 'iyipo',
            'definition': 'A programming construct that repeats instructions'
        },
        'method': {
            'french': 'methode',
            'spanish': 'metodo',
            'hausa': 'hanya',
            'igbo': 'uzo',
            'yoruba': 'ọna',
            'definition': 'A function associated with an object'
        },
        'network': {
            'french': 'reseau',
            'spanish': 'red',
            'hausa': 'hanyar sadarwa',
            'igbo': 'netwok',
            'yoruba': 'nẹtiwọọki',
            'definition': 'A group of interconnected computers'
        },
        'object': {
            'french': 'objet',
            'spanish': 'objeto',
            'hausa': 'abu',
            'igbo': 'ihe',
            'yoruba': 'ohun',
            'definition': 'An instance of a class'
        },
        'parse': {
            'french': 'analyser',
            'spanish': 'analizar',
            'hausa': 'bincika',
            'igbo': 'nyochaa',
            'yoruba': 'ṣe itupalẹ',
            'definition': 'To analyze data by breaking it into parts'
        },
        'query': {
            'french': 'requete',
            'spanish': 'consulta',
            'hausa': 'tambaya',
            'igbo': 'ajuju',
            'yoruba': 'ibeere',
            'definition': 'A request for information from a database'
        },
        'record': {
            'french': 'enregistrement',
            'spanish': 'registro',
            'hausa': 'rikodin',
            'igbo': 'ndekọ',
            'yoruba': 'igbasilẹ',
            'definition': 'A single entry in a database'
        },
        'server': {
            'french': 'serveur',
            'spanish': 'servidor',
            'hausa': 'sabar',
            'igbo': 'sava',
            'yoruba': 'olutọju',
            'definition': 'A computer that provides services to other computers'
        },
        'syntax': {
            'french': 'syntaxe',
            'spanish': 'sintaxis',
            'hausa': 'tsarin rubutu',
            'igbo': 'usoro edemede',
            'yoruba': 'ilana kikọ',
            'definition': 'Rules that define valid code structure'
        },
        'variable': {
            'french': 'variable',
            'spanish': 'variable',
            'hausa': 'mai canzawa',
            'igbo': 'ihe na-agbanwe',
            'yoruba': 'oniyipada',
            'definition': 'A named storage location for data'
        }
    }
    return translations

# Header
st.title("Tech Terms Translator")
st.write("Translate technical terms to multiple languages")

# Sidebar
with st.sidebar:
    st.header("Language")
    language = st.selectbox(
        "Select:",
        ["French", "Spanish", "Hausa", "Igbo", "Yoruba", "All Languages"]
    )
    
    st.divider()
    
    st.subheader("Available Terms")
    terms = [
        'Algorithm', 'Binary', 'Cache', 'Database', 'Encode',
        'Function', 'Gateway', 'Hash', 'Interface', 'Keyword',
        'Loop', 'Method', 'Network', 'Object', 'Parse',
        'Query', 'Record', 'Server', 'Syntax', 'Variable'
    ]
    for term in terms:
        st.text(term)

# Main Area
word_input = st.text_input("Enter term to translate:")

# Translation
if word_input:
    translations = get_translations()
    word = word_input.lower().strip()
    
    if word in translations:
        data = translations[word]
        
        st.success("Translation found!")
        
        st.subheader(word_input.title())
        
        lang_map = {
            'French': 'french',
            'Spanish': 'spanish',
            'Hausa': 'hausa',
            'Igbo': 'igbo',
            'Yoruba': 'yoruba'
        }
        
        if language == "All Languages":
            st.write(f"**French:** {data['french']}")
            st.write(f"**Spanish:** {data['spanish']}")
            st.write(f"**Hausa:** {data['hausa']}")
            st.write(f"**Igbo:** {data['igbo']}")
            st.write(f"**Yoruba:** {data['yoruba']}")
        else:
            lang_key = lang_map[language]
            st.write(f"**{language}:** {data[lang_key]}")
        
        st.write(f"**Definition:** {data['definition']}")
        
    else:
        st.error("Term not found. Check available terms in sidebar.")
