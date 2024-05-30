import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

def getLLMResponse(form_input,email_sender,email_recipient,email_style):
    
    llm = CTransformers(model='TheBloke/Llama-2-7B-Chat-GGML',    
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
    
    
    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:
    
    """

    prompt = PromptTemplate(
    input_variables=["style","email_topic","sender","recipient"],
    template=template,)

    response=llm.invoke(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_recipient,style=email_style))
    print(response)

    return response


st.set_page_config(page_title="Generate Emails",
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Emails")

form_input = st.text_area('Enter the email subject', height=275)

col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    email_sender = st.text_input('Sender Name')
with col2:
    email_recipient = st.text_input('Recipient Name')
with col3:
    email_style = st.selectbox('Writing Style',
                                    ('Formal', 'Appreciating', 'Not Satisfied', 'Neutral'),
                                       index=0)


submit = st.button("Generate")


if submit:
    st.write(getLLMResponse(form_input,email_sender,email_recipient,email_style))
