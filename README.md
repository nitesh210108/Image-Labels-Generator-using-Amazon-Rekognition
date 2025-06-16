# 🏷️ Image Labels Generator using Amazon Rekognition

This project uses **Amazon Rekognition** and **Amazon S3** to analyze images and automatically generate object labels. It’s a beginner-friendly way to explore AWS AI services like Rekognition, ideal for practical use cases like surveillance, product detection, and accessibility tools.

---

## 🖼️ Demo Screenshots

| Upload to S3 | AWS Rekognition Call | Output with Labels |
|--------------|----------------------|---------------------|
| ![1](screenshots/1.png) | ![2](screenshots/2.png) | ![3](screenshots/3.png) |
| ![4](screenshots/4.png) | ![5](screenshots/5.png) | ![6](screenshots/6.png) |
| ![7](screenshots/7.png) | ![8](screenshots/8.png) | ![9](screenshots/9.png) |
| ![10](screenshots/10.png) | ![11](screenshots/11.png) | ![12](screenshots/12.png) |
| ![13](screenshots/13.png) | ![13](screenshots/random.jpg) | ![13](screenshots/Figure_1.jpg) |

---

## 🚀 Features

- Upload images to an S3 bucket
- Detect objects using Amazon Rekognition’s `detect_labels`
- Visualize results with bounding boxes and labels using Matplotlib
- Customize confidence threshold and label limits
- Easily extend for real-world applications

---

## 📦 Requirements

- AWS Account
- IAM user with permissions: `AmazonS3FullAccess` and `AmazonRekognitionFullAccess`
- Python 3.7 or higher
- AWS CLI configured with your credentials
- Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
