import requests

try:
    # Read the Minikube service URL from the file
    with open('k8s_url.txt', 'r') as f:
        service_url = f.read().strip()

    # Test the deployable app with a GET method
    url = f"{service_url}/users/1"
    response = requests.get(url)

    # Print the response content
    print(response.content)

except FileNotFoundError:
    print("Error: Could not find file 'k8s_url.txt'.")
except requests.exceptions.RequestException as e:
    print("Error: Could not connect to Minikube service.")
    print(e)

