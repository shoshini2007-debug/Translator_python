from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

def translate_text():
    text = input_text.get("1.0", END).strip()
    source = languages[source_lang.get()]
    target = languages[target_lang.get()]

    if text:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        output_text.delete("1.0", END)
        output_text.insert(END, translated)

root = Tk()
root.title("Language Translation Tool")
root.geometry("700x700")

Label(root, text="Enter Text").pack()

input_text = Text(root, height=6, width=60)
input_text.pack()

frame = Frame(root)
frame.pack()

source_lang = ttk.Combobox(frame, values=list(languages.keys()), state="readonly")
source_lang.set("English")
source_lang.grid(row=0, column=0)

Label(frame, text="To").grid(row=0, column=1)

target_lang = ttk.Combobox(frame, values=list(languages.keys()), state="readonly")
target_lang.set("Tamil")
target_lang.grid(row=0, column=2)

Button(root, text="Translate", command=translate_text).pack(pady=10)

output_text = Text(root, height=6, width=60)
output_text.pack()

root.mainloop()
