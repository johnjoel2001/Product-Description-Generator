
# AI-Powered Product Description Generator

This is a full-stack web application that uses **Amazon Bedrock (Claude v2)** to generate creative product descriptions based on user input. Ideal for small business owners and e-commerce sellers, the app allows customization of tone, length, and enhancement options.
## Live Demo

 [View Live on AWS App Runner](https://ansiymdpbt.us-east-1.awsapprunner.com/)

##  Features

- ✏️ Generate descriptions for any product by entering basic details
- 🎭 Choose tone: Friendly, Professional, or Playful
- 📏 Choose length: Short, Medium, or Long
- 🧠 Enhance options:
  - Make it more persuasive
  - Add SEO keywords
  - Turn into a Twitter post
- 🔁 Option to generate **3 creative variants**
- 📋 Outputs formatted as clean bullet points
- 💡 Built with Flask and deployed via AWS App Runner

---

## 🛠Tech Stack

- **Frontend:** HTML, CSS (custom styling), Jinja2 templates
- **Backend:** Python Flask
- **AI Model:** Amazon Bedrock (Claude v2)
- **Deployment:** AWS App Runner
- **Testing:** `pytest`

---

##  API Documentation

### `/` (Main Route)

| Method | Description                          |
|--------|--------------------------------------|
| GET    | Load the homepage                    |
| POST   | Submits product form and calls Claude for description generation |

**Form Fields:**
- `product`: (string) product name or description
- `tone`: (friendly | professional | playful)
- `length`: (short | medium | long)
- `action`: `generate` or `enhance`
- `enhancement`: (optional) selected enhancement prompt
