# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:55:36 2024

@author: Kelum.Perera
"""


import pandas as pd
from presidio_analyzer import AnalyzerEngine

# Sample DataFrame
data = {
    'text': [
        "Kelum Perera's phone number is 425-555-1234",
        "Visit https://www.kelum123.com for more info",
        "No PII here"
    ]
}
df = pd.DataFrame(data)

# Initialize the AnalyzerEngine
analyzer = AnalyzerEngine()

# Function to detect PII in a text string and replace it with asterisks
def detect_and_replace_pii(text):
    analysis_results = analyzer.analyze(text=text, language='en')
    pii_entity_types = []
    pii_texts = []
    text_modified = text
    offset = 0
    
    # Filter out URL results
    analysis_results = [result for result in analysis_results if result.entity_type != 'URL']
    
    for result in analysis_results:
        pii_entity_types.append(result.entity_type)
        pii_texts.append(text[result.start:result.end])
        
        # Calculate the replacement text
        replacement = '*' * (result.end - result.start)
        
        # Replace the PII text with asterisks
        text_modified = text_modified[:result.start + offset] + replacement + text_modified[result.end + offset:]
        
        # Update the offset due to text modifications
        offset += len(replacement) - (result.end - result.start)
    
    return text_modified, pii_entity_types, pii_texts

# Apply the function to the DataFrame column
df[['text_modified', 'entity_types', 'pii_texts']] = df.apply(lambda row: pd.Series(detect_and_replace_pii(row['text'])), axis=1)

# Replace the original text with the modified text
df['text'] = df['text_modified']
df.drop('text_modified', axis=1, inplace=True)

# Display the results
print(df)