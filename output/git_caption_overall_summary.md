# GIT Caption Overall Summary

## GIT-base-caption

| preset                |   avg_inference_time |   avg_tokens |   images |   total_time |
|:----------------------|---------------------:|-------------:|---------:|-------------:|
| chart_analysis        |             0.168737 |      9.27778 |       18 |      12.9136 |
| comprehensive_caption |             0.133965 |     10.0556  |       18 |      12.9136 |
| precision_focused     |             0.133114 |      8.94444 |       18 |      12.9136 |
| structured_analysis   |             0.144213 |     10.7778  |       18 |      12.9136 |
| technical_description |             0.137396 |      8.61111 |       18 |      12.9136 |

## GIT-base-coco-caption

| preset                |   avg_inference_time |   avg_tokens |   images |   total_time |
|:----------------------|---------------------:|-------------:|---------:|-------------:|
| chart_analysis        |             0.172142 |      9.33333 |       18 |      12.6334 |
| comprehensive_caption |             0.116377 |      9       |       18 |      12.6334 |
| precision_focused     |             0.13219  |      9.11111 |       18 |      12.6334 |
| structured_analysis   |             0.14031  |     10.6111  |       18 |      12.6334 |
| technical_description |             0.140839 |      9.11111 |       18 |      12.6334 |

## GIT-large-coco-caption

| preset                |   avg_inference_time |   avg_tokens |   images |   total_time |
|:----------------------|---------------------:|-------------:|---------:|-------------:|
| chart_analysis        |             0.306717 |      12.4444 |       18 |      25.5936 |
| comprehensive_caption |             0.26243  |      12.7778 |       18 |      25.5936 |
| precision_focused     |             0.28854  |      12.9444 |       18 |      25.5936 |
| structured_analysis   |             0.268934 |      13.1667 |       18 |      25.5936 |
| technical_description |             0.295248 |      12.5556 |       18 |      25.5936 |

## Cross-model comparison by preset

### Avg inference time (s)

| preset                |   GIT-base-caption |   GIT-base-coco-caption |   GIT-large-coco-caption |
|:----------------------|-------------------:|------------------------:|-------------------------:|
| chart_analysis        |           0.168737 |                0.172142 |                 0.306717 |
| comprehensive_caption |           0.133965 |                0.116377 |                 0.26243  |
| precision_focused     |           0.133114 |                0.13219  |                 0.28854  |
| structured_analysis   |           0.144213 |                0.14031  |                 0.268934 |
| technical_description |           0.137396 |                0.140839 |                 0.295248 |

### Avg tokens

| preset                |   GIT-base-caption |   GIT-base-coco-caption |   GIT-large-coco-caption |
|:----------------------|-------------------:|------------------------:|-------------------------:|
| chart_analysis        |            9.27778 |                 9.33333 |                  12.4444 |
| comprehensive_caption |           10.0556  |                 9       |                  12.7778 |
| precision_focused     |            8.94444 |                 9.11111 |                  12.9444 |
| structured_analysis   |           10.7778  |                10.6111  |                  13.1667 |
| technical_description |            8.61111 |                 9.11111 |                  12.5556 |
