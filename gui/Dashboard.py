import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.MemorablePasswordGenerator import MemorablePasswordGenerator
from src.Pin_Generator import PinGenerator
from src.Random_Password_Generator import RandomPasswordGenerator

st.title(":lock: Password Generator")
option = st.radio("select a password generator" , ('Pin Code' , 'Memorable Password' ,'Random Password' ))
if option == 'Pin Code':
    length = st.slider('Select the length of your password' , 4 , 34 )
    generator = PinGenerator(length)
elif option == 'Random Password':
    length = length = st.slider('Select the length of your password' , 8 , 34 )
    include_symbols = st.toggle('include symbols')
    include_numbers = st.toggle('include numbers')
    generator = RandomPasswordGenerator( include_numbers = include_numbers , include_symbols = include_symbols , length = length  )
elif option == 'Memorable Password' :
    num_of_words =  st.slider('Select the number of words you want' , 4 , 34 )
    separator = st.text_input('separator')
    capitalize = st.toggle('capitalization')
    generator = MemorablePasswordGenerator(num_of_words , capitalize , separator)
st.write(f'Your password is: `{generator.generate()}`')
