# AI Autocorrect and Suggestion Tool

## Project Overview

The AI Autocorrect and Suggestion Tool is a Natural Language Processing (NLP) based application developed using Python and Streamlit. The project automatically corrects spelling mistakes and provides intelligent contextual word suggestions using Artificial Intelligence techniques.

The application combines:

* autocorrect library for spelling correction
* TextBlob for NLP refinement
* BERT transformer model for contextual predictions
* Streamlit for the web interface

# Features

## 1. Sentence Autocorrection

* Detects spelling mistakes
* Corrects words automatically
* Uses NLP-based refinement

### Example

Input:
i havf ti lern artificil inteligence

Output:
i have to learn artificial intelligence

## 2. AI Word Suggestions

* Uses BERT transformer model
* Predicts contextually suitable words
* Displays top suggestions

### Example

Input:
She is wearing a [MASK] today

Output:
she is wearing a dress today
she is wearing a jacket today
she is wearing a hat today


# Technologies Used

* Python
* Streamlit
* autocorrect
* TextBlob
* BERT
* Transformers

# Libraries Required

pip install streamlit autocorrect textblob transformers torch

# How to Run the Project

1. Save the code as app.py
2. Open terminal in the project folder
3. Run:

streamlit run app.py

4. The application opens in the browser automatically.

# Project Workflow

User Input
↓
Autocorrect Library
↓
TextBlob NLP Refinement
↓
BERT Contextual Prediction
↓
Final Output

# Future Enhancements

* Grammar correction
* Voice input support
* Real-time typing suggestions
* Multilingual support
* Custom-trained NLP models


# Conclusion

The AI Autocorrect and Suggestion Tool demonstrates how NLP and Transformer-based AI models can be integrated into a functional application for spell correction and contextual text prediction.
