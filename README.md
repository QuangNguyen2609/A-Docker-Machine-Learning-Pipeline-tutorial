# Cloud Training and Dockerization with PyTorch 

This project builds a data pipeline that pulls data from Google Cloud, preprocesses it, stores it in MongoDB, and trains machine learning models using PyTorch.

## Running the Project with Docker

To run the project using Docker, follow these steps:

### Step 1: Build the Docker Image

Use the following command to build the Docker image:
`docker build -t cloud .`

### Step 2: Run the Docker Image

Use the following command to run the Docker image:
`docker run -p 8000:8000 -t cloud`

### Step 3: Tag the Image with Repository Path

Use the following command to tag the Docker image with the repository path (Create this repo on docker registry first):

`docker tag cloud quangnguyennnnn/cloud-training:pytorch-cloud`

Note: Replace `quangnguyennnnn` with your Docker Hub username or the name of your Docker repository.

### Step 4: Login to Docker Registry

Use the following command to login to your Docker registry:

`docker login`

### Step 5: Push the Tag to the Repository

Use the following command to push the tag to the repository:

`docker push quangnguyennnnn/cloud-training:pytorch-cloud`

Note: Replace `quangnguyennnnn` with your Docker Hub username or the name of your Docker repository.

### Step 6: Pull the Tag from the Repository Remotely

Use the following command to pull the tag from the repository remotely:
`docker pull quangnguyennnnn/cloud-training:pytorch-cloud`

### Step 7: Run the Whole Program

Use the following command to run the whole program:

`docker run quangnguyennnnn/cloud-training:pytorch-cloud`

### STEP 8 (Optional) ###
Use the following command to access to the source code
`docker run -it quangnguyennnnn/cloud-training:pytorch-cloud /bin/bash`

Note: Replace `quangnguyennnnn` with your Docker Hub username or the name of your Docker repository.

## Conclusion

Congratulations on completing your project! By following the steps outlined in this README file, others will be able to easily build and run your project using Docker. Don't forget to update this file with any additional information or changes to the project.
