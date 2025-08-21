# GIT (Generative Image-to-text Transformer) Testing

This folder contains scripts to batch-test GIT models on OCR sample
images and produce readable comparisons and a summary.

- Docs: https://huggingface.co/docs/transformers/en/model_doc/git
- Example models:
  - microsoft/git-base-coco
  - microsoft/git-large-coco
  - microsoft/git-base
  - microsoft/git-base-textvqa

## Environment

```bash
uv venv git-vlm
source git-vlm/bin/activate
uv pip install torch torchvision pillow transformers accelerate pandas tabulate
```

## Scripts

- `git_batch_test.py`: batch inference with per-preset timings and tokens
- `git_postprocess_tables.py`: generate Markdown/CSV comparisons
- `git_summary.py`: aggregate stats across images/presets

## Usage

```bash
# Batch test
auth_token=hf_xxx  # if needed for gated models
python3 experiments/git_vlm/git_batch_test.py \
  --model_name microsoft/git-base-coco \
  --image_dir data/pdf_ocr_samples \
  --output_dir output/GIT-base-coco \
  --device cuda

# Post-process
python3 experiments/git_vlm/git_postprocess_tables.py --results_dir output/GIT-base-coco

# Summary
python3 experiments/git_vlm/git_summary.py --results_dir output/GIT-base-coco
```

## Output layout

```
output/GIT-base-coco/
├── 1.json
├── 1_comparison.md
├── 1_comparison.csv
├── 2.json
├── 2_comparison.md
├── 2_comparison.csv
└── ...
```

## Notes

- We slice off prompt tokens from generated sequences to ensure `output_text`
  does not include the prompt.
- Each preset prints its own timing/tokens in terminal and is saved in JSON.
- Long outputs may still repeat; tune `repetition_penalty` and
  `no_repeat_ngram_size` accordingly.
