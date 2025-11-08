import os
import sys
from PIL import Image
import io
import base64

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


def process_image(uploaded_file):
    """
    Process uploaded image file and prepare for LLM
    
    Args:
        uploaded_file: Streamlit uploaded file object
    
    Returns:
        tuple: (PIL Image object, bytes data)
    
    Raises:
        Exception: If image processing fails
    """
    try:
        # Read image bytes
        image_bytes = uploaded_file.read()
        
        # Open with PIL
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if needed (for JPEG compatibility)
        if image.mode not in ('RGB', 'RGBA'):
            image = image.convert('RGB')
        
        # Reset file pointer
        uploaded_file.seek(0)
        
        return image, image_bytes
    
    except Exception as e:
        raise Exception(f"Failed to process image: {str(e)}")


def encode_image_to_base64(image_bytes):
    """
    Encode image bytes to base64 string
    
    Args:
        image_bytes: Image data in bytes
    
    Returns:
        str: Base64 encoded string
    """
    try:
        return base64.b64encode(image_bytes).decode('utf-8')
    except Exception as e:
        raise Exception(f"Failed to encode image: {str(e)}")


def get_image_info(image):
    """
    Get image metadata and information
    
    Args:
        image: PIL Image object
    
    Returns:
        dict: Image information
    """
    try:
        info = {
            "format": image.format,
            "mode": image.mode,
            "size": image.size,
            "width": image.width,
            "height": image.height
        }
        return info
    except Exception as e:
        return {"error": str(e)}


def resize_image_if_needed(image, max_size=(1024, 1024)):
    """
    Resize image if it exceeds maximum dimensions
    
    Args:
        image: PIL Image object
        max_size: Tuple of (max_width, max_height)
    
    Returns:
        PIL.Image: Resized image if needed, original otherwise
    """
    try:
        if image.width > max_size[0] or image.height > max_size[1]:
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
        return image
    except Exception as e:
        raise Exception(f"Failed to resize image: {str(e)}")


def prepare_image_for_gemini(uploaded_file):
    """
    Prepare image for Gemini Vision API
    
    Args:
        uploaded_file: Streamlit uploaded file object
    
    Returns:
        dict: Prepared image data with metadata
    """
    try:
        # Process image
        image, image_bytes = process_image(uploaded_file)
        
        # Resize if too large
        image = resize_image_if_needed(image)
        
        # Get image info
        image_info = get_image_info(image)
        
        # Convert to bytes for API
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=image.format or 'PNG')
        final_bytes = img_byte_arr.getvalue()
        
        return {
            "image": image,
            "bytes": final_bytes,
            "info": image_info,
            "filename": uploaded_file.name
        }
    
    except Exception as e:
        raise Exception(f"Failed to prepare image for processing: {str(e)}")
