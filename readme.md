# Rick and Morty Application
## 1. Overview

This project fetches data from the "Rick and Morty" public API for characters that are:

    Species: Human
    Status: Alive
    Origin: Earth

It then stores that data in a CSV file (name, location, image) and exposes a Flask-based REST API with two endpoints:

    `GET /healthcheck` for checking the application's health
    `GET /characters` for retrieving the filtered characters in JSON format

### What Has Been Done

1. Data Extraction and CSV Generation:
        Initially, a script was created to query the "Rick and Morty" API and find all characters who are:
        - Species: Human
        - Status: Alive
        - Origin: Earth

    After retrieving the data, the script generates a CSV file containing each character’s:
        - Name
        - Current Location
        - Image URL

2. RESTful Service Implementation:
        Building on the script, the functionality was turned into a RESTful Flask application, providing:
        - /healthcheck endpoint to verify that the application is up and running.
        - /characters endpoint returning JSON with the filtered character data.

    This allows easy retrieval of the filtered data via standard HTTP requests.

3. Containerization and Documentation:
        A Dockerfile was created to containerize the application. Detailed instructions on how to build and run the container - have been added. The README now guides you through:
        - Building the Docker image.
        - Running the container locally.
        - Verifying the endpoints.

4. Kubernetes Deployment with Minikube:
        To showcase how this can be run in a Kubernetes environment, a set of YAML manifests (Deployment, Service, Ingress) were prepared. The README includes instructions for:
        - Starting Minikube.
        - Applying the Kubernetes manifests.
        - Accessing the application endpoints via Ingress.
    
    5. Helm Deployment
        A Helm chart is also included for a more modular and scalable Kubernetes deployment. This README explains:
        - Installing Helm
        - Deploying the app via Helm
        - Testing the endpoints on Minikube

## 2. Requirements

    - Python 3.9 (for local runs)
    - Flask (for the RESTful API)
    - requests (for API calls)
    - Docker (for building and running the container)
    - Minikube and kubectl (for Kubernetes deployment)
    - Helm (optional) – for Helm-based deployment

## 3. Running Locally

1. Create and Activate a Virtual Environment (Optional):
```sh
    python3 -m venv venv
    source venv/bin/activate
```

2. Install Dependencies:
```sh
    pip install -r requirements.txt
```

3. Run the Application:
```sh
    python app.py
```
The service should start on http://0.0.0.0:5000.
        - Healthcheck: http://localhost:5000/healthcheck
        - Characters: http://localhost:5000/characters

## 4. Building and Running with Docker

1. Build the Docker Image:
```sh
    docker build -t rickmortyapp:latest .
```
2. Run the Container:
```sh
    docker run -p 5000:5000 rickmortyapp:latest
```
Now you can access:
        - http://localhost:5000/healthcheck
        - http://localhost:5000/characters

## 5. Deploying to Kubernetes (Minikube)

1. Start Minikube:
```sh
    minikube start
```
2. Use Minikube’s Docker Daemon (optional if building locally):
```sh
    eval $(minikube docker-env)
    docker build -t rickmortyapp:latest .
```
3. Apply Kubernetes Manifests:
```sh
    kubectl apply -f yamls/deployment.yaml
    kubectl apply -f yamls/servic.yaml
    kubectl apply -f yamls/ingress.yaml
```
4. Check resources:
```sh
    kubectl get pods
    kubectl get svc
    kubectl get ingress
```
4. Access the Application via Ingress:

    - Get the Minikube IP:
```sh
    minikube ip
```
    - Update your /etc/hosts file:
```sh
    <minikube_ip> rickmorty.local
```
Now you can access:
            - http://rickmorty.local/healthcheck
            - http://rickmorty.local/characters

## 6. Deploying with Helm on Minikube

If you prefer to use a Helm chart instead of raw YAML manifests, follow these steps:

### 6.1 Install Helm (If Not Already Installed)

macOS:

```sh
    brew install helm
```

Linux:

```sh
    curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

Windows:

```sh
    winget install kubernetes-helm
```
### 6.2 Start Minikube

```sh
    minikube start
```
### 6.3 Build Docker Image Inside Minikube

If you’re building locally rather than pulling from a registry:
```sh
    eval $(minikube docker-env)
    docker build -t rickmortyapp:latest .
```

### 6.4 Deploy via Helm

Go to the Helm chart directory (or specify its path):
```sh
    cd helm/rickmortyapp
```

Install or Upgrade the Release:
```sh
    helm upgrade --install rickmortyapp . --wait
```
## 📝 Note:
 >   `GET --install` creates a new release if it doesn’t exist.
 >    `GET --wait` ensures Helm waits for Pods to be in a ready state.

Check Resources:
```sh
    kubectl get pods
    kubectl get svc
    kubectl get ingress
```

### 6.5 Testing the Application

If your Service is of type ClusterIP and you have Ingress:

Get the Minikube IP:
```sh 
    minikube ip
```

Add `GET /etc/hosts` entry:
```sh 
sudo sh -c "echo '<MINIKUBE_IP> rickmorty.local' >> /etc/hosts"
```

Curl:
```sh 
    curl http://rickmorty.local/healthcheck
    curl http://rickmorty.local/characters
```

Alternatively, if your Service is NodePort, you can do:
```sh 
    kubectl get svc rickmortyapp-service
```
# Then curl using <node_port> and minikube IP


## Notes

    - The provided endpoints are running on a basic Flask development server. For production, consider using a more robust WSGI server like Gunicorn or uWSGI.
    - The filtered character data is retrieved on-demand from the "Rick and Morty" API, so response times will depend on API latency.
    - If any changes are made to the code or requirements, remember to rebuild the Docker image and redeploy to update the running instance.
