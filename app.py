import json

import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

import utils

with open('assets/data.json') as file:
    my_info = json.loads(file.read())

with open('assets/raj_kapadia.pdf', 'rb') as file:
    pdf_data = file.read()

lottie_animation = 'https://assets10.lottiefiles.com/packages/lf20_O2ci8jA9QF.json'
lottie_getintouch = 'https://assets5.lottiefiles.com/private_files/lf30_T12D5w.json'
img_heroku = Image.open('images/heroku.webp')
img_translate = Image.open('images/translate.webp')
img_photo = Image.open('images/my_photo-modified.png')

st.set_page_config(page_title='Raj Kapadia', page_icon=':tada:', layout='wide')
st.markdown(utils.local_css('style/style.css'), unsafe_allow_html=True)

with st.container():
    left, right = st.columns((2, 3), gap='small')

    with right:
        st.subheader(my_info['header'])
        st.title(my_info['title'])
        st.write(my_info['about_me'])

        st.download_button(
            label=" 📄 Download Resume",
            data=pdf_data,
            file_name='RajKKapadia.pdf',
            mime="application/octet-stream",
        )

        st.write(my_info['github'])
    
    with left:
        st.image(img_photo, width=200)

with st.container():
    st.write('---')
    interests, annimation = st.columns((2, 3), gap='small')

    with interests:
        st.write(
            '''
            ## My interests are:
            * Chatbot development using Dialogflow CX/ES, RASA
            * Computer Vision
            * Natural Language Processing
            * RESTFul API development Python+Falsk and NodeJS+Express
            * Machine Learning projects
            '''
        )
        st.write(my_info['youtube'])
    
    with annimation:
        st_lottie(
            utils.load_data_from_url(lottie_animation),
            height=300,
            key='animation'
        )

with st.container():
    st.write('---')
    st.header('My Projects')
    image, text = st.columns((1, 3), gap='small')

    with image:
        st.image(img_heroku)

    with text:
        st.subheader('How to deploy Python Application on Heroku')
        st.write(
            '''
            Hello friends,
            In this video, I will show you how you can deploy a Python Flask application on Heroku for free and even use it for free up to its limit.
            You will need the following things:
            * active Heroku account [here](https://www.heroku.com/)
            * Github account
            * Python installed on your system
            * optional CONDA virtual environment
            The code used in this video can be found at my [GitHub repository](https://github.com/RajKKapadia/Heroku-Python-Youtube-Demo)
            '''
        )
        st.markdown('[Watch the video >](https://youtu.be/x8hVoalU0MA)')

with st.container():
    st.write('---')
    image, text = st.columns((1, 3), gap='small')

    with image:
        st.image(img_translate)

    with text:
        st.subheader('Google Cloud Translate API with NodeJS')
        st.write(
            '''
            Hello everyone, I will talk about how you can use Google Cloud Translate API with NodeJS step by step.
            - Create a new Google Cloud Project, get service account key, enable Google Cloud Translate API
            - NodeJS part, you need to watch the video.
            The code used in this video can be found at my [GitHub repository](https://github.com/RajKKapadia/Google_Translate_Youtube_Demo)
            '''
        )
        st.markdown('[Watch the video >](https://youtu.be/Sjl9ilOpHG8)')

with st.container():
    st.write('---')
    st.header('Get in touch with me...')

    contact_form = '''
    <form action="https://formsubmit.co/50aae58420241ff21a01db9f23cc81b6" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <input type="text" name="service" placeholder="What kind of service you are looking for..." required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''

    form, empty = st.columns(2)
    with form:
        st.markdown(contact_form, unsafe_allow_html=True)
    with empty:
        st_lottie(
            utils.load_data_from_url(lottie_getintouch),
            height=300,
            key='getintouch'
        )