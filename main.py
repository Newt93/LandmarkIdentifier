import requests
import json

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Replace YOUR_IMAGE_URL with the URL of the image you want to analyze
image_url = "YOUR_IMAGE_URL"

# Set up the request headers
headers = {
    "Content-Type": "application/json",
}

# Set up the request data
data = """
{
    "requests": [
        {
            "image": {
                "source": {
                    "imageUri": """ + '"' + image_url + '"' + """
                }
            },
            "features": [
                {
                    "type": "LANDMARK_DETECTION"
                }
            ]
        }
    ]
}
"""

# Send the request to the API
response = requests.post(
    "https://vision.googleapis.com/v1/images:annotate?key=" + api_key,
    headers=headers,
    data=data,
)

# Print the response
print(response.text)
