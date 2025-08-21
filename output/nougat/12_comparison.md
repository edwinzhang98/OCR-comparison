# Comparison for 12.jpg

## Preset: fast

**Description:** 快速模式 - 牺牲一些质量换取速度

**Time:** 0.23s  
**Length:** 24 characters  
**Speed:** 85.7 tokens/s  

### Generated Text

```markdown
Attn(\(H\)) = softmax() 
```

---

## Preset: balanced

**Description:** 平衡模式 - 速度和质量的平衡

**Time:** 0.32s  
**Length:** 35 characters  
**Speed:** 81.5 tokens/s  

### Generated Text

```markdown
Attn(_H_) = softmax(\(\sqrt{dx}\)) 
```

---

## Preset: quality

**Description:** 高质量模式 - 最佳识别质量

**Time:** 0.58s  
**Length:** 40 characters  
**Speed:** 54.0 tokens/s  

### Generated Text

```markdown
Attn(\(H\)) = softmax(\(\sqrt{d_{K}}\)) 
```

---

## Preset: math

**Description:** 数学文档模式 - 优化数学公式识别

**Time:** 0.47s  
**Length:** 38 characters  
**Speed:** 63.2 tokens/s  

### Generated Text

```markdown
Attn(_H_) = softmax(\(\sqrt{d_{K}}\)) 
```

---

## Preset: table

**Description:** 表格文档模式 - 优化表格识别

**Time:** 0.47s  
**Length:** 40 characters  
**Speed:** 67.0 tokens/s  

### Generated Text

```markdown
Attn(\(H\)) = softmax(\(\sqrt{d_{K}}\)) 
```

---

