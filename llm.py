# import libraries
import requests
from PIL import Image
import os
import glob

# suppress warnings
import warnings
warnings.filterwarnings("ignore")

import gradio as gr
from together import Together
import textwrap

# Get Client
your_api_key = "d47f79bb599c16d0ee0cede92f6f9864f032fc7a8fb89a277673c6c593552a9a"
client = Together(api_key=your_api_key)

## FUNCTION 1: This Allows Us to Prompt the AI MODEL
# -------------------------------------------------
def prompt_llm(prompt, with_linebreak=False):
    # This function allows us to prompt an LLM via the Together API

    # model
    model = "meta-llama/Meta-Llama-3-8B-Instruct-Lite"

    # Calculate the number of tokens
    tokens = len(prompt.split())

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    output = response.choices[0].message.content

    if with_linebreak:
      # Wrap the output
      wrapped_output = textwrap.fill(output, width=50)

      return wrapped_output
    else:
      return output

## FUNCTION 2: This Allows Us to Generate Images
# -------------------------------------------------
def get_next_image_filename():
    # Find existing image files and return the next available filename
    existing = glob.glob("image*.png")
    if not existing:
        return "image1.png"
    numbers = []
    for f in existing:
        name = os.path.splitext(os.path.basename(f))[0]  # "image1"
        num_part = name.replace("image", "")
        if num_part.isdigit():
            numbers.append(int(num_part))
    next_num = max(numbers, default=0) + 1
    return f"image{next_num}.png"

def gen_image(prompt, width=256, height=256):
    # This function allows us to generate images from a prompt
    response = client.images.generate(
        prompt=prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",  # Using a supported model
        steps=30,
        n=1,
    )
    image_url = response.data[0].url
    image_filename = get_next_image_filename()

    # Download the image using requests instead of wget
    response = requests.get(image_url)
    with open(image_filename, "wb") as f:
        f.write(response.content)
    img = Image.open(image_filename)
    img = img.resize((height, width))

    return img

print("LLM Ready!")
#print(prompt_llm("What is the capital of Mars and Pluto"))
#gen_image("A group of people freezing in a Vancouver beach")