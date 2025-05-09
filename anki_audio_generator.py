import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import os
import asyncio
import edge_tts
import csv

LANGUAGE_MAP = {
"Afrikaans (South Africa)": "af-ZA",
"Amharic (Ethiopia)": "am-ET",
"Arabic (United Arab Emirates)": "ar-AE",
"Arabic (Bahrain)": "ar-BH",
"Arabic (Algeria)": "ar-DZ",
"Arabic (Egypt)": "ar-EG",
"Arabic (Iraq)": "ar-IQ",
"Arabic (Jordan)": "ar-JO",
"Arabic (Kuwait)": "ar-KW",
"Arabic (Lebanon)": "ar-LB",
"Arabic (Libya)": "ar-LY",
"Arabic (Morocco)": "ar-MA",
"Arabic (Oman)": "ar-OM",
"Arabic (Qatar)": "ar-QA",
"Arabic (Saudi Arabia)": "ar-SA",
"Arabic (Syria)": "ar-SY",
"Arabic (Tunisia)": "ar-TN",
"Arabic (Yemen)": "ar-YE",
"Assamese (India)": "as-IN",
"Azerbaijani (Latin, Azerbaijan)": "az-AZ",
"Bulgarian (Bulgaria)": "bg-BG",
"Bangla (Bangladesh)": "bn-BD",
"Bengali (India)": "bn-IN",
"Bosnian (Bosnia and Herzegovina)": "bs-BA",
"Catalan": "ca-ES",
"Czech (Czechia)": "cs-CZ",
"Welsh (United Kingdom)": "cy-GB",
"Danish (Denmark)": "da-DK",
"German (Austria)": "de-AT",
"German (Switzerland)": "de-CH",
"German (Germany)": "de-DE",
"Greek (Greece)": "el-GR",
"English (Australia)": "en-AU",
"English (Canada)": "en-CA",
"English (United Kingdom)": "en-GB",
"English (Hong Kong SAR)": "en-HK",
"English (Ireland)": "en-IE",
"English (India)": "en-IN",
"English (Kenya)": "en-KE",
"English (Nigeria)": "en-NG",
"English (New Zealand)": "en-NZ",
"English (Philippines)": "en-PH",
"English (Singapore)": "en-SG",
"English (Tanzania)": "en-TZ",
"English (United States)": "en-US",
"English (South Africa)": "en-ZA",
"Spanish (Argentina)": "es-AR",
"Spanish (Bolivia)": "es-BO",
"Spanish (Chile)": "es-CL",
"Spanish (Colombia)": "es-CO",
"Spanish (Costa Rica)": "es-CR",
"Spanish (Cuba)": "es-CU",
"Spanish (Dominican Republic)": "es-DO",
"Spanish (Ecuador)": "es-EC",
"Spanish (Spain)": "es-ES",
"Spanish (Equatorial Guinea)": "es-GQ",
"Spanish (Guatemala)": "es-GT",
"Spanish (Honduras)": "es-HN",
"Spanish (Mexico)": "es-MX",
"Spanish (Nicaragua)": "es-NI",
"Spanish (Panama)": "es-PA",
"Spanish (Peru)": "es-PE",
"Spanish (Puerto Rico)": "es-PR",
"Spanish (Paraguay)": "es-PY",
"Spanish (El Salvador)": "es-SV",
"Spanish (United States)": "es-US",
"Spanish (Uruguay)": "es-UY",
"Spanish (Venezuela)": "es-VE",
"Estonian (Estonia)": "et-EE",
"Basque": "eu-ES",
"Persian (Iran)": "fa-IR",
"Finnish (Finland)": "fi-FI",
"Filipino (Philippines)": "fil-PH",
"French (Belgium)": "fr-BE",
"French (Canada)": "fr-CA",
"French (Switzerland)": "fr-CH",
"French (France)": "fr-FR",
"Irish (Ireland)": "ga-IE",
"Galician": "gl-ES",
"Gujarati (India)": "gu-IN",
"Hebrew (Israel)": "he-IL",
"Hindi (India)": "hi-IN",
"Croatian (Croatia)": "hr-HR",
"Hungarian (Hungary)": "hu-HU",
"Armenian (Armenia)": "hy-AM",
"Indonesian (Indonesia)": "id-ID",
"Icelandic (Iceland)": "is-IS",
"Italian (Italy)": "it-IT",
"Inuktitut (Syllabics, Canada)": "iu-CANS-CA",
"Inuktitut (Latin, Canada)": "iu-LATN-CA",
"Japanese (Japan)": "ja-JP",
"Javanese (Latin, Indonesia)": "jv-ID",
"Georgian (Georgia)": "ka-GE",
"Kazakh (Kazakhstan)": "kk-KZ",
"Khmer (Cambodia)": "km-KH",
"Kannada (India)": "kn-IN",
"Korean (Korea)": "ko-KR",
"Language": "Locale (BCP-47)",
"Lao (Laos)": "lo-LA",
"Lithuanian (Lithuania)": "lt-LT",
"Latvian (Latvia)": "lv-LV",
"Macedonian (North Macedonia)": "mk-MK",
"Malayalam (India)": "ml-IN",
"Mongolian (Mongolia)": "mn-MN",
"Marathi (India)": "mr-IN",
"Malay (Malaysia)": "ms-MY",
"Maltese (Malta)": "mt-MT",
"Burmese (Myanmar)": "my-MM",
"Norwegian Bokmal (Norway)": "nb-NO",
"Nepali (Nepal)": "ne-NP",
"Dutch (Belgium)": "nl-BE",
"Dutch (Netherlands)": "nl-NL",
"Odia (India)": "or-IN",
"Punjabi (India)": "pa-IN",
"Polish (Poland)": "pl-PL",
"Pashto (Afghanistan)": "ps-AF",
"Portuguese (Brazil)": "pt-BR",
"Portuguese (Portugal)": "pt-PT",
"Romanian (Romania)": "ro-RO",
"Russian (Russia)": "ru-RU",
"Sinhala (Sri Lanka)": "si-LK",
"Slovak (Slovakia)": "sk-SK",
"Slovenian (Slovenia)": "sl-SI",
"Somali (Somalia)": "so-SO",
"Albanian (Albania)": "sq-AL",
"Serbian (Latin, Serbia)": "sr-LATN-RS",
"Serbian (Cyrillic, Serbia)": "sr-RS",
"Sundanese (Indonesia)": "su-ID",
"Swedish (Sweden)": "sv-SE",
"Kiswahili (Kenya)": "sw-KE",
"Kiswahili (Tanzania)": "sw-TZ",
"Tamil (India)": "ta-IN",
"Tamil (Sri Lanka)": "ta-LK",
"Tamil (Malaysia)": "ta-MY",
"Tamil (Singapore)": "ta-SG",
"Telugu (India)": "te-IN",
"Thai (Thailand)": "th-TH",
"Turkish (Turkiye)": "tr-TR",
"Ukrainian (Ukraine)": "uk-UA",
"Urdu (India)": "ur-IN",
"Urdu (Pakistan)": "ur-PK",
"Uzbek (Latin, Uzbekistan)": "uz-UZ",
"Vietnamese (Vietnam)": "vi-VN",
"Chinese (Wu, Simplified)": "wuu-CN",
"Chinese (Cantonese, Simplified)": "yue-CN",
"Chinese (Mandarin, Simplified)": "zh-CN",
"Chinese (Guangxi Accent Mandarin, Simplified)": "zh-CN-GUANGXI",
"Chinese (Zhongyuan Mandarin Henan, Simplified)": "zh-CN-henan",
"Chinese (Northeastern Mandarin, Simplified)": "zh-CN-liaoning",
"Chinese (Zhongyuan Mandarin Shaanxi, Simplified)": "zh-CN-shaanxi",
"Chinese (Jilu Mandarin, Simplified)": "zh-CN-shandong",
"Chinese (Southwestern Mandarin, Simplified)": "zh-CN-sichuan",
"Chinese (Cantonese, Traditional)": "zh-HK",
"Chinese (Taiwanese Mandarin, Traditional)": "zh-TW",
"isiZulu (South Africa)": "zu-ZA",
}

class AnkiAudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anki Audio Generator")
        self.df = None
        self.voices_list = asyncio.run(edge_tts.list_voices())

        # CSV Selection
        self.csv_label = tk.Label(root, text="Step 1: Select CSV File")
        self.csv_label.pack()
        self.csv_button = tk.Button(root, text="Browse CSV", command=self.load_csv)
        self.csv_button.pack()

        # Column Selection
        self.column_label = tk.Label(root, text="Step 2: Select Column with Text")
        self.column_label.pack()
        self.column_menu = ttk.Combobox(root, state="readonly")
        self.column_menu.pack()

        # Media Folder Selection
        self.media_label = tk.Label(root, text="Step 3: Select Anki media folder")
        self.media_label.pack()
        self.media_button = tk.Button(root, text="Browse Folder", command=self.select_media_folder)
        self.media_button.pack()
        self.media_path = tk.StringVar()
        self.media_entry = tk.Entry(root, textvariable=self.media_path, width=50)
        self.media_entry.pack()

        # Language and Voice Selection
        self.lang_label = tk.Label(root, text="Step 4: Select Language")
        self.lang_label.pack()
        self.languages = sorted(LANGUAGE_MAP.keys())
        self.lang_menu = ttk.Combobox(root, values=self.languages, state="readonly")
        self.lang_menu.pack()
        self.lang_menu.bind("<<ComboboxSelected>>", self.update_voices)

        self.voice_label = tk.Label(root, text="Step 5: Select Voice")
        self.voice_label.pack()
        self.voice_menu = ttk.Combobox(root, state="readonly")
        self.voice_menu.pack()

        # Output File
        self.output_label = tk.Label(root, text="Step 6: Output File Name")
        self.output_label.pack()
        self.output_name = tk.Entry(root, width=40)
        self.output_name.insert(0, "anki_ready.csv")
        self.output_name.pack()

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Audio", command=self.start_generation)
        self.generate_button.pack(pady=10)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not path:
            return
        self.df = pd.read_csv(path, quoting=csv.QUOTE_ALL)
        self.csv_path = path
        self.column_menu["values"] = list(self.df.columns)
        if self.df.columns.any():
            self.column_menu.current(0)

    def select_media_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.media_path.set(path)

    def update_voices(self, event=None):
        selected_nice_lang = self.lang_menu.get()
        locale_code = LANGUAGE_MAP.get(selected_nice_lang)
        voices = [v["ShortName"] for v in self.voices_list if v["Locale"] == locale_code]
        self.voice_menu["values"] = voices
        if voices:
            self.voice_menu.current(0)

    def start_generation(self):
        if self.df is None:
            messagebox.showerror("Error", "CSV not loaded.")
            return

        column = self.column_menu.get()
        media_folder = self.media_path.get()
        voice = self.voice_menu.get()
        output_filename = self.output_name.get()

        if not all([column, media_folder, voice, output_filename]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not output_filename.endswith(".csv"):
            output_filename += ".csv"

        output_path = os.path.join(os.path.dirname(self.csv_path), output_filename)

        asyncio.run(self.generate_audio_files(column, media_folder, voice, output_path))

    async def generate_audio_files(self, column, media_folder, voice, output_path):
        audio_filenames = []
        for idx, row in self.df.iterrows():
            text = str(row[column])
            filename = f"audio_{idx}.mp3"
            filepath = os.path.join(media_folder, filename)

            communicate = edge_tts.Communicate(text=text, voice=voice)
            await communicate.save(filepath)
            audio_filenames.append(f"[sound:{filename}]")

        self.df["Audio"] = audio_filenames
        self.df.to_csv(output_path, index=False, sep=";", quoting=csv.QUOTE_NONE)
        messagebox.showinfo("Success", f"Audio generated and CSV saved to:\n{output_path}")

root = tk.Tk()
app = AnkiAudioApp(root)
root.mainloop()
