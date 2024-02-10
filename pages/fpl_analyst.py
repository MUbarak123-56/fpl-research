import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType

st.set_page_config(page_title='FPL Data Analyst')
st.markdown("<h5 style='text-align: center;'>Hey There, Soccer Friends. Load your FPL data for GPT to analyze.</h5>", unsafe_allow_html=True)

def load_file(input_file):
  if input_file.name[-4:] == ".csv":
      df = pd.read_csv(input_file)
  elif input_file.name[-5:] == ".xlsx":
      df = pd.read_excel(input_file)
  with st.expander('See DataFrame'):
    st.write(df)
  return df

# Generate LLM response
def generate_response(input_file, input_query):
  llm = ChatOpenAI(model_name='gpt-4', temperature=0.1, openai_api_key=openai_api_key)
  df = load_file(input_file)
  # Create Pandas DataFrame Agent
  agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
  # Perform Query using the Agent
  response = agent.run(input_query)
  return st.success(response)

# Input widgets
uploaded_file = st.file_uploader('Upload a CSV or Excel file', type=['csv', 'xlsx'])
question_list = [
  'Who had the highest number of points on GW 38 in the 2022/23 season?',
  'Other']
query_text = st.selectbox('Select an example query:', question_list, disabled=not uploaded_file)
openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text))

# App logic
if query_text is 'Other':
  query_text = st.text_input('Enter your query:', placeholder = 'Enter query here ...', disabled=not uploaded_file)
if not openai_api_key.startswith('sk-'):
  st.warning('Please enter your OpenAI API key!', icon='⚠')
if openai_api_key.startswith('sk-') and (uploaded_file is not None):
  st.header('Output')
  generate_response(uploaded_file, query_text)
  
st.link_button("You can also have a chat with our custom-made FPL Analyst on GPT here", "https://chat.openai.com/g/g-OxrmR8wbw-fantasy-league-analyst")
