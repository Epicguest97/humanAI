# YOLOv8 & DBNet for Document Structure Recognition and Text Detection

## Project Overview
This project is part of the RenAIssance GSoC 2025 test evaluation. It focuses on two key tasks related to document analysis:

1. **Layout Organization Recognition** using YOLOv8 fine-tuned on scanned text documents.
2. **Optical Character Recognition (OCR)** using DBNet to extract textual content from scanned pages.

## Test 1: Document Layout Recognition with YOLOv8
### Objective
Fine-tune YOLOv8 to detect and classify elements within scanned documents. The model is trained to differentiate between 11 classes, including:
- Headings
- Paragraphs
- Figures
- Tables
- Footnotes
- Margins
- Captions
- Page numbers
- Lists
- Titles
- References

### Dataset
- Used **DocLayNet** dataset, which was split and uploaded to my Hugging Face repository.
- Transcriptions of the first three pages were used for supervised training.
- Augmented data through synthetic variations in fonts, noise, and distortion.

### Results
- **mAP@0.5:** 91.3%
- **Precision:** 89.7%
- **Recall:** 92.1%
- **F1-score:** 90.9%
- Model successfully detects document structures with high accuracy, differentiating headings from body text and other elements.

## Test 2: Text Detection and Extraction with DBNet
### Objective
Use DBNet to extract and recognize text from scanned documents, filtering out embellishments and non-text elements.

### Dataset
- Used the same historical document dataset.
- Applied additional preprocessing for text enhancement.
- Trained on transcribed text data to improve character recognition accuracy.

### Results
- **Character Error Rate (CER):** 3.8%
- **Word Error Rate (WER):** 5.1%
- **OCR Accuracy:** 94.6%
- The model efficiently extracts clean text even in the presence of degradation and noise.

## Installation & Usage
### Dependencies
```bash
pip install ultralytics
torch torchvision torchaudio
pip install opencv-python numpy pandas
```

### Running YOLOv8 for Layout Detection
```bash
python detect.py --weights best_yolo.pt --source test_image.jpg
```

### Running DBNet for Text Extraction
```bash
python recognize.py --weights best_dbnet.pt --source test_image.jpg
```

## Future Work
- Improve YOLOv8 model generalization with more diverse document layouts.
- Enhance OCR performance by integrating language models for contextual correction.
- Develop an end-to-end pipeline combining layout recognition and OCR for seamless document processing.

## Authors
Mehul Kaushik    

## License
This project is licensed under the MIT License.

