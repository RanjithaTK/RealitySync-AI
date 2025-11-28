from PIL import Image, ImageOps
import io

def load_image(uploaded_file):
    """
    uploaded_file: Streamlit UploadedFile object
    returns PIL.Image
    """
    if uploaded_file is None:
        return None
    image = Image.open(uploaded_file).convert("RGB")
    return image

def resize_for_model(image_pil, max_size=1024):
    """Resize preserving aspect ratio to avoid overly large uploads."""
    image_pil.thumbnail((max_size, max_size))
    return image_pil
