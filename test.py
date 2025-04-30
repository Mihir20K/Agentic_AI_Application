import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # Use the new API method for embeddings
    response = openai.embeddings.create(
        model="text-embedding-ada-002",  # Use the newer model version (try text-embedding-ada-001 or -002)
        input="Test sentence"
    )
    print(response)

except openai.error.RateLimitError as e:
    print(f"Rate Limit Exceeded: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
