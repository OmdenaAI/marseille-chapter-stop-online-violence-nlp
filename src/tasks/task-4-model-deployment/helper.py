# import streamlit as st

import numpy as np
import transformers
import tensorflow as tf
from transformers import AutoTokenizer, CamembertModel, TFAutoModelForSequenceClassification


    
def predict_text(prediction_value):
  if prediction_value == 0:
    return 'bullying'
  elif prediction_value == 1:
    return 'hate_speech'
  elif prediction_value == 2:
    return 'homophobia'
  elif prediction_value == 3:
    return 'non_toxic'
  elif prediction_value == 4:
    return 'racism'
  elif prediction_value == 5:
    return 'sexism'

# input_text = input("Enter a text to classify")

def classify(input_text):
  """
  This method takes in the input text and returns the predicted class and the probability score of each class.
  """
  loaded_tokenizer = AutoTokenizer.from_pretrained('model_camembert')
  loaded_model = TFAutoModelForSequenceClassification.from_pretrained('model_camembert')
  classes = ['bullying', 'hate_speech', 'homophobia', 'none', 'racism', 'sexism']
  if(input_text):
      # inference on input text
      tokens=loaded_tokenizer(input_text, padding=True,truncation=True, return_tensors='tf')
      logits=loaded_model.predict(dict(tokens), verbose=1).logits
      prob=tf.nn.softmax(logits, axis=1).numpy()
      predictions=np.argmax(prob, axis=1)
      
      prob_val = [round(p,4) for p in prob[0]]
      prob_values = dict(map(lambda i,j : (i,j),classes,prob_val))
      
  return predict_text(predictions), prob_values
