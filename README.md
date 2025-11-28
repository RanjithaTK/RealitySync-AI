🌀 RealitySync AI
A Multimodal Real-World Understanding Agent
Google AI 5-Day Hackathon – Freestyle Track Submission
🚀 Overview

RealitySync AI is a powerful multimodal freestyle agent that interprets real-world images and videos and generates meaningful insights, recommendations, and problem-solving steps. It blends Gemini 2.0 Flash’s visual reasoning with a custom multi-agent pipeline to deliver context-aware understanding across any domain: travel, productivity, home setup, safety, learning, design, and more.

This project is built to be domain-free, meaning it can solve problems from any field—making it perfect for the Freestyle track.

🌟 Key Capabilities
🧠 Multimodal Scene Understanding

Accepts images and videos (via frame extraction)

Identifies objects, relationships, risks, and opportunities

Understands environment context, layout, mood, and usage

⚡ Actionable Insight Engine

Generates step-by-step advice

Highlights issues or improvements

Provides contextual guidance

🛠️ Multi-Agent Workflow

Vision Agent → Interprets visual content

Insight Agent → Performs reasoning and suggestion-making

Decision Agent → Produces final structured output

🔮 Freestyle Use Cases

Because it is not limited to any one theme, it works for:

Travel planning from suitcase photos

Home/desk setup optimization

Product recommendations from item inspection

Room décor analysis

Safety checks (non-medical)

Learning assistance

Gardening / plant health advice

Artistic/creative inspiration

Workspace productivity improvements
               ┌─────────────────────────┐
               │     User Uploads         │
               │  (Image / Video Frame)   │
               └─────────────┬───────────┘
                             ▼
                 ┌────────────────────┐
                 │    Vision Agent    │
                 │  (Gemini 2.0 Flash)│
                 └─────────┬──────────┘
                           ▼
              ┌──────────────────────────┐
              │     Insight Agent        │
              │  (Reasoning + Planning)  │
              └──────────┬──────────────┘
                         ▼
           ┌─────────────────────────────────┐
           │     Decision + Output Layer     │
           │  Recommendations / Steps / Tips │
           └─────────────────────────────────┘


🛠️ Tech Stack
| Layer            | Technology                            |
| ---------------- | ------------------------------------- |
| AI Model         | Gemini 2.0 Flash                      |
| Backend          | Python + FastAPI                      |
| Frontend         | Streamlit                             |
| Agents           | Custom Vision + Insight agents        |
| Video Processing | OpenCV                                |
| Deployment       | (Optional) GCP / HuggingFace / Render |




🔧 How It Works
Step 1: Upload Image / Video

User uploads a picture of:

a room

a desk

plants

outfits

groceries

luggage

tools

anything visual

Step 2: Vision Agent Processing

Gemini processes:

objects

lighting

problems

relationships

pose detection

textures

anomalies

Step 3: Insight Agent

It uses:

contextual reasoning

environmental understanding

user intent parsing

Step 4: Final Output

Delivers:

insights

steps

recommendations

optimizations

warnings

pros & cons

🧪 Example Outputs
Input: an image of a messy desk
Output:

Identify clutter hotspots

Suggest cable management

Recommend plant placement

Estimate ergonomics

Provide productivity tips
