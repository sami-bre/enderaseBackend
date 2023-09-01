import google.generativeai as palm
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("PALM_API_KEY")
palm.configure(api_key=api_key)

# Selecting the first and only text generation model available in palm
text_model = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_models
][0]
