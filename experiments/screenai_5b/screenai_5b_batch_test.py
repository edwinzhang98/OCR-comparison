#!/usr/bin/env python3
"""
ScreenAI-5B batch testing script for OCR sample images.

This script tests the ScreenAI-5B model on multiple images using different
preset configurations and records timing, parameters, and results.
"""

import os
import json
import time
import argparse
from pathlib import Path
from typing import Dict, Any, List
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq


def get_presets() -> Dict[str, Dict[str, Any]]:
    """Define preset configurations optimized for complex chart/scientific image captioning.
    
    Returns:
        Dict containing preset configurations with generation parameters.
    """
    return {
        "chart_analysis": {
            "prompt": "Analyze this chart or scientific diagram in detail. Describe the data, labels, axes, trends, and any text elements you can see. Focus on accuracy and completeness.",
            "gen": {
                "max_new_tokens": 800,
                "do_sample": True,
                "temperature": 0.3,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
                "no_repeat_ngram_size": 3,
            }
        },
        "technical_description": {
            "prompt": "Provide a technical description of this image. Identify all text, numbers, symbols, and structural elements. Be precise and systematic in your analysis.",
            "gen": {
                "max_new_tokens": 600,
                "do_sample": False,
                "num_beams": 3,
                "repetition_penalty": 1.15,
                "length_penalty": 1.0,
                "early_stopping": True,
            }
        },
        "comprehensive_caption": {
            "prompt": "Create a comprehensive caption for this image. Include all visible text, data points, chart elements, and contextual information. Make it suitable for academic or technical documentation.",
            "gen": {
                "max_new_tokens": 1000,
                "do_sample": True,
                "temperature": 0.4,
                "top_p": 0.95,
                "repetition_penalty": 1.2,
                "no_repeat_ngram_size": 4,
            }
        },
        "structured_analysis": {
            "prompt": "Analyze this image using a structured approach: 1) Identify the main elements, 2) Describe any text or labels, 3) Note data patterns or trends, 4) Summarize the overall purpose.",
            "gen": {
                "max_new_tokens": 700,
                "do_sample": True,
                "temperature": 0.5,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
                "no_repeat_ngram_size": 3,
            }
        },
        "precision_focused": {
            "prompt": "Describe this image with high precision. Pay special attention to exact text, numbers, symbols, and spatial relationships. Avoid speculation and focus on observable facts.",
            "gen": {
                "max_new_tokens": 500,
                "do_sample": False,
                "num_beams": 4,
                "repetition_penalty": 1.2,
                "length_penalty": 1.1,
                "early_stopping": True,
            }
        }
    }


def run_once(
    model: AutoModelForVision2Seq,
    processor: AutoProcessor,
    device: torch.device,
    image_path: str,
    preset_name: str,
    preset_cfg: Dict[str, Any],
) -> Dict[str, Any]:
    """Run a single inference with the ScreenAI model.
    
    Args:
        model: The loaded ScreenAI model
        processor: The model processor
        device: Target device (CPU/GPU)
        image_path: Path to the input image
        preset_name: Name of the preset configuration
        preset_cfg: Preset configuration dictionary
        
    Returns:
        Dictionary containing results and metadata
    """
    # Load and preprocess image
    img = Image.open(image_path).convert("RGB")
    
    # Prepare prompt
    prompt = str(preset_cfg.get("prompt", ""))
    
    # Format input for BLIP2 - use simple prompt for image captioning
    simple_prompt = "a photo of"
    inputs = processor(
        text=simple_prompt,
        images=img,
        return_tensors="pt"
    )
    
    # Move inputs to device
    for key, value in inputs.items():
        if isinstance(value, torch.Tensor):
            inputs[key] = value.to(device)
    
    # Get generation parameters
    gen_kwargs = dict(preset_cfg.get("gen", {}))
    
    # Record start time
    start_time = time.time()
    
    # Generate output
    with torch.inference_mode():
        out = model.generate(**inputs, **gen_kwargs)
        seq = out.sequences if hasattr(out, "sequences") else out
        
        # Decode output - BLIP2 outputs the generated text directly
        output_text = processor.batch_decode(seq, skip_special_tokens=True)[0]
        
        # Clean up the output text - remove any prompt artifacts
        if prompt and prompt.lower() in output_text.lower():
            # Remove the prompt from the output if it appears
            output_text = output_text.replace(prompt, "").strip()
        
        # If output is still empty or just whitespace, try alternative decoding
        if not output_text or output_text.strip() == "":
            # Try decoding without skip_special_tokens
            output_text = processor.batch_decode(seq, skip_special_tokens=False)[0]
            # Clean up special tokens manually
            output_text = output_text.replace("<|endoftext|>", "").replace("<|im_start|>", "").replace("<|im_end|>", "").strip()
    
    # Record end time
    end_time = time.time()
    
    # Calculate total tokens generated
    total_tokens = len(seq[0]) - inputs['input_ids'].shape[1]
    
    return {
        "preset": preset_name,
        "prompt": prompt,
        "generation_kwargs": gen_kwargs,
        "output_text": output_text,
        "inference_time": end_time - start_time,
        "total_tokens": total_tokens,
    }


