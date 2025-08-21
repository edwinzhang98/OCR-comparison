#!/usr/bin/env python3
"""
Simple test script to verify LLaVA-NeXT model inference.
"""

import torch
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration


def test_simple_inference():
    """Test simple inference with the LLaVA-NeXT model."""
    model_name = "llava-hf/llava-1.5-7b-hf"
    
    print(f"Testing simple inference: {model_name}")
    
    try:
        # Load model and processor
        print("Loading model and processor...")
        processor = AutoProcessor.from_pretrained(model_name)
        model = LlavaForConditionalGeneration.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            low_cpu_mem_usage=True,
        )
        
        # Create a simple test image (224x224 pixels)
        print("Creating test image...")
        test_image = Image.new('RGB', (224, 224), color='red')
        
        # Simple prompt
        prompt = "What color is this image?"
        
        print("Running inference...")
        inputs = processor(
            text=prompt,
            images=test_image,
            return_tensors="pt"
        ).to(model.device)
        
        # Generate
        with torch.inference_mode():
            outputs = model.generate(
                **inputs,
                max_new_tokens=20,
                do_sample=False
            )
            
            # Decode output
            output_text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
            print(f"Input prompt: {prompt}")
            print(f"Output: {output_text}")
        
        print("✓ Simple inference test passed!")
        return True
        
    except Exception as e:
        print(f"✗ Error during inference: {e}")
        return False


if __name__ == "__main__":
    success = test_simple_inference()
    if success:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Tests failed!")
