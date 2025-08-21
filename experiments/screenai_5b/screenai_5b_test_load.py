#!/usr/bin/env python3
"""
Simple test script to verify ScreenAI-5B model loading.
"""

import torch
from transformers import AutoProcessor, AutoModelForVision2Seq


def test_model_loading():
    """Test if the ScreenAI-5B model can be loaded successfully."""
    model_name = "google/screenai-5b"
    
    print(f"Testing model loading: {model_name}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    
    try:
        print("Loading processor...")
        processor = AutoProcessor.from_pretrained(model_name)
        print("✓ Processor loaded successfully")
        
        print("Loading model...")
        model = AutoModelForVision2Seq.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto" if torch.cuda.is_available() else None,
            low_cpu_mem_usage=True,
        )
        print("✓ Model loaded successfully")
        
        if torch.cuda.is_available():
            print(f"Model device: {model.device}")
            print(f"Model dtype: {model.dtype}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        return False


if __name__ == "__main__":
    success = test_model_loading()
    if success:
        print("\n✓ Model loading test passed!")
    else:
        print("\n✗ Model loading test failed!")
