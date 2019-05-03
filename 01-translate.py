from google.cloud import translate

# you need to use pip to install google-cloud-translate using "pip install --upgrade google-cloud-translate"
# you also need the private key json file downloaded. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the file.

translate_client = translate.Client()

text_to_translate = "Good morning"
langcode_from = "en"
langcode_to = "ms" #Malay
translated_text = translate_client.translate(text_to_translate,target_language=langcode_to)

print(f"{text_to_translate} in English is {translated_text['translatedText']} in Malay")
