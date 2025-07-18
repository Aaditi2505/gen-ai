# -*- coding: utf-8 -*-
"""predict word.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18ufENQu-mIeWWghRTJaj-q11PQ1DxQI1
"""

# Step 1: Install transformers if not already installed
!pip install transformers

# Step 2: Import pipeline
from transformers import pipeline

# Step 3: Load BERT model for fill-mask task
fill_mask = pipeline("fill-mask", model="bert-base-uncased")

# Step 4: Take input from user
user_input = input("Enter [MASK] in the sentence where you want the model to predict a word : ")

# Step 5: Predict and show result
output = fill_mask(user_input)

# Step 6: Print predictions
print("\nPredictions:")
for prediction in output:
    print(f"{prediction['sequence']}  |  Score: {prediction['score']:.4f}")