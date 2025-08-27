> **Note:** The following article is reproduced verbatim from  
> Codecademy Team, *Codecademy* (2025):  
> [Build a Sentiment Analysis App with Hugging Face and Streamlit](https://www.codecademy.com/article/hugging-face-with-streamlit-app)  
> for internal educational use only (non-profit).

# Build a Sentiment Analysis App with Hugging Face and Streamlit

Sentiment analysis helps computers understand if text expresses positive, negative, or neutral emotions. In this tutorial, we'll build a web app that analyzes emotions in text using Hugging Face transformers and Streamlit. You'll learn how to use pre-trained AI models to create a professional sentiment analyzer that can process any text input and provide confidence scores for its predictions.

Let's get started.

## Step 1: Setting up the environment

Before we start coding, we need to set up our development environment with all the necessary tools.

### Create a project directory

First, create a new folder for the project and navigate into it:

```bash
mkdir sentiment-analysis-app
cd sentiment-analysis-app
```

### Set up a Python virtual environment

A virtual environment keeps the project dependencies isolated from other Python projects on your computer:

```bash
python -m venv sentiment_env
# Activate on Windows: sentiment_env\Scripts\activate
# Activate on Mac/Linux: source sentiment_env/bin/activate
```

### Install required libraries

Install all the libraries we'll need for sentiment analysis:

```bash
pip install transformers torch streamlit pandas plotly
```

Here's what each library does:

- **transformers**: Provides access to Hugging Face pre-trained models
- **torch**: The deep learning framework that runs the models
- **streamlit**: Creates web interfaces with Python
- **pandas**: Handles data in table format

### Create project files

Create two Python files in your project directory:

- `sentiment_utils.py` - Contains helper functions
- `app.py` - Main application file

This will be our final project structure:

```
sentiment-analysis-app/
├── app.py
├── sentiment_utils.py
└── sentiment_env/
```

## Step 2: Building the sentiment analysis utility

Let's start by creating the core sentiment analysis functionality in `sentiment_utils.py`:

```python
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import plotly.express as px

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the sentiment analysis pipeline
        self.pipeline = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest",
            tokenizer="cardiffnlp/twitter-roberta-base-sentiment-latest"
        )
        
    def analyze_text(self, text):
        """
        Analyze the sentiment of a given text
        Returns: dict with label and score
        """
        if not text.strip():
            return {"label": "NEUTRAL", "score": 0.0}
        
        result = self.pipeline(text)[0]
        return {
            "label": result["label"],
            "score": result["score"]
        }
    
    def analyze_multiple_texts(self, texts):
        """
        Analyze multiple texts and return results as a DataFrame
        """
        results = []
        for text in texts:
            if text.strip():
                result = self.analyze_text(text)
                results.append({
                    "text": text,
                    "sentiment": result["label"],
                    "confidence": result["score"]
                })
        
        return pd.DataFrame(results)
    
    def create_sentiment_chart(self, df):
        """
        Create a bar chart showing sentiment distribution
        """
        if df.empty:
            return None
        
        sentiment_counts = df["sentiment"].value_counts()
        fig = px.bar(
            x=sentiment_counts.index,
            y=sentiment_counts.values,
            title="Sentiment Distribution",
            labels={"x": "Sentiment", "y": "Count"}
        )
        return fig

# Initialize the analyzer
analyzer = SentimentAnalyzer()
```

## Step 3: Creating the Streamlit web app

Now let's build the user interface in `app.py`:

```python
import streamlit as st
import pandas as pd
from sentiment_utils import analyzer

# Configure the page
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="wide"
)

# Main title and description
st.title("😊 Sentiment Analysis App")
st.markdown("""
This app analyzes the sentiment of your text using AI models from Hugging Face.
Upload a file or enter text to get started!
""")

# Sidebar for options
st.sidebar.header("Options")
analysis_type = st.sidebar.selectbox(
    "Choose analysis type:",
    ["Single Text", "Multiple Texts", "File Upload"]
)

# Main content area
if analysis_type == "Single Text":
    st.header("Single Text Analysis")
    
    # Text input
    user_text = st.text_area(
        "Enter your text here:",
        height=150,
        placeholder="Type or paste your text here..."
    )
    
    if st.button("Analyze Sentiment"):
        if user_text.strip():
            with st.spinner("Analyzing..."):
                result = analyzer.analyze_text(user_text)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Sentiment")
                sentiment_emoji = {
                    "POSITIVE": "😊",
                    "NEGATIVE": "😞",
                    "NEUTRAL": "😐"
                }
                st.write(f"{sentiment_emoji.get(result['label'], '😐')} {result['label']}")
            
            with col2:
                st.subheader("Confidence")
                st.progress(result['score'])
                st.write(f"{result['score']:.2%}")
            
            # Show the analyzed text
            st.subheader("Analyzed Text")
            st.write(user_text)
        else:
            st.warning("Please enter some text to analyze.")

elif analysis_type == "Multiple Texts":
    st.header("Multiple Texts Analysis")
    
    # Text input for multiple texts
    texts_input = st.text_area(
        "Enter multiple texts (one per line):",
        height=200,
        placeholder="Enter your first text here...\nEnter your second text here...\nEnter your third text here..."
    )
    
    if st.button("Analyze All"):
        if texts_input.strip():
            texts = [text.strip() for text in texts_input.split('\n') if text.strip()]
            
            with st.spinner("Analyzing multiple texts..."):
                results_df = analyzer.analyze_multiple_texts(texts)
            
            # Display results table
            st.subheader("Analysis Results")
            st.dataframe(results_df)
            
            # Create and display chart
            if not results_df.empty:
                st.subheader("Sentiment Distribution")
                chart = analyzer.create_sentiment_chart(results_df)
                if chart:
                    st.plotly_chart(chart, use_container_width=True)

elif analysis_type == "File Upload":
    st.header("File Upload Analysis")
    
    uploaded_file = st.file_uploader(
        "Choose a text file:",
        type=['txt', 'csv']
    )
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                # Assuming the text column is named 'text'
                if 'text' in df.columns:
                    texts = df['text'].tolist()
                else:
                    st.error("CSV file must contain a 'text' column")
                    st.stop()
            else:
                # For .txt files
                content = uploaded_file.read().decode('utf-8')
                texts = [line.strip() for line in content.split('\n') if line.strip()]
            
            if st.button("Analyze File"):
                with st.spinner("Analyzing file contents..."):
                    results_df = analyzer.analyze_multiple_texts(texts)
                
                # Display results
                st.subheader("Analysis Results")
                st.dataframe(results_df)
                
                # Create and display chart
                if not results_df.empty:
                    st.subheader("Sentiment Distribution")
                    chart = analyzer.create_sentiment_chart(results_df)
                    if chart:
                        st.plotly_chart(chart, use_container_width=True)
                        
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**About this app:**
- Built with Hugging Face Transformers
- Powered by Streamlit
- Uses the Twitter RoBERTa model for sentiment analysis
""")
```

## Step 4: Running the application

Now let's run our sentiment analysis app:

```bash
streamlit run app.py
```

This will start the web server and open your browser to the application. You should see a clean interface where you can:

1. **Single Text Analysis**: Enter individual text and get sentiment results
2. **Multiple Texts**: Analyze several texts at once
3. **File Upload**: Upload CSV or text files for batch analysis

## Step 5: Understanding the results

The app provides several types of output:

### Sentiment Labels
- **POSITIVE**: Text expresses positive emotions
- **NEGATIVE**: Text expresses negative emotions
- **NEUTRAL**: Text is emotionally neutral

### Confidence Scores
Each prediction comes with a confidence score (0-1) indicating how certain the model is about its prediction.

### Visualizations
The app creates interactive charts showing the distribution of sentiments across multiple texts.

## Step 6: Customizing the model

You can easily switch to different Hugging Face models by modifying the pipeline initialization:

```python
# For a different sentiment model
self.pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    tokenizer="nlptown/bert-base-multilingual-uncased-sentiment"
)

# For emotion detection
self.pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)
```

## Advanced Features

### Adding more analysis types

You can extend the app with additional NLP tasks:

```python
# Named Entity Recognition
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# Text summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Question answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
```

### Improving performance

For production use, consider:

1. **Model caching**: Cache model predictions to avoid re-computation
2. **Batch processing**: Process multiple texts efficiently
3. **Error handling**: Add robust error handling for edge cases
4. **Model optimization**: Use quantized models for faster inference

## Conclusion

Congratulations! You've built a complete sentiment analysis web application using Hugging Face transformers and Streamlit. This app demonstrates how to:

- Use pre-trained transformer models for NLP tasks
- Create interactive web interfaces with Streamlit
- Process both single texts and batch files
- Visualize results with interactive charts
- Structure code for maintainability and extensibility

The skills you've learned here can be applied to build other NLP applications like:
- Text classification systems
- Named entity recognition tools
- Language translation apps
- Text summarization tools

Keep experimenting with different models and features to expand your AI application development skills!
