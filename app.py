import streamlit as st
from dotenv import load_dotenv
from utils import *

def main():
    load_dotenv()

    st.set_page_config(page_title="Invoice Extraction Bot")
    st.title("Invoice Extraction Bot...")
    st.subheader("I can help you in extracting invoice data")

    pdf = st.file_uploader("Upload invoices here", type = ["pdf"], accept_multiple_files=True)

    submit = st.button("Extract Data")

    if submit:
        with st.spinner('Running'):


            df=create_docs(pdf)
            
            st.write(df.head())

            data_as_csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download data as CSV",
                data_as_csv,
                "Invoice_extracted_data.csv",
                "text/csv",
                key="download-tools-csv",
            )

        st.success("Run Successfully")

if __name__ == '__main__':
    main()