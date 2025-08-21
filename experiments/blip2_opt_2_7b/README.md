# BLIP2-opt-2.7B Testing Scripts

This directory contains scripts for testing the BLIP2-opt-2.7B model on OCR sample images.

## Model Information

- **Model**: Salesforce/blip2-opt-2.7B
- **Repository**: https://huggingface.co/Salesforce/blip2-opt-2.7b
- **Type**: Vision-Language Model for image captioning
- **Size**: 2.7B parameters
- **Specialization**: Image understanding and description

## Environment Setup

1. Create virtual environment:
```bash
uv venv blip2-opt-2-7b
source blip2-opt-2-7b/bin/activate
```

2. Install dependencies:
```bash
uv pip install torch torchvision pillow transformers accelerate pandas tabulate
```

## Scripts Overview

### 1. `blip2_batch_test.py` - Main Testing Script
- **Purpose**: Batch test BLIP2-opt-2.7B on multiple images with different presets
- **Features**: 
  - 5 preset configurations optimized for complex chart/scientific image captioning
  - Records timing for each preset individually
  - Uses detailed prompts to encourage longer, more descriptive outputs
  - Saves results to JSON files
  - Supports GPU acceleration

**Usage**:
```bash
python3 blip2_batch_test.py [options]

Options:
  --model_name MODEL_NAME    BLIP2 model name (default: Salesforce/blip2-opt-2.7b)
  --image_dir IMAGE_DIR      Directory containing test images (default: data/pdf_ocr_samples)
  --output_dir OUTPUT_DIR    Output directory (default: output/BLIP2-opt-2.7B)
  --device {auto,cuda,cpu}  Device to run inference on (default: auto)
```

**Example**:
```bash
python3 blip2_batch_test.py --image_dir data/pdf_ocr_samples --output_dir output/BLIP2-opt-2.7B
```

### 2. `blip2_postprocess_tables.py` - Results Processing
- **Purpose**: Convert JSON results to comparison tables
- **Output**: Markdown and CSV comparison tables for each image
- **Features**: Shows preset, output_text, prompt, timing, and generation parameters

**Usage**:
```bash
python3 blip2_postprocess_tables.py --results_dir output/BLIP2-opt-2.7B
```

## Preset Configurations

### chart_analysis
- **Purpose**: Detailed chart and scientific diagram analysis
- **Parameters**: max_new_tokens=150, temperature=0.7, top_p=0.9
- **Use case**: Comprehensive chart understanding

### technical_description
- **Purpose**: Technical and systematic analysis
- **Parameters**: max_new_tokens=120, num_beams=4, beam search
- **Use case**: Precise technical documentation

### comprehensive_caption
- **Purpose**: Academic and technical captioning
- **Parameters**: max_new_tokens=200, temperature=0.6, top_p=0.95
- **Use case**: Research documentation

### structured_analysis
- **Purpose**: Structured approach to image analysis
- **Parameters**: max_new_tokens=180, temperature=0.8, top_p=0.9
- **Use case**: Systematic analysis

### precision_focused
- **Purpose**: High-precision factual description
- **Parameters**: max_new_tokens=100, num_beams=5, beam search
- **Use case**: Accurate, factual reporting

## Key Improvements Over Previous Version

1. **Detailed Prompts**: Uses full descriptive prompts instead of simple "a photo of"
2. **Higher Token Limits**: Increased max_new_tokens to 100-200 for longer outputs
3. **Optimized Parameters**: Better temperature and sampling settings for detailed descriptions
4. **Proper Model Usage**: Correctly implements BLIP2 input format with text + image

## Output Structure

```
output/BLIP2-opt-2.7B/
├── 1.json                    # Raw results for image 1
├── 1_comparison.md          # Markdown comparison table
├── 1_comparison.csv         # CSV comparison table
├── 2.json
├── 2_comparison.md
├── 2_comparison.csv
└── ...                      # (18 images total)
```

## Performance Notes

- **Model**: Salesforce/blip2-opt-2.7B
- **GPU**: NVIDIA RTX 4090 (25.3 GB VRAM)
- **Expected performance**: Fast inference, concise but accurate descriptions
- **Specialization**: Image captioning and visual understanding

## Comparison with Other Models

This BLIP2 implementation follows the same structure as:
- LLaVA-NeXT-7B testing scripts
- Qwen2-VL-7B-Instruct testing scripts
- ScreenAI-5B testing scripts (previous version)

All models use consistent output formats for easy comparison.

## Expected Output Quality

BLIP2 models typically generate:
- **Concise descriptions**: 10-50 words per image
- **Accurate content**: Good at identifying main elements
- **Fast inference**: Optimized for speed over length
- **Consistent style**: Similar output patterns across presets

## Key Features

1. **Individual Preset Timing**: Shows timing for each preset separately
2. **Complex Chart Optimization**: Presets specifically designed for scientific images
3. **Detailed Prompts**: Uses full descriptive prompts to encourage longer outputs
4. **Consistent Output Format**: Matches other model testing scripts
5. **Error Handling**: Comprehensive error reporting and recovery
