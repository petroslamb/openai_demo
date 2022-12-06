import os
import streamlit as st
import openai

st.markdown("# OpenAI Demo 🎈")
st.sidebar.markdown("# OpenAI Demo 🎈")

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

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

st.markdown("## Job Description")
job_description = st.text_area("Enter a job description here", height=400, value='''Job description: 

Python Developer

We are looking for a highly skilled software engineer with experience in Python and cloud technologies.
The successful candidate will be responsible for designing, implementing, and maintaining complex software systems, as well as collaborating with cross-functional teams to drive innovation and excellence.

Candidate Requirements:
- Bachelor's degree in Computer Science or a related field
- 5+ years of experience in software engineering
- Strong proficiency in Python and cloud technologies (e.g. AWS, Azure, GCP)
- Experience with agile development processes and best practices''')

# Create a dropdown with questions on the job description
job_description_questions = [
    "What is the job title?", "What are the candidate requirements?", "How many years of experience are required?",
    "What level of education is required?", "Where is this job located?",
    "What are the skills required?", "What are the responsibilities of the candidate?",
    "What are the benefits of the job?", "What are the perks of the job?",
    ]

job_description_question = st.selectbox("Select a question", job_description_questions)

# Create a button to send the question to the OpenAI API
button = st.button("Get Answer for Job")

if button:
    response = call_the_model(job_description + "\n\nQ: " + job_description_question + "\nA:")
    st.markdown("### Answer")
    st.write(response)



st.markdown("## Resume")
resume = st.text_area("Enter a resume here", height=400, value='''Resume:

John Doe
Software Engineer

Education:
- Bachelor's degree in Computer Science, XYZ University (2014-2018)

Experience:
- Software Engineer, ABC Corporation (2018-present)
- Developed and maintained Python-based software systems using AWS, Azure, and GCP
- Collaborated with cross-functional teams to drive innovation and excellence
- Utilized agile development processes and best practices

Skills:
- Python
- Cloud technologies (AWS, Azure, GCP)
- Agile development processes
- Best practices in software engineering

Contact:
- Email:
- Phone: 555-555-5555''')

# Create a dropdown with questions on the resume
resume_questions = [
    "What is the candidate's name?", 
    "What is the candidate's email?", "What is the candidate's phone number?",
    "What is the candidate's education?", "What is the candidate's experience?", "What are the candidate's skills?",
    "Where is the candidate located?", "What is the candidate's current job title?", "What is the candidate's current employer?",
    "What is the candidate's previous job title?", "What is the candidate's previous employer?",
    "Where is the cadidate's previous job located?", "What is the candidate's previous job start date?",
    "How many years of experience does the candidate have?", "What is the candidate's current job start date?"
    ]

resume_question = st.selectbox("Select a question", resume_questions)

# Create a button to send the question to the OpenAI API
button = st.button("Get Answer for Candidate")

if button:
    response = call_the_model(resume + "\n\nQ: " + resume_question + "\nA:")
    st.markdown("### Answer")
    st.write(response)


st.markdown("### Combined Questions")

combined_questions = [
    "Is the candidate qualified for the job?",
    "Has the candidate the experience required for the job?",
    "Does the candidate have the skills required for the job?",
    "Does the candidate have the education required for the job?",
    "Does the candidate have the location required for the job?",
    "Does the candidate have the job title required for the job?",
    "What are the condidates strengths for being a good fit for the job?",
    "What are the condidates weaknesses for not being a good fit for the job?",
]

combined_question = st.selectbox("Select a question", combined_questions)

if combined_question:
    response = call_the_model(job_description + "\n\n" + resume + "\n\nQ: " + combined_question + "\nA:")
    st.markdown("### Answer")
    st.write(response)


st.markdown("## Open ended questions")

open_ended_question = st.text_input(
    "Enter an open ended question here", 
    value="What is a list of technical interview questions for this candidate, that relate to the job requirements?"
    )

prompt = job_description + "\n\nResume: \n\n" + resume + "\n\n Q: " + open_ended_question + "\nA:"

button = st.button("Get Answer for Open Ended Question")

if button:
    response = call_the_model(prompt)
    st.markdown("### Answer")
    st.write(response)
