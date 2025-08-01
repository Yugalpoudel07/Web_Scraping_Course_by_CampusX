# requests_tutorial.py
# A Python script demonstrating the use of the requests library for HTTP requests
# Covers GET, POST, PUT, DELETE methods, headers, and error handling with public APIs

import requests
import json

# Helper function to get response data format
def get_data_format(rcvd_response):
    """Extract and print the response data format from Content-Type header."""
    try:
        json_response = rcvd_response.json()
        data_format = json_response['headers']['Content-Type'].split("/")[-1]
        print(f"Response data format: {data_format}")
    except (KeyError, ValueError) as e:
        print(f"Error extracting data format: {e}")

def check_requests_version():
    """Print the version of the requests library."""
    print(f"Requests library version: {requests.__version__}")

def github_api_get():
    """Send a GET request to GitHub API and display response details."""
    uri = 'https://api.github.com'
    response = requests.get(uri)
    print(f"\nGitHub API GET Request:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Content (first 500 chars): {response.content[:500]}")
    if response.status_code == 200:
        print("Successful GET request!")
    else:
        print("Unsuccessful GET request!")

def github_repo_search():
    """Search GitHub repositories for 'requests' in Python using query parameters."""
    uri = 'https://api.github.com/search/repositories'
    params = {"q": "requests+language:python"}
    response = requests.get(uri, params=params)
    print(f"\nGitHub Repository Search:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Content (first 500 chars): {response.content[:500]}")
    if response.status_code == 200:
        print("Successful search request!")
    else:
        print("Unsuccessful search request!")

def httpbin_post_form():
    """Send a POST request with form data to httpbin.org."""
    uri = 'https://httpbin.org/post'
    data = {'username': 'bruce', 'password': 'bruce123'}
    response = requests.post(uri, data=data)
    print(f"\nPOST Request (Form Data):")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    get_data_format(response)
    if response.status_code == 200:
        print("Successful POST request!")
    else:
        print("Unsuccessful POST request!")

def httpbin_post_json():
    """Send a POST request with JSON data to httpbin.org."""
    uri = 'https://httpbin.org/post'
    data = {'username': 'bruce', 'password': 'bruce123'}
    response = requests.post(uri, json=data)
    print(f"\nPOST Request (JSON Data):")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    get_data_format(response)
    if response.status_code == 200:
        print("Successful POST request!")
    else:
        print("Unsuccessful POST request!")

def httpbin_put():
    """Send a PUT request to update data on httpbin.org."""
    uri = 'https://httpbin.org/put'
    data = {"param1": "value1"}
    response = requests.put(uri, data=data)
    print(f"\nPUT Request:")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    if response.status_code == 200:
        print("Successful PUT request!")
    else:
        print("Unsuccessful PUT request!")

def httpbin_delete():
    """Send a DELETE request to httpbin.org."""
    uri = 'https://httpbin.org/delete'
    response = requests.delete(uri)
    print(f"\nDELETE Request:")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    if response.status_code == 200:
        print("Successful DELETE request!")
    else:
        print("Unsuccessful DELETE request!")

def httpbin_headers():
    """Send a GET request with custom headers to httpbin.org."""
    uri = 'https://httpbin.org/headers'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
        'Content-Type': 'application/json',
        'X-Custom-Header': 'CustomValue',
    }
    response = requests.get(uri, headers=headers)
    print(f"\nHeaders Request:")
    print(f"Status Code: {response.status_code}")
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header:<30}: {value}")
    print("\nRequest Headers (from response):")
    for header, value in response.json()['headers'].items():
        print(f"{header:<20}: {value}")
    if response.status_code == 200:
        print("Successful headers request!")
    else:
        print("Unsuccessful headers request!")

def github_response_object():
    """Explore response object attributes from a GitHub API GET request."""
    uri = 'https://api.github.com'
    response = requests.get(uri)
    print(f"\nGitHub Response Object Exploration:")
    print(f"Status Code: {response.status_code}")
    print(f"Text (first 100 chars): {response.text[:100]}")
    print(f"Content (first 100 chars): {response.content[:100]}")
    print("Headers:")
    for header, value in response.headers.items():
        print(f"{header:<30}: {value}")
    print(f"JSON Response: {response.json()}")
    if response.status_code == 200:
        print("Successful response object request!")
    else:
        print("Unsuccessful response object request!")

def jsonplaceholder_get_posts():
    """Retrieve posts from JSONPlaceholder API with error handling."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    else:
        print(f"\nJSONPlaceholder GET Posts:")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Successful GET request!")
            posts = response.json()
            for i in range(3):
                print(f"\nPost {i + 1}:")
                print(posts[i])
        else:
            print("Unsuccessful GET request!")

def jsonplaceholder_post():
    """Submit a new post to JSONPlaceholder API with error handling."""
    url = "https://jsonplaceholder.typicode.com/posts"
    new_post = {
        "title": "Sample Post",
        "body": "This is a sample post",
        "userId": 101
    }
    try:
        response = requests.post(url, json=new_post)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    else:
        print(f"\nJSONPlaceholder POST Request:")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 201:
            print("Successful POST request!")
            post = response.json()
            print("\nPost:")
            print(post)
        else:
            print("Unsuccessful POST request!")

def main():
    """Main function to run all API request demonstrations."""
    print("Starting Requests Library Tutorial\n" + "="*40)
    
    check_requests_version()
    github_api_get()
    github_repo_search()
    httpbin_post_form()
    httpbin_post_json()
    httpbin_put()
    httpbin_delete()
    httpbin_headers()
    github_response_object()
    jsonplaceholder_get_posts()
    jsonplaceholder_post()
    
    print("\n" + "="*40 + "\nTutorial Completed!")

if __name__ == "__main__":
    main()