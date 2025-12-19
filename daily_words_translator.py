# Daily Words Translator
# Translation Program for Common Words
# Introduction to Programming - 100 Level

# Program Header
print("=" * 60)
print("          DAILY WORDS TRANSLATOR PROGRAM")
print("=" * 60)

# Available words header
print("\nAVAILABLE WORDS FOR TRANSLATION:")
print("-" * 60)

word_list = [
    "Days", "Later", "Machine", "Learn", "Bright", 
    "Light", "Names", "Funny", "Future", "Game",
    "Good", "Food", "Rice", "Spaghetti", "Pasta",
    "Chinese Rice", "Snarled", "Spark", "Power", "Tea"
]

counter = 1
for word in word_list:
    print(f"{counter}. {word}")
    counter = counter + 1

print("-" * 60)

# Translation dictionary
translations = {
    'days': {
        'hindi': 'din',
        'hausa': 'kwanaki',
        'korean': '날들 (naldeul)',
        'tiv': 'shie',
        'igbo': 'ubochi',
        'definition': 'Period of 24 hours'
    },
    'later': {
        'hindi': 'baad mein',
        'hausa': 'daga baya',
        'korean': '나중에 (najung-e)',
        'tiv': 'kpa u se',
        'igbo': 'mgbe e mechara',
        'definition': 'At a time in the future'
    },
    'machine': {
        'hindi': 'yantra',
        'hausa': 'injin',
        'korean': '기계 (gigye)',
        'tiv': 'u kpaa aôndo',
        'igbo': 'igwe',
        'definition': 'A device with moving parts'
    },
    'learn': {
        'hindi': 'seekhna',
        'hausa': 'koyi',
        'korean': '배우다 (baeuda)',
        'tiv': 'kpa ishima',
        'igbo': 'muta ihe',
        'definition': 'To gain knowledge or skill'
    },
    'bright': {
        'hindi': 'chamakdar',
        'hausa': 'haske',
        'korean': '밝은 (balgeun)',
        'tiv': 'wuhe kwagh',
        'igbo': 'na-egbuke egbuke',
        'definition': 'Giving out or reflecting light'
    },
    'light': {
        'hindi': 'prakash',
        'hausa': 'haske',
        'korean': '빛 (bit)',
        'tiv': 'wuhe',
        'igbo': 'ihe',
        'definition': 'Natural illumination'
    },
    'names': {
        'hindi': 'naam',
        'hausa': 'sunaye',
        'korean': '이름들 (ireumdeul)',
        'tiv': 'iveren',
        'igbo': 'aha',
        'definition': 'Words by which people or things are known'
    },
    'funny': {
        'hindi': 'mazaakiya',
        'hausa': 'abin dariya',
        'korean': '재미있는 (jaemiissneun)',
        'tiv': 'lu sha',
        'igbo': 'ihe ochi',
        'definition': 'Causing laughter or amusement'
    },
    'future': {
        'hindi': 'bhavishya',
        'hausa': 'gaba',
        'korean': '미래 (mirae)',
        'tiv': 'shie sha angbian',
        'igbo': 'odinihu',
        'definition': 'Time that is to come'
    },
    'game': {
        'hindi': 'khel',
        'hausa': 'wasa',
        'korean': '게임 (geim)',
        'tiv': 'iwase',
        'igbo': 'egwuregwu',
        'definition': 'Activity for entertainment or competition'
    },
    'good': {
        'hindi': 'accha',
        'hausa': 'mai kyau',
        'korean': '좋은 (joh-eun)',
        'tiv': 'tar',
        'igbo': 'oma',
        'definition': 'Of high quality or standard'
    },
    'food': {
        'hindi': 'bhojan',
        'hausa': 'abinci',
        'korean': '음식 (eumsig)',
        'tiv': 'ibiamenya',
        'igbo': 'nri',
        'definition': 'Substance consumed for nutrition'
    },
    'rice': {
        'hindi': 'chawal',
        'hausa': 'shinkafa',
        'korean': '쌀 (ssal)',
        'tiv': 'imahimin',
        'igbo': 'osikapa',
        'definition': 'A cereal grain used as food'
    },
    'spaghetti': {
        'hindi': 'spaghetti',
        'hausa': 'taliya',
        'korean': '스파게티 (seupageti)',
        'tiv': 'spaghetti',
        'igbo': 'spaghetti',
        'definition': 'Long thin pasta'
    },
    'pasta': {
        'hindi': 'pasta',
        'hausa': 'taliya',
        'korean': '파스타 (paseuta)',
        'tiv': 'pasta',
        'igbo': 'pasta',
        'definition': 'Italian food made from flour and water'
    },
    'chinese rice': {
        'hindi': 'chinese chawal',
        'hausa': 'shinkafar chinese',
        'korean': '중국 쌀 (jungguk ssal)',
        'tiv': 'imahimin China',
        'igbo': 'osikapa China',
        'definition': 'Rice prepared in Chinese style'
    },
    'snarled': {
        'hindi': 'gussa',
        'hausa': 'fushi',
        'korean': '으르렁거리다 (eureureonggeorida)',
        'tiv': 'biam ku kpa',
        'igbo': 'iwe',
        'definition': 'Growled angrily or spoke in an angry way'
    },
    'spark': {
        'hindi': 'chingari',
        'hausa': 'tartsatsi',
        'korean': '불꽃 (bulkkot)',
        'tiv': 'wuhe ter',
        'igbo': 'oku',
        'definition': 'A small particle of fire'
    },
    'power': {
        'hindi': 'shakti',
        'hausa': 'iko',
        'korean': '힘 (him)',
        'tiv': 'gba',
        'igbo': 'ike',
        'definition': 'The ability to do something'
    },
    'tea': {
        'hindi': 'chai',
        'hausa': 'shayi',
        'korean': '차 (cha)',
        'tiv': 'tii',
        'igbo': 'tii',
        'definition': 'A hot drink made from leaves'
    }
}

