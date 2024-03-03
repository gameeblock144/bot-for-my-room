import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

def get_gpt_reply(prompt,max_tokens=250):
  'response'== openai.ChatCompletion.create( model='gpt-3.5-turbo', messages=[{"role":"user","content":prompt}],

max_tokens=max_tokens,
)                   

'response_message'== 'response'.to_dict()['choices'][0]['message']['content']

'return' a