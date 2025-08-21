# LLaVA-NeXT-7B Testing Scripts

This directory contains scripts for testing the LLaVA-NeXT-7B model on OCR sample images.

## Environment Setup

1. Create virtual environment:
```bash
uv venv llava-next
source llava-next/bin/activate
```

2. Install dependencies:
```bash
uv pip install torch torchvision pillow transformers accelerate pandas tabulate
```

## Scripts Overview

### 1. `llava_next_batch_test.py` - Main Testing Script
- **Purpose**: Batch test LLaVA-NeXT-7B on multiple images with different presets
- **Features**: 
  - 5 preset configurations (fast_draft, balanced_beam, detailed_analysis, concise_summary, academic_style)
  - Records timing, token counts, and generation parameters
  - Saves results to JSON files
  - Supports GPU acceleration

**Usage**:
```bash
python3 llava_next_batch_test.py [options]

Options:
  --model_name MODEL_NAME    LLaVA model name (default: llava-hf/llava-1.5-7b-hf)
  --image_dir IMAGE_DIR      Directory containing test images (default: data/pdf_ocr_samples)
  --output_dir OUTPUT_DIR    Output directory (default: output/LLaVA-NeXT-7B)
  --device {auto,cuda,cpu}  Device to run inference on (default: auto)
```

**Example**:
```bash
python3 llava_next_batch_test.py --image_dir data/pdf_ocr_samples --output_dir output/LLaVA-NeXT-7B
```

### 2. `llava_next_postprocess_tables.py` - Results Processing
- **Purpose**: Convert JSON results to comparison tables
- **Output**: Markdown and CSV comparison tables for each image
- **Features**: Shows preset, output_text, prompt, timing, and generation parameters

**Usage**:
```bash
python3 llava_next_postprocess_tables.py --results_dir output/LLaVA-NeXT-7B
```

### 3. `llava_next_summary.py` - Results Summary
- **Purpose**: Generate overview statistics of testing results
- **Features**: 
  - Timing statistics per image and preset
  - Token count averages
  - Error reporting
  - File count summary

**Usage**:
```bash
python3 llava_next_summary.py --results_dir output/LLaVA-NeXT-7B
```

### 4. Test Scripts
- `llava_next_test_load.py` - Test model loading
- `llava_next_simple_test.py` - Test with synthetic image
- `llava_next_real_image_test.py` - Test with real sample image

## Preset Configurations

### fast_draft
- **Purpose**: Quick, creative generation
- **Parameters**: max_new_tokens=256, temperature=0.7, top_p=0.9
- **Use case**: Rapid prototyping, brainstorming

### balanced_beam
- **Purpose**: Balanced quality and speed
- **Parameters**: max_new_tokens=512, num_beams=4, beam search
- **Use case**: Production use, quality-focused tasks

### detailed_analysis
- **Purpose**: Comprehensive analysis
- **Parameters**: max_new_tokens=1024, temperature=0.6, top_p=0.95
- **Use case**: Detailed reports, thorough analysis

### concise_summary
- **Purpose**: Brief, focused output
- **Parameters**: max_new_tokens=128, num_beams=2
- **Use case**: Quick summaries, headlines

### academic_style
- **Purpose**: Formal, academic writing
- **Parameters**: max_new_tokens=768, temperature=0.5, top_p=0.9
- **Use case**: Research documentation, formal reports

## Output Structure

```
output/LLaVA-NeXT-7B/
├── 1.json                    # Raw results for image 1
├── 1_comparison.md          # Markdown comparison table
├── 1_comparison.csv         # CSV comparison table
├── 2.json
├── 2_comparison.md
├── 2_comparison.csv
└── ...                      # (18 images total)
```

## Performance Notes

- **Model**: llava-hf/llava-1.5-7b-hf
- **GPU**: NVIDIA RTX 4090 (25.3 GB VRAM)
- **Average time per image**: ~13.6 seconds
- **Average time per preset**: 2.3-4.0 seconds
- **Total processing time**: ~4 minutes for 18 images

## Troubleshooting

### Common Issues

1. **CUDA out of memory**: Reduce batch size or use CPU
2. **Model loading errors**: Check internet connection and model name
3. **Image format issues**: Ensure images are JPG/PNG format
4. **Missing dependencies**: Install required packages with `uv pip install`

### Error Handling

The scripts include comprehensive error handling:
- Individual preset failures don't stop the entire batch
- Errors are logged in the JSON output
- Failed presets show "ERROR: [error message]" in output_text

## Comparison with Other Models

This LLaVA-NeXT implementation follows the same structure as:
- Qwen2-VL-7B-Instruct testing scripts
- DONUT model testing scripts

All models use consistent output formats for easy comparison.
