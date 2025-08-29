from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv
from getpass4 import getpass
# Load environment variables
load_dotenv(override=True)

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY") 
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")    
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING") 
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"




#promt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates English to French."),
        ("human",  "Input: {input}"),
    ]
)

#streamlit framework
st.title("English to French Translator")
input_text = st.text_input("Enter text in English:")

#0llama model
llm = OllamaLLM(model="gemma3:1b", temperature=0.2)
output_parser = StrOutputParser()
chain = prompt |llm | output_parser

button =  st.button("Translate")

if button and input_text:  
    st.write("Translating...")
    result = chain.invoke({"input": input_text})
    st.write("Translation:", result)
else:   
    st.write("Please enter text to translate.")


#ollama run gemma3:1b runn this in command promt than execute the app