import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Daily Words Translator",
    layout="wide"
)

# Program Header
st.title("DAILY WORDS TRANSLATOR PROGRAM")
st.divider()

# Available words
word_list = [
    "Days", "Later", "Machine", "Learn", "Bright",
    "Light", "Names", "Funny", "Future", "Game",
    "Good", "Food", "Rice", "Spaghetti", "Pasta",
    "Chinese Rice", "Snarled", "Spark", "Power", "Tea"
]

# Translation dictionary
translations = {
    'days': {
        'Hindi': 'din',
        'Hausa': 'kwanaki',
        'Korean': '날들 (naldeul)',
        'Tiv': 'shie',
        'Igbo': 'ubochi',
        'definition': 'Period of 24 hours'
    },
    'later': {
        'Hindi': 'baad mein',
        'Hausa': 'daga baya',
        'Korean': '나중에 (najung-e)',
        'Tiv': 'kpa u se',
        'Igbo': 'mgbe e mechara',
        'definition': 'At a time in the future'
    },
    'machine': {
        'Hindi': 'yantra',
        'Hausa': 'injin',
        'Korean': '기계 (gigye)',
        'Tiv': 'u kpaa aôndo',
        'Igbo': 'igwe',
        'definition': 'A device with moving parts'
    },
    'learn': {
        'Hindi': 'seekhna',
        'Hausa': 'koyi',
        'Korean': '배우다 (baeuda)',
        'Tiv': 'kpa ishima',
        'Igbo': 'muta ihe',
        'definition': 'To gain knowledge or skill'
    },
    'bright': {
        'Hindi': 'chamakdar',
        'Hausa': 'haske',
        'Korean': '밝은 (balgeun)',
        'Tiv': 'wuhe kwagh',
        'Igbo': 'na-egbuke egbuke',
        'definition': 'Giving out or reflecting light'
    },
    'light': {
        'Hindi': 'prakash',
        'Hausa': 'haske',
        'Korean': '빛 (bit)',
        'Tiv': 'wuhe',
        'Igbo': 'ihe',
        'definition': 'Natural illumination'
    },
    'names': {
        'Hindi': 'naam',
        'Hausa': 'sunaye',
        'Korean': '이름들 (ireumdeul)',
        'Tiv': 'iveren',
        'Igbo': 'aha',
        'definition': 'Words by which people or things are known'
    },
    'funny': {
        'Hindi': 'mazaakiya',
        'Hausa': 'abin dariya',
        'Korean': '재미있는 (jaemiissneun)',
        'Tiv': 'lu sha',
        'Igbo': 'ihe ochi',
        'definition': 'Causing laughter or amusement'
    },
    'future': {
        'Hindi': 'bhavishya',
        'Hausa': 'gaba',
        'Korean': '미래 (mirae)',
        'Tiv': 'shie sha angbian',
        'Igbo': 'odinihu',
        'definition': 'Time that is to come'
    },
    'game': {
        'Hindi': 'khel',
        'Hausa': 'wasa',
        'Korean': '게임 (geim)',
        'Tiv': 'iwase',
        'Igbo': 'egwuregwu',
        'definition': 'Activity for entertainment or competition'
    },
    'good': {
        'Hindi': 'accha',
        'Hausa': 'mai kyau',
        'Korean': '좋은 (joh-eun)',
        'Tiv': 'tar',
        'Igbo': 'oma',
        'definition': 'Of high quality or standard'
    },
    'food': {
        'Hindi': 'bhojan',
        'Hausa': 'abinci',
        'Korean': '음식 (eumsig)',
        'Tiv': 'ibiamenya',
        'Igbo': 'nri',
        'definition': 'Substance consumed for nutrition'
    },
    'rice': {
        'Hindi': 'chawal',
        'Hausa': 'shinkafa',
        'Korean': '쌀 (ssal)',
        'Tiv': 'imahimin',
        'Igbo': 'osikapa',
        'definition': 'A cereal grain used as food'
    },
    'spaghetti': {
        'Hindi': 'spaghetti',
        'Hausa': 'taliya',
        'Korean': '스파게티 (seupageti)',
        'Tiv': 'spaghetti',
        'Igbo': 'spaghetti',
        'definition': 'Long thin pasta'
    },
    'pasta': {
        'Hindi': 'pasta',
        'Hausa': 'taliya',
        'Korean': '파스타 (paseuta)',
        'Tiv': 'pasta',
        'Igbo': 'pasta',
        'definition': 'Italian food made from flour and water'
    },
    'chinese rice': {
        'Hindi': 'chinese chawal',
        'Hausa': 'shinkafar chinese',
        'Korean': '중국 쌀 (jungguk ssal)',
        'Tiv': 'imahimin China',
        'Igbo': 'osikapa China',
        'definition': 'Rice prepared in Chinese style'
    },
    'snarled': {
        'Hindi': 'gussa',
        'Hausa': 'fushi',
        'Korean': '으르렁거리다 (eureureonggeorida)',
        'Tiv': 'biam ku kpa',
        'Igbo': 'iwe',
        'definition': 'Growled angrily or spoke in an angry way'
    },
    'spark': {
        'Hindi': 'chingari',
        'Hausa': 'tartsatsi',
        'Korean': '불꽃 (bulkkot)',
        'Tiv': 'wuhe ter',
        'Igbo': 'oku',
        'definition': 'A small particle of fire'
    },
    'power': {
        'Hindi': 'shakti',
        'Hausa': 'iko',
        'Korean': '힘 (him)',
        'Tiv': 'gba',
        'Igbo': 'ike',
        'definition': 'The ability to do something'
    },
    'tea': {
        'Hindi': 'chai',
        'Hausa': 'shayi',
        'Korean': '차 (cha)',
        'Tiv': 'tii',
        'Igbo': 'tii',
        'definition': 'A hot drink made from leaves'
    }
}

# Sidebar
st.sidebar.title("Available Words")
for i, word in enumerate(word_list, 1):
    st.sidebar.write(f"{i}. {word}")

language = st.sidebar.selectbox(
    "Select Language",
    ["Hindi", "Hausa", "Korean", "Tiv", "Igbo"]
)

# Main content
st.subheader("Translate a Word")

word_input = st.text_input("Enter word to translate")

if st.button("Translate"):
    key = word_input.lower()

    if key in translations:
        st.success(f"**Translation ({language}):** {translations[key][language]}")
        st.info(f"**Meaning:** {translations[key]['definition']}")
    else:
        st.error("Word not found. Please select from the available words list.")

st.divider()
st.caption("Thank you for using Daily Words Translator")
