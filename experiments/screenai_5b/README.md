# ScreenAI-5B Testing Scripts

This directory contains scripts for testing the ScreenAI-5B model on OCR sample images.

## Environment Setup

1. Create virtual environment:
```bash
uv venv screenai-5b
source screenai-5b/bin/activate
```

2. Install dependencies:
```bash
uv pip install torch torchvision pillow transformers accelerate pandas tabulate
```

## Scripts Overview

### 1. `screenai_5b_batch_test.py` - Main Testing Script
- **Purpose**: Batch test ScreenAI-5B on multiple images with different presets
- **Features**: 
  - 5 preset configurations optimized for complex chart/scientific image captioning
  - Records timing for each preset individually
  - Saves results to JSON files
  - Supports GPU acceleration

**Usage**:
```bash
python3 screenai_5b_batch_test.py [options]

Options:
  --model_name MODEL_NAME    ScreenAI model name (default: google/screenai-5b)
  --image_dir IMAGE_DIR      Directory containing test images (default: data/pdf_ocr_samples)
  --output_dir OUTPUT_DIR    Output directory (default: output/ScreenAI-5B)
  --device {auto,cuda,cpu}  Device to run inference on (default: auto)
```

**Example**:
```bash
python3 screenai_5b_batch_test.py --image_dir data/pdf_ocr_samples --output_dir output/ScreenAI-5B
```

### 2. `screenai_5b_postprocess_tables.py` - Results Processing
- **Purpose**: Convert JSON results to comparison tables
- **Output**: Markdown and CSV comparison tables for each image
- **Features**: Shows preset, output_text, prompt, timing, and generation parameters

**Usage**:
```bash
python3 screenai_5b_postprocess_tables.py --results_dir output/ScreenAI-5B
```

### 3. `screenai_5b_summary.py` - Results Summary
- **Purpose**: Generate overview statistics of testing results
- **Features**: 
  - Timing statistics per image and preset
  - Token count averages
  - Error reporting
  - File count summary

**Usage**:
```bash
python3 screenai_5b_summary.py --results_dir output/ScreenAI-5B
```

### 4. Test Scripts
- `screenai_5b_test_load.py` - Test model loading

## Preset Configurations

### chart_analysis
- **Purpose**: Detailed chart and scientific diagram analysis
- **Parameters**: max_new_tokens=800, temperature=0.3, top_p=0.9
- **Use case**: Comprehensive chart understanding

### technical_description
- **Purpose**: Technical and systematic analysis
- **Parameters**: max_new_tokens=600, num_beams=3, beam search
- **Use case**: Precise technical documentation

### comprehensive_caption
- **Purpose**: Academic and technical captioning
- **Parameters**: max_new_tokens=1000, temperature=0.4, top_p=0.95
- **Use case**: Research documentation

### structured_analysis
- **Purpose**: Structured approach to image analysis
- **Parameters**: max_new_tokens=700, temperature=0.5, top_p=0.9
- **Use case**: Systematic analysis

### precision_focused
- **Purpose**: High-precision factual description
- **Parameters**: max_new_tokens=500, num_beams=4, beam search
- **Use case**: Accurate, factual reporting

## Output Structure

```
output/ScreenAI-5B/
├── 1.json                    # Raw results for image 1
├── 1_comparison.md          # Markdown comparison table
├── 1_comparison.csv         # CSV comparison table
├── 2.json
├── 2_comparison.md
├── 2_comparison.csv
└── ...                      # (18 images total)
```

## Performance Notes

- **Model**: google/screenai-5B
- **GPU**: NVIDIA RTX 4090 (25.3 GB VRAM)
- **Expected performance**: Similar to LLaVA-NeXT-7B
- **Specialization**: Screen understanding and UI analysis

## Comparison with Other Models

This ScreenAI-5B implementation follows the same structure as:
- LLaVA-NeXT-7B testing scripts
- Qwen2-VL-7B-Instruct testing scripts
- DONUT model testing scripts

All models use consistent output formats for easy comparison.

## Key Features

1. **Individual Preset Timing**: Shows timing for each preset separately
2. **Complex Chart Optimization**: Presets specifically designed for scientific images
3. **Consistent Output Format**: Matches other model testing scripts
4. **Error Handling**: Comprehensive error reporting and recovery
