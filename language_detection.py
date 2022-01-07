from langdetect import detect

all_language_codes ={
    "en": "English",
    "ja": "Japanese",
    "ar": "Arabic",
    "fr": "French",
    'nl': 'Dutch',
    'cs': 'Czech',
    'tl': 'Tagalog',
    'tr': 'Turkish',
    'th': 'Thai',
    'pt': 'Portuguese',
    'uk': 'Ukrainian',
    
}

input_sentences = [
    "My name is Ivan Santoso, I am a student at Pamulang University",
    "私の名前はイワン・サントソです。パムラン大学の学生です。",
    "اسمي إيفان سانتوسو ، أنا طالب في جامعة بامولانج",
    "ฉันชื่อ Ivan Santoso ฉันเป็นนักศึกษาที่ Pamulang University",
    "Meu nome é Ivan Santoso, sou estudante da Universidade Pamulang",
    "Benim adım Ivan Santoso, Pamulang Üniversitesi'nde öğrenciyim.",
    "Je m'appelle Ivan Santoso, je suis étudiant à l'Université de Pamulang",
    "Mitt navn er Ivan Santoso, jeg er student ved Pamulang University",
    "Ang pangalan ko ay Ivan Santoso, ako ay isang estudyante sa Pamulang University",
    "Мене звати Іван Сантосо, я студент університету Памуланга"
    
]

lemmatizer_names = ["Language Code", "Input Sentence"]
format_text = "{:24}" *(len(lemmatizer_names) + 1)
print ('\n', format_text.format("Language Name", *lemmatizer_names),'\n','='*120)
for data in input_sentences:
    language_code = detect(data)    
    sentence = [all_language_codes.get(language_code), language_code, data]
    print (format_text.format(*sentence))