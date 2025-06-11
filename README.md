UPDATE log:
 11-JUNE-2025 
 9:45:PM : PROGRAMMED PDF_parser.py file , it is extracting the text from pdf file and storing it in a text file only if the program is runned from vs code terminal .
 when fast api is run it shows the extracted file in browser in json format 



TO RUN PROGRAM :
1. open vs code terminal and do git clone 
2. open a new terminal and write :
python -m venv virtualenviornment
3. activate the virtual environment by writing : 
cd  .\AI-Powered-Job-Assistant\virtualenviornment\Scripts\
4. >>./activate



now cut the requirements.txt file from  the root directory and paste it in the Scripts folder inside virtualenviornment

5. >>pip install -r requirements.txt 
open a new terminal 
6. >>cd .\AI-Powered-Job-Assistant\

7. >>uvicorn app.main:app --reload

Remember to keep atleast one pdf file inside utils "AI-Powered-Job-Assistant\backend\utils"
folder and change the name in main.py file to match the name of the pdf file you have in utils folder.
 
now open the local host 8000 on browser and you will see the extracted text in json format