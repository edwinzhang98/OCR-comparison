#!/usr/bin/env python3
"""
Simple test script to verify BLIP2 model usage.
"""

import torch
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration


def test_blip2():
    """Test BLIP2 model with a simple image."""
    model_name = "Salesforce/blip2-opt-2.7b"
    
    print(f"Testing BLIP2 model: {model_name}")
    
    try:
        # Load model and processor
        processor = Blip2Processor.from_pretrained(model_name)
        model = Blip2ForConditionalGeneration.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        
        print("✓ Model loaded successfully")
        
        # Create a simple test image (1x1 pixel)
        test_image = Image.new('RGB', (224, 224), color='red')
        
        # Test different input formats
        print("\nTesting input formats:")
        
        # Format 1: Just image
        try:
            inputs = processor(images=test_image, return_tensors="pt")
            print("✓ Format 1 (image only): Success")
            print(f"  Keys: {list(inputs.keys())}")
        except Exception as e:
            print(f"✗ Format 1 (image only): {e}")
        
        # Format 2: Image with text
        try:
            inputs = processor(text="describe this image", images=test_image, return_tensors="pt")
            print("✓ Format 2 (image + text): Success")
            print(f"  Keys: {list(inputs.keys())}")
        except Exception as e:
            print(f"✗ Format 2 (image + text): {e}")
        
        # Format 3: Text only
        try:
            inputs = processor(text="describe this image", return_tensors="pt")
            print("✓ Format 3 (text only): Success")
            print(f"  Keys: {list(inputs.keys())}")
        except Exception as e:
            print(f"✗ Format 3 (text only): {e}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


if __name__ == "__main__":
    success = test_blip2()
    if success:
        print("\n✓ BLIP2 test completed!")
    else:
        print("\n✗ BLIP2 test failed!")
