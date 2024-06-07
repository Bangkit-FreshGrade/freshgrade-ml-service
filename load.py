import tensorflow as tf
import os
from dotenv import load_dotenv

load_dotenv()

async def load_condition_model():
  try:
    model = tf.keras.models.load_model(os.getenv("CONDITION_MODEL"))
    return model
  except Exception as e:
    raise e
  
async def load_disease_model():
  try:
    model = tf.keras.models.load_model(os.getenv("DISEASE_MODEL"))
    return model
  except Exception as e:
    raise e