from llm import gen_image, prompt_llm

### YOUR CODE HERE
text_prompt = "write a 3 line post about the importance of pima cotton for babies"
image_prompt = f"give me an image that represents this {text_prompt}"

# Generate Text
response = prompt_llm(text_prompt, with_linebreak=True)

print(response)

# Generate Image
img = gen_image(prompt=image_prompt, width=256, height=256)
