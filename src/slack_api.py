import requests
import json
import logging

logging.basicConfig(filename='slack_api.log',
    level=logging.INFO,filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s')

class SlackAPI:
    def __init__(self, token):
        self.base_url = "https://slack.com/api/"
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_conversations(self):
        """Implementing method for Fetching Conversations List"""
        try:
            url = f"{self.base_url}conversations.list"
            response = requests.get(url, headers=self.headers)
            # response.raise_for_status()
            
            # Ensure the response contains valid JSON
            data = response.json()
            formatted_data = json.dumps(data, indent=4)
            logging.info(f"Conversations List: {formatted_data}")
            # return formatted_data
            return response

        except Exception as e:
            # Log the exception and return a generic message
            logging.error(f"Error fetching conversations: {e}")
            return None

    def get_users(self):
        """Implementing method for Fetching Users List"""
        try:
            url = f"{self.base_url}users.list"
            response = requests.get(url, headers=self.headers)
            # response.raise_for_status()
            
            # Ensure the response contains valid JSON
            data = response.json()
            formatted_data = json.dumps(data, indent=2)
            logging.info(f"Users List: {formatted_data}")
            # return formatted_data
            return response

        except Exception as e:
            # Log the exception and return a generic message
            logging.error(f"Error fetching users: {e}")
            return None
    def get_files(self):
        """Implementing method for Fetching files List"""
        try:
            url = f"{self.base_url}files.list"
            response = requests.get(url, headers=self.headers)
            # response.raise_for_status()
            
            # Ensure the response contains valid JSON
            data = response.json()
            formatted_data = json.dumps(data, indent=2)
            logging.info(f"files List: {formatted_data}")
            # return formatted_data
            return response

        except Exception as e:
            # Log the exception and return a generic message
            logging.error(f"Error fetching files: {e}")
            return None
    def get_users_info(self):
        """Implementing method for Fetching Users information List"""
        try:
            params={"user":"U086Z9CEJJ2"}
            url = f"{self.base_url}users.info"
            response = requests.get(url, headers=self.headers,params=params)
            # response.raise_for_status()
            
            # Ensure the response contains valid JSON
            data = response.json()
            formatted_data = json.dumps(data, indent=2)
            logging.info(f"Users information: {formatted_data}")
            # return formatted_data
            return response

        except Exception as e:
            # Log the exception and return a generic message
            logging.error(f"Error fetching users information: {e}")
            return None
        

import os
slack_token = os.getenv("SLACK_API_TOKEN")
# Initialize the SlackAPI class
Slack_api = SlackAPI(slack_token)

# Slack_api.get_conversations()
# Slack_api.get_users()
# Slack_api.get_files()
# Slack_api.get_users_info()
