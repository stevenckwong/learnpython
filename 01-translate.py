from google.cloud import translate

# you need to use pip to install google-cloud-translate using "pip install --upgrade google-cloud-translate"
# you also need the private key json file downloaded. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the file.

translate_client = translate.Client()

text_to_translate = input(f"Enter phrase in English: ")
langcode_from = "en"
print("""Please select language to translate to:
1. Malay
2. Italian
3. Russian
""")
selection = input("Enter selection: ")

if selection.isdigit():
    if selection == "1":
        langcode_to = "ms" #Malay
        language_name = "Malay"
    elif selection == "2":
        langcode_to = "it"
        language_name = "Italian"
    elif selection == "3":
        langcode_to = "ru"
        language_name = "Russian"
    else:
        print("Why can't you just follow the instructions???")
        exit()

    translated_text = translate_client.translate(text_to_translate,target_language=langcode_to)

    print(f"'{text_to_translate}' in English is '{translated_text['translatedText']}' in {language_name}")

else:
    print("Why can't you just follow the instructions???")
