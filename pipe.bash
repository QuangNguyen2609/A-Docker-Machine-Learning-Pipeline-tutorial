export GOOGLE_APPLICATION_CREDENTIALS=./dummy-mles.json

python download.py
python version_data.py
python pytorch_images_classification.py