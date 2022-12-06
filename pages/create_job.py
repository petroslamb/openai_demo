import streamlit as st
import openai

st.markdown("# Create Jobs :file_cabinet:")
st.sidebar.markdown("# create jobs ️:file_folder:")

model_list = openai.Model.list()
model_names = [model["id"] for model in model_list["data"]]


model_names = ["text-davinci-003"] + model_names

model = st.sidebar.selectbox("Select a model", model_names, index=0)

# Get the model for the selected model
st.sidebar.write(openai.Model.retrieve(model))

@st.cache
def call_the_model(prompt):
    result = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.9,
        max_tokens=550,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return result['choices'][0]['text']

# Create a text prompt input in the main page. This will be used to send input to the OpenAI API. 
# The result will be displayed in the main page.

st.markdown("## Create a job description!")
prompt = st.text_area(
    "Modify the prompt to your liking", 
    value="Generate in Markdown a job description for a Python Software Engineer in a Data Science team for the company Workable. Include an introduction of the company, the team, the role, the responsibilities, the requirements and the benefits."
    )


if prompt:
    st.markdown("### Job Description")
    st.write(call_the_model(prompt))