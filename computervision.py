from openai import OpenAI

endpoint = "https://project401-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4-mini"
api_key = "Dd2eOP5rZQGNCkdRpLgosRLGPlltRFkKD3ITY2EbcYWQ5pfHhLSGJQQJ99CKACF24PCXJ3w3AAAAACOGkHPL"

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
