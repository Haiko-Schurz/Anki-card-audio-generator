# Anki-card-audio-generator
Automatically create text to speach audio files for anki language cards

How to use the software:
Step 1: Download the software here https://drive.google.com/file/d/1qIJPJPNV8JckpEE_ONjnf0E-V-Y37qaU/view?usp=drive_link
Note it currently only works for windows.

Step 2: Create a CSV file that has at least two columns, for exaxmple column 1 "Chinese" and column two "English" as shown in the example below, the order of the columns does not matter. 
Note1: Make sure you save the CSV file as CSV UTF-8 comma delimited file in Excel. 
Note2: as the columns of hte final output file are seperated by ";" make sure your Chinese and English words or sentances do not contain any ";" otherwise you will have problems loading it into ANKi later.

![image](https://github.com/user-attachments/assets/eeb72fc3-449e-40fd-91b3-c8ed62c77bb8)

Step 3: Double click the downloaded "anki_audio_generator.exe" program to run it, you shoul dsee hte following: 
![image](https://github.com/user-attachments/assets/7b53b959-c383-4029-b865-5b55e2e0cb76)

Step 4: Follow th esteps in the Anki Audio Generator program

Select CSV file-> this is the file you created in Step 2 above

Select Column with Text -> Here you select the column containing th etext you want to generate audio files for.

Browse Folder -> Navigate to your ANKI "collection.media" folder you can do this by pasting ,%APPDATA%\Anki2, hit enter and click on "User 1" (or whatever your username is) and then click the collection.media folder and then click "Select folder".
![image](https://github.com/user-attachments/assets/9010fcf4-3d6c-491c-b683-6ccce0aae2de)


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

In the "Field mapping" section amke sure your Front, Back and Audio fields are selected based on the column names in your imprted CSV file. 
Finally Hit import

![image](https://github.com/user-attachments/assets/3798386c-7b3d-4972-8bc3-338885d66cde)

At this point it is very possible that your Audio will not work, if it is not working follow these steps
In Anki click "Browse" 
![image](https://github.com/user-attachments/assets/787be4bc-0fc1-4b71-a8d2-0cab202dbfeb)

Then click Fields... in to top right
Then click Add on the right side and type "Audio" in the popup window and click OK then click save and close the window. 
![image](https://github.com/user-attachments/assets/c769a233-4df8-4a06-8c77-91c4bb28fecc)
![image](https://github.com/user-attachments/assets/7e59e661-eb55-4fc0-b592-f34d6769b999)

Next click on Cards... which is next to the Fields.. button you clicked in the previous step.
Here you now need to add the Audio field to either the "Front Template" or the "Back Template" depending on which side of the flashcard you want the audio to play.
You can also select the card type, it depends on if you chose Basic or Basic (and reversed card) in the Import options when you imported the cards. You may want to use the Card type dropdown menu to add the Audio field to all your card types.
Select aither Front Template or Back template then click Add Field at the bottom and select the Audio filed to add and hit OK. Then click save and close the Card Type window.

![image](https://github.com/user-attachments/assets/0b089c94-54a6-4d12-8640-ccabb72e05b0)

At this point it is possible that your Audio still does not play. If this is the case delete the card deck and import it again and choose all the same settings as decribed above, especially important to choose the same Note type in the Import options and have the columns assigned correctly in the Field mapping section.

Now you can start studying your new flashcards! Have fun!!









