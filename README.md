# Day_3

** do again 

##Step 1 - Create Virtual Environment

create virtual environment
python -m venv .venv **
make sure the .venv folder was created, then activate virtual environment
source .venv/bin/activate **

##Step 2 - Install Dependencies / Python Libraries

create a requirements.txt file ***
add, each on a newline, openai + streamlit + python-dotenv + chromadb + pypdf 

##make sure to freeze open AI

run:
pip install -r requirements.txt ** do again 
pip freeze > requirements.txt #freeze verions to rely on them **do this every time you add a new library

##Step 3 - Create a .env file to store our secrets (including OpenAI API Key)

create .env file
touch .env
add the OPENAI_API_KEY to the .env file
password = "" 

#add pages folder 

mkdir pages 

# add streamlit entrypoint file 
- touch home.py

#run streamlit server 

- streamlit run home.py ***