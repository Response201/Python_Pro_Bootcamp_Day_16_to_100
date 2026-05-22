import edge_tts
from playsound3 import playsound
from pypdf import PdfReader
import re



def get_text():

    text = input("\nVad vill du ha uppläst?\nSkriv en egen text eller 'pdf' för att läsa upp text från pdf-fil\nSkriv 'stop' för att avsluta\n").strip()
    return text

def text_to_speech(text):
    communicate = edge_tts.Communicate(text, "sv-SE-MattiasNeural")

    with open("output.mp3", "wb") as file:
        for item in communicate.stream_sync():
            if item["type"] == "audio":
                file.write(item["data"])

    playsound("output.mp3")






def open_pdf():
    try:
        reader = PdfReader("exempel-text.pdf")
        pages = []
        for page in reader.pages:
            text = page.extract_text()

            if not text:
                continue

            pages.append(text.strip())

        return pages

    except Exception:
            print("pdf-filen gick inte att ladda")
            return []






def clean_text(text):

        return re.sub(r"[^a-zA-ZåäöÅÄÖ0-9.!?\s]", "", text)