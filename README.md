# Anki-card-audio-generator
Automatically create text to speach audio files for anki language cards

How to use the software:
Step 1: Download the software

Step 2: Create a CSV file that has at least two columns, for exaxmple column 1 "Chinese" and column two "English" as shown in the example below, the order of the columns does not matter. 
Note1: Make sure you save the CSV file as CSV UTF-8 comma delimited file in Excel. 
Note2: as the columns of hte final output file are seperated by ";" make sure your Chinese and English words or sentances do not contain any ";" otherwise you will have problems loading it into ANKi later.

![image](https://github.com/user-attachments/assets/eeb72fc3-449e-40fd-91b3-c8ed62c77bb8)

Step 3: Double click the downloaded "anki_audio_generator.exe" program to run it, you shoul dsee hte following: 
![image](https://github.com/user-attachments/assets/7b53b959-c383-4029-b865-5b55e2e0cb76)

Step 4: Follow th esteps in the Anki Audio Generator program
  Select CSV file-> this is the file you created in Step 2 above
  Select Column with Text -> Here you select the column containing th etext you want to generate audio files for
  Browse Folder -> Navigate to your ANKI "collection.media" folder you can do this by pasting ,%APPDATA%\Anki2, hit enter and click on "User 1" (or whatever your username is) and then click the collection.media folder and then click "Select folder".
  Select Language -> Here you select the language you wan tto create audio files for (The same language as the words/sentances selected in the "Select Column with Text" section).
  Select Voice -> Select hte voice you want 
  Output file name -> Write the output file name here and make sure it end with ".csv". This output file is the file you will import into Anki and it is storted in the same place as the file you ceated in Step 2.
  Finally hit Generate Audio and wait for the program to finish (A pop up window will let you know it is done) 

  Note you can browse the available languages here: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#text-to-speech
  and you can listen to samples of the different voices here: https://speech.microsoft.com/portal/voicegallery

Step 5: Import into ANKI
It is a bit tricky to import this into ANKI, here are some guidelines.
When you select the .csv file to imprt the ANKI Import File window will pop up.
Under the "File" section make sure the first option "Field separator" is set to "Semicolon"
Next enable "Allow HTML in fields" 
Have a look at the table to make sure all your columns are present and properly seperated. 

In the "Import options" sectio select your "Note Type" Basic or Basic (and reversed card)

In the "Filed mapping" section amke sure your Front, Back and Audio fields are selected based on the column names in your imprted CSV file. 
Finally Hit import

![image](https://github.com/user-attachments/assets/3798386c-7b3d-4972-8bc3-338885d66cde)
