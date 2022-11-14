import streamlit as st
from happytransformer import HappyTextToText
from happytransformer import TTSettings


@st.cache
def load_model():
    happy_tt_model = HappyTextToText("T5", "t5-base", load_path='model/')
    return happy_tt_model


happy_tt = HappyTextToText("T5", "t5-base", load_path='model/')
beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)

st.title('Grammar Correction Using Happy Transformer')

input_user = st.text_area('Add a sentence or paragraph to correct grammar')


def predict_model(input_):
    text = "grammar: " + input_
    result = happy_tt.generate_text(text, args=beam_settings)
    return result


if st.button("Predict"):
    st.text(predict_model(input_user).text)
