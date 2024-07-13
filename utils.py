from langchain.llms import openai
from pypdf import PdfReader
from langchain.llms.openai import OpenAI
import pandas as pd
import re
import replicate
from langchain.prompts import PromptTemplate

#Extracting data from PDF files
def get_pdf_text(pdf_doc):
    text =""
    pdf_reader  = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

#Function to extract data form text using LLM
def extracted_data(pages_data):
    template = """Extract all the following values : invoice no., Description, Quantity, date, 
        Unit price, Amount, Total, email, phone number and address from this data: {pages}
    
        Expected output: remove any dollar symbols {{'Invoice no.': '1001329', 'Description': 'Office Chair', 'Quantity': '2', 'Date': '5/4/2023, 'Unit price': '1100.00', 'Amount': '2200.00', 'Total': '2200.00', 'Email': 'Santoshvarma0988@gmail.com', 'Phone number': '9999999999', 'Address': 'Mumbai, India' }}
        """
    prompt_template = PromptTemplate(input_variables=["pages"], template=template)

    llm = OpenAI(temperature=0.7)
    full_response=llm(prompt_template.format(pages=pages_data))

    print("LLM ResponseL ", full_response)

    return full_response

def create_docs(user_pdf_list):


    df = pd.DataFrame({'Invoice no.': pd.Series(dtype='str'),
                       'Description': pd.Series(dtype='str'),
                       'Quantity': pd.Series(dtype='str'),
                       'Date': pd.Series(dtype='str'),
                       'Unit price': pd.Series(dtype='str'),
                       'Amount': pd.Series(dtype='int'),
                       'Total': pd.Series(dtype='str'),
                       'Email': pd.Series(dtype='str'),
                       'Phone number': pd.Series(dtype='str'),
                       'Address': pd.Series(dtype='str')
                       })
    
    for filename in user_pdf_list:

        print(filename)
        raw_data=get_pdf_text(filename)


        llm_extracted_data=extracted_data(raw_data)
        print("Extracted Data: ", llm_extracted_data)

        #Capture kjust the required data and excluding unwanted text from the LLM
        pattern = r'{(.+)}'
        match = re.search(pattern, llm_extracted_data, re.DOTALL)

        if match:
            extracted_text = match.group(1)

            data_dict = eval('{' + extracted_text +'}')
            print(data_dict)
            temp_df = pd.DataFrame([data_dict])
            df = pd.concat([df, temp_df], ignore_index=True)
        else:
            print('No Match Found.')
 #           data_dict = {}

    #    df=df.append([data_dict], ignore_index=True)
        print("******************DONE**************")

    print("Final Dataframe:", df.head())
    return df