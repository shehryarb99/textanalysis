import streamlit as st
from textblob import TextBlob
from pattern.en import pluralize, singularize, comparative, superlative
import spacy  # Add import for spaCy

# Define function for Named Entity Recognition
def named_entity_recognition(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    st.success(f"Entities: {entities}")

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

def main():
    st.title("Text Analysis App")

    # Spell Correction Section
    st.header("Spell Correction")
    text_data = st.text_area("Enter Text Here")
    corrected_text = TextBlob(text_data).correct()
    if st.button("Correction"):
        st.success(corrected_text)

    # Pluralize/Singularize Section
    st.header("Pluralize/Singularize")
    text_data1 = st.text_input("Enter a word For pluralize / singularize")
    if st.checkbox("Pluralize"):
        st.warning(pluralize(text_data1))
    if st.checkbox("Singularize"):
        st.warning(singularize(text_data1))

    # Comparative/Superlative Section
    st.header("Comparative/Superlative")
    text2 = st.text_input("Enter Text For comparative & superlative")
    if st.checkbox("Comparative"):
        st.success(comparative(text2))
    if st.checkbox("Superlative"):
        st.success(superlative(text2))

    # Sentiment Analysis Section
    st.header("Sentiment Analysis")
    sentiment_text = st.text_area("Enter text for sentiment analysis")
    if st.button("Analyze Sentiment"):
        sentiment_result = analyze_sentiment(sentiment_text)
        st.success(f"Sentiment: {sentiment_result}")

    # Named Entity Recognition Section
    st.header("Named Entity Recognition")
    text_for_ner = st.text_area("Enter Text for Named Entity Recognition")
    if st.button("Perform NER"):
        named_entity_recognition(text_for_ner)

if __name__ == '__main__':
    main()
