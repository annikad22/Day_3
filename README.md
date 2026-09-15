# Day_3

##Step 1 - Create Virtual Environment

create virtual environment
python -m venv .venv
make sure the .venv folder was created, then activate virtual environment
source .venv/bin/activate

##Step 2 - Install Dependencies / Python Libraries

create a requirements.txt file
add, each on a newline, openai + streamlit + python-dotenv + chromadb + pypdf 

##make sure to freeze open AI

run:
pip install -r requirements.txt
pip freeze > requirements.txt #freeze verions to rely on them 

##Step 3 - Create a .env file to store our secrets (including OpenAI API Key)

create .env file
touch .env
add the OPENAI_API_KEY to the .env file
password = "" 