# DOCKER BUILD CMD #

## STEP 1 ## 
build docker
`docker build -t cloud .`

## STEP 2 ##
run dockerized image 
`docker run -p 8000:8000 -t cloud`

## STEP 3 ##
tagging image with repo path (create repo before this)
`docker tag cloud quangnguyennnnn/cloud-training:pytorch-cloud`

## STEP 4 ##
login to docker registry
`docker login`

## STEP 5
push tag to repo
`docker push quangnguyennnnn/cloud-training:pytorch-cloud`

## STEP 6 ##
pull tag from repo remotely
`docker pull quangnguyennnnn/cloud-training:pytorch-cloud`

## STEP 7 ##
run the whole program 
`docker run quangnguyennnnn/cloud-training:pytorch-cloud`

## STEP 8 (Optional) ##
access to the source code
`docker run -it quangnguyennnnn/cloud-training:pytorch-cloud /bin/bash`
