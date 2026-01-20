# English Vocabulary Translator
# Translates English words to 5 different languages
# Student Project - CSC 101

# Display program title
print("\n" + "*" * 55)
print("*" + " " * 53 + "*")
print("*     ENGLISH VOCABULARY TRANSLATOR PROJECT        *")
print("*" + " " * 53 + "*")
print("*" * 55)

# Dictionary containing all word translations
word_database = {
    'vibrant': {
        'igbo': 'nke na-egbuke egbuke',
        'yoruba': 'alabara',
        'hausa': 'mai haske',
        'hungarian': 'élénk',
        'crimean': 'canlı',
        'definition': 'Full of energy and life; bright and striking'
    },
    'whimsical': {
        'igbo': 'nke ochi',
        'yoruba': 'alarinrin',
        'hausa': 'mai ban dariya',
        'hungarian': 'szeszélyes',
        'crimean': 'fantastik',
        'definition': 'Playfully quaint or fanciful'
    },
    'xylophia': {
        'igbo': 'osisi xylophia',
        'yoruba': 'igi xylophia',
        'hausa': 'itacen xylophia',
        'hungarian': 'xylophia',
        'crimean': 'ksilofiya',
        'definition': 'A genus of flowering plants in the family Annonaceae'
    },
    'yearning': {
        'igbo': 'aguu',
        'yoruba': 'ifẹ takuntakun',
        'hausa': 'marmari',
        'hungarian': 'vágyakozás',
        'crimean': 'hasret',
        'definition': 'A strong feeling of desire or longing'
    },
    'zestful': {
        'igbo': 'nwere ume',
        'yoruba': 'afẹfẹ',
        'hausa': 'mai kuzari',
        'hungarian': 'lelkes',
        'crimean': 'şevkli',
        'definition': 'Full of enthusiasm and energy'
    },
    'aerial': {
        'igbo': 'nke ikuku',
        'yoruba': 'ti oju ọrun',
        'hausa': 'na sama',
        'hungarian': 'légi',
        'crimean': 'hava',
        'definition': 'Existing or happening in the air'
    },
    'bizarre': {
        'igbo': 'ihe iju anya',
        'yoruba': 'ajeji',
        'hausa': 'mai ban mamaki',
        'hungarian': 'bizarr',
        'crimean': 'acayip',
        'definition': 'Very strange or unusual'
    },
    'captive': {
        'igbo': 'onye a tugidere',
        'yoruba': 'ẹlẹwọn',
        'hausa': 'kamamme',
        'hungarian': 'fogoly',
        'crimean': 'esir',
        'definition': 'A person who has been taken prisoner or confined'
    },
    'dazzle': {
        'igbo': 'mee ka o nwuo',
        'yoruba': 'tan imọlẹ',
        'hausa': 'haskaka',
        'hungarian': 'kápráztat',
        'crimean': 'qamaştırmaq',
        'definition': 'To blind temporarily with bright light or impress deeply'
    },
    'ephemeral': {
        'igbo': 'nke na-agafe ngwa ngwa',
        'yoruba': 'airekọja',
        'hausa': 'na dan lokaci',
        'hungarian': 'efemer',
        'crimean': 'qısa ömürlü',
        'definition': 'Lasting for a very short time'
    },
    'fluid': {
        'igbo': 'mmiri',
        'yoruba': 'omi',
        'hausa': 'ruwa',
        'hungarian': 'folyékony',
        'crimean': 'suyuq',
        'definition': 'A substance that flows freely; smooth and graceful'
    },
    'gritty': {
        'igbo': 'aja',
        'yoruba': 'garungbẹrun',
        'hausa': 'yashi',
        'hungarian': 'durva',
        'crimean': 'qumsal',
        'definition': 'Containing or covered with grit; showing courage'
    },
    'holistic': {
        'igbo': 'niile',
        'yoruba': 'gbogbogbo',
        'hausa': 'dukkanin',
        'hungarian': 'holisztikus',
        'crimean': 'bütünleyici',
        'definition': 'Characterized by the treatment of the whole person'
    },
    'inexorable': {
        'igbo': 'nke a na-apughi igbochi',
        'yoruba': 'alagbara',
        'hausa': 'maras tsayawa',
        'hungarian': 'kérlelhetetlen',
        'crimean': 'qaçılmaz',
        'definition': 'Impossible to stop or prevent'
    },
    'juxtapose': {
        'igbo': 'dobe n\'akuku',
        'yoruba': 'fi lelẹ',
        'hausa': 'dora kusa',
        'hungarian': 'egymás mellé helyez',
        'crimean': 'yan-yana qoymaq',
        'definition': 'To place side by side for comparison'
    },
    'kaleidoscope': {
        'igbo': 'kaleidoscope',
        'yoruba': 'kaleidoscope',
        'hausa': 'kaleidoscope',
        'hungarian': 'kaleidoszkóp',
        'crimean': 'kaleydoskop',
        'definition': 'A toy showing changing patterns of colors'
    },
    'loyal': {
        'igbo': 'ikwesiri ntukwasi obi',
        'yoruba': 'oloootitọ',
        'hausa': 'mai aminci',
        'hungarian': 'hűséges',
        'crimean': 'sadıq',
        'definition': 'Giving or showing firm support or allegiance'
    },
    'maverick': {
        'igbo': 'onye na-eme ihe ya',
        'yoruba': 'alailagbara',
        'hausa': 'mai cin gashin kansa',
        'hungarian': 'különc',
        'crimean': 'başıbozuq',
        'definition': 'An independent-minded person'
    },
    'nuance': {
        'igbo': 'obere ihe dị iche',
        'yoruba': 'iyatọ kekere',
        'hausa': 'dan bambanci',
        'hungarian': 'árnyalat',
        'crimean': 'nüans',
        'definition': 'A subtle difference in meaning or expression'
    },
    'oboe': {
        'igbo': 'oboe',
        'yoruba': 'oboe',
        'hausa': 'oboe',
        'hungarian': 'oboa',
        'crimean': 'oboy',
        'definition': 'A woodwind instrument with a double reed'
    }
}

