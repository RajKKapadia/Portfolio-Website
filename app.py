import json
import os

import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

import utils

with open('assets/data.json') as file:
    my_info = json.loads(file.read())

with open('assets/raj_kapadia.pdf', 'rb') as file:
    pdf_data = file.read()

lottie_animation = 'https://assets10.lottiefiles.com/packages/lf20_O2ci8jA9QF.json'
lottie_getintouch = 'https://assets5.lottiefiles.com/private_files/lf30_T12D5w.json'
img_quiz_bot = Image.open('images/quiz_bot.webp')
img_translate = Image.open('images/translate.webp')
img_photo = Image.open('images/my_photo-modified.png')

st.set_page_config(page_title='Raj Kapadia', page_icon='😎', layout='wide')
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
    
    with left:
        st.image(img_photo, width=200)

st.write('---')
st.header('Connect with me...')

c1, c2, c3, c4 = st.columns(4)
with st.container():
    c1.write(my_info['github'])
    c2.write(my_info['fiverr'])
    c3.write(my_info['upwork'])
    c4.write(my_info['linkedin'])

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
        st.image(img_quiz_bot)

    with text:
        st.subheader('How to deploy Python Application on Heroku')
        st.write(
            '''
            Hello everyone, welcome to this tutorial series on Google Dialogflow, you will learn the following things from this tutorial series:
            * build a maths quiz chat-bot
            * develop the back-end functionality in NodeJS
            * connect the maths quiz chat-bot to Telegram
            * test everything
            * deploy the back-end on Render
            The code used in this video can be found at my [GitHub repository](https://github.com/RajKKapadia/YouTube-Quiz-Chatbot-Dialogflow)
            '''
        )
        st.markdown('[Watch the video >](https://youtu.be/dMUbKaI003E)')

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

    contact_form = f'''
    <form action="https://formsubmit.co/{os.getenv("form_submit")}" method="POST">
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