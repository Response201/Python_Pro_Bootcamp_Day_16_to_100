import os
from functions import get_text, open_pdf, clean_text, text_to_speech
create_text_to_speech = True


while create_text_to_speech:

    text = get_text()

    if not text:
        continue


    if text.lower() == "stop":
        print("Program avslutat")

        if os.path.exists("output.mp3"):
            os.remove("output.mp3")

        break



    if text.lower() == "pdf":
        pages = open_pdf()

        for i, page in enumerate(pages):
            print(f"Läser sida {i + 1}")

            try:
                cleaned_page = clean_text(page)
                text_to_speech(cleaned_page)
            except Exception as e:
                print(f"Något gick fel på sida {i + 1}: {e}")

        continue



    cleaned_text = clean_text(text)

    if not cleaned_text:
        continue



    try:
        text_to_speech(cleaned_text)
    except Exception as e:
        print(f"Något gick fel")

