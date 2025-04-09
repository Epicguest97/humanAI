# 🧠 Document Layout Recognition with YOLOv8

This project fine-tunes a YOLOv8 model to detect and classify structural components in scanned historical or academic documents using the [DocLayNet](https://github.com/Layout-Parser/DocLayNet) dataset.

## i have two pdf containing the yolo finetuning and the inference of this model

## 🎯 Objective

- Detect and classify 11 layout classes:
  - Headings, Paragraphs, Figures, Tables, Footnotes, Margins, Captions, Page Numbers, Lists, Titles, References

- Build a lightweight and accurate model for layout understanding in digitized documents.

## 📚 Dataset

- **Source**: DocLayNet Dataset  
- **Preprocessing**:
  - Focused on first three transcribed pages for supervised learning
  - Data augmentation: font variation, noise injection, rotation, and print distortion
- **Annotations**: Converted to YOLO format using a custom script
- **Hosted on**: My [Hugging Face Dataset Repo](#) (add your link here)

## 🧪 Results

| Metric        | Score   |
|---------------|---------|
| mAP@0.5       | 91.3%   |
| Precision     | 89.7%   |
| Recall        | 92.1%   |
| F1-Score      | 90.9%   |

- The model shows strong performance across all layout classes.
- Especially effective in recognizing **marginalia**, **tables**, and **multi-level headers**.

## 🧩 Model

- **Base Model**: YOLOv8n
- **Framework**: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- **Training & Inference Notebook**: [`Yolo_finetuning.ipynb`](./Yolo_finetuning.ipynb)

## 🖼️ Visual Results

(Add a few screenshots or prediction examples here)

## 🛠️ How to Run

### 1. Clone Repo & Install Requirements
```bash
git clone https://github.com/your-username/layout-yolov8.git
cd layout-yolov8
pip install -r requirements.txt
