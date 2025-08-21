# 图像: 1.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 2.55 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.43 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. A = = , = 4 4 2 2 3 3 4 = 0 0
```

**JSON 输出:**

```json
{
  "text_sequence": "A = = , = 4 4 2 2 3 3 4 = 0 0</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 2.71 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.29 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. A = = = A = = = = A = = = A = = = A = = = A = = A = = A = = A = = A = A = A = A = A = A = = = = = A = = A = = A = A = = = = = = A = = = = A = = = = = = A = = = = = = = = = = A = = = = = = = = = = = = = = A = = = = = = = = = = = = = = = = = = = = = A = = = = = = = = = = = = = A = = = A = = A=:TheThe5.W.....E..B..5.:F.B.B.PoPoPoPoPoPo
```

**JSON 输出:**

```json
{
  "text_sequence": "A = = = A = = = = A = = = A = = = A = = = A = = A = = A = = A = = A = A = A = A = A = A = = = = = A = = A = = A = A = = = = = = A = = = = A = = = = = = A = = = = = = = = = = A = = = = = = = = = = = = = = A = = = = = = = = = = = = = = = = = = = = = A = = = = = = = = = = = = = A = = = A = = A=:TheThe5.W.....E..B..5.:F.B.B.PoPoPoPoPoPo</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 1.13 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. .
```

**JSON 输出:**

```json
{
  "text_sequence": ".</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 1.39 秒

```text
<s_cord-v2> || |||| 0|||0||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "|| |||| 0|||0|||<unk>|||</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 1.18 秒

```text
Provide a concise one-sentence summary of the page content. A S S S S S S S
```

**JSON 输出:**

```json
{
  "text_sequence": "A S S S S S S S</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.56 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A = A</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 1.33 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. must do be on anywhere use only is not to you a listing for yourselves us that me
```

**JSON 输出:**

```json
{
  "text_sequence": "must do be on anywhere use only is not to you a listing for yourselves us that me</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.58 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. A = = A = = = = , A = = ▲ A = , = ▲ A = =
```

**JSON 输出:**

```json
{
  "text_sequence": "A = = A = = = = , A = = ▲ A = , = ▲<unk> A = =</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 1.41 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.V.W.W.V.V.B.W.BeBeBeGeGeGeGeBeBeBeBeB.BeBeEBeBeBeReBeBeBeBaBaBaBaBeBeBeSoSoSoSoBeBeBeMeMeMeMeBeBeBeE.BeBeBBeBeBeSBeBeBeDeBeBeBeHeBeBeBeInBeBeBePoPoPoPoBeBeBeSeSeBeBeBeMaBeBeBeBiBeBeBeMoBeBeBeFiBeBeBePaBeBeBeBoBeBeBeGaGeGeGeMeBeBeB
```

**JSON 输出:**

```json
{
  "text_sequence": "V.W.W.V.V.B.W.BeBeBeGeGeGeGeBeBeBeBeB.BeBeEBeBeBeReBeBeBeBaBaBaBaBeBeBeSoSoSoSoBeBeBeMeMeMeMeBeBeBeE.BeBeBBeBeBeSBeBeBeDeBeBeBeHeBeBeBeInBeBeBePoPoPoPoBeBeBeSeSeBeBeBeMaBeBeBeBiBeBeBeMoBeBeBeFiBeBeBePaBeBeBeBoBeBeBeGaGeGeGeMeBeBeB</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 0.84 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. A = A = , A = = , = , 4 = = . A = .A = , , A A =  , A
```

**JSON 输出:**

```json
{
  "text_sequence": "A = A = , A = = , = , 4 = = . A = .A = , , A A = <unk> , A</s>"
}
```

---

# 图像: 10.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 2.06 秒

```text
<s_cord-v2> |||| 0|||0|||5||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "|||| 0|||0|||5|||<unk>|||</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.30 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. = HW , V = = HHW WWWWW .
```

**JSON 输出:**

```json
{
  "text_sequence": "= HW , V = = HHW WWWWW .</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 2.27 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 0.46 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. = HW V = HW , = HWK
```

**JSON 输出:**

```json
{
  "text_sequence": "= HW V = HW , = HWK</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 1.80 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. = = HW W W W
```

**JSON 输出:**

```json
{
  "text_sequence": "= = HW W W W</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 2.27 秒

```text
<s_cord-v2> |||| 0|||0|||5||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "|||| 0|||0|||5|||<unk>|||</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 1.94 秒

```text
Provide a concise one-sentence summary of the page content. PRE = HW W = HW ,
```

**JSON 输出:**

```json
{
  "text_sequence": "PRE = HW W = HW ,</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.49 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. = |||s_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. = |||s_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_t_</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 1.89 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. 하여 you may behave notbee yourse<sep/> From you ve do you you have a
```

**JSON 输出:**

```json
{
  "text_sequence": "하여 you may behave notbee yourse<sep/> From you ve do you you have a</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.51 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. . . = HW W W W W = HW V = = HW K = HW , V = HW = HWK
```

**JSON 输出:**

```json
{
  "text_sequence": ". . = HW W W W W = HW V = = HW K = HW , V = HW = HWK</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 0.59 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.V.V.W.W.V.
```

**JSON 输出:**

```json
{
  "text_sequence": "V.V.W.W.V.</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 0.79 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. = = = = HW W W W W , = = = , K = = || ||||
```

**JSON 输出:**

```json
{
  "text_sequence": "= = = = HW W W W W , = = = , K = = || ||||</s>"
}
```

---

# 图像: 11.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 1.11 秒

```text
<s_cord-v2> A. A.j. =
```

**JSON 输出:**

```json
{
  "text_sequence": "A. A.j. =</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.27 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. A;; =
```

**JSON 输出:**

```json
{
  "text_sequence": "A;; =</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 5.43 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.05 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. A;; = W W A;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
```

**JSON 输出:**

```json
{
  "text_sequence": "A;; = W W A;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 1.72 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. A ij |
```

**JSON 输出:**

```json
{
  "text_sequence": "A ij |</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 1.15 秒

```text
<s_cord-v2> A. A.;- - ) - - ) - ) | ||| |||||
```

**JSON 输出:**

```json
{
  "text_sequence": "A. A.;- - ) - - ) - ) | ||| |<unk>||||</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 0.99 秒

```text
Provide a concise one-sentence summary of the page content. A i is in -
```

**JSON 输出:**

```json
{
  "text_sequence": "A i is in -</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.39 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. A;;;;;;;sssssssssssssssssssssss.
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. A;;;;;;;sssssssssssssssssssssss.</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 1.74 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. A if it is a real full fullfully with I any life to do not be you have may more use or lo yoursearson that like my meathow they used by the right and we're use only for form uperable all items in i scientify (a) must behave dead by anywhere will us herehave value at any of you
```

**JSON 输出:**

```json
{
  "text_sequence": "A if it is a real full fullfully with I any life to do not be you have may more use or lo yoursearson that like my meathow they used by the right and we're use only for form uperable all items in i scientify (a) must behave dead by anywhere will us herehave value at any of you</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.34 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. A;; = A;;
```

**JSON 输出:**

```json
{
  "text_sequence": "A;; = A;;</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 1.41 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.V.V.W.V.BeBeBeBeGeGeGeGeSoSoSoSoGeGeGeBeBeBeBaBaBaBaBeBeBeReBeBeBeB.BeBeBBeBeBeEBeBeBeSoSoSoBeBeBeSeSeSeSeBeBeBeHeBeBeBeMeGeGeGeBBeBeGeBeBeGeB.BeGeGeBeGeGeBGeGeGeMeMeBeBeBeMoBeBeBeBiBeBeBeInBeBeBeSBeBeBeMaMaBeBeBeFiBeBeBeDeBeBeBePoPoPoPoBeBeBeKeBeBeBeWKBeBeBePaBeBeBeBoBeBeBeDBeBeBeDoBeBeBe
```

**JSON 输出:**

```json
{
  "text_sequence": "V.V.W.V.BeBeBeBeGeGeGeGeSoSoSoSoGeGeGeBeBeBeBaBaBaBaBeBeBeReBeBeBeB.BeBeBBeBeBeEBeBeBeSoSoSoBeBeBeSeSeSeSeBeBeBeHeBeBeBeMeGeGeGeBBeBeGeBeBeGeB.BeGeGeBeGeGeBGeGeGeMeMeBeBeBeMoBeBeBeBiBeBeBeInBeBeBeSBeBeBeMaMaBeBeBeFiBeBeBeDeBeBeBePoPoPoPoBeBeBeKeBeBeBeWKBeBeBePaBeBeBeBoBeBeBeDBeBeBeDoBeBeBe</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 0.39 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. A A A A i i i ii i i i
```

**JSON 输出:**

```json
{
  "text_sequence": "A A A A i i i ii i i i</s>"
}
```

---

# 图像: 12.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 0.91 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.41 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. Attn(H) = softmax( ) = softmax ( Att)()=softmax Att( H) == softmax( Att)
```

**JSON 输出:**

```json
{
  "text_sequence": "Attn(H) = softmax( ) = softmax ( Att)()=softmax Att( H) == softmax( Att)</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 0.92 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.20 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. Attn(H) = software( Attn(H) = softmax(X Attn(H) = softmax(X Attn(H) = softmax(X) X X X X X XK XK XKXKXKKKKkKkKKKkKKKKKKKKKKkKKKKKKk.Kkk.KkKKK.KKKKKKkKkkKKkKKKKKKK.K.KKkKKkKkKKXkKKKkXKkFKkKKKbKk.KkKKKkKf.KkKkkFkEkkkE.KkWKkKKKkIkE
```

**JSON 输出:**

```json
{
  "text_sequence": "Attn(H) = software( Attn(H) = softmax(X Attn(H) = softmax(X Attn(H) = softmax(X) X X X X X XK XK XKXKXKKKKkKkKKKkKKKKKKKKKKkKKKKKKk.Kkk.KkKKK.KKKKKKkKkkKKkKKKKKKK.K.KKkKKkKkKKXkKKKkXKkFKkKKKbKk.KkKKKkKf.KkKkkFkEkkkE.KkWKkKKKkIkE</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 1.00 秒

```text
Transcribe math as LaTeX when clear; keep original text for body.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 0.80 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 0.88 秒

```text
Provide a concise one-sentence summary of the page content.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.47 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts. Atts. Atts.
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts Atts. Atts. Atts.</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 0.80 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. () 는
```

**JSON 输出:**

```json
{
  "text_sequence": "() 는</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.53 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. Attn(H) = softmax ( ) = softmax( Attn( H) = software
```

**JSON 输出:**

```json
{
  "text_sequence": "Attn(H) = softmax ( ) = softmax( Attn( H) = software</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 0.94 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.PoPoPoPossesssesssessses.SoSoSoSoGeGeGeGeBeBeBeBeBaBaBaBaBeBeBeGeGeGeSoSoSoBeBeBeReReBeBeBeB
```

**JSON 输出:**

```json
{
  "text_sequence": "PoPoPoPossesssesssessses.SoSoSoSoGeGeGeGeBeBeBeBeBaBaBaBaBeBeBeGeGeGeSoSoSoBeBeBeReReBeBeBeB</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 0.57 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. Attn(H) = Af Af Af Af Effect Att Att(H) ) = softmax() = H) = softmax ( )
```

**JSON 输出:**

```json
{
  "text_sequence": "Attn(H) = Af Af Af Af Effect Att Att(H) ) = softmax() = H) = softmax ( )</s>"
}
```

---

# 图像: 13.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 2.43 秒

```text
<s_cord-v2> TAPASEASE 1p TAPASBASE 2p TAPSBASE 4p TAPASE 4p TAPASE 8p TAPABASE 16p TAPASASE 8p 16p 63.4 64.6 65. 62.4 35.6 37.0 62.4 34.6 64.5 65. 63.4 62.5 33.4 64.5 37.0 37.3 33.6 62.4 9.9% 8.4% 2p P TAPASE 2p p p TAPASE 1p P TAPASE 4p TA PASBASE 1 6p TAP A B B B BASE 4 TAP TAP TAPASE TAPA TAPA TAP T
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASEASE 1p TAPASBASE 2p TAPSBASE 4p TAPASE 4p TAPASE 8p TAPABASE 16p TAPASASE 8p 16p 63.4 64.6 65.<unk> 62.4 35.6 37.0 62.4 34.6 64.5 65.<unk> 63.4 62.5 33.4 64.5 37.0 37.3 33.6 62.4 9.9% 8.4% 2p P TAPASE 2p p p TAPASE 1p P TAPASE 4p TA PASBASE 1 6p TAP A B B B BASE 4 TAP TAP TAPASE TAPA TAPA TAP T</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 1.16 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. 2p TA TA BA BA 4p .5. 37.3 62.4 6 6 5 0 0 1 % %%%6%6%.6% 6%.6 65.0 0.1% % TAPASBASE 8 p TA PA SBASE I6p TAP A B BASEASE 2 p T AP A S D A E E F F R R A A T PASBASE 4 p A P T. S. 0 %.2. 1 0 1. % 0 , 0 6.7. 1. 0 66. I T TAF S 0 r r 0 n n 0 T A. T P P A r. / / 0 63. % ns. d.f. p p 64. b. s. l p 5.8 0 68.
```

**JSON 输出:**

```json
{
  "text_sequence": "2p TA TA BA BA 4p .5.<unk> 37.3 62.4 6 6 5 0 0 1 % %%%6%6%.6% 6%.6 65.0 0.1% % TAPASBASE 8 p TA PA SBASE I6p TAP A B BASEASE 2 p T AP A S D A E E F F R R A A T PASBASE 4 p A P T. S. 0 %.2. 1 0 1. % 0 , 0 6.7. 1. 0 66. I T TAF S 0 r r 0 n n 0 T A. T P P A r. / / 0 63. % ns. d.f. p p 64. b. s. l p 5.8 0 68.</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 4.52 秒

```text
<s_cord-v2> TAPASBASE 1p TAPSBASE 2p TAPASE 4p TAPAS 8p TABASE 6p TPASBASE 16p TAPPASES [6p 63.4 TAPASASE 8p 16p PABASE | 6p 0p p S A BASE 1P TAPASPASE 4 5 3 9 p TAPASRASE 2 6.9 p TAPASASA INPARABE 1p TAPISASE 48456565666666666666 TAPASSASE 8p TA PASBASE 8c 14p TIPAPE MARE BEFORESTONERS EARb
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASBASE 1p TAPSBASE 2p TAPASE 4p TAPAS 8p TABASE 6p TPASBASE 16p TAPPASES [6p 63.4 TAPASASE 8p 16p PABASE | 6p 0p p S A BASE 1P TAPASPASE 4 5 3 9 p TAPASRASE 2 6.9 p TAPASASA INPARABE 1p TAPISASE 48456565666666666666 TAPASSASE 8p TA PASBASE 8c 14p TIPAPE MARE BEFORESTONERS EARb</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.18 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. 4p TAPAAPASBASE 8p TAPASBASE 16p TAPASBASE 4p TAPASBASE 8p TAPASBASE 2p TAPASBASE 4p TAPASBASE TAPSBASE 2p 2p TAPA PA. Tp .p P TAPAB.p.p. Tp.pp.p.pp.p.pp.pp.p.pp TAPA.p.pp.pppp TAPA.pppp.pppp.pppp.pppppppppp T.pppppppppppppppppp T.pp T.c.pppppppp.pp.p pp.pppp.pppp.Po.pppppp.com.pppppppp.pp.pppp.pppppp.Po.pppp.pppp
```

**JSON 输出:**

```json
{
  "text_sequence": "4p TAPAAPASBASE 8p TAPASBASE 16p TAPASBASE 4p TAPASBASE 8p TAPASBASE 2p TAPASBASE 4p TAPASBASE TAPSBASE 2p 2p TAPA PA. Tp .p P TAPAB.p.p. Tp.pp.p.pp.p.pp.pp.p.pp TAPA.p.pp.pppp TAPA.pppp.pppp.pppp.pppppppppp T.pppppppppppppppppp T.pp T.c.pppppppp.pp.p pp.pppp.pppp.Po.pppppp.com.pppppppp.pp.pppp.pppppp.Po.pppp.pppp</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 2.64 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. TAPASBASE 4p TA PASBASE 8p TA SBASE 16p 63.4 64.6 65. 65. 62.4 34.6 35.6 37.0 37.3 63.6 32.4 34.5 64.5 65.0 64.3 33.6 32.2 9.9% 8.4% 8.1% 7.2% 7.0%
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASBASE 4p TA PASBASE 8p TA SBASE 16p 63.4 64.6 65. 65. 62.4 34.6 35.6 37.0 37.3 63.6 32.4 34.5 64.5 65.0 64.3 33.6 32.2 9.9% 8.4% 8.1% 7.2% 7.0%</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 7.46 秒

```text
<s_cord-v2> TAPASEASE 1p TAPASBASE 2p TAPSBASE 4p TAPASE 8p TAPASRASE 8p 16p TAPASASE 8p TAPABASE 16p 63.4 64.6 65. 62.4 35.6 37.0 62.4 34.6 64.5 65. 63.4 62.5 63.0 37.3 33.6 62.4 9.9% 8.4% 2p TAPASPASE 2p P P P P TAPASPARE TAPASPA TAPASP TAPASPE TAPASP BASE 8 p TAPASBSE 16p 16p p TAPASP
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASEASE 1p TAPASBASE 2p TAPSBASE 4p TAPASE 8p TAPASRASE 8p 16p TAPASASE 8p TAPABASE 16p 63.4 64.6 65.<unk> 62.4 35.6 37.0 62.4 34.6 64.5 65.<unk> 63.4 62.5 63.0 37.3 33.6 62.4 9.9% 8.4% 2p TAPASPASE 2p P P P P TAPASPARE TAPASPA TAPASP TAPASPE TAPASP BASE 8 p TAPASBSE 16p 16p p TAPASP</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 6.14 秒

```text
Provide a concise one-sentence summary of the page content. 1p A BASE 2p TAPASBASE 4 TAPASBASE 8p TAPASBASE 16p TAPASBASE 1 6 8p TAPASBASE 8p TAPASBASE 16p 63.4 64.5 35. 62.4 64.6 35.0 6
```

**JSON 输出:**

```json
{
  "text_sequence": "1p A BASE 2p TAPASBASE 4 TAPASBASE 8p TAPASBASE 16p TAPASBASE 1 6 8p TAPASBASE 8p TAPASBASE 16p 63.4 64.5 35.<unk> 62.4 64.6 35.0 6</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.37 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP IP</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 6.57 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. TAPASBASE 4p p SP ABAB 8p PSP 1 6p TFPFFRKS TA TRASE 16 60 30 50506040908080 0 0 0 64 58585545856545 4949594739 39.4 5 TAPA SBASE 8p TAP TP SEASE 8c f APARSHEEP SARE % %%%% [ 6.7 63.4 68 69 62.6 65. PA PASBASE &p TAPA BASE L EARFORMERBAE 6g 36.5 APT
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASBASE 4p p SP ABAB 8p PSP 1 6p TFPFFRKS TA TRASE 16 60 30 50506040908080 0 0 0 64 58585545856545 4949594739 39.4 5 TAPA SBASE 8p TAP TP SEASE 8c f APARSHEEP SARE % %%%% [ 6.7 63.4 68 69 62.6 65.<unk> PA PASBASE &p TAPA BASE L EARFORMERBAE 6g 36.5 APT</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 2.30 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. 1p TAPASBASE 4p TAPA SBASE 8p T TAPASBATE 16p T TATASBASE 8p TA PASBASE 16p 63.4 64.6 65. 65. 62.4 T TAPA S BASE 8 p T TAPA BASE 1 p TAPA 2p TAPA S T TAPA 2 TAPA SASE 1p TABASE 2p T T TAPA 1p T. TAPA 1 p T T T T. T TAPASE TAPASE 1p T TAP TAPASE 16p TAPASE 8p TAPA 16pp TAPASE 18 TAPASE 19 TAPA 16p 65. 16p T 16pp T 16p TAP 16p T 6 T 16p TA T 16pp 65. 19 T 16pp TA T 16 16 16 16pp T 10 65. 16 16 16 p T 16 16 p 65. 15 16 16 16 pp 65. 8p 65. 8pp 65. 16pp T 6 65. 16 p TA T 16p 69 65. 5 65. 6 65. 19 63. 16p 65 1 65. 8c 65. 16m 65. 6 63. 6 65 65. 19 65. 19 TORP TAPAS 65. 63. 63. . 63. SAMPA 63. SPORT @
```

**JSON 输出:**

```json
{
  "text_sequence": "1p TAPASBASE 4p TAPA SBASE 8p T TAPASBATE 16p T TATASBASE 8p TA PASBASE 16p 63.4 64.6 65.<unk> 65.<unk> 62.4 T TAPA S BASE 8 p T TAPA BASE 1 p TAPA 2p TAPA S T TAPA 2 TAPA SASE 1p TABASE 2p T T TAPA 1p T. TAPA 1 p T T T T. T TAPASE TAPASE 1p T TAP TAPASE 16p TAPASE 8p TAPA 16pp TAPASE 18 TAPASE 19 TAPA 16p 65. 16p T 16pp T 16p TAP 16p T 6 T 16p TA T 16pp 65. 19 T 16pp TA T 16 16 16 16pp T 10 65. 16 16 16 p T 16 16 p 65. 15 16 16 16 pp 65. 8p 65. 8pp 65. 16pp T 6 65. 16 p TA T 16p 69 65. 5 65. 6 65. 19 63. 16p 65 1 65. 8c 65. 16m 65. 6 63. 6 65 65. 19 65. 19 TORP TAPAS 65. 63. 63. . 63. SAMPA 63. SPORT @</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 0.91 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON. From From From From Total Total Total
```

**JSON 输出:**

```json
{
  "text_sequence": "From From From From Total Total Total</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 3.09 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. 4p TAPA SBASE 8p TAPASBASE 16p TAPASBASE 8p S S S SASE 1 6 6 8 8 8 8 4 8 8 4 4 8 8 8 6 8 8 1 6 6 6 6 8 1 6p TA SBASE 4p TA PASBASE 4p 8p 8p 6p TAPA BASE 8p 4p BASE 1p 4p 2p 4p 4p 8 p TAPA 2p 2p P 2p SP 8p 2p TABABSE 2p TAPAP 2p TIP 2p TAP 2p T&amp TAPAp 2p S&amp T&ampt 2p T 2p T P 2p TTP 2p TPMENT 2p TSP 2p T AP AP AP AP T&amp P P 2p TABE 2p T 8p TAP T&amp TAPE T&amps T&amp D&amp TAP&amp TABBE T&amp BASE 2p T T&amp SAMPT 2p BABE 8.8p TABE TOUR 8.8 T&amp p T&amp dp BABE TABE TABLE 2p THATE TABLE TOUR P P P Qp TABE
```

**JSON 输出:**

```json
{
  "text_sequence": "4p TAPA SBASE 8p TAPASBASE 16p TAPASBASE 8p S S S SASE 1 6 6 8 8 8 8 4 8 8 4 4 8 8 8 6 8 8 1 6 6 6 6 8 1 6p TA SBASE 4p TA PASBASE 4p 8p 8p 6p TAPA BASE 8p 4p BASE 1p 4p 2p 4p 4p 8 p TAPA 2p 2p P 2p SP 8p 2p TABABSE 2p TAPAP 2p TIP 2p TAP 2p T&amp TAPAp 2p S&amp T&ampt 2p T 2p T P 2p TTP 2p TPMENT 2p TSP 2p T AP AP AP AP T&amp P P 2p TABE 2p T 8p TAP T&amp TAPE T&amps T&amp D&amp TAP&amp TABBE T&amp BASE 2p T T&amp SAMPT 2p BABE 8.8p TABE TOUR 8.8 T&amp p T&amp dp BABE TABE TABLE 2p THATE TABLE TOUR P P P Qp TABE</s>"
}
```

---

# 图像: 14.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 1.89 秒

```text
<s_cord-v2> - - Same - Same e e e e r r r r t r r r e e e d e e e f r r r - Same to - ) - ) - to 0 0 0 0 6 0 0 0 9 9 9 9 8 9 9 9 6 1 - - ) - 0 0 0 4, 0 0 0 2, 4, 6) 62.1 61.8 60.7 60.5 60.5 60.6 61. 60.8 61.0 60.8 60.8 - Sentence to Header - Senence to Sentence - All - ) - - - ) Sentence to to - - Sentence - to - - - Senence - to to - Sentence , , . . - . , - .
```

**JSON 输出:**

```json
{
  "text_sequence": "- - Same - Same e e e e r r r r t r r r e e e d e e e f r r r - Same to - ) - ) - to 0 0 0 0 6 0 0 0 9 9 9 9 8 9 9 9 6 1 - - ) - 0 0 0 4, 0 0 0 2, 4, 6) 62.1 61.8 60.7 60.5 60.5 60.6 61.<unk> 60.8 61.0 60.8 60.8 - Sentence to Header - Senence to Sentence - All - ) - - - ) Sentence to to - - Sentence - to - - - Senence - to to - Sentence , , . . - . , - .</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 1.21 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. . Same Row - - Samp Se Sell - Call to Column Header - Came to Coll - Reader to Cotumn Cell 60.7 60.5 60.6 61.0 60 54.5 - All Columbus Realer , 4, 6) - Seatence to - Header to _ - | - ) - () - 2, 9, 4) - _ _ 6 2.1 - 62.1 - Header to ______________ - Standard - Hader - 1 - Meader - State - Headr - -1 - I - l - [ - i - ! - / - ' - E - a - = - : - L - 3 - A - " -_ - 1. - Beader in - e - 0 - Le -
```

**JSON 输出:**

```json
{
  "text_sequence": ". Same Row - - Samp Se Sell - Call to Column Header - Came to Coll - Reader to Cotumn Cell 60.7 60.5 60.6 61.0 60 54.5 - All Columbus Realer , 4, 6) - Seatence to - Header to _ - | - ) - () - 2, 9, 4) - _ _ 6 2.1 - 62.1 - Header to ______________ - Standard - Hader - 1 - Meader - State - Headr - -1 - I - l - [ - i - ! - / - ' - E - a - = - : - L - 3 - A - \" -_ - 1. - Beader in - e - 0 - Le -</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 7.12 秒

```text
<s_cord-v2> - Same e l a d t r . 0 1 - ) - Same Coll - Call to Column - Cell to - Header to - Header to - Reader to Other Header - Headar to Same Header () - - Hender to Sentence - Sentence to Cell - - Sentence to Cll - Sentance to - Sentenc to - Senence to Hell - Sentend to Selentence - to Sender - Sentence to Helder - Sentense to Sentenc - All to Counc - - - ) / - - A11 - - to - - Alliance to - ) --() - )------------------------------ - -
```

**JSON 输出:**

```json
{
  "text_sequence": "- Same e l a d t r . 0 1 - ) - Same Coll - Call to Column - Cell to - Header to - Header to - Reader to Other Header - Headar to Same Header () - - Hender to Sentence - Sentence to Cell - - Sentence to Cll - Sentance to - Sentenc to - Senence to Hell - Sentend to Selentence - to Sender - Sentence to Helder - Sentense to Sentenc - All to Counc - - - ) / - - A11 - - to - - Alliance to - ) --() - )------------------------------ - -</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.22 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . - . - . - . - . - . . - . . - . - . - . . - . - . - . - . - . .. . . .
```

**JSON 输出:**

```json
{
  "text_sequence": ". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . - . - . - . - . - . . - . . - . - . - . . - . - . - . - . - . .. . . .</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 2.15 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. 32.1 62.1 61.8 60.7 60.5 60.6 61. 60.8 - Sentence to Header - Senence to Sentence - All Column Related (# 2, 4, 6) 2.8 37.7 38.4 36.6 36.4 36.4 35.8 35.8 36.9 36.3 36.2 37.3 35.3 29.3 62.1 61.1 60.0 54.5 32.1 62. 62.1 31.8 62.1 - Header to 2.8 33.4 2.8 32.4.
```

**JSON 输出:**

```json
{
  "text_sequence": "32.1 62.1 61.8 60.7 60.5 60.6 61.<unk> 60.8 - Sentence to Header - Senence to Sentence - All Column Related (# 2, 4, 6) 2.8 37.7 38.4 36.6 36.4 36.4 35.8 35.8 36.9 36.3 36.2 37.3 35.3 29.3 62.1 61.1 60.0 54.5 32.1 62.<unk> 62.1 31.8 62.1 - Header to 2.8 33.4 2.8 32.4.</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 6.69 秒

```text
<s_cord-v2> - - - Same e e e e r r r r - Same Coll - ) - - ) - ) - 0 0 0 0 9 9 9 9 6 9 9 9 8 9 9 9 5 9 9 9 3 9 9 6 6 1 0 0 0 - - - Sentence to Center to - Sentence - to Cll - ) - to to Sentence to Header 60.8 61.0 60.0 0 0 0 2, 4, 6) - All Column Related (# 2, 5 32.1 62.1 61.8 60.7 60.5 60.5 60.6 61.0 61.1 60.8 60.8 0 0 0 611 - - ) |||| | || , | . , , . . | ,
```

**JSON 输出:**

```json
{
  "text_sequence": "- - - Same e e e e r r r r - Same Coll - ) - - ) - ) - 0 0 0 0 9 9 9 9 6 9 9 9 8 9 9 9 5 9 9 9 3 9 9 6 6 1 0 0 0 - - - Sentence to Center to - Sentence - to Cll - ) - to to Sentence to Header 60.8 61.0 60.0 0 0 0 2, 4, 6) - All Column Related (# 2, 5 32.1 62.1 61.8 60.7 60.5 60.5 60.6 61.0 61.1 60.8 60.8 0 0 0 611 - - ) |||| | || , | . , , . . | ,</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 1.13 秒

```text
Provide a concise one-sentence summary of the page content. - Same Pee - Same R R - - Seatence to - Seat to - Seat Cell - Seat Call - Secution to - Header to Column - Header to - Header to - - Senence - Sentence to Call - - Sentence to Header -
```

**JSON 输出:**

```json
{
  "text_sequence": "- Same Pee - Same R R - - Seatence to - Seat to - Seat Cell - Seat Call - Secution to - Header to Column - Header to - Header to - - Senence - Sentence to Call - - Sentence to Header -</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.50 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. - - - - - - - - - - - - - - - - - - - - State to State: - |||||||||||||||||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. - - - - - - - - - - - - - - - - - - - - State to State: - |||||||||||||||||||||</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 5.21 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. - Please Send to - Same To Se Re Re Rear - Sentence - ||=0704060000000000000 - And Call to Coll - ---------- () All State In - Column - ) (All A C ee - 1 - _________________ - 60 9 61.1 0 61.8 60.6 - Sentance to Header - Sentense to Sentence to - All - 'Sentence to Centence - - - Sentence to to - to - - Sentende - - in 2, of the 2, and a dshall 42, 4, 4.9 2.0% 40. sholds 24. 24 % 34.2 442 20. 23.46 263 31.3136. 50. 36.3. 36.3 26. 4949301326 6688 30. 8 8.29 21.9698 29 29.4 25, 43. 46.28 50525 28.40% 4110 00.2018 60. 45: 3.60 080 25.45 2, 21, 2017.02.03 32.39 25.20 2, 55% 9.2 $15050 20, 4& 33.24.95 9/2 24.48 28, 23,
```

**JSON 输出:**

```json
{
  "text_sequence": "- Please Send to - Same To Se Re Re Rear - Sentence - ||<unk>=0704060000000000000 - And Call to Coll - ---------- () All State In - Column - ) (All A C ee - 1 - _________________ - 60 9 61.1 0 61.8 60.6 - Sentance to Header - Sentense to Sentence to - All - 'Sentence to Centence - - - Sentence to to - to - - Sentende - - in 2, of the 2, and a dshall 42, 4, 4.9 2.0% 40. sholds 24. 24 % 34.2 442 20. 23.46 263 31.3136. 50. 36.3. 36.3 26. 4949301326 6688 30. 8 8.29 21.9698 29 29.4 25, 43. 46.28 50525 28.40% 4110 00.2018 60. 45: 3.60 080 25.45 2, 21, 2017.02.03 32.39 25.20 2, 55% 9.2 $15050 20, 4& 33.24.95 9/2 24.48 28, 23,</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 4.01 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. - Same Row - Same Column Column - Same Cell to Column Reader - Cell to Coll - - - - . - . . - - - Same to - - - Samples. ... - - Same Lown - - - Sale to - .. . ( ) - - Same To - . () - .s - - - Came - - - to - - to . - Same to to to - - Steam - - -. - - to to the - - - Sta - . to to to to ( ) - . 3. - . 3 - . 0 - . 10 - . 5 - . 1 - . 9 - . I - . 62.1 - . 2, - . 8 - . 60. . 0. . , . - to to . 0 . 2.8 - . 4 - . 30 - . 50 - . 56. . 3 . 3.00 - . 40 2, . 0.00 - . 2. . 8.00 . 5.00 . 5.8 . 4.00 2, 3.00 . 0.01 0.00 2, 2, 0.00 . 0000 0.00 0.00 3.00 0.00 0000 . 002 2, 2.8 0.00 , 2,2 2, , 0.00 60. 0.00 2.8 . 888 60. 2.8 2.8 3.00 2.8 , 2.8 60. 3.00 3.00 4.00 60. 2, 4, 4, 2, 33.3 35. 2.8 62.1 62.1 2.8 37. 2.8 38. 2.8 36.6 2.8 5.8 60. 60. 60 60. 5.8 35.8 60. 4.00 36.6 60. 5.6 60. 603 60. 60 2.8 36.4 36.3 60. 35.8 35.8 36.3 35. 60. 34.3 36.3 35.8 34.3 34.3 60.4 36.3 34.3 35.8 36.3 60.3 60.4 34.3 36.3 35.8 33.3 60.3 35.8 36.8 60.3 35.3 60 60.3 25.3 60. 24.3 60.2,
```

**JSON 输出:**

```json
{
  "text_sequence": "- Same Row - Same Column Column - Same Cell to Column Reader - Cell to Coll - - - - . - . . - - - Same to - - - Samples. ... - - Same Lown - - - Sale to - .. . ( ) - - Same To - . () - .s - - - Came - - - to - - to . - Same to to to - - Steam - - -. - - to to the - - - Sta - . to to to to ( ) - . 3. - . 3 - . 0 - . 10 - . 5 - . 1 - . 9 - . I - . 62.1 - . 2, - . 8 - . 60. . 0. . , . - to to . 0 . 2.8 - . 4 - . 30 - . 50 - . 56. . 3 . 3.00 - . 40 2, . 0.00 - . 2. . 8.00 . 5.00 . 5.8 . 4.00 2, 3.00 . 0.01 0.00 2, 2, 0.00 . 0000 0.00 0.00 3.00 0.00 0000 . 002 2, 2.8 0.00 , 2,2 2, , 0.00 60. 0.00 2.8 . 888 60. 2.8 2.8 3.00 2.8 , 2.8 60. 3.00 3.00 4.00 60. 2, 4, 4, 2, 33.3 35. 2.8 62.1 62.1 2.8 37. 2.8 38. 2.8 36.6 2.8 5.8 60. 60. 60 60. 5.8 35.8 60. 4.00 36.6 60. 5.6 60. 603 60. 60 2.8 36.4 36.3 60. 35.8 35.8 36.3 35. 60. 34.3 36.3 35.8 34.3 34.3 60.4 36.3 34.3 35.8 36.3 60.3 60.4 34.3 36.3 35.8 33.3 60.3 35.8 36.8 60.3 35.3 60 60.3 25.3 60. 24.3 60.2,</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 3.11 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.WWWWWWWWWWSWSWSWS - .WBASE - .com/PoPoPoPossesssessses.WWWWSWSWWWWWWSPSPS://WWWWW.WWSWSWSMSMSMSMSWSWSWSPSPSPSPSWSWSWSWWSWSMSWSWSWMSMSMSRSEWSWSWSHSHSMSMSMS/WWWWWWWWWSWWWWSMSMSRSRSRSRSWSWSWSKSWSWSWSWWWWWW.SWSWSWSRSRSRSMSMSMS,WWWWWMSMSMSWWWWW,WWWWSRSRSMSWSWSPSWSWSWBWSWSWS/PoPoRTWSWSWS.WWW.WMSWSWSMSRSRSMSRSRS/PoPownWSWSWSRFRFRFRFRSRSRS/WWWWS/WMSMSRSMSMSWSMSMS/Prs.WMSMS/ToToToTownWSWSRSMSMS/PoPoRPWSWSWSPGMSMSMSRFRFRFWSWSWSProProProPromoWSWSWS, WSWSWSMISMISMISMISMSMSMS (%), RFRFRFGMSMSMS 62.1 62.1 2.8 62.1 6, 2.8 9, 2.8 2.8 3, 2.8 2, 2.8 %, 2.8 35.8 62.1 62.0 2.8 62.8 62.1 61. 2.8 32.8 2.8 37. 2.8 5.8 62.1 35.8 35.8 62.8 2.8 61.1 62.1 62.8 35.8 37./WWW 2.8 2.8. 2.8 37.6 2.8 37.7.WWWWS 2.8 35.6 35.8 32.8 37.
```

**JSON 输出:**

```json
{
  "text_sequence": "WWWWWWWWWWSWSWSWS - .WBASE - .com/PoPoPoPossesssessses.WWWWSWSWWWWWWSPSPS://WWWWW.WWSWSWSMSMSMSMSWSWSWSPSPSPSPSWSWSWSWWSWSMSWSWSWMSMSMSRSEWSWSWSHSHSMSMSMS/WWWWWWWWWSWWWWSMSMSRSRSRSRSWSWSWSKSWSWSWSWWWWWW.SWSWSWSRSRSRSMSMSMS,WWWWWMSMSMSWWWWW,WWWWSRSRSMSWSWSPSWSWSWBWSWSWS/PoPoRTWSWSWS.WWW.WMSWSWSMSRSRSMSRSRS/PoPownWSWSWSRFRFRFRFRSRSRS/WWWWS/WMSMSRSMSMSWSMSMS/Prs.WMSMS/ToToToTownWSWSRSMSMS/PoPoRPWSWSWSPGMSMSMSRFRFRFWSWSWSProProProPromoWSWSWS, WSWSWSMISMISMISMISMSMSMS (%), RFRFRFGMSMSMS 62.1 62.1 2.8 62.1 6, 2.8 9, 2.8 2.8 3, 2.8 2, 2.8 %, 2.8 35.8 62.1 62.0 2.8 62.8 62.1 61. 2.8 32.8 2.8 37. 2.8 5.8 62.1 35.8 35.8 62.8 2.8 61.1 62.1 62.8 35.8 37./WWW 2.8 2.8. 2.8 37.6 2.8 37.7.WWWWS 2.8 35.6 35.8 32.8 37.</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 9.00 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. - - Header to Column Cell - - - - . - . All Column Reated (# 2, 4, 6) Column Related to Sentence - - - All - - - Sentence to Sentence to - - - Se . - - All Sendence to to - . Sentence to to Se . All - . . - Same . HASSE - - - Same - . to . , . RESE - . Reader - . Header - . _ . - to . - State - . Scale - . Send Send Send Send . - Send Send Send - . Please - to Send Send - to Send - , Send Send - Send Send - - Send - Send . Send - Send - to Center - . 3, Send Send Send 2, to Send Send Send _ Send Send - ) 2, Send - to to Send - Send 2, Send Send , to Send - - to Send 2, - to Send . 3 3, - Send - ) - Send - CONT - Send - you 2, - ) - , - Send Sender - to Sender - Send - - - Sender - ) - - - 2, 2, - - - _ - - - ) - 2, - _ _ _ _ - - _ _ - 2, to to to _ _ _ 3 | | , 3 | 3 | 62.1 62.1 61 | 2.8 2.8 | . 2.8 . | LL 2.8 6 2.8 , 2.8 YO 2.8 5.8 2.8 6.2 2.8 XO 2.8 LL | YO , YO YO | XO YO IO 2.8 IO YO 3 2.8 ROL 2.8 SHO YO XO XO IO XO | IO IO | HQ YO LL YO dd YO THAN YO UO YO WO YO ARE YO ROL YO HQ XO LL XO ROL XO , XO wor YO ll YO TAL YO MOR YO EO YO OU YO OO YO HL YO SHO XO HQ IO LL IO ROL IO , IO HQ 2.8 HQ LL LL ROL ROL LL HQ ROL | ROL WO XO dd XO THAN XO UO XO YR YO wor XO MOR XO WO IO dd IO SHO IO THAN IO UO IO WO LL WO ROL HQ HQ WO HQ | WO WO | dd LL dd ROL dd HQ dd WO dd dd | SHO LL , LL SHO HQ SHO dd SHO WO SHO ROL SHO | wor IO ll XO HL XO ll LL ll IO HL IO wor LL UO LL THAN LL MOR IO MOR LL 999 YO LOR YO STO YO USE YO MON YO 666 YO HH YO YS YO AUD YO YK YO YAR YO . YO 999 XO TAL XO ARE XO SHO SHO 2.8 dd 2.8 WO 2.8 ll WO MOR SHO , WO , | MOR | HL LL TAL IO TAL LL JR YO LS YO ISS YO TAI YO YM YO IH YO SN YO 866 YO RES YO SON YO 7% YO TOK YO 888 YO MARK YO LONG YO WW YO WAN YO JU YO 980 YO 0.00 YO UND YO GOR YO JR XO STO XO . XO 666 XO MON XO 999 IO . IO STO IO MON SHO THAN SHO MOR WO THAN 2.8 MOR 2.8 UO SHO . SHO UO 2.8 THAN , , SHO MON 2.8 MON , UO , THAN . LL . WO . UO . THAN WO UO WO CONT YO HAS YO 5.8 YO CONTROL YO 61.1 YO 60.5 2.8 38. 2.8 60.5 . 5.8 . 5.6 2.8 5.6 , 5.8 , CONTROL THE . 6.2 , 7.3 , 6.2 . CONTROL TO , LONG , ). . 7.3 .
```

**JSON 输出:**

```json
{
  "text_sequence": "- - Header to Column Cell - - - - . - . All Column Reated (# 2, 4, 6) Column Related to Sentence - - - All - - - Sentence to Sentence to - - - Se . - - All Sendence to to - . Sentence to to Se . All - . . - Same . HASSE - - - Same - . to . , . RESE - . Reader - . Header - . _ . - to . - State - . Scale - . Send Send Send Send . - Send Send Send - . Please - to Send Send - to Send - , Send Send - Send Send - - Send - Send . Send - Send - to Center - . 3, Send Send Send 2, to Send Send Send _ Send Send - ) 2, Send - to to Send - Send 2, Send Send , to Send - - to Send 2, - to Send . 3 3, - Send - ) - Send - CONT - Send - you 2, - ) - , - Send Sender - to Sender - Send - - - Sender - ) - - - 2, 2, - - - _ - - - ) - 2, - _ _ _ _ - - _ _ - 2, to to to _ _ _ 3 | | , 3 | 3 | 62.1 62.1 61 | 2.8 2.8 | . 2.8 . | LL 2.8 6 2.8 , 2.8 YO 2.8 5.8 2.8 6.2 2.8 XO 2.8 LL | YO , YO YO | XO YO IO 2.8 IO YO 3 2.8 ROL 2.8 SHO YO XO XO IO XO | IO IO | HQ YO LL YO dd YO THAN YO UO YO WO YO ARE YO ROL YO HQ XO LL XO ROL XO , XO wor YO ll YO TAL YO MOR YO EO YO OU YO OO YO HL YO SHO XO HQ IO LL IO ROL IO , IO HQ 2.8 HQ LL LL ROL ROL LL HQ ROL | ROL WO XO dd XO THAN XO UO XO YR YO wor XO MOR XO WO IO dd IO SHO IO THAN IO UO IO WO LL WO ROL HQ HQ WO HQ | WO WO | dd LL dd ROL dd HQ dd WO dd dd | SHO LL , LL SHO HQ SHO dd SHO WO SHO ROL SHO | wor IO ll XO HL XO ll LL ll IO HL IO wor LL UO LL THAN LL MOR IO MOR LL 999 YO LOR YO STO YO USE YO MON YO 666 YO HH YO YS YO AUD YO YK YO YAR YO . YO 999 XO TAL XO ARE XO SHO SHO 2.8 dd 2.8 WO 2.8 ll WO MOR SHO , WO , | MOR | HL LL TAL IO TAL LL JR YO LS YO ISS YO TAI YO YM YO IH YO SN YO 866 YO RES YO SON YO 7% YO TOK YO 888 YO MARK YO LONG YO WW YO WAN YO JU YO 980 YO 0.00 YO UND YO GOR YO JR XO STO XO . XO 666 XO MON XO 999 IO . IO STO IO MON SHO THAN SHO MOR WO THAN 2.8 MOR 2.8 UO SHO . SHO UO 2.8 THAN , , SHO MON 2.8 MON , UO , THAN . LL . WO . UO . THAN WO UO WO CONT YO HAS YO 5.8 YO CONTROL YO 61.1 YO 60.5 2.8 38. 2.8 60.5 . 5.8 . 5.6 2.8 5.6 , 5.8 , CONTROL THE . 6.2 , 7.3 , 6.2 . CONTROL TO , LONG , ). . 7.3 .</s>"
}
```

---

# 图像: 15.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 7.65 秒

```text
<s_cord-v2> TAPASE TAPASBASE-SAT TA TA TA SBASE-SO TABLEFORMERBASE-SO TA TA TA TA B B BASE-SO 57.6 TAPASE---- 57.6 45.2 - 60.0 62.2 57.6 47.4 - 60.2 61.5 46.4 - 59.8 61.5
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASE TAPASBASE-SAT TA TA TA SBASE-SO TABLEFORMERBASE-SO TA TA TA TA B B BASE-SO 57.6 TAPASE---- 57.6 45.2 - 60.0 62.2 57.6 47.4 - 60.2 61.5 46.4 - 59.8 61.5</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 1.30 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.com TAPASE-SAT TABLEFORMERBASE-SO 62.2 57.6 45.2 60.0 64.2 62.5 6.2 61.5 . - 59.8 61.7 60.7 61 9 6 6 5 6 4 4 - 60 0 6 2 6 1 5 7 4 , - 60.5 61.1 6 9 9 8 6 3 5 4 5 2 2 60 60 61.2 61.4 - - 69.3 61.3 6 0.6 63.2 63.5 6 2.8 66.2 2 5 7.6 46.4 - 60- 60- 6- 6-2- 6 6.5 62.1 6.5.2 65.8 61.7.9 6 8p 47.4-4- - -60.02 6:5 - 61-7 6:1.9 TAPASBASE -
```

**JSON 输出:**

```json
{
  "text_sequence": "com TAPASE-SAT TABLEFORMERBASE-SO 62.2 57.6 45.2 60.0 64.2 62.5 6.2 61.5 . - 59.8 61.7 60.7 61 9 6 6 5 6 4 4 - 60 0 6 2 6 1 5 7 4 , - 60.5 61.1 6 9 9 8 6 3 5 4 5 2 2 60 60 61.2 61.4 - - 69.3 61.3 6 0.6 63.2 63.5 6 2.8 66.2 2 5 7.6 46.4 - 60- 60- 6- 6-2- 6 6.5 62.1 6.5.2 65.8 61.7.9 6 8p 47.4-4- - -60.02 6:5 - 61-7 6:1.9 TAPASBASE -</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 3.25 秒

```text
<s_cord-v2> TAPASBASE TAPSBASE-SO TABASE-S TAPABLEFORMERBASE-50 TAPAS TA TA TA FA A B E SBSSSSSSS 57.6 0 62.2 47.4 - 60.0 62.2 57.6 45.2458565656666666666666666665655555555555555555555565856 TAPARAMASAKA KATAKA TAPANESEARS TAPANEWSPORT TAPANET ARE TOUR PRESENTED TO THE
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASBASE TAPSBASE-SO TABASE-S TAPABLEFORMERBASE-50 TAPAS TA TA TA FA A B E SBSSSSSSS 57.6 0 62.2 47.4 - 60.0 62.2 57.6 45.2458565656666666666666666665655555555555555555555565856 TAPARAMASAKA KATAKA TAPANESEARS TAPANEWSPORT TAPANET ARE TOUR PRESENTED TO THE</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.12 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. TABASES 57.6 45.2 60.0 62.2 57.6 5.6 5.2. TABLAFORMERBASE TABA FORMERBASE 57.6 45.2 60.0 62.2 57.6 5.6 57.6 5.6 55.6 57.6 TABLEFORMERBASE.SO 7.6 5.6 57.6 55.6 56.0 .0 .com TA TABLAKE. .com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com
```

**JSON 输出:**

```json
{
  "text_sequence": "TABASES 57.6 45.2 60.0 62.2 57.6 5.6 5.2. TABLAFORMERBASE TABA FORMERBASE 57.6 45.2 60.0 62.2 57.6 5.6 57.6 5.6 55.6 57.6 TABLEFORMERBASE.SO 7.6 5.6 57.6 55.6 56.0 .0 .com TA TABLAKE. .com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com.com</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 1.63 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. TAPASBASE-SO TABLEFORMERBASE TABLEFORMERBSE 57.6 45.2 60.0 62.2 47.4 - 60.2 61.5 46.4 1 - 59.8 61.7 29. - 60.7 61.9 49 49 49494949
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASBASE-SO TABLEFORMERBASE TABLEFORMERBSE 57.6 45.2 60.0 62.2 47.4 - 60.2 61.5 46.4 1 - 59.8 61.7 29.<unk> - 60.7 61.9 49 49 49494949</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 2.98 秒

```text
<s_cord-v2> TAPASE TAPASBASE-SAT TA TA TA SBASE-SO TABLEFORMERBASE-SO TA TA TA TA B BASE-SO 57.6 TAPASE---- T T T TAPASE 47.4 - 60.0 62.2 57.6 45.2 - 60.2 61.5 46.4 - 59.8 61.5
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASE TAPASBASE-SAT TA TA TA SBASE-SO TABLEFORMERBASE-SO TA TA TA TA B BASE-SO 57.6 TAPASE---- T T T TAPASE 47.4 - 60.0 62.2 57.6 45.2 - 60.2 61.5 46.4 - 59.8 61.5</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 4.04 秒

```text
Provide a concise one-sentence summary of the page content. TAPASBASE-S TA TA SP SP TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA B BLEFORMERBASE-S BLE FORMER BASE-SO 5 7.6 65 65 36 33 33 2 6 3 2
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASBASE-S TA TA SP SP TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA TA B BLEFORMERBASE-S BLE FORMER BASE-SO 5 7.6 65 65 36 33 33 2 6 3 2</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.42 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. ||||||||||||||||||||||||||||||||||||||||||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. ||||||||||||||||||||||||||||||||||||||||||||||</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 6.44 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. TA TAPASBASE-SO TABLEFORMERBASE 55.6565656225235355655555454545 S BASE-CO TABLEFORMERB C TABLAZE-SC A TABLACK-S 56.6 3 0 62.2 4 9 7 2 - 60.0 62.2 61.5 57.6 47.4 | 4948985848394946545678789 89 61.7 62.50338288588805242863635-FOFSPABE-so BEEN SO 8226259 323282SEARBABE-BOSEE-ROOffee-SON
```

**JSON 输出:**

```json
{
  "text_sequence": "TA TAPASBASE-SO TABLEFORMERBASE 55.6565656225235355655555454545 S BASE-CO TABLEFORMERB C TABLAZE-SC A TABLACK-S 56.6 3 0 62.2 4 9 7 2 - 60.0 62.2 61.5 57.6 47.4 | 4948985848394946545678789 89 61.7 62.50338288588805242863635-FOFSPABE-so BEEN SO 8226259 323282SEARBABE-BOSEE-ROOffee-SON</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 2.29 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. TAPA SBASE-SAT TABLEFORMERBASE-SO TABLE FORMERBASE TAPASBASE-SAT TABLEFORMERBASE. TABLEFCRMERBASE TA PASBASE-SAT BLEFORMERBASE-SO TAPASBASE-SAI TAPASBASE-SAI TABLEFFORMERDASE-SIO TAPASBBASE-SAST TAPASBSE-SATE SPARE FOR SPARE-S-S.S.S TAPA SPASE.S.BASE.S. S.S-S T T TAPA T T T T S-S-s-S-SE-S-So T T T .S T TAPA SP SP SP SPART T T T SP SP SPARE-SO T T T.S T SP SP T T T FIRFORMERBSE-S TO T T TAP SP SP SPORMERBEST-S TAPA SPARE-SPORMERBFORMERB T TAPASE-S SP SPARE T TAPA SPACEFORM SP SP SPENDED FOR SP SP SPANDED FOR SPENDEDED FOR SPARE TAPAS SPENDED SPENDED TO THE SPENDED ( ) ( ) () ( )
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPA SBASE-SAT TABLEFORMERBASE-SO TABLE FORMERBASE TAPASBASE-SAT TABLEFORMERBASE. TABLEFCRMERBASE TA PASBASE-SAT BLEFORMERBASE-SO TAPASBASE-SAI TAPASBASE-SAI TABLEFFORMERDASE-SIO TAPASBBASE-SAST TAPASBSE-SATE SPARE FOR SPARE-S-S.S.S TAPA SPASE.S.BASE.S. S.S-S T T TAPA T T T T S-S-s-S-SE-S-So T T T .S T TAPA SP SP SP SPART T T T SP SP SPARE-SO T T T.S T SP SP T T T FIRFORMERBSE-S TO T T TAP SP SP SPORMERBEST-S TAPA SPARE-SPORMERBFORMERB T TAPASE-S SP SPARE T TAPA SPACEFORM SP SP SPENDED FOR SP SP SPANDED FOR SPENDEDED FOR SPARE TAPAS SPENDED SPENDED TO THE SPENDED ( ) ( ) () ( )</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 3.53 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.WWWWWWWWW.WWW.WB.WBload.V.WB/B.WPWB.V.V.B.VGeGeGeGeBeBeBeBeSoSoSoSoBeBeBeGeGeGeWBeBeBeE.BeBeBeReBeBeBeMeMeMeMeGeGeGeB.BeBeGeBeBeGeWBeGeGeBeGeGeOBeBeBeHeGeGeGeMeMeBeBeBeBaBeBeBeBBeBeBeInGeGeGeSoSoSoGeGeGeHeBeBeBeMaMaMaMaBeBeBeSeBeBeBeMoMoMoMoBeBeBePaBeBeBeDeBeBeBeSGeGeGeOE-SoSoSoMeGeGeMeBeBeGeMeMeMeBeGeGeMeGeBeBeBHeHeBeBeMeBeBeBXBeBeBePoPoPoPoBeBeBeBiBeBeBePerBeBeBeGaGeGeGeReGeGeGeMoMoMoMeBeBeHeHeHeHeMeBeBeMeGeGeBeHeBeBeHeMeMeMeHeHeHeGeBeBeHeBeGeGeWHeHeHeBeHeHeMeGeGeWHGeGeGeDoBeBeBeWHeBeBeGeOHeHeGeGeWGeGeGeNeBeBeBeAnGeGeGeDGeGeGeRGeGeGeRoBeBeBeGHeHeHeWHeHeMeMeGeWHeGeGeOHeBeBeB-PoPoPoMeGeGeO
```

**JSON 输出:**

```json
{
  "text_sequence": "WWWWWWWWW.WWW.WB.WBload.V.WB/B.WPWB.V.V.B.VGeGeGeGeBeBeBeBeSoSoSoSoBeBeBeGeGeGeWBeBeBeE.BeBeBeReBeBeBeMeMeMeMeGeGeGeB.BeBeGeBeBeGeWBeGeGeBeGeGeOBeBeBeHeGeGeGeMeMeBeBeBeBaBeBeBeBBeBeBeInGeGeGeSoSoSoGeGeGeHeBeBeBeMaMaMaMaBeBeBeSeBeBeBeMoMoMoMoBeBeBePaBeBeBeDeBeBeBeSGeGeGeOE-SoSoSoMeGeGeMeBeBeGeMeMeMeBeGeGeMeGeBeBeBHeHeBeBeMeBeBeBXBeBeBePoPoPoPoBeBeBeBiBeBeBePerBeBeBeGaGeGeGeReGeGeGeMoMoMoMeBeBeHeHeHeHeMeBeBeMeGeGeBeHeBeBeHeMeMeMeHeHeHeGeBeBeHeBeGeGeWHeHeHeBeHeHeMeGeGeWHGeGeGeDoBeBeBeWHeBeBeGeOHeHeGeGeWGeGeGeNeBeBeBeAnGeGeGeDGeGeGeRGeGeGeRoBeBeBeGHeHeHeWHeHeMeMeGeWHeGeGeOHeBeBeB-PoPoPoMeGeGeO</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 3.08 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. TAPA SBASE-SAT TABLEFORMERBASE-SO TABLEFORMERBASE. TABLEFCRMERBASE SO TABLE FORMERBASE TABLEFGRMERBASE - - - - 0 0 0 0 62.2 62.2 TABLEFFORMERBSE-SO TAPASBASE-SAT TABLEF ORMERBASE-50 TABLEFLORMERBASE-30 TABLEFARE-SO TABEFORMERBBE-SO TABLEPORMERBSESE-SO TO TO THE BEAT TO THE BE-SO TO THERE-SO ON THESE-SO BE-SO AND-SO TO BE-SO DO DO NOT-SO TO SO TO THESE-SCHOUSE-SO AND TO TO TO TO SOUND-SOUND-SO TO-SO AND COUNTE-SO AND SOUND TO SOFTSOUND-soUND-SO SOUND-S-SOUNDASE-SO SO 0.SO SOUNDASE-SO AND AND-SO SOFTSO SOUND TO-SOUNDAND-SOUNDASE-SCHOSE-SOUND TO SOUND AND-SOUNDANGE-SOUND SOUND-SC-SOUND AND SOUND-SE-SE-soUND TO BE-soUND AND-soUNDED-SOUNDARBE-SOUND CONTROLSE-SO THANSE-SO ABE-SE-se-SE-s-SE-SSE-SO 0 0 8SE-SO 00% 62.2 63.2 62.2 61.2 62.2 0 0 0 2 62.2 66.2 62.2 0 62.2 0 8 62.2 62.5 62.2 61.5 62.2 6 0 0 0 6.0 62.2 0 6.0 0 0 61.2 0 0 61.5 6 0 0 6 0 0 6.7 0 0 0
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPA SBASE-SAT TABLEFORMERBASE-SO TABLEFORMERBASE. TABLEFCRMERBASE SO TABLE FORMERBASE TABLEFGRMERBASE - - - - 0 0 0 0 62.2 62.2 TABLEFFORMERBSE-SO TAPASBASE-SAT TABLEF ORMERBASE-50 TABLEFLORMERBASE-30 TABLEFARE-SO TABEFORMERBBE-SO TABLEPORMERBSESE-SO TO TO THE BEAT TO THE BE-SO TO THERE-SO ON THESE-SO BE-SO AND-SO TO BE-SO DO DO NOT-SO TO SO TO THESE-SCHOUSE-SO AND TO TO TO TO SOUND-SOUND-SO TO-SO AND COUNTE-SO AND SOUND TO SOFTSOUND-soUND-SO SOUND-S-SOUNDASE-SO SO 0.SO SOUNDASE-SO AND AND-SO SOFTSO SOUND TO-SOUNDAND-SOUNDASE-SCHOSE-SOUND TO SOUND AND-SOUNDANGE-SOUND SOUND-SC-SOUND AND SOUND-SE-SE-soUND TO BE-soUND AND-soUNDED-SOUNDARBE-SOUND CONTROLSE-SO THANSE-SO ABE-SE-se-SE-s-SE-SSE-SO 0 0 8SE-SO 00% 62.2 63.2 62.2 61.2 62.2 0 0 0 2 62.2 66.2 62.2 0 62.2 0 8 62.2 62.5 62.2 61.5 62.2 6 0 0 0 6.0 62.2 0 6.0 0 0 61.2 0 0 61.5 6 0 0 6 0 0 6.7 0 0 0</s>"
}
```

---

# 图像: 16.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 5.05 秒

```text
<s_cord-v2> <<<<<>>>>
```

**JSON 输出:**

```json
{
  "text_sequence": "<<<<<>>>></s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.30 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. Attn(H) = softmax(A) A
```

**JSON 输出:**

```json
{
  "text_sequence": "Attn(H) = softmax(A) A</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 4.95 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 0.64 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.. Attn(H) = software Attn(H) = software.com Attn(H) = software. Attn(H) = software. Attn(H) = software. (A(H)
```

**JSON 输出:**

```json
{
  "text_sequence": ". Attn(H) = software Attn(H) = software.com Attn(H) = software. Attn(H) = software. Attn(H) = software. (A(H)</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 3.70 秒

```text
Transcribe math as LaTeX when clear; keep original text for body.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 2.34 秒

```text
<s_cord-v2>>>>><><><><>><><>>> >>>> <>>><->>>
```

**JSON 输出:**

```json
{
  "text_sequence": ">>>><><><><>><><>>> >>>> <>>><->>></s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 8.58 秒

```text
Provide a concise one-sentence summary of the page content.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.51 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}.
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}.</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 4.90 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text.If youhave a
```

**JSON 输出:**

```json
{
  "text_sequence": "If youhave a</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 1.49 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. H = softmax ( ) = softmax( )
```

**JSON 输出:**

```json
{
  "text_sequence": "H = softmax ( ) = softmax( )</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 1.43 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.SoSoSoSoGeGeGeGeBeBeBeBeE
```

**JSON 输出:**

```json
{
  "text_sequence": "SoSoSoSoGeGeGeGeBeBeBeBeE</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 2.19 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. Attachment ( ) = softwares. H H H H = = softmax( ) = softmax ( ) = softmax( )
```

**JSON 输出:**

```json
{
  "text_sequence": "Attachment ( ) = softwares. H H H H = = softmax( ) = softmax ( ) = softmax( )</s>"
}
```

---

# 图像: 17.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 7.94 秒

```text
<s_cord-v2> Herzig et al. (2020) Eisenschlos et al. (2020) Eisenschlos at al. (2021) et al. (1921) 67.2 71.0 71.7 0.4.8 46. - - 31.3 39.7 66.8 70.3 TAPASBASE inter TAPASBLEFORMERBASE TARGE TABARGE al.(2021) 27.2 0.2 0.) 67.2 40.4 71.4.4.6.6.4.5.6.5.5.9.6..6.3.6.9..9.9.3.9.
```

**JSON 输出:**

```json
{
  "text_sequence": "Herzig et al. (2020) Eisenschlos et al. (2020) Eisenschlos at al. (2021) et al. (1921) 67.2 71.0 71.7 0.4.8 46.<unk> - - 31.3 39.7 66.8 70.3 TAPASBASE inter TAPASBLEFORMERBASE TARGE TABARGE al.(2021) 27.2 0.2 0.) 67.2 40.4 71.4.4.6.6.4.5.6.5.5.9.6.<unk>.6.3.6.9.<unk>.9.9.3.9.</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.55 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. et al. (2020) .0 0. 66.7 70.3 67.5 6 1 1 7 1 0 1 2 1 4 1 3 1 5 1 % 70,6.8 70 70:4 70 60.4 4 61.1 1 61.6, 70 : 70 0 0,.9.
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (2020) .0 0.<unk> 66.7 70.3 67.5 6 1 1 7 1 0 1 2 1 4 1 3 1 5 1 % 70,6.8 70 70:4 70 60.4 4 61.1 1 61.6, 70 : 70 0 0,<unk>.9.</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 6.97 秒

```text
<s_cord-v2> Herzig et al. (2020) Eisenschlos et al .(2020) Eisenschloset al. (202) et al (2021) 67. 71.0 7. - 40 44 8 46. _ -1 31.3 39.7 TAPASE inter TAPLEFORMERBASE 66.8 70.3 36.9 0.4.6464646414949493939392929292826262636363636569593939999999999999996989393933333333333 Hergergergergers,Heresserssesssesssessed.SPSPSPSSSSSSSSESSESSESSISSISSISTSSPSPPPPPPSPSPSPRPRPRPHRPPPPPpppppppppppsperspersperperPerPerPerStrStrStr
```

**JSON 输出:**

```json
{
  "text_sequence": "Herzig et al. (2020) Eisenschlos et al .(2020) Eisenschloset al. (202) et al (2021) 67. 71.0 7. - 40 44 8 46.<unk> _ -1 31.3 39.7 TAPASE inter TAPLEFORMERBASE 66.8 70.3 36.9 0.4.6464646414949493939392929292826262636363636569593939999999999999996989393933333333333 Hergergergergers,Heresserssesssesssessed.SPSPSPSSSSSSSSESSESSESSISSISSISTSSPSPPPPPPSPSPSPRPRPRPHRPPPPPpppppppppppsperspersperperPerPerPerStrStrStr</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.15 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. et al. (2020) Hisenschos et al. (2020) Liu et al. (202). Eisensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensen.28.18.Perfe:5.Bessesssessses.Dependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependepende
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (2020) Hisenschos et al. (2020) Liu et al. (202). Eisensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensensen.28.18.Perfe:5.Bessesssessses.Dependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependependepende</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 3.44 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. Eisenschlos et al. (2020) Liu et (2021) Et al. (2020) Eisenschlos at. (2021) Lin et al . (202) TA TA TA BA BA BAE inter TABLEFORMERLARGE TA TA PA BA BABE inter TAPAS TA PA TA TA PAS . . 66. .2 .
```

**JSON 输出:**

```json
{
  "text_sequence": "Eisenschlos et al. (2020) Liu et (2021) Et al. (2020) Eisenschlos at. (2021) Lin et al . (202) TA TA TA BA BA BAE inter TABLEFORMERLARGE TA TA PA BA BABE inter TAPAS TA PA TA TA PAS . .<unk> 66.<unk> .2 .</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 8.09 秒

```text
<s_cord-v2> Herzig et al. (2020) Eisenschlos et al. (2020) Eisenschlos at al. (2021) et al. (1921) 67.2 71.0 71.77777777877877877877777777771777777707070707071011011011011111111111111111111114141414242424242626262623232323333333333333333333333332323232223232332333333333333333333 Herz Herz Herz HerzHerHerHerHers Herz Herz Herz.HerHerHere Herz Herz Herz,HerHerssssSssssperspersperspersss'sssStrStrStrStrsss.sss
```

**JSON 输出:**

```json
{
  "text_sequence": "Herzig et al. (2020) Eisenschlos et al. (2020) Eisenschlos at al. (2021) et al. (1921) 67.2 71.0 71.77777777877877877877777777771777777707070707071011011011011111111111111111111114141414242424242626262623232323333333333333333333333332323232223232332333333333333333333 Herz Herz Herz HerzHerHerHerHers Herz Herz Herz.HerHerHere Herz Herz Herz,HerHerssssSssssperspersperspersss'sssStrStrStrStrsss.sss</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 6.49 秒

```text
Provide a concise one-sentence summary of the page content. et al. (2020) Eisenschlos et al. (2020) Eisenschlos et al. (2020) Liu et al. (202) A A B E Eisenschlos et al. (20)))))))))))))))))))))
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (2020) Eisenschlos et al. (2020) Eisenschlos et al. (2020) Liu et al. (202) A A B E Eisenschlos et al. (20)))))))))))))))))))))</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.38 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) (
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) (</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 6.02 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. or it it is in al. (20) Elsenschlos et al. ( ) Liu et al (2021) 67.2 71.0 0 0 0 | - !?!?! ????! (?)?!!?! L 7 / 1 I S E TABASASBASK ORMERBE inter REPEARLE ut al. (1921) (2015) 2015 11 10 20) of at alset al. anter let after EXPt itter (046 (21) Inter TABERBASE infer infer for meter only enter not all of the older to perfor er PERFERRE inter inter inter 35 inter inter
```

**JSON 输出:**

```json
{
  "text_sequence": "or it it is in al. (20) Elsenschlos et al. ( ) Liu et al (2021) 67.2 71.0 0 0 0 | - !?!?! ????! (?)?!!?! L 7 / 1 I S E TABASASBASK ORMERBE inter REPEARLE ut al. (1921) (2015) 2015 11 10 20) of at alset al.<unk> anter let after EXPt itter (046 (21) Inter TABERBASE infer infer for meter only enter not all of the older to perfor er PERFERRE inter inter inter 35 inter inter</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 2.64 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. Herzie et al. 2020) Eisenschlos et al. (1920) et al. (2020) Herzig et et al. et (2021) et et et et at al. et al. 2021) et et at at al. (2021) Herzie et et et al et et at (2021) et at at et et et (2021) Herzig et at et et at et at at at (2021) (2020) et et et (2020) (2020) 2021) (2012. (2021) ( ) (2020) 67. (2012) (20121) (2020) 0. (2020 ) (20121) . (20121) 67. (2020. (20201) (20121) 0 71. (2021) . (20021) (2020 ) 0 71. (2012. ( ) (2012) 67. (2021) 67. (2021) (20201) - - - - 61. (201211 . ( ) 67. ( 2021) 67. (192021) 67. (1021) 67. 0 71. (1021) - - - 0 71. 0 0 71. (1. ( ) - - - 1 61. ( ) 61. (2020 . 0 0 61. ( 0 71. (21) 67. 0 61. 0. ( ) . () 67. (10. ( ) 40. ( ) 60. ( ) 66. ( ) 0 0 0 0 71 0 0 0 11.0 0 0 0. 0 0 0 . 0. 0 . . 0 , 0 0 , . , 0 . ( 0 . TA TA TA TA B . 0
```

**JSON 输出:**

```json
{
  "text_sequence": "Herzie et al. 2020) Eisenschlos et al. (1920) et al. (2020) Herzig et et al. et (2021) et et et et at al. et al. 2021) et et at at al. (2021) Herzie et et et al et et at (2021) et at at et et et (2021) Herzig et at et et at et at at at (2021) (2020) et et et (2020) (2020) 2021) (2012. (2021) ( ) (2020) 67. (2012) (20121) (2020) 0. (2020 ) (20121) . (20121) 67. (2020. (20201) (20121) 0 71. (2021) . (20021) (2020 ) 0 71. (2012. ( ) (2012) 67. (2021) 67. (2021) (20201) - - - - 61. (201211 . ( ) 67. ( 2021) 67. (192021) 67. (1021) 67. 0 71. (1021) - - - 0 71. 0 0 71. (1. ( ) - - - 1 61. ( ) 61. (2020 . 0 0 61. ( 0 71. (21) 67. 0 61. 0. ( ) . () 67. (10. ( ) 40. ( ) 60. ( ) 66. ( ) 0 0 0 0 71 0 0 0 11.0 0 0 0. 0 0 0 . 0. 0 . . 0 , 0 0 , . , 0 . ( 0 . TA TA TA TA B . 0</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 4.00 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.WWWWWWWWW.PoPoPoPoPerPerSoSoSoSoBeBeBeBePaPaPaPaPoPoPoSoSoSoPoPoPoDoDoBeBeBeSoSoSoGeGeGeGeSoSoSoToToToToBeBeBePoPoPoBeBeBeGeGeGeBeBeBeReBeBeBeB.SoSoSoSeSeSeSoSoSoReReReRePoPoPoDeBeBeBeMeMeMeMeBeBeBeE .PoPoP-PoPoPoMoMoMoMoSoSoSoffeffeffeffeGeGeGePoPoPoMeMeMePoPoPoReReReBeBeBoddoddoddoddPoPoPoP.PoPoDoPoPoPoGeGeGeHeHeHeHeBeBeBeInInInInBeBeBeMoMoMoPoPoPoS.PoPoBeSoSoGeBeBeB-PoPoMe,PoPoPoPorPorPorPorPoPoPoffeffee,PoPoDoBeBeGeSoSoffee,SoSoSome,PoPoffee-PoPoffe,PoPoMoGeGeGeStatStatStatStateGeGeGeMoMoMoToToToPoPoPoRTBeBeBeBiBiBiBiBeBeBe (PoPoPokeSoSoSo Anal Anal Anal Analmetrimetrimetrimetrimetrmetrmetr Anal Anal Analmetrmetrmetrmetr An An An An Anal Anal Analysis Anal Anal AnalySoSoSo Error Error Error Error/PoPoPoR 0.0 0.05 0.SoSome Anal Anal Anal
```

**JSON 输出:**

```json
{
  "text_sequence": "WWWWWWWWW.PoPoPoPoPerPerSoSoSoSoBeBeBeBePaPaPaPaPoPoPoSoSoSoPoPoPoDoDoBeBeBeSoSoSoGeGeGeGeSoSoSoToToToToBeBeBePoPoPoBeBeBeGeGeGeBeBeBeReBeBeBeB.SoSoSoSeSeSeSoSoSoReReReRePoPoPoDeBeBeBeMeMeMeMeBeBeBeE .PoPoP-PoPoPoMoMoMoMoSoSoSoffeffeffeffeGeGeGePoPoPoMeMeMePoPoPoReReReBeBeBoddoddoddoddPoPoPoP.PoPoDoPoPoPoGeGeGeHeHeHeHeBeBeBeInInInInBeBeBeMoMoMoPoPoPoS.PoPoBeSoSoGeBeBeB-PoPoMe,PoPoPoPorPorPorPorPoPoPoffeffee,PoPoDoBeBeGeSoSoffee,SoSoSome,PoPoffee-PoPoffe,PoPoMoGeGeGeStatStatStatStateGeGeGeMoMoMoToToToPoPoPoRTBeBeBeBiBiBiBiBeBeBe (PoPoPokeSoSoSo Anal Anal Anal Analmetrimetrimetrimetrimetrmetrmetr Anal Anal Analmetrmetrmetrmetr An An An An Anal Anal Analysis Anal Anal AnalySoSoSo Error Error Error Error/PoPoPoR 0.0 0.05 0.SoSome Anal Anal Anal</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 3.99 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. et al. 2020) Liu et al. (2021) Herzig et al. (2020) Eisenschlos et al. et (2020) al. (2021) et (2021) (2020) et et (2021) (2021) 202) (2021) Hisenschlos et et et et at (2021) et al.(2020) (2021) et et at at. (2021) et at at (2021) ent et et et al.2020) et at at at at et at at et et at et et etet at at at At At (2021) er et et et onmerBASE et et at At At At At at at at Et Et Et Et at at at ElforMERBASE int et at at At at at At et et et Et Et Et EfforMERBSE int et et atet et et at EforMERBE inter at at at EforMerBSE in ter at at atet et at at E for et et et At At At EforMERBASE at at at not et et et EfforMERBE int at at at all. Et Et Et At At At Effor et at at Et At At at At At Ist at at at List List List List et at at al.at at at at of at at at any at at at set at at atat at at allot at at at Allot at at At al. USERBASE Befor et al. USIBESE at at allon MBEASE Befor at at at ast at at at use at at at as set at at allos et al. Asklos et at at all as at at at you may may may may be at at at alonMERBASE et alonMERBASE et al as you may may not you you you you to you you you<sep/><sep/><sep/><sep/> Before Perturb efore
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. 2020) Liu et al. (2021) Herzig et al. (2020) Eisenschlos et al. et (2020) al. (2021) et (2021) (2020) et et (2021) (2021) 202) (2021) Hisenschlos et et et et at (2021) et al.(2020) (2021) et et at at. (2021) et at at (2021) ent et et et al.2020) et at at at at et at at et et at et et etet at at at At At (2021) er et et et onmerBASE et et at At At At At at at at Et Et Et Et at at at ElforMERBASE int et at at At at at At et et et Et Et Et EfforMERBSE int et et atet et et at EforMERBE inter at at at EforMerBSE in ter at at atet et at at E for et et et At At At EforMERBASE at at at not et et et EfforMERBE int at at at all. Et Et Et At At At Effor et at at Et At At at At At Ist at at at List List List List et at at al.at at at at of at at at any at at at set at at atat at at allot at at at Allot at at At al. USERBASE Befor et al. USIBESE at at allon MBEASE Befor at at at ast at at at use at at at as set at at allos et al. Asklos et at at all as at at at you may may may may be at at at alonMERBASE et alonMERBASE et al as you may may not you you you you to you you you<sep/><sep/><sep/><sep/> Before Perturb efore</s>"
}
```

---

# 图像: 18.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 5.16 秒

```text
<s_cord-v2> <<<<<><><><><>>>>><><><<<<>>> ><->>><->><-><->->>->-><-><><->:->-->-()-)->-
```

**JSON 输出:**

```json
{
  "text_sequence": "<<<<<><><><><>>>>><><><<<<>>> ><->>><->><-><->->>->-><-><><->:->-->-()-)->-</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.29 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. VP = + + f2t)
```

**JSON 输出:**

```json
{
  "text_sequence": "VP = + + f2t)</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 6.03 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 0.69 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. VP = VP = VP = VP = VP = VP = VP = VP = VP = +++2f ++f2t VP = VP = VP = VP + f2f ++ f2f2f2f +f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2c5c2f2f2f2c2c2f2
```

**JSON 输出:**

```json
{
  "text_sequence": "VP = VP = VP = VP = VP = VP = VP = VP = VP = +++2f ++f2t VP = VP = VP = VP + f2f ++ f2f2f2f +f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2c5c2f2f2f2c2c2f2</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 4.69 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. .
```

**JSON 输出:**

```json
{
  "text_sequence": ".</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 5.78 秒

```text
<s_cord-v2> |||| 0|||0|||||| | || 0 0 0 0
```

**JSON 输出:**

```json
{
  "text_sequence": "|||| 0|||0|||<unk>||| | || 0 0 0 0</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 3.52 秒

```text
Provide a concise one-sentence summary of the page content. Plan-Resection-related A
```

**JSON 输出:**

```json
{
  "text_sequence": "Plan-Resection-related A</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.41 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. VP = VP = VP = VP = VP = VP = VP = VP VP VP VP VP VP VP VP VP VP VP VP VP
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. VP = VP = VP = VP = VP = VP = VP = VP VP VP VP VP VP VP VP VP VP VP VP VP</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 4.81 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. please be you may behavehave not anywhere, it is correctable to yourselves use use fore cigarettemakes a n n ow the kind of you'representatives with what nobody like
```

**JSON 输出:**

```json
{
  "text_sequence": "please be you may behavehave not anywhere, it is correctable to yourselves use use fore cigarettemakes a n n ow the kind of you'representatives with what nobody like</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.42 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. V P = V P = = (t2t + t2f + f2t)
```

**JSON 输出:**

```json
{
  "text_sequence": "V P = V P = = (t2t + t2f + f2t)</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 1.31 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.SoSoSoSoBeBeBeGeGeGeGeBeBeBeBeE.BeBeBeB.BeBeGeBeBeBBeBeBeBaBaBaBaBeBeBeSoSoSoGeGeGeSoSoSoReBeBeBeMeMeBeBeBeReBeBeGeSoSoBeGeGeBeGeGeB.GeGeGeSBeBeBeDeBeBeBeSeSeBeBeBeGaGeGeGeMeMeMeMeGeGeGeOBeBeBeInBeBeBeMaMaMaMaBeBeBeHeBeBeBePoPoPoPoBeBeBePaBeBeBeMoMoMoMoBeBeBeFiGeGeGeReGeGeGeB
```

**JSON 输出:**

```json
{
  "text_sequence": "SoSoSoSoBeBeBeGeGeGeGeBeBeBeBeE.BeBeBeB.BeBeGeBeBeBBeBeBeBaBaBaBaBeBeBeSoSoSoGeGeGeSoSoSoReBeBeBeMeMeBeBeBeReBeBeGeSoSoBeGeGeBeGeGeB.GeGeGeSBeBeBeDeBeBeBeSeSeBeBeBeGaGeGeGeMeMeMeMeGeGeGeOBeBeBeInBeBeBeMaMaMaMaBeBeBeHeBeBeBePoPoPoPoBeBeBePaBeBeBeMoMoMoMoBeBeBeFiGeGeGeReGeGeGeB</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 0.28 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. V V = P = = V P = =
```

**JSON 输出:**

```json
{
  "text_sequence": "V V = P = = V P = =</s>"
}
```

---

# 图像: 2.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 8.76 秒

```text
<s_cord-v2> h' h's h'n h'n length . . h" h" h' h n length ... h' 5:00 h' | h'n queen 5:00 Transformer (SelfAttention) . h' l lorgest h' . h l | h t t t t h I length : . h I h'l | h I | |||| | h l l | s t t t r r r r f r r r e f f f f t t h" longest h" | h" n || h'||| h||| n) || n n n n h'n longest h'n n n n leng | , , | . , . || ,, , s s , s , S , s, , e e , p p p ppppppppp ppppppppPPPPPPPPppppppppeppeppeppe . ppeppeppesperspersperspers. .com . e e e eppeppeppessesssesssesssess e e epppppp ppeppessesssss e eppessesssesss eppeppesss. eppeppesses e e effessesssessses eppeppespersssppeppeppessississississesssesssesssessessesssesssessperspersperssesssesssesppeppeppeppetppetssssubsubsubsubsssssussussussussesssesssesssississippeppeppesppessessses essentsss/sss'sss: ppessesssesssessesssessppeppessesppessessses,sss assesssessses, e e emissmissmissmiss e e e.'s e effee e e e .'ss, ppeppe e e eppet e e e-b eppeppe ppeppes e e ppeppe , eppeppe epppple e e eppppppple sppeppeppe eppeppesser, epppp ppr> ppeppeappeppeppe p epppp ppppp pp pp pp pppppp p e-> e> e> </> e> b> e> 0> e> p e> p> e>> e> g> e> <> e> sppe> e> P> e> D> p> p> <> ><> p >> p>> p> ><><> e>
```

**JSON 输出:**

```json
{
  "text_sequence": "h' h's h'n h'n length . . h\" h\" h' h n length ... h' 5:00 h' | h'n queen 5:00 Transformer (SelfAttention) . h' l lorgest h' . h l | h t t t t h I length : . h I h'l | h I | |||| | h l l | s t t t r r r r f r r r e f f f f t t h\" longest h\" | h\" n || h'||| h||| n) || n n n n h'n longest h'n n n n leng | , , | . , . || ,, , s s , s , S , s, , e e , p p p ppppppppp ppppppppPPPPPPPPppppppppeppeppeppe . ppeppeppesperspersperspers. .com . e e e eppeppeppessesssesssesssess e e epppppp ppeppessesssss e eppessesssesss eppeppesss. eppeppesses e e effessesssessses eppeppespersssppeppeppessississississesssesssesssessessesssesssessperspersperssesssesssesppeppeppeppetppetssssubsubsubsubsssssussussussussesssesssesssississippeppeppesppessessses essentsss/sss'sss: ppessesssesssessesssessppeppessesppessessses,sss assesssessses, e e emissmissmissmiss e e e.'s e effee e e e .'ss, ppeppe e e eppet e e e-b eppeppe ppeppes e e ppeppe , eppeppe epppple e e eppppppple sppeppeppe eppeppesser, epppp ppr> ppeppeappeppeppe p epppp ppppp pp pp pp pppppp p e-> e> e> </> e> b> e> 0> e> p e> p> e>> e> g> e> <> e> sppe> e> P> e> D> p> p> <> ><> p >> p>> p> ><><> e></s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 1.14 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. h'm . b"" h"m "m" , p.p. P.P. on task direction biness based based base. Bases, tow, based (Sif Action. S: S. ns, ts, was used. We use. Assed. He's: (Ct, assess based. Wc usc. (Factions; rs. In" Sc, Scece. Uc: nc. I' nces use use is use, we use foreses, asceeeeee. Eases. The uses sease. C. Toucc. Use use () usa base base-based. Wac; We us
```

**JSON 输出:**

```json
{
  "text_sequence": "h'm . b\"\" h\"m \"m\" , p.p. P.P. on task direction biness based based base. Bases, tow, based (Sif Action. S: S. ns, ts, was used. We use. Assed. He's: (Ct, assess based. Wc usc. (Factions; rs. In\" Sc, Scece. Uc: nc. I' nces use use is use, we use foreses, asceeeeee. Eases. The uses sease. C. Toucc. Use use () usa base base-based. Wac; We us</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 6.21 秒

```text
<s_cord-v2> h" h'n ||| h" longest h" lh" h" " h" n length ... h" 5:00 h" k" q ucen ::() Transformer (SelfAttention) . h I i f r t t t h l a d e b" [S] / h" s c e e e f h" | 0 0 0 1 2 3 4,st h" 't' | h'm | | S p! ?? h h's |0 0 0 h h" = h" {}{"|| lengthi***. h"" h n |5:00 5:00 |\ | 6= ___________________________________________ | @ h' h'along: | g/s: . | w w w .jpg .pppppp ppppppPPPPPPPPPPPOPOPOPORPOSPOSPOSSESSESSESSEE .VPSPSPSPE .companpanpan .copppppppeppeppessessed. .jpppppsperspersperspanspanspance
```

**JSON 输出:**

```json
{
  "text_sequence": "h\" h'n ||| h\" longest h\" lh\" h\" \" h\" n length ... h\" 5:00 h\" k\" q ucen ::() Transformer (SelfAttention) . h I i f r t t t h l a d e b\" [S] / h\" s c e e e f h\" | 0 0 0 1 2 3 4,<unk>st h\" 't' | h'm | | S p! ?? h h's |0 0 0 h h\" = h\" {}{\"|| lengthi***. h\"\" h n |5:00 5:00 |\\ | 6= ___________________________________________ | @ h' h'along: | g/s: . | w w w .jpg .pppppp ppppppPPPPPPPPPPPOPOPOPORPOSPOSPOSSESSESSESSEE .VPSPSPSPE .companpanpan .copppppppeppeppessessed. .jpppppsperspersperspanspanspance</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.04 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. In loaaaa h m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ..mmm.m.m .m.Memememememem.M..m.mmmmm.m.m.InIn/M.m.mm.M.M.M.
```

**JSON 输出:**

```json
{
  "text_sequence": "In loaaaa h m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ..mmm.m.m .m.Memememememem.M..m.mmmmm.m.m.InIn/M.m.mm.M.M.M.</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 6.91 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. . hn longest hn | [ ] ||| | | h h l longest Transformer (SelfAttention) hn hn n n n h n hn title length ... 5: 00 | 2 2 2 4 4 4 7 7 7 , , Z Z Z z z z , T T T L L L h h'l of ... longest . | l l lh'l longest s s s c c c e e e r r r t t r r e ee e e d e e f r r h h h n e e b b b e e c r r p p , p p p e e a r r / / e e p p r r , e e t e e l l e e g e e , ' ' 't e e s e e S e r e d d d e r . e e u e e i r e r / e r a r e c e r d e c , d e s s e c on e e x e e w w e e Ear e e C e e
```

**JSON 输出:**

```json
{
  "text_sequence": ". hn longest hn | [ ] ||| |<unk> | h h l longest Transformer (SelfAttention) hn hn n n n h n hn title length ... 5: 00 | 2 2 2 4 4 4 7 7 7 , , Z Z Z z z z , T T T L L L h h'l of ... longest . | l l lh'l longest s s s c c c e e e r r r t t r r e ee e e d e e f r r h h h n e e b b b e e c r r p p , p p p e e a r r / / e e p p r r , e e t e e l l e e g e e , ' ' 't e e s e e S e r e d d d e r . e e u e e i r e r / e r a r e c e r d e c , d e s s e c on e e x e e w w e e Ear e e C e e</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 6.63 秒

```text
<s_cord-v2> h' h'n h'n lh'n length .... h' h n h'n . h' quen . 5:00 h'n k'n qucen 5:00 | h'n 5:00 h" <> Transformer (SelfAttention) . . h l lorgest h' | h l | h I longest h'l | | h t t t t h I length . ... h' l lh'l queen 5: 00 |||| h'| || h" | h" longest h" h'n t tttle h" h" length" . h" . || | , , . ,, ,,,, ., , s s s s d h h's s s s w w w w s s s . h h h h s s s e e h h h b b b b s s s b b b e e e e b b b a b b b d b b bs b b b h h h e e e a b b e b b eb b b bbbbbbbbb e e e d e e eppeppeppeppessesssesssessses e e effee e e e ss e e epppppppp e e eb e e e D e e e p p e e effer e e e S e e e g e e e o e e essent e e essesssesssess e eppessesssessss e e assessesssessses assesssesssessed e e e, e e e ippeppeppe e e e. e e emiss e e e- e e e , e e assessses e asses e e assassassassas e effeffee assessses assesses e e s e e e r e e e E e e e m e e e n e e e 0 e e ep e e e t e e e w e e ee e e s: e e e cpppppple e e e pppppppp p e e a e e e f e e e hppppppr e e ease p e e-b e e- p e e Spppppp pp pp pp pp e e-> e> e> b e> p e> p> e> 0> e> g> e> p >> e> P> e>> p> p> b> e> <> e> D> e> spppppp> e> Q> e>
```

**JSON 输出:**

```json
{
  "text_sequence": "h' h'n h'n lh'n length .... h' h n h'n . h' quen . 5:00 h'n k'n qucen 5:00 | h'n 5:00 h\" <> Transformer (SelfAttention) . . h l lorgest h' | h l | h I longest h'l | | h t t t t h I length . ... h' l lh'l queen 5: 00 |||| h'| || h\" | h\" longest h\" h'n t tttle h\" h\" length\" . h\" . || | , , . ,, ,,,, ., , s s s s d h h's s s s w w w w s s s . h h h h s s s e e h h h b b b b s s s b b b e e e e b b b a b b b d b b bs b b b h h h e e e a b b e b b eb b b bbbbbbbbb e e e d e e eppeppeppeppessesssesssessses e e effee e e e ss e e epppppppp e e eb e e e D e e e p p e e effer e e e S e e e g e e e o e e essent e e essesssesssess e eppessesssessss e e assessesssessses assesssesssessed e e e, e e e ippeppeppe e e e. e e emiss e e e- e e e , e e assessses e asses e e assassassassas e effeffee assessses assesses e e s e e e r e e e E e e e m e e e n e e e 0 e e ep e e e t e e e w e e ee e e s: e e e cpppppple e e e pppppppp p e e a e e e f e e e hppppppr e e ease p e e-b e e- p e e Spppppp pp pp pp pp e e-> e> e> b e> p e> p> e> 0> e> g> e> p >> e> P> e>> p> p> b> e> <> e> D> e> spppppp> e> Q> e></s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 5.44 秒

```text
Provide a concise one-sentence summary of the page content. h" . h" h" h" h" h" h" h""""""""""""""""""""""""""""""""""""""""""""""
```

**JSON 输出:**

```json
{
  "text_sequence": "h\" . h\" h\" h\" h\" h\" h\" h\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.41 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. Transformer (CLS_{s| Transformer (CLS_{s_transform: Transformer (. Transformer (. Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. Transformer (CLS_{s| Transformer (CLS_{s_transform: Transformer (. Transformer (. Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans Trans</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 6.89 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. h" f | H = if or on you do do do b r l f . 0 0 0 o o a a r ee t | I ch longest Transformer (Self Attention) h'n title h n qween 5: 00 0 0 4 6 8 8 2 7 3 3 3 2 1 6 6 6 9 g [ ] A S S S s s s w - - W iongst transforter (SeIf Attention ) <> h= of .... hn m th t length ... : 5:00 0 0 h " 5:00 querwhen kenness knessessfullynesses gesigners feelesser unfereeeeee weeeaseaseserveserves sege usessusesusesusesusauseusesuses . We usedeseeseeseasssussussue usesusesusesusessesssesssessedused summung essussesssesspersonsslesslessless sensessubjectbelesslessusesusesuesusesusesusedusedused beses deservesessessses states.Noteelesslessisunderstand havedestdestinessmaymaynesgesmissmissinglesslesses anythelessless andlesslessehavessesssesssessessses dissessasserses hashasbestbesbased pleaseskholderholdersmittersendspeskessessses deliveries wereholdsbegient so been nottoffeemisseit perissentident dates maynoneseuses based mustimpos
```

**JSON 输出:**

```json
{
  "text_sequence": "h\" f | H = if or on you do do do b r l f . 0 0 0 o o a a r ee t | I ch longest Transformer (Self Attention) h'n title h n qween 5: 00 0 0 4 6 8 8 2 7 3 3 3 2 1 6 6 6 9 g [ ] A S S S s s s w - - W iongst transforter (SeIf Attention ) <> h= of .... hn m th t length ... : 5:00 0 0 h \" 5:00 querwhen kenness knessessfullynesses gesigners feelesser unfereeeeee weeeaseaseserveserves sege usessusesusesusesusauseusesuses . We usedeseeseeseasssussussue usesusesusesusessesssesssessedused summung essussesssesspersonsslesslessless sensessubjectbelesslessusesusesuesusesusesusedusedused beses deservesessessses states.Noteelesslessisunderstand havedestdestinessmaymaynesgesmissmissinglesslesses anythelessless andlesslessehavessesssesssessessses dissessasserses hashasbestbesbased pleaseskholderholdersmittersendspeskessessses deliveries wereholdsbegient so been nottoffeemisseit perissentident dates maynoneseuses based mustimpos</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 3.13 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. h-{ h-{ }}-{ |-{-{-}-{-|-||-|-{--- h-{-!-{-[-{-]-{-(-{- h={-{{-{ h={{{={={{= {{{{{======== h"{{{=" h" {{{======={={===={{{ ={{{5{{{n{{{ ="{-{ =" h"{-{a h" {c{-{ -{-{ b= {{-{s: h" {-{a f= { {{- {{a f=" h= =" h= {{ =" {{{- { {{ {{{ {{ { { {{{ s: h= { {{{s. {{{ . { {{ . 5: { {{s { {{= . {{= { { { {t. {{s h= . S: {{{a of... h= ====== ==== ="=" h= b= . We use h===== . We =" b= h= h= }} h= | h= h* == h= h's }}}}}}}}{ }}}}{{}{{{} }}{{{ }3 }}{}{}{ }} }}}} {}{{ }}{ . }}}}}{{}}}}}} }}{}}}}{}}}}}}} {{{}}{{} {}{} . .{{{}}{{  .  }}}} , }}}}
```

**JSON 输出:**

```json
{
  "text_sequence": "h-{ h-{ }}-{ |-{-{-}-{-|-||-|-{--- h-{-!-{-[-{-]-{-(-{- h={-{{-{ h={{{={={{= {{{{{======== h\"{{{=\" h\" {{{======={={===={{{ ={{{5{{{n{{{ =\"{-{ =\" h\"{-{a h\" {c{-{ -{-{ b= {{-{s: h\" {-{a f= { {{- {{a f=\" h= =\" h= {{ =\" {{{- { {{ {{{ {{ { { {{{ s: h= {<unk> {{{s. {{{ . { {{ . 5: { {{s { {{= . {{= { { { {t. {{s h= . S: {{{a of... h= ====== ==== =\"=\" h= b= . We use h===== . We =\" b= h= h= }} h= | h= h* == h= h's }}}}}}}}{ }}}}{{}{{{} }}{{{ }3 }}{}{}{ }} }}}} {}{{ }}{ . }}}}}{{}}}}}} }}{}}}}{}}}}}}} {{{}}{{} {}{} . .{{{}}{{ <unk> . <unk> }}}} , }}}}</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 3.98 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON. .jpgjpgjpghttpshttpshttpshttps://www.jpgjpghttps://wwwwwwwwwwww..jpgjpg.jpgjpg .jpghttpshttps https://wwwwww.jpg . ..jpg.jpg.... . Mess Mess Mess Messes... Mess Mess...B. .W .B.B.BeBeBeBeGeGeGeGeSoSoSoSoPoPoPoPoBeBeBeE .SoSoSoBeBeBeSoSoSoGeGeGeBeBeBeMeMeMeMeBeBeBeReBeBeBeSeSeSeSeBeBeBessessesssesssessses.BeBeGeBeBeEBeBeBePREBeBeBeBBeBeBePoPoPoMeMeMeGeGeGeMeMeMeSoSoSoMeMeMeE.MeMeMePoPoPoE .MeMeBeMeMeBeE.MeBeBeMeBeBeE.BeBeMeGeBeBeB.MeMeGeMeBeBeB B.MeMeB.MeGeGeBeMeMeGeBeMeBeMeGeGeMeGeGeSoMeMeBeB.BeMeMeSGeGeGeB.MeBeMeBeE ,MeMeMe,MeMeBeGeGeBeB.E.MeGeBeE.E.E .E.B.E ,WBeBeBeMoMoMeMeMe.MeMe,E.E,MeBeBeGeMeMeBeSoSoMeBeBeSoBeBeMe,MeBeB .E GruppeInBeBeBePaPaPaPaMeMeMeMaMeMeMeMoMoMoMoMeBeBemeMeMeMeHeMeMeMe-MeMeMeMiMiMiMiMeMeMeSeSeSeSoSoSome,MeMe,BeBeBeBiBiBiBeBeBe,BeBeBleMeMeMeS(BeBeBeme,BeBeE,MeMeSomeMeMeGe Gruppe [SoSoSo Anal Anal Anal Analme Anal Anal Anal
```

**JSON 输出:**

```json
{
  "text_sequence": ".jpgjpgjpghttpshttpshttpshttps://www.jpgjpghttps://wwwwwwwwwwww..jpgjpg.jpgjpg .jpghttpshttps https://wwwwww.jpg . ..jpg.jpg.... . Mess Mess Mess Messes... Mess Mess...B. .W .B.B.BeBeBeBeGeGeGeGeSoSoSoSoPoPoPoPoBeBeBeE .SoSoSoBeBeBeSoSoSoGeGeGeBeBeBeMeMeMeMeBeBeBeReBeBeBeSeSeSeSeBeBeBessessesssesssessses.BeBeGeBeBeEBeBeBePREBeBeBeBBeBeBePoPoPoMeMeMeGeGeGeMeMeMeSoSoSoMeMeMeE.MeMeMePoPoPoE .MeMeBeMeMeBeE.MeBeBeMeBeBeE.BeBeMeGeBeBeB.MeMeGeMeBeBeB B.MeMeB.MeGeGeBeMeMeGeBeMeBeMeGeGeMeGeGeSoMeMeBeB.BeMeMeSGeGeGeB.MeBeMeBeE ,MeMeMe,MeMeBeGeGeBeB.E.MeGeBeE.E.E .E.B.E ,WBeBeBeMoMoMeMeMe.MeMe,E.E,MeBeBeGeMeMeBeSoSoMeBeBeSoBeBeMe,MeBeB .E GruppeInBeBeBePaPaPaPaMeMeMeMaMeMeMeMoMoMoMoMeBeBemeMeMeMeHeMeMeMe-MeMeMeMiMiMiMiMeMeMeSeSeSeSoSoSome,MeMe,BeBeBeBiBiBiBeBeBe,BeBeBleMeMeMeS(BeBeBeme,BeBeE,MeMeSomeMeMeGe Gruppe [SoSoSo Anal Anal Anal Analme Anal Anal Anal</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 3.08 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. h n n n s:00 h n h n qutca | 5: 00 h n n h" 5: 00 | 5:00 h n n | 5:0 0 0 0 0 h h h n h" |5: 00 0 0 0 2 0 0 0 b" h" h" longest h" h' |5||| ||| h"||||[[[[s]|||=============== ="="="====== =======<======[[[ ==== ====== [[[[ h" =" ===== ====($ =" =" lengthe lengthes. lengthe eeeeeeeee == . . leng . | . , lenglengthe , , . == , | , =" . =" , lingui , ====. .com . returretur, .. ., ,- . lingui, . SEE . 0000000000000000 . 666666666666 , 666666 . fter, . Ear, . pleases, .
```

**JSON 输出:**

```json
{
  "text_sequence": "h n n n s:00 h n h n qutca | 5: 00 h n n h\" 5: 00 | 5:00 h n n | 5:0 0 0 0 0 h h h n h\" |5: 00 0 0 0 2 0 0 0 b\" h\" h\" longest h\" h' |5||| ||| h\"||||[[[[s]|||=============== =\"=\"=\"====== =======<======[[[ ==== ====== [[[[ h\" =\" ===== ====($ =\" =\" lengthe lengthes. lengthe eeeeeeeee == . . leng . | . , lenglengthe , , . == , | , =\" . =\" , lingui , ====. .com . returretur, .. ., ,- . lingui, . SEE . 0000000000000000 . 666666666666 , 666666 . fter, . Ear, . pleases, .</s>"
}
```

---

# 图像: 3.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 4.74 秒

```text
<s_cord-v2> TABLE TABLEFORMERBASE 1 10 M - 2*512*10101101101101111111111111 TABLEORMERBASE 140 M - 0.8 M + 0.02 M 340 M M - - 2*512*13 = M M M M = 0.8 0 0 0 0 8 8 8 8 6 8 8 8 9 9 9 9 3 4 0 0 0 M M M - M M M T M M M * M M TABLEPORMERLARGE 340 M - - 24*16*13 = 340 340 M - M - - 0. 0 8 8 0 0 0. 0 0 0 005 M M M + 0 0 0 3 8 8 3 8 8 8 3 3 8 8 5 8 8 8 0 8 8 3 0 8 8 9 8 8 8
```

**JSON 输出:**

```json
{
  "text_sequence": "TABLE TABLEFORMERBASE 1 10 M - 2*512*10101101101101111111111111 TABLEORMERBASE 140 M - 0.8 M + 0.02 M 340 M M - - 2*512*13 = M M M M = 0.8 0 0 0 0 8 8 8 8 6 8 8 8 9 9 9 9 3 4 0 0 0 M M M - M M M T M M M * M M TABLEPORMERLARGE 340 M - - 24*16*13 = 340 340 M - M - - 0. 0 8 8 0 0 0. 0 0 0 005 M M M + 0 0 0 3 8 8 3 8 8 8 3 3 8 8 5 8 8 8 0 8 8 3 0 8 8 9 8 8 8</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 1.08 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. = 1 10 M - 0.8 M + 0.002 M T T A A B B E E R R BASE 340 M M . 1.0 - 2*512*13= = 0 8 M 4 0.005M M = = *515*1024 240 M I - 1.0 M 1 + 0.002 M r r m m - - 0.52*7( ) - M 340 34 34 M 110 M S - -1.0 -8 -3 - 3 - 5 - 1 0 -4 -5 -2 -6- 3 0 M 1110 - , - 30 - 40 M 10 - 20 - 104545 -
```

**JSON 输出:**

```json
{
  "text_sequence": "= 1 10 M - 0.8 M + 0.002 M T T A A B B E E R R BASE 340 M M . 1.0 - 2*512*13= = 0 8 M 4 0.005M M = = *515*1024 240 M I - 1.0 M 1 + 0.002 M r r m m - - 0.52*7( ) - M 340 34 34 M 110 M S - -1.0 -8 -3 - 3 - 5 - 1 0 -4 -5 -2 -6- 3 0 M 1110 - , - 30 - 40 M 10 - 20 - 104545 -</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 3.81 秒

```text
<s_cord-v2> TABLEFORMERBASE 1 10 M - 2*512*768 TA B A S E I I O O O o o o r a m m m = 0.8 M + M 340 M - 0. 8 M + 0.002 M |10 M - 24*16*13 = 240 M - 2. *1525656565666666666666666666
```

**JSON 输出:**

```json
{
  "text_sequence": "TABLEFORMERBASE 1 10 M - 2*512*768 TA B A S E I I O O O o o o r a m m m = 0.8 M + M 340 M - 0. 8 M + 0.002 M |10 M - 24*16*13 = 240 M - 2. *1525656565666666666666666666</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.01 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T B B B E E OR R R R ARGE ALEFORMER LARGE M M M M - 2*5 2*512*768 M M M M M = 0.3 M 10 M - 0.8 2*5.0 M M M = 1010: .0.2.3 = 10.9.9: 0.0.4.0.0.B3.2.8:9B.20.2:B.BASE 0.BASE.B.B.B.O.B.B3.B.B3.B.B.B.B
```

**JSON 输出:**

```json
{
  "text_sequence": "T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T T B B B E E OR R R R ARGE ALEFORMER LARGE M M M M - 2*5 2*512*768 M M M M M = 0.3 M 10 M - 0.8 2*5.0 M M M = 1010: .0.2.3 = 10.9.9: 0.0.4.0.0.B3.2.8:9B.20.2:B.BASE 0.BASE.B.B.B.O.B.B3.B.B3.B.B.B.B</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 3.66 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. TABLEFORMERBASE 340 M - 0.8 M - 10 10 M - 2*512*13 = 240 M - - 0 8 M + 0.002 M TABLEFORMERLARGE 340 34 M - 1.0 M + 0.005M
```

**JSON 输出:**

```json
{
  "text_sequence": "TABLEFORMERBASE 340 M - 0.8 M - 10 10 M - 2*512*13 = 240 M - - 0 8 M + 0.002 M TABLEFORMERLARGE 340 34 M - 1.0 M + 0.005M</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 4.43 秒

```text
<s_cord-v2> TABLE TABLEFORMERBASE 1 10 M - 2*512*101010110110110111111111111111111111111 TABLEORMERBASE 140 M - 0.8 M M M M TABLEPORMERLARGE 340 M M - - 2*512*13 = + 0.02 M 340 M - - 0. 8 M + 0.002 M M TAPLEFORMERLARGE 240 M - - 2. *512*13 = M TAPALE M M M + 0.042 M M T TAPALEFORMERLERGE
```

**JSON 输出:**

```json
{
  "text_sequence": "TABLE TABLEFORMERBASE 1 10 M - 2*512*101010110110110111111111111111111111111 TABLEORMERBASE 140 M - 0.8 M M M M TABLEPORMERLARGE 340 M M - - 2*512*13 = + 0.02 M 340 M - - 0. 8 M + 0.002 M M TAPLEFORMERLARGE 240 M - - 2. *512*13 = M TAPALE M M M + 0.042 M M T TAPALEFORMERLERGE</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 3.57 秒

```text
Provide a concise one-sentence summary of the page content. TA BLEFORMERBSE I 10 M - 2*512*768 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 M M M M TABLEFORMERLARGE 240 M M - 2*512*10 0 0 0 0 0 0 0 0 0
```

**JSON 输出:**

```json
{
  "text_sequence": "TA BLEFORMERBSE I 10 M - 2*512*768 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 M M M M TABLEFORMERLARGE 240 M M - 2*512*10 0 0 0 0 0 0 0 0 0</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.31 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}.," ||||||||||||||||||||||||||||||||||||||||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}.,\" ||||||||||||||||||||||||||||||||||||||||||||</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 1.19 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. TABLEFORMERBASE 1 0 M - 2* = 140 100 100 100100 100 100000000000000000 TAILE FORMERBSE 240 M M - - 0.8 M + 0.02 M 340 M - 1.0 M + 0.00M
```

**JSON 输出:**

```json
{
  "text_sequence": "TABLEFORMERBASE 1 0 M - 2*<unk> = 140 100 100 100100 100 100000000000000000 TAILE FORMERBSE 240 M M - - 0.8 M + 0.02 M 340 M - 1.0 M + 0.00M</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 1.30 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. 1 10 M - 2*512*768 T T T TABLEFORMERBASE 1 10 10 M - - 0.8 M - - M - M - - *512*13 0.8 0.8 2*510 M - - 2*512*768 12*12*13 = 1 10 10 10 10 12*13 M - - - M * - - M M - - 1 10 10 12 10 10 10 M M - M M M - 10 M - 10 10 10 11 10 10 10 0 10 10 M + M - M 1 10 M *5 10 M - M 10 10 M 1 10 10 0 M - 10 0 10 M - 0 10 10 10 14 10 10 M 340 M - 10 12*5 10 10 10 13 10 10 M 10 10 10 3 10 10 10 100 10 10 10 16 10 10 10
```

**JSON 输出:**

```json
{
  "text_sequence": "1 10 M - 2*512*768 T T T TABLEFORMERBASE 1 10 10 M - - 0.8 M - - M - M - - *512*13 0.8 0.8 2*510 M - - 2*512*768 12*12*13 = 1 10 10 10 10 12*13 M - - - M * - - M M - - 1 10 10 12 10 10 10 M M - M M M - 10 M - 10 10 10 11 10 10 10 0 10 10 M + M - M 1 10 M *5 10 M - M 10 10 M 1 10 10 0 M - 10 0 10 M - 0 10 10 10 14 10 10 M 340 M - 10 12*5 10 10 10 13 10 10 M 10 10 10 3 10 10 10 100 10 10 10 16 10 10 10</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 0.17 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.W
```

**JSON 输出:**

```json
{
  "text_sequence": "W</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 1.63 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. TABLEFORMERBASE 1 10 M - 2*512*768 + 12*12*13 = 110 M - 0.8 M - + 0.02 M TA TA TA TA SLARGE 1 10 10 M - - *512*76 1 1 1 1 0 M - - 2*5124 + 12*13 12*768 = 0.8 0 0 0 0 M M - M - - M - 0 8 M - - - M 0.8 - M M - - 0. 2*1512*13 0. M - 0 0 0. M M - 2 *5 M - *5 M M - 3 0 0. 0 0. 2 *15 M - M + M - *13 M - 0 M *13 M *13 *13 *1024 *13 *15 *13 *16 *13 * 13 *13 *194 *13 *168 *13 *12*13 *13 = *13 *14 *13 M M - 1024 * 13 M - 20 1024 *13SE
```

**JSON 输出:**

```json
{
  "text_sequence": "TABLEFORMERBASE 1 10 M - 2*512*768 + 12*12*13 = 110 M - 0.8 M - + 0.02 M TA TA TA TA SLARGE 1 10 10 M - - *512*76 1 1 1 1 0 M - - 2*5124 + 12*13 12*768 = 0.8 0 0 0 0 M M - M - - M - 0 8 M - - - M 0.8 - M M - - 0. 2*1512*13 0. M - 0 0 0. M M - 2 *5 M - *5 M M - 3 0 0. 0 0. 2 *15 M - M + M - *13 M - 0 M *13 M *13 *13 *1024 *13 *15 *13 *16 *13 * 13 *13 *194 *13 *168 *13 *12*13 *13 = *13 *14 *13 M M - 1024 * 13 M - 20 1024 *13SE</s>"
}
```

---

# 图像: 4.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 5.32 秒

```text
<s_cord-v2> - ) -
```

**JSON 输出:**

```json
{
  "text_sequence": "- ) -</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.18 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. A;; =
```

**JSON 输出:**

```json
{
  "text_sequence": "A;; =</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 6.13 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.07 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. A.; = = (h;TWq)6;6;6;6;6;6;6;6;6;6;6;6;6;6;7;6;6;6;6;6;6;6;6;6;6;6;6,5:5:3:3:6.3:5:5.5:5:5:5:5:2:5:5:5:3:5:5:5:5:5:5:5:5:5:5:5:5:4:5:5:5:5:3:5.9:5:5:5.5:5.5:5.0.5:5:5:5:5.9:5:4.9.3:5
```

**JSON 输出:**

```json
{
  "text_sequence": "A.; = = (h;TWq)6;6;6;6;6;6;6;6;6;6;6;6;6;6;7;6;6;6;6;6;6;6;6;6;6;6;6,5:5:3:3:6.3:5:5.5:5:5:5:5:2:5:5:5:3:5:5:5:5:5:5:5:5:5:5:5:5:4:5:5:5:5:3:5.9:5:5:5.5:5.5:5.0.5:5:5:5:5.9:5:4.9.3:5</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 5.45 秒

```text
Transcribe math as LaTeX when clear; keep original text for body.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 6.33 秒

```text
<s_cord-v2> - ) - ) ||| | || 0|||0|||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "- ) - ) ||| | || 0|||0|||<unk>||||</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 4.76 秒

```text
Provide a concise one-sentence summary of the page content. A ;
```

**JSON 输出:**

```json
{
  "text_sequence": "A ;</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.28 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. A;;;;;s_t A;s_t A;
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. A;;;;;s_t A;s_t A;</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 6.02 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. with you like it is if
```

**JSON 输出:**

```json
{
  "text_sequence": "with you like it is if</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.29 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. A;; = A;;
```

**JSON 输出:**

```json
{
  "text_sequence": "A;; = A;;</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 2.87 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.WK.BeBeBeBeGeGeGeGeBeBeBeB.BeBeE.BeBeSoSoSoSoBeBeBeBaBaBaBaBeBeBeReBeBeBeDeBeBeBeMeMeMeMeBeBeBeDBeBeBeEBeBeBeHeBeBeBeSeSeSeSeBeBeBeSBeBeBeBiBeBeBeMoBeBeBeInBeBeBeMaBeBeBeSoBeBeGeBeBeBBeBeBeFiGeGeGeSoSoSoGeGeGeMeBeBeB-BeBeBeKeBeBeBeRoBeBeBePaBeBeBePerBeBeBeNoBeBeBeNeBeBeBePoPoBeBeBeDoBeBeBeHaBeBeBeBoBeBeBeWBeBeBeMBeBeBeFeBeBeBeBerBeBeBeRXBeBeMeBeBeMeGeGeBeGeGeBeB-PoPoPoPoMeMeMeGeGeGeB-PoBeBeMoMoMoMoGeGeGeMoMoMoBeBeGeMeMeMeSoSoSoSeSeSeGeGeGeHeHeHeBeBeB
```

**JSON 输出:**

```json
{
  "text_sequence": "WK.BeBeBeBeGeGeGeGeBeBeBeB.BeBeE.BeBeSoSoSoSoBeBeBeBaBaBaBaBeBeBeReBeBeBeDeBeBeBeMeMeMeMeBeBeBeDBeBeBeEBeBeBeHeBeBeBeSeSeSeSeBeBeBeSBeBeBeBiBeBeBeMoBeBeBeInBeBeBeMaBeBeBeSoBeBeGeBeBeBBeBeBeFiGeGeGeSoSoSoGeGeGeMeBeBeB-BeBeBeKeBeBeBeRoBeBeBePaBeBeBePerBeBeBeNoBeBeBeNeBeBeBePoPoBeBeBeDoBeBeBeHaBeBeBeBoBeBeBeWBeBeBeMBeBeBeFeBeBeBeBerBeBeBeRXBeBeMeBeBeMeGeGeBeGeGeBeB-PoPoPoPoMeMeMeGeGeGeB-PoBeBeMoMoMoMoGeGeGeMoMoMoBeBeGeMeMeMeSoSoSoSeSeSeGeGeGeHeHeHeBeBeB</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 1.21 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. A A A A i i i ii
```

**JSON 输出:**

```json
{
  "text_sequence": "A A A A i i i ii</s>"
}
```

---

# 图像: 5.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 3.50 秒

```text
<s_cord-v2> 0 0 0 0 00 0 0 0 1 0 0 0 8 0 0 0 6 0 0 0 3 0 0 0.6 0 0 0 .5 T T T T A A A A B B E E E E R R R R E E E D D D D
```

**JSON 输出:**

```json
{
  "text_sequence": "0 0 0 0 00 0 0 0 1 0 0 0 8 0 0 0 6 0 0 0 3 0 0 0.6 0 0 0 .5 T T T T A A A A B B E E E E R R R R E E E D D D D</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 1.14 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. at al. (2020) .0 T.P.A.S.E. Eisentschloss at 21. (0221) || 0 81.4.7.9.6.5,2,3,8,6, 810, 92.2.3.8. 73.5,5. 811. 90.5 8 818.. 11.1 8 10 91.21.2. 22.1 91.2. 7.8 81 0. 71.2.3 81 10: 92.1.31. 90. 315. 912.3.1 819. 31.0 81 10.516. 80.81. 81 - 81 :1. 31 92.0 8 1 92.5 8 -1. 11: 8 81_810 81.1.
```

**JSON 输出:**

```json
{
  "text_sequence": "at al. (2020) .0 T.P.A.S.E. Eisentschloss at 21. (0221) || 0 81.4.7.9.6.5,2,3,8,6, 810, 92.2.3.8. 73.5,5. 811. 90.5 8 818.<unk>. 11.1 8 10 91.21.2. 22.1 91.2. 7.8 81 0. 71.2.3 81 10: 92.1.31. 90. 315. 912.3.1 819. 31.0 81 10.516. 80.81. 81 - 81 :1. 31 92.0 8 1 92.5 8 -1. 11: 8 81_810 81.1.</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 1.31 秒

```text
<s_cord-v2> 0. e t al. () - ) ||| et al. (2021) T A BASE inter r m m m n a d o 8 1 6 9 7 5 4 3 2
```

**JSON 输出:**

```json
{
  "text_sequence": "0.<unk> e t al. () - ) ||| et al. (2021) T A BASE inter r m m m n a d o 8 1 6 9 7 5 4 3 2</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.06 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. Inter TAR TAR ARE ORMER BASE Inter TAR MARKET.ABLE. ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "Inter TAR TAR ARE ORMER BASE Inter TAR MARKET.ABLE. ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 5.29 秒

```text
Transcribe math as LaTeX when clear; keep original text for body.com et al. (2021) .0 0 0 0 8 8 8 6 6 6 7 7 7 9 9 9 3 3
```

**JSON 输出:**

```json
{
  "text_sequence": "com et al. (2021) .0 0 0 0 8 8 8 6 6 6 7 7 7 9 9 9 3 3</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 5.13 秒

```text
<s_cord-v2> 0 0 0 0 8 0 0 0 00 0 0 0 1 0 0 0 6 0 0 0 3 0 0 0.6 0 0 0 .5 T T T T A A A A B B B B E E E E R R R R E E E D D D D
```

**JSON 输出:**

```json
{
  "text_sequence": "0 0 0 0 8 0 0 0 00 0 0 0 1 0 0 0 6 0 0 0 3 0 0 0.6 0 0 0 .5 T T T T A A A A B B B B E E E E R R R R E E E D D D D</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 5.13 秒

```text
Provide a concise one-sentence summary of the page content. et al. (20) tst. (-) et al. (20 20 21 21 11 18 10 19 13 21 17 17 20 20 18 20 20 30 30 30
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (20) tst. (-) et al. (20 20 21 21 11 18 10 19 13 21 17 17 20 20 18 20 20 30 30 30</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.41 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. ||||||||||||||||||||||||||||||||||||||||||||||
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. ||||||||||||||||||||||||||||||||||||||||||||||</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 5.09 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. I BASE inter TAKE it' at al. (2021) | () et al. (010) 02 8 5 3 2 7 0 0 0
```

**JSON 输出:**

```json
{
  "text_sequence": "I BASE inter TAKE it' at al. (2021) | () et al. (010) 02 8 5 3 2 7 0 0 0</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.92 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. Perturb dev 81.0 0 0 0 0 8 0 0 0.6 82.0 81.6 80.6 81.6 82.1 81.6 93.3 After Perturb
```

**JSON 输出:**

```json
{
  "text_sequence": "Perturb dev 81.0 0 0 0 0 8 0 0 0.6 82.0 81.6 80.6 81.6 82.1 81.6 93.3 After Perturb</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 3.78 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON. Test Test Test Test Data Data Data Data . Data Data Data Date Data Data Data To To To To Data Data Data In In In In Stati Stati Stati Statimetrimetrimetriometriometriometriometrimetrimetrimetrimetric Stati Stati Statimetrmetrmetrmetr
```

**JSON 输出:**

```json
{
  "text_sequence": "Test Test Test Test Data Data Data Data . Data Data Data Date Data Data Data To To To To Data Data Data In In In In Stati Stati Stati Statimetrimetrimetriometriometriometriometrimetrimetrimetrimetric Stati Stati Statimetrmetrmetrmetr</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 2.23 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. ( ( ( ) 0 0 0 0 8 8 8 2 3 3 3 3 2 2 2 2 3 3 4 4 4 7 7 7 7 9 9 9 9 6 8 8 8 0 0 0.6 0 0. 1 1 1 1 3 3 3 5 3 3 3 6 8 8 6 8 8 0.6 TABLEFORMERLRGE inter . .0 0.6 8 82.0 8 8 8 8 7 9 9 8 8 8 6 6 8 8 2 8 8 8 5 3 3 2 3 2 3 3 7 7 7 5 3 3 9 9 9 2 3 3 1 2 2 3 2 2 3 1 2 3 3 2 1 2 2 2 1 3 3 1 3 3 2 . 3 3 3 . 2 2 2 . 2 . , . 2 3 3 , 2 2 3 . 3 2 2 , , 2 .2 . 3 .3 . 2 8 8 2 .5 . 3 1, .2 2 . 0. . 3 % . 335 . 3, . 3 3. . 3
```

**JSON 输出:**

```json
{
  "text_sequence": "( ( ( ) 0 0 0 0 8 8 8 2 3 3 3 3 2 2 2 2 3 3 4 4 4 7 7 7 7 9 9 9 9 6 8 8 8 0 0 0.6 0 0.<unk> 1 1 1 1 3 3 3 5 3 3 3 6 8 8 6 8 8 0.6 TABLEFORMERLRGE inter . .0 0.6 8 82.0 8 8 8 8 7 9 9 8 8 8 6 6 8 8 2 8 8 8 5 3 3 2 3 2 3 3 7 7 7 5 3 3 9 9 9 2 3 3 1 2 2 3 2 2 3 1 2 3 3 2 1 2 2 2 1 3 3 1 3 3 2 . 3 3 3 . 2 2 2 . 2 . , . 2 3 3 , 2 2 3 . 3 2 2 , , 2 .2 . 3 .3 . 2 8 8 2 .5 . 3 1, .2 2 . 0. . 3 % . 335 . 3, . 3 3. . 3</s>"
}
```

---

# 图像: 6.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 3.02 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.12 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 4.34 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 0.19 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. Up Schetto Quen
```

**JSON 输出:**

```json
{
  "text_sequence": "Up Schetto Quen</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 2.98 秒

```text
Transcribe math as LaTeX when clear; keep original text for body.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 1.91 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 2.98 秒

```text
Provide a concise one-sentence summary of the page content. Eighter
```

**JSON 输出:**

```json
{
  "text_sequence": "Eighter</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.14 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}.
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}.</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 2.68 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. You you may not be to it is not only with anyon a fter use for your me that
```

**JSON 输出:**

```json
{
  "text_sequence": "You you may not be to it is not only with anyon a fter use for your me that</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.30 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. S S S S O O O O o o o o O O O
```

**JSON 输出:**

```json
{
  "text_sequence": "S S S S O O O O o o o o O O O</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 0.21 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.V.WB
```

**JSON 输出:**

```json
{
  "text_sequence": "V.WB</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 0.36 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. . . 0 0 0 0 00 0 0 0 8 8 8 8 5 8 8 8 6 8 8 8 Queen
```

**JSON 输出:**

```json
{
  "text_sequence": ". . 0 0 0 0 00 0 0 0 8 8 8 8 5 8 8 8 6 8 8 8 Queen</s>"
}
```

---

# 图像: 7.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 3.02 秒

```text
<s_cord-v2> Question: "Ofall song lengths, which one is the longest ?? Question: “Ofall ongths, one is the longest ?
```

**JSON 输出:**

```json
{
  "text_sequence": "Question: \"Ofall song lengths, which one is the longest ?? Question: “Ofall ongths, one is the longest ?</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 1.14 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. Query, is the longest ,, S S () 2 5 00 Question: "Ofall song lengths, which one is on the Longest ?? .
```

**JSON 输出:**

```json
{
  "text_sequence": "Query, is the longest ,, S S () 2 5 00 Question: \"Ofall song lengths, which one is on the Longest ?? .</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 4.34 秒

```text
<s_cord-v2> Question: Query Qustion: "Ofall song length, one is the longest ?? Question: “Ofall sog leng th, which one is longer ?
```

**JSON 输出:**

```json
{
  "text_sequence": "Question: Query Qustion: \"Ofall song length, one is the longest ?? Question: “Ofall sog leng th, which one is longer ?</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 1.36 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values. Query Question: "Ofall song lengths, which one is the longest ?" Question: "Ofall song lengths, which one is the longest ?" Question: "Ofall song lengths, which one is the longest ?" Question: "" ?" == == == == == == == == == ==== ====== ============================================================================================================================================================================
```

**JSON 输出:**

```json
{
  "text_sequence": "Query Question: \"Ofall song lengths, which one is the longest ?\" Question: \"Ofall song lengths, which one is the longest ?\" Question: \"Ofall song lengths, which one is the longest ?\" Question: \"\" ?\" == == == == == == == == == ==== ====== ============================================================================================================================================================================</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 5.47 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. Question: "Ofall song lengths, which one is the longest ?? Question: “Ofall ong lengthy, one is longest ?"
```

**JSON 输出:**

```json
{
  "text_sequence": "Question: \"Ofall song lengths, which one is the longest ?? Question: “Ofall ong lengthy, one is longest ?\"</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 5.38 秒

```text
<s_cord-v2> Question: "Ofall song lengths, which one is the longest ? Question: “Ofall ongths, one is the longest ?
```

**JSON 输出:**

```json
{
  "text_sequence": "Question: \"Ofall song lengths, which one is the longest ? Question: “Ofall ongths, one is the longest ?</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 3.19 秒

```text
Provide a concise one-sentence summary of the page content. Question: ‘Ofall song lengths, which one is the longest ?? Question: “Ofall song lengths, which one is the longest ???????????????????????????
```

**JSON 输出:**

```json
{
  "text_sequence": "Question: ‘Ofall song lengths, which one is the longest ?? Question: “Ofall song lengths, which one is the longest ???????????????????????????</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.38 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. guestion: " " Question: " " Questionssssssssssssssssssssssssssssssssssss
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. guestion: \" \" Question: \" \" Questionssssssssssssssssssssssssssssssssssss</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 5.72 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text. Question: "Ofall song lengths, which one is the longest ??
```

**JSON 输出:**

```json
{
  "text_sequence": "Question: \"Ofall song lengths, which one is the longest ??</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 1.44 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. Query Query Question: “Ofall song lengths, which one is the longest ?" Question: ‘Ofall song longths, which one is the longest ?” Question: ‘‘Ofall longths’, ’{a}{a}}{a!a!?!a! , ’''''" Query.'''s.''s's 's's', , .'s'(a!a.'s "'s''s " Query.s.'s.s's (uery.'s ''s.i Query!a!a's. Query. Query, Query, s.s.s.i.s.
```

**JSON 输出:**

```json
{
  "text_sequence": "Query Query Question: “Ofall song lengths, which one is the longest ?\" Question: ‘Ofall song longths, which one is the longest ?” Question: ‘‘Ofall longths’, ’{a}{a}}{a!a!?!a! , ’''''\" Query.'''s.''s's 's's', , .'s'(a!a.'s \"'s''s \" Query.s.'s.s's (uery.'s ''s.i Query!a!a's. Query. Query, Query, s.s.s.i.s.</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 2.94 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.PoPoPoPossesssesssessses.SoSoSoSoBeBeBeBeGeGeGeGeBeBeBeB.PoPoBeBeBeE.BeBeBeMeMeMeBeBeBeBaBaBaBaBeBeBeDeBeBeBeReBeBeBeWBeBeBeeBeBeBeMoMoMoMoBBeBeBeBiGeGeGeMeMeMeMeGeGeGeSoSoSoGeGeGeWGeGeGeBGeGeGeMoMoMoBeBeBeInGeGeGeOBeBeBeSoSoSoMeMeMeEBeBeBeMaMaMaMaMeMeMeMoMoMoMGeGeGeReBeBeMeBeBeGeBeBeGeMeMeBeGeGeBeGeGeMeBeBeMeGeGeBeMeMeGeBeBeBBeBeBXBeBeBePaPaPaBeBeBeBerBeBeBeHeMoMoMoMeMeMeMaMaMaBeBeBePoPoPoMeMeMeSoSoSoMaMaMaGeGeGeSeSeSeSeGeGeGeBiBeBeBePGeGeGeDoDoBeBeBeBoBeBeBeGaGeGeGeRoBeBeBePerSoSoSoToGeGeGeHeMoMoMeGeGeOffeeGeGeGe
```

**JSON 输出:**

```json
{
  "text_sequence": "PoPoPoPossesssesssessses.SoSoSoSoBeBeBeBeGeGeGeGeBeBeBeB.PoPoBeBeBeE.BeBeBeMeMeMeBeBeBeBaBaBaBaBeBeBeDeBeBeBeReBeBeBeWBeBeBeeBeBeBeMoMoMoMoBBeBeBeBiGeGeGeMeMeMeMeGeGeGeSoSoSoGeGeGeWGeGeGeBGeGeGeMoMoMoBeBeBeInGeGeGeOBeBeBeSoSoSoMeMeMeEBeBeBeMaMaMaMaMeMeMeMoMoMoMGeGeGeReBeBeMeBeBeGeBeBeGeMeMeBeGeGeBeGeGeMeBeBeMeGeGeBeMeMeGeBeBeBBeBeBXBeBeBePaPaPaBeBeBeBerBeBeBeHeMoMoMoMeMeMeMaMaMaBeBeBePoPoPoMeMeMeSoSoSoMaMaMaGeGeGeSeSeSeSeGeGeGeBiBeBeBePGeGeGeDoDoBeBeBeBoBeBeBeGaGeGeGeRoBeBeBePerSoSoSoToGeGeGeHeMoMoMeGeGeOffeeGeGeGe</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 3.44 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. Query Question:“Ofall song lengths, which one is the longest ?" Question: “Ofall fang" length" ?" ?" !" !" ?" !!!!!!!!!!!!!!!!!!!!!!!!???? Question: "Of all song leng ths, one is the lowest ?" Question ?" Song ?" Question is ?" Questions ?" Question on is the is any any any anywhere is any anyon is not any any any may may may may not any anyon any any anyon you any any any of any any any not any any may any any any with any any anyanyanyanyany may may may any anywhere any any anymaymaymaymay may may may only any any any and any any may not any may may not may may may must may may maymaymaymay any any any you may may not you may may may be any may may anymaymay may any may maymay may may anyon any may may are any any any other may may may as you may may anywhere may may may and any anyon may any anyon
```

**JSON 输出:**

```json
{
  "text_sequence": "Query Question:“Ofall song lengths, which one is the longest ?\" Question: “Ofall fang\" length\" ?\" ?\" !\" !\" ?\" !!!!!!!!!!!!!!!!!!!!!!!!???? Question: \"Of all song leng ths, one is the lowest ?\" Question ?\" Song ?\" Question is ?\" Questions ?\" Question on is the is any any any anywhere is any anyon is not any any any may may may may not any anyon any any anyon you any any any of any any any not any any may any any any with any any anyanyanyanyany may may may any anywhere any any anymaymaymaymay may may may only any any any and any any may not any may may not may may may must may may maymaymaymay any any any you may may not you may may may be any may may anymaymay may any may maymay may may anyon any may may are any any any other may may may as you may may anywhere may may may and any anyon may any anyon</s>"
}
```

---

# 图像: 8.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 3.94 秒

```text
<s_cord-v2> et al. (2020) Eisenschlos et al. (2021) TAPASBASE et al.(2020) (20)))) )))) TAPASE int-sq al. (202) (20)) () et al. al. (20)) (202)) ()) et al al. () () - 0.8 42.5 40.8 42.5 40.8 41.7 43.9 TA TA TA TA LABLEFORMERBASE inter-sqa et al. et al.. (202)))) ( ) () ()() () ( ) ) () ) ()
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (2020) Eisenschlos et al. (2021) TAPASBASE et al.(2020) (20)))) )))) TAPASE int-sq al. (202) (20)) () et al. al. (20)) (202)) ()) et al al. () () - 0.8 42.5 40.8 42.5 40.8 41.7 43.9 TA TA TA TA LABLEFORMERBASE inter-sqa et al. et al.. (202)))) ( ) () ()() () ( ) ) () ) ()</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.72 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols. T T E Eisenschlos et al. (2021) TA TA BA BA .8 51.5 23.6 34.4 24. 34.8 42.5 34.5 40.2 21.7 43.9 45. 41.7 44.6.5 48.4 515.02021.
```

**JSON 输出:**

```json
{
  "text_sequence": "T T E Eisenschlos et al. (2021) TA TA BA BA .8 51.5 23.6 34.4 24.<unk> 34.8 42.5 34.5 40.2 21.7 43.9 45.<unk> 41.7 44.6.5 48.4 515.02021.</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 3.44 秒

```text
<s_cord-v2> et al. (2020) Eisenschlos et al . () TAPASBASE ener at. (20 ) - 0 8 42.5 e r a d i t p p p P P P N N S L A B R M K K K H WWWWWWWWWWWWWSPSPSPSSSSSSS TA BABE inter-q ue stlessnessessss s m m m = 1 31.9 ot ornm m mrm m n m mcp m m rwh m m c r wheel m m
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (2020) Eisenschlos et al . () TAPASBASE ener at. (20 ) - 0 8 42.5 e r a d i t p p p P P P N N S L A B R M K K K H WWWWWWWWWWWWWSPSPSPSSSSSSS TA BABE inter-q ue stlessnessessss s m m m = 1 31.9 ot ornm m mrm m n m mcp m m rwh m m c r wheel m m</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 0.96 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.E Eisenschlos et al. (202) ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||:: .: .....0.WBASE...... .20202018.0020......V....0.8..
```

**JSON 输出:**

```json
{
  "text_sequence": "E Eisenschlos et al. (202) ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||:: .: .....0.WBASE...... .20202018.0020......V....0.8..</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 2.69 秒

```text
Transcribe math as LaTeX when clear; keep original text for body. TAPASBASE inter-s TAPASE al. (2021) TA TA TA FA FA FA TA TA ORMERBASE int-sq et al. (2017.01.11) 24. 23.6 34.4 40.8 42.5 41.7 43.9 44.8 46.7 48.8 51.5 23.6 24. 34.8 24. 33.9 49 49.9 51.3 45.5 43.4 24.8 34.4 24.4 .
```

**JSON 输出:**

```json
{
  "text_sequence": "TAPASBASE inter-s TAPASE al. (2021) TA TA TA FA FA FA TA TA ORMERBASE int-sq et al. (2017.01.11) 24.<unk> 23.6 34.4 40.8 42.5 41.7 43.9 44.8 46.7 48.8 51.5 23.6 24.<unk> 34.8 24.<unk> 33.9 49 49.9 51.3 45.5 43.4 24.8 34.4 24.4 .</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 4.16 秒

```text
<s_cord-v2> et al. (2020) Eisenschlos et al. (2021) TAPASE et al.(2020) () () ) - - TA TA TA TA BA BAE int-sq al. (20 (20) (2021) (2021)) et al. 20 20 20 20 10 10 10 10 ( ) - ) - 0 8 42.5 40.8 42.5 41.7 43.9 TAPASE inter-sqa TA TA TA LABLEPORMERBASE inter-sq TA TA TA FA LABLEFORMERBASE interes-sq a TA TA TA PASLARGE fter-sqq u TABLEFORMERMERBEBEBE inter-squ
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (2020) Eisenschlos et al. (2021) TAPASE et al.(2020) () () ) - - TA TA TA TA BA BAE int-sq al. (20 (20) (2021) (2021)) et al. 20 20 20 20 10 10 10 10 ( ) - ) - 0 8 42.5 40.8 42.5 41.7 43.9 TAPASE inter-sqa TA TA TA LABLEPORMERBASE inter-sq TA TA TA FA LABLEFORMERBASE interes-sq a TA TA TA PASLARGE fter-sqq u TABLEFORMERMERBEBEBE inter-squ</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 1.56 秒

```text
Provide a concise one-sentence summary of the page content. (2) et al. (2021) e r r r r r r r r r r e e e p T T T r r r r r r r r r r r r r e r r r r r r r r r r r r r r r r r r r r r r r r r
```

**JSON 输出:**

```json
{
  "text_sequence": "(2) et al. (2021) e r r r r r r r r r r e e e p T T T r r r r r r r r r r r r r e r r r r r r r r r r r r r r r r r r r r r r r r r</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.34 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}. ( ) - - - - - -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( )
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}. ( ) - - - - - -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( ) -s. ( )</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 2.69 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text.(Herigh) | - TA BABE inter-qa enerc or at al. (2021) (2016 ) -- : ________________________________________________ TA PA S BASE inter-q a TARLEFORMERBASE inter~sqa e r TAPASBASE exceeces: et al. 20 10 3 40 8 2 m 5 6 38 35 49 4. 4 % ASMSPARE an int of the states PARKBRLESETERBREBASE 24.688285262218646505308
```

**JSON 输出:**

```json
{
  "text_sequence": "(Herigh) | - TA BABE inter-qa enerc or at al. (2021) (2016 ) -- : ________________________________________________ TA PA S BASE inter-q a TARLEFORMERBASE inter~sqa e r TAPASBASE exceeces: et al. 20 10 3 40 8 2 m 5 6 38 35 49 4. 4 % ASMSPARE an int of the states PARKBRLESETERBREBASE 24.688285262218646505308</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 1.22 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize. T T T T A B B BASE et al. (2021) TA TA TA TA BA BA BA BA TA TA TA PA BA BA BABE et al. (2020) Eisenschlos et al. (4021) T T TAPA BA BA BA FA TA TA TA FA BA BA BA FORMER BEFORMER BE BEFORMER ORMER BE TA TA PA TA TA TA PER FORMER BE FORMER BE at at at at al. TA TA TA S B B B B T T T. (2020 . (2021) TARGE TA TA TA T T TEST T T T S T T T M T T T . T T. T T A T T T 0. T T F ORMER T T T P T T T F R T T T
```

**JSON 输出:**

```json
{
  "text_sequence": "T T T T A B B BASE et al. (2021) TA TA TA TA BA BA BA BA TA TA TA PA BA BA BABE et al. (2020) Eisenschlos et al. (4021) T T TAPA BA BA BA FA TA TA TA FA BA BA BA FORMER BEFORMER BE BEFORMER ORMER BE TA TA PA TA TA TA PER FORMER BE FORMER BE at at at at al. TA TA TA S B B B B T T T. (2020 . (2021) TARGE TA TA TA T T TEST T T T S T T T M T T T . T T. T T A T T T 0. T T F ORMER T T T P T T T F R T T T</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 1.91 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.WWWWWWWWW.PoPoPoPoR.WWW.WBoddoddoddodd.W.WB.W.V.W.PoPoW.WPPPPPPPPPpppppppp.WPppppppPPPPPPGeGeGeGeBeBeBeBeGeGeGeSoSoSoSoGeGeGeWPPPPPPPSPSPSPSPPPPPP.PPPPP.PoPoPPPPPPSPPPP.VPPPPPPPCPPPPPPPOPPPPPPRPRPRPRPPPPPPPMPMPMPMPPPPPPP,PPPPPPPPPPPppPPPP.PPPPPPHPHPHPHPPPPPPP .PPPP.pppppp pppppppp,PPPPP,PppppPPpppp.Ppppp.PPPPPS.PPPppppPP.PppPPPPPS,PPPP.WPPPP.com/PPPPPPGPGPGPGPPPPPP-PPPPP-PPPPPPMSRT.PPPP,VPPPP,PoPoPo
```

**JSON 输出:**

```json
{
  "text_sequence": "WWWWWWWWW.PoPoPoPoR.WWW.WBoddoddoddodd.W.WB.W.V.W.PoPoW.WPPPPPPPPPpppppppp.WPppppppPPPPPPGeGeGeGeBeBeBeBeGeGeGeSoSoSoSoGeGeGeWPPPPPPPSPSPSPSPPPPPP.PPPPP.PoPoPPPPPPSPPPP.VPPPPPPPCPPPPPPPOPPPPPPRPRPRPRPPPPPPPMPMPMPMPPPPPPP,PPPPPPPPPPPppPPPP.PPPPPPHPHPHPHPPPPPPP .PPPP.pppppp pppppppp,PPPPP,PppppPPpppp.Ppppp.PPPPPS.PPPppppPP.PppPPPPPS,PPPP.WPPPP.com/PPPPPPGPGPGPGPPPPPP-PPPPP-PPPPPPMSRT.PPPP,VPPPP,PoPoPo</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 1.84 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content. et al. (2021) Eisenschlos al. (202) TAPASBASE TA TA TA TA TRA TRA TRA TRASE FORMERBASE inter-sqa TA TA TA BA BABE inter-sq TA ORMERBASE enter-sq TARGE et al. (2020) Fisenschlos et al. et (2021) et TAPERMERBASE TA TAMERMERBASE ent orMERBASE et al. 2021) TAMERBASE in ter-s at at at at all. (2021) TA TA TAMERBBE inter-styles at at an an an an ast at at at on at at at any any any any may at at at as at at at and and and and at at atenterenterenterenters at at any may may may at any any may may at at any forMERLARGE inter-s at any may not at any any of at any any at any any forMERLANGE TAPERMERLARGE MARGE inter-style and any may may not at an an any may may and and and any may at any may at an any any any and any any may any may may any any may not any any any are any any anyonMERRMERBASE any any any you may may may may any may any any any
```

**JSON 输出:**

```json
{
  "text_sequence": "et al. (2021) Eisenschlos al. (202) TAPASBASE TA TA TA TA TRA TRA TRA TRASE FORMERBASE inter-sqa TA TA TA BA BABE inter-sq TA ORMERBASE enter-sq TARGE et al. (2020) Fisenschlos et al. et (2021) et TAPERMERBASE TA TAMERMERBASE ent orMERBASE et al. 2021) TAMERBASE in ter-s at at at at all. (2021) TA TA TAMERBBE inter-styles at at an an an an ast at at at on at at at any any any any may at at at as at at at and and and and at at atenterenterenterenters at at any may may may at any any may may at at any forMERLARGE inter-s at any may not at any any of at any any at any any forMERLANGE TAPERMERLARGE MARGE inter-style and any may may not at an an any may may and and and any may at any may at an any any any and any any may any may may any any may not any any any are any any anyonMERRMERBASE any any any you may may may may any may any any any</s>"
}
```

---

# 图像: 9.jpg

## 预设: `balanced_beam`

* 提示: `<s_cord-v2>`
* 运行时间: 2.92 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `eq_compact`

* 提示: `Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.`
* 运行时间: 0.13 秒

```text
Transcribe visible equations using LaTeX; keep inline math inline; do not invent symbols.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `fast_draft`

* 提示: `<s_cord-v2>`
* 运行时间: 2.88 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `figure_bullets`

* 提示: `Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.`
* 运行时间: 0.17 秒

```text
Summarize the figure with up to 5 bullet points: (1) key entities, (2) relationships, (3) notable labels/values.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `formula_friendly`

* 提示: `Transcribe math as LaTeX when clear; keep original text for body.`
* 运行时间: 4.53 秒

```text
Transcribe math as LaTeX when clear; keep original text for body.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `long_page_strict`

* 提示: `<s_cord-v2>`
* 运行时间: 3.27 秒

```text
<s_cord-v2>
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `page_summary`

* 提示: `Provide a concise one-sentence summary of the page content.`
* 运行时间: 4.31 秒

```text
Provide a concise one-sentence summary of the page content. A
```

**JSON 输出:**

```json
{
  "text_sequence": "A</s>"
}
```

## 预设: `router_probe`

* 提示: `Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool,  "is_text": bool, "dominant": "table|equation|figure|text|mixed",  "table_size": "none|small|large", "confidence": number}.`
* 运行时间: 0.15 秒

```text
Classify the page layout. Output STRICT JSON ONLY with keys: {"is_table": bool, "is_equation": bool, "is_figure": bool, "is_text": bool, "dominant": "table|equation|figure|text|mixed", "table_size": "none|small|large", "confidence": number}.
```

**JSON 输出:**

```json
{
  "text_sequence": "Classify the page layout. Output STRICT JSON ONLY with keys: {\"is_table\": bool, \"is_equation\": bool, \"is_figure\": bool, \"is_text\": bool, \"dominant\": \"table|equation|figure|text|mixed\", \"table_size\": \"none|small|large\", \"confidence\": number}.</s>"
}
```

## 预设: `table_markdown`

* 提示: `If tables are present, render them as GitHub-flavored Markdown; otherwise read text.`
* 运行时间: 2.95 秒

```text
If tables are present, render them as GitHub-flavored Markdown; otherwise read text.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `table_strict_md`

* 提示: `Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.`
* 运行时间: 0.22 秒

```text
Extract all tables as GitHub-Flavored Markdown. Preserve headers, numbers, and punctuation exactly. Do not summarize.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

## 预设: `universal_doc`

* 提示: `Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.`
* 运行时间: 0.21 秒

```text
Analyze the page image and output STRICT JSON with keys: {"page_type": ["table"|"equation"|"figure"|"text"|"mixed"], "tables_md": [], "equations_latex": [], "caption": "", "text": ""}. Rules: 1) If the page is predominantly a TABLE and small enough, transcribe it exactly as GitHub-Flavored Markdown into tables_md. 2) If the page is predominantly EQUATIONS with little body text, transcribe equations into equations_latex (LaTeX). 3) If the layout is MIXED or too large to reproduce, do NOT hallucinate; return a short caption and key body text; keep tables_md/equations_latex empty. Always return valid JSON and no text outside JSON.WBr
```

**JSON 输出:**

```json
{
  "text_sequence": "WBr</s>"
}
```

## 预设: `wide_table_md`

* 提示: `If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.`
* 运行时间: 0.27 秒

```text
If the table is wide, split into multiple Markdown tables by logical sections. Preserve header rows; avoid wrapping cell content.
```

**JSON 输出:**

```json
{
  "text_sequence": "</s>"
}
```

---
