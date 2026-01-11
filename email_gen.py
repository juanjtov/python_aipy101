
from llm import *

# YOUR CODE HERE
user_email_content = '''At what time does the restaurant close?'''

text_prompt = f"""
1] SYSTEM PROMPT:
- 'You are a friendly restaurant manager who is always helpful and friendly'

Respond to this email:
{user_email_content}

with the following instructions:

2] INSTRUCTIONS:
- Be Concise
- Professional
- Always end with a smiley face
--Keep three things 3 lines max

3] For Questions Related to Policy,
   make sure to base your answers on these policies:
- 'Restaurants close at 10 p.m'
- 'We are open from 11 am to 10 p.m'

4] Here are examples of how I respond to emails,
 - Example 1:
     - Question: Is it possible to make a reservation?
     - Answer: Hello Mr Smith,
               Yes, you can make a reservation through our website.
                We'll be honored to have you in our restaurant.

- Example 2:
    - Question: What type of food do you serve?
    - Answer: Hello Ms Pelosi, We are truly happy to see your interest in our menu. We are Texan BBQ restauran, therefore you'll find a great variety of bbq options, including pulled pork and brisket bbq.
"""

image_prompt = f"""
YOU CODE HERE
Example: Give me an image that represents the person's mood {user_email_content}
"""

########################################
print('*'*30)
print("User Email Content:")
print(user_email_content)
print("*"*30)

print("Draft Response:")
# Generate Text
response = prompt_llm(text_prompt, with_linebreak=False)

print(response)

# Generate Image
img = gen_image(prompt=image_prompt, width=256, height=256)