# Function to translate word
def translate_word(word, language):
    word = word.lower()
    
    if word in translations:
        translation = translations[word][language]
        meaning = translations[word]['definition']
        
        print("\n" + "=" * 60)
        print(f"WORD: {word.upper()}")
        print("=" * 60)
        print(f"Translation: {translation}")
        print(f"Meaning: {meaning}")
        print("=" * 60)
    else:
        print("\nWord not found in database!")
        print("Please check the available words list.")

# Main program loop
program_running = True

while program_running:
    print("\n" + "=" * 60)
    print("MENU - SELECT LANGUAGE:")
    print("=" * 60)
    print("1. Hindi")
    print("2. Hausa")
    print("3. Korean")
    print("4. Tiv")
    print("5. Igbo")
    print("6. Exit")
    print("=" * 60)
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        word = input("\nEnter word to translate: ")
        translate_word(word, 'hindi')
        input("\nPress Enter to continue...")
    
    elif choice == '2':
        word = input("\nEnter word to translate: ")
        translate_word(word, 'hausa')
        input("\nPress Enter to continue...")
    
    elif choice == '3':
        word = input("\nEnter word to translate: ")
        translate_word(word, 'korean')
        input("\nPress Enter to continue...")
    
    elif choice == '4':
        word = input("\nEnter word to translate: ")
        translate_word(word, 'tiv')
        input("\nPress Enter to continue...")
    
    elif choice == '5':
        word = input("\nEnter word to translate: ")
        translate_word(word, 'igbo')
        input("\nPress Enter to continue...")
    
    elif choice == '6':
        print("\n" + "=" * 60)
        print("Thank you for using Daily Words Translator!")
        print("=" * 60)
        program_running = False
    
    else:
        print("\nInvalid choice! Please enter 1-6.")
        input("\nPress Enter to continue...")

print("\nProgram ended.")
