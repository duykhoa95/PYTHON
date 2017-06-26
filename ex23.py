import sys

encoding, errors = sys.argv[1:]

languages = [
    "Afrikaans", "አማርኛ", "Аҧсшәа", "العربية",
    "Aragonés", "Arpetan", "Azərbaycanca", "Bamanankan",
    "বাংলা", "Bân-lâm-gú", "Беларуская", "Български",
    "Boarisch", "Bosanski", "Буряад", "Català",
    "Чӑвашла", "Čeština", "Cymraeg", "Dansk",
    "Deutsch", "Eesti", "Ελληνικά", "Español",
    "Esperanto", "فارسی", "Français", "Frysk",
    "Gaelg", "Gàidhlig", "Galego", "한국어",
    "Հայերեն", "हिन्दी", "Hrvatski", "Ido",
    "Interlingua", "Italiano", "עברית", "ಕನ್ನಡ",
    "Kapampangan", "ქართული", "Қазақша", "Kreyòl ayisyen",
    "Latgaļu", "Latina", "Latviešu", "Lëtzebuergesch",
    "Lietuvių", "Magyar", "Македонски", "Malti",
    "मराठी", "მარგალური", "مازِرونی", "Bahasa Melayu",
    "Монгол", "Nederlands", "नेपाल भाषा", "日本語",
    "Norsk bokmål", "Nouormand", "Occitan", "Oʻzbekcha/ўзбекча",
    "ਪੰਜਾਬੀ", "پنجابی", "پښتو", "Plattdüütsch",
    "Polski", "Português", "Română", "Romani",
    "Русский", "Seeltersk", "Shqip", "Simple English",
    "Slovenčina", "کوردیی ناوەندی", "Српски / srpski",
    "Suomi", "Svenska", "Tagalog", "தமிழ்", "ภาษาไทย",
    "Taqbaylit", "Татарча/tatarça", "తెలుగు", "Тоҷикӣ",
    "Türkçe", "Українська", "اردو", "Tiếng Việt",
    "Võro", "文言", "吴语", "ייִדיש", "中文"
]

def run(language_list, encoding, errors):
    if language_list:
        next_lang = language_list.pop()  #pop() return & rremove from the last
        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes, "<===>", cooked_string)

        return run(language_list, encoding, errors)

# run(languages, encoding, errors)

## python3 ex23.py utf-8 strict
###  Decode Bytes Encode Strings

print("\n---------------------------------\n")
def test(language_list, encoding, errors):
    if language_list:
        next_lang = language_list.pop(0)  #pop(0) > return & remove from head
        raw_bytes = next_lang.encode(encoding, errors=errors)
        # cooked_string = raw_bytes.decode(encoding, errors=errors)

        # print(cooked_string, "<<==>>", raw_bytes)
        print(next_lang, "<<==>>", raw_bytes)

        return test(language_list, encoding, errors)

test(languages, encoding, errors)
