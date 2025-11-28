import io
import base64
from config.config import GEMINI_API_KEY, MODEL_NAME
import google.generativeai as genai
from PIL import Image

# Configure the library
genai.configure(api_key=GEMINI_API_KEY)

def image_to_base64(image_pil):
    """Return base64 string of a PIL image"""
    buffered = io.BytesIO()
    image_pil.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def gemini_vision_call(image_pil, prompt_text):
    """
    Send an image + prompt to the Gemini vision-capable model and return text result.
    NOTE: adapt to the exact SDK call / arguments your installed library expects.
    """
    # Many Gemini wrappers accept multipart or base64-encoded images.
    # Here we create a simple multimodal request using genai API.
    image_b64 = image_to_base64(image_pil)

    # Example: build multimodal input — adapt as needed.
    multimodal_instruction = {
        "input": [
            {"type": "text", "text": prompt_text},
            {"type": "image", "image_base64": image_b64}
        ]
    }

    # If your SDK uses a different signature, replace this block.
    # This example uses genai's model.generate (pseudocode-like).
    model = genai.get_model(MODEL_NAME)
    # The actual method name may differ; consult your SDK docs.
    response = model.generate(**{
        "instructions": prompt_text,
        "images": [image_b64],
        "max_output_tokens": 512,
    })

    # Some SDKs return an object with .text or .content
    # Attempt to extract textual answer robustly:
    try:
        return response.text if hasattr(response, "text") else str(response)
    except Exception:
        return str(response)
