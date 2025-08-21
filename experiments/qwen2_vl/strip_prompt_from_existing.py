#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Strip prompt prefix from output_text in existing JSON results for Qwen2-VL.
- Detect the first occurrence of the prompt inside output_text and remove it.
- Writes files in-place.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path('Output/Qwen2-VL-7B-Instruct')

def main():
    for jf in sorted(ROOT.glob('*.json')):
        try:
            data = json.loads(jf.read_text(encoding='utf-8'))
        except Exception as e:
            print(f"[skip] {jf.name}: {e}")
            continue
        changed = False
        for r in data.get('results', []) or []:
            out = r.get('output_text')
            prompt = r.get('prompt') or ''
            if not out or not prompt:
                continue
            idx = out.find(prompt)
            if idx != -1:
                new_out = out[idx+len(prompt):].lstrip()
                if new_out != out:
                    r['output_text'] = new_out
                    changed = True
        if changed:
            jf.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
            print('fixed', jf.name)

if __name__ == '__main__':
    main()
