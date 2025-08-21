#!/usr/bin/env python3
"""
Test LLaVA-NeXT with real images from the sample directory.
"""

import torch
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration
from pathlib import Path


def test_with_real_image():
    """Test LLaVA-NeXT with a real image from samples."""
    model_name = "llava-hf/llava-1.5-7b-hf"
    image_dir = Path("data/pdf_ocr_samples")
    
    print(f"Testing with real image: {model_name}")
    
    # Find first available image
    image_files = list(image_dir.glob("*.jpg"))
    if not image_files:
        print("No JPG images found in data/pdf_ocr_samples/")
        return False
    
    test_image_path = image_files[0]
    print(f"Using image: {test_image_path.name}")
    
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
        
        # Load and process image
        print("Loading test image...")
        test_image = Image.open(test_image_path).convert("RGB")
        
        # Use LLaVA chat template format
        messages = [
            {"role": "user", "content": [
                {"type": "text", "text": "Describe this image briefly."},
                {"type": "image", "image": test_image}
            ]}
        ]
        
        print("Running inference...")
        # Apply chat template and process
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(
            text=[text],
            images=[test_image],
            return_tensors="pt"
        )
        
        # Move inputs to device
        for key, value in inputs.items():
            if isinstance(value, torch.Tensor):
                inputs[key] = value.to(model.device)
        
        # Generate
        with torch.inference_mode():
            outputs = model.generate(
                **inputs,
                max_new_tokens=50,
                do_sample=False
            )
            
            # Decode output
            output_text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
            print(f"Input prompt: Describe this image briefly.")
            print(f"Output: {output_text}")
        
        print("✓ Real image inference test passed!")
        return True
        
    except Exception as e:
        print(f"✗ Error during inference: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_with_real_image()
    if success:
        print("\n✓ All tests passed!")
    else:
        print("\n✗ Tests failed!")
