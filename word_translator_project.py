# Tech Terms Translation Program
# A simple English to French and Spanish translator for technical terms
# Created for: University Programming Project

def show_welcome():
    """Display welcome message"""
    print("\n========================================")
    print("  TECH TERMS TRANSLATOR")
    print("  English to 5 Languages")
    print("========================================")

def show_available_terms():
    """Display list of 20 available terms"""
    print("\nAvailable Terms:")
    print("----------------------------------------")
    terms = [
        'Algorithm', 'Binary', 'Cache', 'Database', 'Encode',
        'Function', 'Gateway', 'Hash', 'Interface', 'Keyword',
        'Loop', 'Method', 'Network', 'Object', 'Parse',
        'Query', 'Record', 'Server', 'Syntax', 'Variable'
    ]
    
    for i, term in enumerate(terms, 1):
        print(f"{i}. {term}")
    print("----------------------------------------")

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

def show_menu():
    """Display the main menu"""
    print("\n========================================")
    print("MENU:")
    print("========================================")
    print("1. Translate to French")
    print("2. Translate to Spanish")
    print("3. Translate to Hausa")
    print("4. Translate to Igbo")
    print("5. Translate to Yoruba")
    print("6. Translate to All Languages")
    print("7. View Available Terms")
    print("8. Exit")
    print("========================================")

def translate_word(word, option):
    """Translate the word based on user option"""
    translations = get_translations()
    word = word.lower()
    
    # Check if word exists
    if word not in translations:
        print("\nError: Word not found in database.")
        print("Please check the available terms list.")
        return
    
    # Get translation data
    data = translations[word]
    
    print("\n========================================")
    print(f"Term: {word.upper()}")
    print("========================================")
    
    # Display based on option
    if option == '1':
        print(f"French: {data['french']}")
    elif option == '2':
        print(f"Spanish: {data['spanish']}")
    elif option == '3':
        print(f"Hausa: {data['hausa']}")
    elif option == '4':
        print(f"Igbo: {data['igbo']}")
    elif option == '5':
        print(f"Yoruba: {data['yoruba']}")
    elif option == '6':
        print(f"French: {data['french']}")
        print(f"Spanish: {data['spanish']}")
        print(f"Hausa: {data['hausa']}")
        print(f"Igbo: {data['igbo']}")
        print(f"Yoruba: {data['yoruba']}")
    
    print(f"\nDefinition: {data['definition']}")
    print("========================================")

def main():
    """Main function to run the program"""
    show_welcome()
    show_available_terms()
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-8): ")
        
        # Exit program
        if choice == '8':
            print("\nThank you for using Tech Terms Translator!")
            print("Goodbye!")
            break
        
        # Show available terms
        elif choice == '7':
            show_available_terms()
        
        # Translation options
        elif choice in ['1', '2', '3', '4', '5', '6']:
            word = input("\nEnter the term you want to translate: ")
            translate_word(word, choice)
            input("\nPress Enter to continue...")
        
        # Invalid input
        else:
            print("\nInvalid choice! Please enter a number between 1 and 8.")
            input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
