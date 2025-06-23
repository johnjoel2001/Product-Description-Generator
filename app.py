from flask import Flask, render_template, request
import boto3
import json
import os

app = Flask(__name__)

MODEL_ID = "anthropic.claude-v2"
BEDROCK_REGION = "us-east-1"
bedrock = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)

def query_claude(prompt, max_tokens=400):
    body = {
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens_to_sample": max_tokens,
        "temperature": 0.7,
        "top_k": 250,
        "top_p": 1,
        "stop_sequences": ["\n\nHuman:"]
    }

    response = bedrock.invoke_model(
        body=json.dumps(body),
        modelId=MODEL_ID,
        accept="application/json",
        contentType="application/json"
    )

    result = json.loads(response['body'].read())
    return result['completion'].strip()

def format_description_as_bullets(text):
    lines = text.strip().split('\n')
    bullets = []
    for line in lines:
        if line.strip():
            bullets.append(f"• {line.strip()}")
    return '\n'.join(bullets)

@app.route("/", methods=["GET", "POST"])
def index():
    description = ""
    enhanced = ""
    show_enhance = False
    description_raw = ""

    if request.method == "POST":
        product = request.form.get("product")
        tone = request.form.get("tone")
        length = request.form.get("length")
        action = request.form.get("action")
        original_desc = request.form.get("original_desc")

        try:
            if action == "generate":
                prompt = f"You are a creative assistant. Write a {length}, {tone} product description for: {product}."
                result = query_claude(prompt)
                description_raw = result
                description = format_description_as_bullets(result)
                show_enhance = True

            elif action == "enhance":
                enhancement = request.form.get("enhancement")
                enhance_prompt = f"""Here is a product description:

\"{original_desc}\"

Please enhance it by: {enhancement}.
Return only the improved text."""
                enhanced_result = query_claude(enhance_prompt)
                enhanced = format_description_as_bullets(enhanced_result)
                description = format_description_as_bullets(original_desc)
                description_raw = original_desc
                show_enhance = True

        except Exception as e:
            description = f"⚠️ Error: {str(e)}"

    return render_template("index.html",
                           description=description,
                           enhanced=enhanced,
                           show_enhance=show_enhance,
                           description_raw=description_raw)

if __name__ == "__main__":
    app.run(debug=True)