def main():
    """Main function to run batch testing."""
    parser = argparse.ArgumentParser(description="ScreenAI-5B batch testing")
    parser.add_argument(
        "--model_name",
        default="Salesforce/blip2-opt-2.7b",
        help="ScreenAI model name or path"
    )
    parser.add_argument(
        "--image_dir",
        default="data/pdf_ocr_samples",
        help="Directory containing test images"
    )
    parser.add_argument(
        "--output_dir",
        default="output/ScreenAI-5B",
        help="Directory to save aggregated JSON outputs"
    )
    parser.add_argument(
        "--device",
        default="auto",
        choices=["auto", "cuda", "cpu"],
        help="Device to run inference on"
    )
    
    args = parser.parse_args()
    
    # Setup device
    if args.device == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device = torch.device(args.device)
    
    print(f"Using device: {device}")
    print(f"Loading model: {args.model_name}")
    
    # Load model and processor
    try:
        # Try to load as BLIP2 model
        from transformers import Blip2ForConditionalGeneration
        model = Blip2ForConditionalGeneration.from_pretrained(
            args.model_name,
            torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
            device_map="auto" if device.type == "cuda" else None,
            low_cpu_mem_usage=True,
        )
    except Exception as e:
        print(f"Failed to load as BLIP2 model: {e}")
        print("Trying alternative model types...")
        # Fallback to other model types
        try:
            model = AutoModelForVision2Seq.from_pretrained(
                args.model_name,
                torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
                device_map="auto" if device.type == "cuda" else None,
                low_cpu_mem_usage=True,
            )
        except Exception as e2:
            print(f"Failed to load as Vision2Seq model: {e2}")
            from transformers import AutoModelForCausalLM
            model = AutoModelForCausalLM.from_pretrained(
                args.model_name,
                torch_dtype=torch.float16 if device.type == "cuda" else torch.float32,
                device_map="auto" if device.type == "cuda" else None,
                low_cpu_mem_usage=True,
            )
    
    if device.type == "cuda" and not hasattr(model, 'hf_device_map'):
        model = model.to(device)
    
    processor = AutoProcessor.from_pretrained(args.model_name)
    
    # Get presets
    presets = get_presets()
    print(f"Loaded {len(presets)} presets: {list(presets.keys())}")
    
    # Setup output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get image files
    image_dir = Path(args.image_dir)
    image_files = sorted([f for f in image_dir.glob("*.jpg") if f.is_file()])
    
    if not image_files:
        print(f"No JPG images found in {image_dir}")
        return
    
    print(f"Found {len(image_files)} images to process")
    
    # Process each image
    for i, image_path in enumerate(image_files, 1):
        print(f"\nProcessing image {i}/{len(image_files)}: {image_path.name}")
        
        results = []
        total_time = 0
        
        # Test with each preset
        for preset_name, preset_cfg in presets.items():
            print(f"  Testing preset: {preset_name}")
            
            try:
                result = run_once(
                    model, processor, device, str(image_path), preset_name, preset_cfg
                )
                results.append(result)
                total_time += result["inference_time"]
                
                # Print individual preset timing
                print(f"    {preset_name}: {result['inference_time']:.2f}s, {result['total_tokens']} tokens")
                
            except Exception as e:
                print(f"    Error with preset {preset_name}: {e}")
                results.append({
                    "preset": preset_name,
                    "prompt": preset_cfg.get("prompt", ""),
                    "generation_kwargs": preset_cfg.get("gen", {}),
                    "output_text": f"ERROR: {str(e)}",
                    "inference_time": 0,
                    "total_tokens": 0,
                    "error": str(e)
                })
        
        # Create output data
        output_data = {
            "image": str(image_path),
            "image_name": image_path.name,
            "total_processing_time": total_time,
            "presets_tested": len(presets),
            "results": results
        }
        
        # Save to JSON
        output_file = output_dir / f"{image_path.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"  Saved results to: {output_file}")
        print(f"  Total processing time: {total_time:.2f}s")
    
    print(f"\nBatch testing completed. Results saved to: {output_dir}")


if __name__ == "__main__":
    main()
