- In this project, a simple FastApi application was presented in Google Cloud using ML algorithm first, then docker and then kubernetes.
- Used technologies
    - Docker
    - Kubernetes
    - Git
    - FastApi
    - Cloud

### 1. Uvicorn

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 2. Docker İmage Build

```
docker image build -t ml_fastapi .
```

### 3. Docker Container Build

```
docker run --rm --name ml_fastapi -p 8000:8000 -d ml_fastapi
```
#### OR

```
docker run -d --name ml_fastapi -p 8000:8000 ml_fastapi
```

### 3. Docker Hub Repository

- You have to create one repository on your account with this name "ml-prediction-with-fastapi"

### 4. Docker Tag
```
docker tag "image_name" "your_docker_repository_name"
```
```
docker tag ml_fastapi hanoguz00/ml-prediction-with-fastapi
```
```
docker image ls
```

### 5. Docker push image with tag

```
docker push hanoguz00/ml-prediction-with-fastapi
```


### 6. Open the Google Cloud Kubernets Engine

- Creta cluster with "Standard: You manage your cluster"

- Connect the cluster with Google terminal


### 7. Send your project to dockerhub

```
docker push hanoguz00/ml-prediction-with-fastapi
```

### 8. Send your project to Github

- Creat new repository named "ml_fastapi_1"

```
git commit -m "first commit"
```

```
git branch -M main
```

```
git remote add origin https://github.com/KuserOguzHan/ml_fastapi_1.git
```

```
git push -u origin main
```
#### Delete origin ıf you error

```
git remote rm origin
```

### 9. Clone repository to kubernetes cluster

```
git clone https://github.com/KuserOguzHan/ml_fastapi_1.git
```

### 10 Create build.yaml for kubernetes

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mymlapp
  labels:
    app: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: predictor 
          image: hanoguz00/ml-prediction-with-fastapi
          ports:
            - containerPort: 8000
```

### 11. Create kubernetes pods

```
kubectl apply -f build.yaml
```
