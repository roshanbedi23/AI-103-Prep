from pathlib import Path

from openai import OpenAI

endpoint = "https://roshan-ai-103-foundry-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5-mini"
api_key_file = Path(__file__).resolve().with_name("api_key.txt")
try:
    api_key = api_key_file.read_text(encoding="utf-8").strip()
except FileNotFoundError as error:
    raise SystemExit("Create api_key.txt next to this script and put your API key in it.") from error

if not api_key:
    raise SystemExit("api_key.txt is empty. Put your API key in it.")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="What is the meaning of delighted?",
)

print(f"answer: {response.output_text}")
