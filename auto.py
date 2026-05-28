import streamlit as st
from autocorrect import Speller
from textblob import TextBlob
from transformers import pipeline

spell = Speller(lang='en')
from transformers import (
    BertTokenizer,
    BertForMaskedLM,
    pipeline
)

tokenizer = BertTokenizer.from_pretrained(
    "bert-base-uncased"
)

model = BertForMaskedLM.from_pretrained(
    "bert-base-uncased"
)

fill_mask = pipeline(
    "fill-mask",
    model=model,
    tokenizer=tokenizer
)
st.title("AI Autocorrect and Suggestion Tool")
option = st.radio(
    "Choose Function",
    (
        "Correct Sentence",
        "Get AI Suggestions"
    )
)


if option == "Correct Sentence":

    text = st.text_input(
        "Enter a sentence"
    )

    if text:
        auto_corrected = spell(text)
        blob = TextBlob(auto_corrected)
        final_corrected = str(blob.correct())
        st.subheader("Corrected Sentence")
        st.success(final_corrected)
        st.subheader("Correction Process")
        st.write("Original:", text)
        st.write(
            "After Autocorrect:",
            auto_corrected
        )
        st.write(
            "After TextBlob:",
            final_corrected
        )
if option == "Get AI Suggestions":

    sentence = st.text_input(
        "Enter sentence using [MASK]"
    )
    if sentence:
        results = fill_mask(sentence)
        st.subheader("AI Suggestions")
        for r in results[:5]: #5 results will be printed
            st.write(
                "•",
                r['sequence']
            )

st.markdown("""
    <style>

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    [data-testid="stStatusWidget"] {
        visibility: hidden;
    }

    [data-testid="stDeployButton"] {
        display: none;
    }

    </style>
""", unsafe_allow_html=True)
