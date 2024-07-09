import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()

    st.set_page_config(page_title="Invoice Extraction Bot")
    st.title("Invoice Extraction Bot...")
    st.subheader("I can help you in extracting invoice data")

    pdf = st.file_uploader("Upload invoices here", type = ["pdf"], accept_multiple_files=True)

    submit = st.button("Extract Data")

    if submit:
        with st.spinner('Running'):
            st.write("response")

        st.success("Run Successfully")

if __name__ == '__main__':
    main()