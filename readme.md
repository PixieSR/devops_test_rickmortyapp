# Rick and Morty Application
## 1. Overview

This project fetches data from the "Rick and Morty" public API, filtering characters based on specific criteria, and then exposes this information through a RESTful API. Additionally, the entire setup has been packaged into a Docker image and deployed to a Kubernetes cluster using Minikube for demonstration purposes.

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

## 2. Requirements

    - Python 3.9 (for local runs)
    - Flask (for the RESTful API)
    - requests (for API calls)
    - Docker (for building and running the container)
    - Minikube and kubectl (for Kubernetes deployment)

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

## Notes

    - The provided endpoints are running on a basic Flask development server. For production, consider using a more robust WSGI server like Gunicorn or uWSGI.
    - The filtered character data is retrieved on-demand from the "Rick and Morty" API, so response times will depend on API latency.
    - If any changes are made to the code or requirements, remember to rebuild the Docker image and redeploy to update the running instance.