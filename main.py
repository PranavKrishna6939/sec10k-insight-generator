import streamlit as st
from sec_edgar_downloader import Downloader
from bs4 import BeautifulSoup
import re
import google.generativeai as genai
import os

GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(
    page_title="Insight Generator",
    page_icon=":bar_chart:",
)

def load_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
        return None

def cleanhtml(raw_html):
    cleanstring = re.sub(r'<[^>]*>', '', raw_html)
    return re.sub(r'&#.*?;', ' ', cleanstring)

def word_count(string):
    words = string.split()
    return len(words)

def extract_text(input_string, start_marker, end_marker, prev_end, diff, x):
    input_string = input_string.lower()
    start_marker = start_marker.lower()
    end_marker = end_marker.lower()
    
    start_indices = [i for i in range(len(input_string)) if input_string.startswith(start_marker, i)]
    if (len(start_indices) > 2) :
        if ((start_indices[2]-start_indices[1]) > (start_indices[1]-start_indices[0]+10000)):
            start_index = start_indices[2]
        else:
            start_index = start_indices[1]
    else:
        start_index = start_indices[1]
        
    if start_index == -1:
        return "Start or end marker not found." 

    end_indices = [i for i in range(len(input_string)) if input_string.startswith(end_marker, i)]
    if (len(end_indices) > 2) :
        if ((end_indices[2]-end_indices[1]) > (end_indices[1]-end_indices[0]+10000)):
            end_index = end_indices[2]
        else:
            end_index = end_indices[1]
    else:
        end_index = end_indices[1]

    j = 1
    while ((j+1< len(start_indices)) and (start_index <= prev_end+diff)):
        start_index = start_indices[j+1]
        j += 1

    i = 1
    while ((i+1< len(end_indices)) and (end_index <= start_index+1000)):
        end_index = end_indices[i+1]
        i += 1

    if (x==1):
        start_index = start_indices[1] 
        
    if end_index == -1:
        return "Start or end marker not found." 
    return input_string[start_index + len(start_marker):end_index], end_index

st.title(" :blue[SEC 10K Filing] Insight Generator")
st.divider()
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
col1, col2= st.columns(2)

with col1:
    ticker = st.text_input(
        "Enter the stock ticker 👇",
        placeholder= "GOOGL, MSFT, AAPL, NVDA, etc",
    )

with col2:
    word_count = st.slider('Word Count?', 0, 1000, 10)


if st.button('Fetch'):
    with st.spinner('Fetching Reports and Generating Insights...'):
        dl = Downloader("JJBigDub", "jjbigdub@gmail.com")
        dl.get("10-K", ticker, limit=1)
        parent_folder_path = f"/home/ec2-user/sec10k/sec10k-insight-generator/sec-edgar-filings/{ticker}/10-K"
        directories = [dir for dir in os.listdir(parent_folder_path) if os.path.isdir(os.path.join(parent_folder_path, dir))]


        for directory in directories:
            files = os.listdir(os.path.join(parent_folder_path, directory))
            
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(parent_folder_path, directory, file)
                    with open(file_path, 'r') as f:
                        html_text = f.read()

        cleantext = cleanhtml(html_text)

        st.title('PART 1:   :green[_Business Overview_]   :briefcase:')
        st.divider()

        Part1_start = "Item 1"
        Part1_end = "Item 1A"
        Part1_text, prev_end = extract_text(cleantext, Part1_start, Part1_end, 0, 0, 1)
        Part1_input = f"Summarise the following SEC 10K Filing Part for {ticker} in about {word_count} words. ENSURE THAT YOU FOLLOW THE BELOW 4 GUIDELINES\n 1) Use multiple neccessary sub-heading, Company Overview and Products, Competition, R&D, Sales and Sourcing.\n 2) USE :orange[<insert sub-heading>] for sub-headings.\n 3) Present the answer in a markdown format. 4) DO NOT USE \' or \" characters in the answer.\n An example of a suitable Format is given as:\n # :orange[Fiscal Year Highlights]\n Nvidia's fiscal year 2024 witnessed: -\n **Rise in Product & Services Performance:**\n - Successful launch of Hopper and Grace CPUs.\n - Growth in gaming, data center, and automotive segments. \n- Sustained leadership in artificial intelligence (AI).\n Format your answer in such a way. The data to be summarised starts below this line. \n {Part1_text}"
        Part1_response = model.generate_content(Part1_input)
        Part1_output = Part1_response.candidates[0].content.parts[0].text
        st.markdown(f"""{Part1_output}""")

        st.title('PART 2:   :green[_Risk Factors_]   :exclamation:')
        st.divider()

        Part2_start = "Item 1A"
        Part2_end = "Item 1B"
        Part2_text, prev_end1 = extract_text(cleantext, Part2_start, Part2_end, prev_end, 0, 0)
        Part2_input = f"Summarise the following SEC 10K Filing Part for {ticker} in about {word_count} words. ENSURE THAT YOU FOLLOW THE BELOW 4 GUIDELINES\n 1) Use multiple neccessary sub-heading with bullet points, discussing Macroeconomic and Industry Risks, Business Risks, Legal and Regulatory Compliance Risks, Financial Risks and General Risks.\n 2) USE :orange[<insert sub-heading>] for sub-headings.\n 3) Present the answer in a markdown format.\n 4) DO NOT USE \' or \" characters in the answer.\n An example of a suitable format is given as:\n # :orange[Fiscal Year Highlights]\n Nvidia's fiscal year 2024 witnessed: -\n **Rise in Product & Services Performance:**\n - Successful launch of Hopper and Grace CPUs.\n - Growth in gaming, data center, and automotive segments. \n- Sustained leadership in artificial intelligence (AI).\n Format your answer in such a way. The data to be summarised starts below this line \n {Part2_text}"
        Part2_response = model.generate_content(Part2_input)
        Part2_output = Part2_response.candidates[0].content.parts[0].text
        st.markdown(f"""{Part2_output}""")

        st.title('PART 3:   :green[_Financial Highlights_]   :chart_with_upwards_trend:')
        st.divider()

        Part3_start = "Item 7"
        Part3_end = "Item 7A"
        Part3_text, _ = extract_text(cleantext, Part3_start, Part3_end, prev_end1, 0, 0)
        Part3_input = f"Summarise the following SEC 10K Filing Part for {ticker} in about {word_count} words. ENSURE THAT YOU FOLLOW THE BELOW 4 GUIDELINES\n 1) Use multiple neccessary sub-heading with bullet points, discussing Fiscal Year Highlights, Products and Services Performance, Segment wise Performance, Operating Expenses and Gross margin, Liquidity and Capital Resources and Conclusion.\n 2) USE :orange[<insert sub-heading>] for sub-headings.\n 3) Present the answer in a markdown format.\n 4) DO NOT USE \' or \" characters in the answer.\n An example of a suitable format is given as:\n # :orange[Fiscal Year Highlights]\n Nvidia's fiscal year 2024 witnessed: -\n **Rise in Product & Services Performance:**\n - Successful launch of Hopper and Grace CPUs.\n - Growth in gaming, data center, and automotive segments. \n- Sustained leadership in artificial intelligence (AI).\n Format your answer in such a way. The data to be summarised starts below this line \n {Part2_text}"
        Part3_response = model.generate_content(Part3_input)
        Part3_output = Part3_response.candidates[0].content.parts[0].text
        st.markdown(f"""{Part3_output}""")
    st.success('Generation Complete!')
        
