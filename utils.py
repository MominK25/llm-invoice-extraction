from langchain.llms import openai
from pypdf import PdfReader
from langchain.llms.openai import OpenAI
import pandas as pd
import re
import replicate
from langchain.prompts import PromptTemplate

def get_pdf_text(pdf_doc)
    text =""
    pdf_reader  = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def 
