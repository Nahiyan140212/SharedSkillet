import boto3
import json
from botocore.exceptions import ClientError

bedrock = boto3.client("bedrock-runtime")
rekognition = boto3.client("rekognition")

def generate_recipe(ingredients: str) -> dict:
    prompt = f"Generate a recipe using these ingredients: {ingredients}"
    try:
        response = bedrock.invoke_model(
            modelId="anthropic.claude-v2",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({"prompt": prompt, "max_tokens": 500})
        )
        recipe_text = json.loads(response["body"].read().decode())["completion"]
        return {"title": "Bedrock Recipe", "ingredients": ingredients.split(), "instructions": recipe_text, "public_url": ""}
    except ClientError:
        # Fallback to OpenAI if Bedrock fails (requires OPENAI_API_KEY)
        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        return {"title": "OpenAI Recipe", "ingredients": ingredients.split(), "instructions": response.choices[0].message.content, "public_url": ""}

def image_to_recipe(image_content: bytes) -> dict:
    response = rekognition.detect_labels(Image={"Bytes": image_content}, MaxLabels=10, MinConfidence=70)
    labels = [label["Name"] for label in response["Labels"]]
    prompt = f"Identify a recipe from these labels: {', '.join(labels)}"
    bedrock_response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({"prompt": prompt, "max_tokens": 500})
    )
    recipe_text = json.loads(bedrock_response["body"].read().decode())["completion"]
    return {"title": "Rekognition Recipe", "ingredients": labels, "instructions": recipe_text, "public_url": ""}

def generate_meal_plan(preferences: dict) -> dict:
    prompt = f"Create a {preferences['days']}-day meal plan for a {preferences['diet']} diet with preferences: {', '.join(preferences['preferences'])}"
    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({"prompt": prompt, "max_tokens": 1000})
    )
    return {"plan": json.loads(response["body"].read().decode())["completion"]}