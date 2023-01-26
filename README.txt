1-Docker İmage Build
docker image build -t ml-prediction-with-fastapi:1.0 .

2-Docker Container Build
docker run --rm --name ml-prediction-with-fastapi -p 8000:8000 -d ml-prediction-with-fastapi:1.0

3-Docker Hub Repisortry
You have to create one repisitory with this name ml-prediction-with-fastapi

4-Docker Tag
docker tag image_name it_will_create_new_image_name
docker tag ml-prediction-with-fastapi:1.0 hanoguz00/ml-prediction-with-fastapi:1.0

docker image ls
