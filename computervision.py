from openai import OpenAI

endpoint = "sdadsdw"
deployment_name = "gpt-5.4-mini"
api_key = "xxassd"

client = OpenAI(
     base_url=endpoint,
     api_key=api_key
 )

response = client.responses.create(
     model=deployment_name,
     input=[{
         "role": "user",
         "content": [
             {"type": "input_text", "text": "what's in this image?"},
             {"type": "input_image", "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"},
         ],
     }],
 )

print(f"answer: {response.output_text}")
