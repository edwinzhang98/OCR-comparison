#!/usr/bin/env python3
"""
Debug script to examine LLaVA model output format.
"""

import torch
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration
from pathlib import Path


def debug_output_format():
    """Debug LLaVA model output format."""
    model_name = "llava-hf/llava-1.5-7b-hf"
    image_path = "data/pdf_ocr_samples/1.jpg"
    
    print(f"Debugging output format for: {model_name}")
    
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
        
        # Load image
        print("Loading test image...")
        test_image = Image.open(image_path).convert("RGB")
        
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
            
            print(f"Output shape: {outputs.shape}")
            print(f"Output type: {type(outputs)}")
            
            # Check if outputs has sequences attribute
            if hasattr(outputs, 'sequences'):
                print(f"Has sequences: {outputs.sequences.shape}")
                seq = outputs.sequences
            else:
                print("No sequences attribute, using outputs directly")
                seq = outputs
            
            # Try different decoding approaches
            print("\n=== Decoding Attempts ===")
            
            # Method 1: Direct decode
            try:
                output_text1 = processor.batch_decode(seq, skip_special_tokens=True)[0]
                print(f"Method 1 (direct): {repr(output_text1)}")
            except Exception as e:
                print(f"Method 1 failed: {e}")
            
            # Method 2: Decode with skip_special_tokens=False
            try:
                output_text2 = processor.batch_decode(seq, skip_special_tokens=False)[0]
                print(f"Method 2 (no skip): {repr(output_text2)}")
            except Exception as e:
                print(f"Method 2 failed: {e}")
            
            # Method 3: Check token by token
            try:
                print(f"First 10 tokens: {seq[0, :10]}")
                print(f"Last 10 tokens: {seq[0, -10:]}")
            except Exception as e:
                print(f"Token inspection failed: {e}")
            
            # Method 4: Try to find where generation starts
            try:
                # Find the start of generation (after input)
                input_length = inputs['input_ids'].shape[1]
                print(f"Input length: {input_length}")
                print(f"Output length: {seq.shape[1]}")
                
                if seq.shape[1] > input_length:
                    generated_tokens = seq[0, input_length:]
                    print(f"Generated tokens shape: {generated_tokens.shape}")
                    generated_text = processor.batch_decode(generated_tokens, skip_special_tokens=True)[0]
                    print(f"Generated text: {repr(generated_text)}")
                else:
                    print("No new tokens generated")
                    
            except Exception as e:
                print(f"Generation analysis failed: {e}")
        
        print("\n✓ Debug completed!")
        return True
        
    except Exception as e:
        print(f"✗ Error during debug: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = debug_output_format()
    if success:
        print("\n✓ Debug successful!")
    else:
        print("\n✗ Debug failed!")
