import os
from pathlib import Path
from  dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()
my_api_key= os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")

client = Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"

#3 prompt to send to the model
prompt1="Hi!"
prompt2="explain time travel in detail but under 100 words"
prompt3="write a 1000 word esssay on machine learning"

system_message={
    "role":"system",
    "content":"You are a helpful assistant that provides information and answers questions."    
}

prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages=[system_message,message]
    response=client.chat.completions.create(model=model, messages=messages, max_tokens=1500) #by usng max_tokens we can limit the number of tokens in the response
    usage=response.usage
    print(f"Prompt:{prompt} --> your tokens:{usage.prompt_tokens}, completion tokens:{usage.completion_tokens}, total tokens:{usage.total_tokens}  finish_reason:{response.choices[0].finish_reason} , answer:{response.choices[0].message.content}\\n") # we can also get the finish reason of the response which can be stop, length, content_filter, null




#mssg mein role and content 
# message={
#     "role":role,
#     "content":prompt
# }

# messages=[message]
# response=client.chat.completions.create(model=model, messages=messages)
