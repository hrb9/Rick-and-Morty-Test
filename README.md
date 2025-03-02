# Rick and Morty REST App

This project fetches data from the Rick and Morty API and exposes a REST interface. The default filters are:
- Species = "Human"
- Status = "Alive"
- Origin contains the word "Earth"

## Project Structure

- **main.py**  
  A Flask application that provides:
  - `/healthcheck` (returns `{"status": "ok"}`)
  - `/characters` (returns the JSON list of characters)

- **Dockerfile**  
  Defines how to containerize the Flask application.

- **yamls/**  
  Kubernetes manifests:
  - `Deployment.yaml`
  - `Service.yaml`
  - `Ingress.yaml`

- **helm/**  
  Helm chart that includes:
  - `Chart.yaml`
  - `values.yaml`
  - `templates/` with Deployment, Service, and Ingress definitions

- **.github/workflows/main.yaml**  
  A GitHub Actions workflow:
  1. Creates a local Kind cluster.
  2. Builds and loads the Docker image into the cluster.
  3. Deploys the manifests.
  4. Tests the endpoints.

---

## How to Build and Run Locally with Docker

1. **Build the Docker image**:
   ```bash
            docker build -t rick-and-morty-app:latest .
    ```
2. **Run the Docker container**:
   ```bash
        docker run -p 5000:5000 rick-and-morty-app:latest
    ```
3. **Test**:
   ```bash
        Healthcheck: http://localhost:5000/healthcheck
        Characters: http://localhost:5000/characters

    ```

## Kubernetes Deployment (manifests in yamls/)

1. **Make sure you have a running cluster (e.g., via Minikube or Kind).**
2. **Apply the manifests**:
    ```bash
        kubectl apply -f yamls/Deployment.yaml
        kubectl apply -f yamls/Service.yaml
        kubectl apply -f yamls/Ingress.yaml
    ```
3. **Verify pods and services**:
    ```bash
    kubectl get pods
    kubectl get svc
    kubectl get ingress
    ```
4. **Access the service. Example: if using an Ingress with host rick.local, add rick.local to your /etc/hosts pointing to your local cluster IP (or 127.0.0.1 if using port-forward), then open:**:
   ```bash
        Healthcheck: http://localhost:5000/healthcheck
        Characters: http://localhost:5000/characters

    ```
## Helm Deployment

1. **Install (or upgrade) the char**:
    ```bash
        helm install rick ./helm                                                                                            
    ```
2. **Check**:
    ```bash
        kubectl get pods
        kubectl get svc
        kubectl get ingress                                                                                      
    ```    
3. **By default, you can configure the domain/host in helm/values.yaml**
