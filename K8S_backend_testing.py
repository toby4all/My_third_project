import requests

try:
    # Read the Minikube service URL from the file
    with open('k8s_url.txt', 'r') as f:
        service_url = f.read().strip()

    # Test the deployable app with a GET method
    url = f"{service_url}/users/1"
    response = requests.get(url)

    # Check the HTTP response status code for success
    if response.status_code == 200:
        print("Success! Response content:")
        print(response.content.decode('utf-8'))
    else:
        print(f"Error: Unexpected HTTP status code {response.status_code}")
        print(f"Response content: {response.content.decode('utf-8')}")

except FileNotFoundError:
    print("Error: Could not find file 'k8s_url.txt'.")
except requests.exceptions.RequestException as e:
    print(f"Error: Could not connect to Minikube service.")
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")


