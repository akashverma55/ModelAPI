# |===================Importing the Libraries=======================|

from langchain.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# |=================================================================|

# |=================Loading Environment Variable====================|

# load_dotenv()  
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# |=================================================================|

# |===================Creating FastAPI App==========================|

app = FastAPI(
    title = 'Langchain Server',
    versions = '1.0',
    Description = 'Simple API Server'
)

# |=================================================================|

# |===================Initializing the LLM Model=====================|

llm = Ollama(model = "qwen")

# |=================================================================|

# |===================Creating the Prompts=======================|

prompt1 = ChatPromptTemplate.from_template("Write an explanation on {topic} between 100 to 150 words without its advantages and disadvantages.")
prompt2 = ChatPromptTemplate.from_template("Write 5 advantages and disadvantages about the {topic}") 

# |=================================================================|

# |===================Adding Routes For API APP=====================|

add_routes(
    app,
    prompt1|llm,
    path = "/explanation"
)
add_routes(
    app,
    prompt2|llm,
    path = "/adv&disadv"
)

# |=================================================================|

# |===================Initializing the Server=======================|

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

# |=================================================================|
