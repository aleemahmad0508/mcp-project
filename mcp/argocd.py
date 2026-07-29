import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read values from .env
ARGOCD_URL = os.getenv("ARGOCD_URL")
ARGOCD_TOKEN = os.getenv("ARGOCD_TOKEN")

def get_application_status(app_name: str):
    """
    Return the status of an ArgoCD application.
    """

    url = f"{ARGOCD_URL}/api/v1/applications/{app_name}"

    response = requests.get(url)

    return response.json()