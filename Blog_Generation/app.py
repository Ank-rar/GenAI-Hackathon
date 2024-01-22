
import streamlit as st
from langchain.prompts import PromptTemplate
from chat import get_response


def getLLamaresponse(input_text,no_words,blog_style,num_sections):

   
    
    template="""
        Write a article in {blog_style}
         for a topic {input_text}
        within {no_words} words under {num_sections} headings.
         dont write heading number
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words','num_sections'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=get_response(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words,num_sections=num_sections))
    print(response)
    return response






st.set_page_config(page_title="Generate article",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate article 🤖")

input_text=st.text_input("Enter the article Topic")

## creating to more columns for additonal 2 fields

col1, col2, col3 = st.columns([5, 5, 5])

with col1:
    no_words = st.text_input('No of Words')

with col2:
    blog_style = st.selectbox('Writing the article in',
                              ('English', 'French', 'Italian', 'German', 'Spanish'), index=0)

with col3:
    num_sections = st.number_input('Number of Sections', min_value=1, max_value=10, value=4)

# Second column for inputting section content
    

# section_names = []
# for i in range(num_sections):
#     section_name = st.text_input(f'Section {i + 1} Content', key=f'section_{i + 1}')
#     section_names.append(section_name)

submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style,num_sections))