# Function to show all available words
def show_words():
    print("\n" + "=" * 55)
    print("LIST OF AVAILABLE WORDS:")
    print("=" * 55)
    
    word_list = list(word_database.keys())
    number = 1
    
    for w in word_list:
        print(f"{number}. {w.capitalize()}")
        number = number + 1
    
    print("=" * 55)

# Function to perform translation
def do_translation(word, lang):
    word = word.lower()
    
    # Check if word exists in database
    if word in word_database:
        result = word_database[word][lang]
        meaning = word_database[word]['definition']
        
        print("\n" + "-" * 55)
        print(f"English Word: {word.upper()}")
        print("-" * 55)
        print(f"Translation: {result}")
        print(f"Definition: {meaning}")
        print("-" * 55)
    else:
        print("\nError: This word is not in our database.")
        print("Please check the word list and try again.")

# Show all words at start
show_words()

# Main loop
running = True

while running:
    # Display menu
    print("\n" + "=" * 55)
    print("MAIN MENU - SELECT TARGET LANGUAGE:")
    print("=" * 55)
    print("1. Igbo")
    print("2. Yoruba")
    print("3. Hausa")
    print("4. Hungarian")
    print("5. Crimean Tatar")
    print("6. Exit")
    print("=" * 55)
    
    # Get user choice
    user_choice = input("\nPlease enter your choice (1-6): ")
    
    # Process choice
    if user_choice == '6':
        print("\n" + "*" * 55)
        print("Thank you for using the translator!")
        print("Goodbye!")
        print("*" * 55)
        running = False
    
    elif user_choice == '1':
        user_word = input("\nEnter the word to translate: ")
        do_translation(user_word, 'igbo')
        input("\nPress Enter to continue...")
    
    elif user_choice == '2':
        user_word = input("\nEnter the word to translate: ")
        do_translation(user_word, 'yoruba')
        input("\nPress Enter to continue...")
    
    elif user_choice == '3':
        user_word = input("\nEnter the word to translate: ")
        do_translation(user_word, 'hausa')
        input("\nPress Enter to continue...")
    
    elif user_choice == '4':
        user_word = input("\nEnter the word to translate: ")
        do_translation(user_word, 'hungarian')
        input("\nPress Enter to continue...")
    
    elif user_choice == '5':
        user_word = input("\nEnter the word to translate: ")
        do_translation(user_word, 'crimean')
        input("\nPress Enter to continue...")
    
    else:
        print("\nInvalid input! Please enter a number from 1 to 6.")
        input("\nPress Enter to continue...")

# End of program
print("\nProgram terminated.")
