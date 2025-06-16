import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import io

def detect_labels_and_visualize(bucket_name, image_key):
    """
    Detects labels in an image stored in S3 using Amazon Rekognition
    and visualizes them with bounding boxes using Matplotlib.

    Args:
        bucket_name (str): The name of the S3 bucket where the image is stored.
        image_key (str): The key (path) to the image file in the S3 bucket.
    """
    rekognition_client = boto3.client('rekognition')
    s3_client = boto3.client('s3')

    print(f"Detecting labels for '{image_key}' in bucket '{bucket_name}'...")

    try:
        # 1. Call Rekognition to detect labels
        response = rekognition_client.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': 'rekognition-image-bucket-x7a9kf3',
                    'Name': 'random.jpg'
                }
            },
            MaxLabels=10,  # Max number of labels to return
            MinConfidence=70 # Minimum confidence score for a label to be returned
        )

        labels = response['Labels']
        print(f"Detected {len(labels)} labels:")
        for label in labels:
            print(f"  - {label['Name']} (Confidence: {label['Confidence']:.2f}%)")

        # 2. Download the image from S3
        print(f"\nDownloading image '{image_key}' from S3...")
        obj = s3_client.get_object(Bucket=bucket_name, Key=image_key)
        image_bytes = io.BytesIO(obj['Body'].read())
        image = Image.open(image_bytes)

        # 3. Prepare for visualization with Matplotlib
        fig, ax = plt.subplots(1)
        ax.imshow(image)
        current_width, current_height = image.size

        # 4. Draw bounding boxes for instances
        for label in labels:
            if 'Instances' in label:
                for instance in label['Instances']:
                    bbox = instance['BoundingBox']
                    x = bbox['Left'] * current_width
                    y = bbox['Top'] * current_height
                    width = bbox['Width'] * current_width
                    height = bbox['Height'] * current_height

                    rect = patches.Rectangle(
                        (x, y),
                        width,
                        height,
                        linewidth=1,
                        edgecolor='r', # Red bounding box
                        facecolor='none'
                    )
                    ax.add_patch(rect)

                    # Add text label (adjust position to avoid overlapping box)
                    label_text = f"{label['Name']} ({instance['Confidence']:.2f}%)"
                    plt.text(
                        x, y - 5,  # Slightly above the bounding box
                        label_text,
                        color='white',
                        fontsize=8,
                        bbox=dict(facecolor='red', alpha=0.7, edgecolor='none', pad=1)
                    )
            elif 'Parents' in label: # Sometimes labels have parents but no instances, useful for general categories
                # You can choose to visualize these differently or not at all
                pass


        ax.axis('off') # Hide axes
        plt.title(f"Image Analysis: {image_key}")
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # --- Configuration ---
    S3_BUCKET_NAME = 'rekognition-image-bucket-x7a9kf3' # Your S3 bucket name
    S3_IMAGE_KEY = 'random.jpg'                         # Your image key in S3

    detect_labels_and_visualize(S3_BUCKET_NAME, S3_IMAGE_KEY)