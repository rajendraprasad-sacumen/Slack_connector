import requests
import logging
import pytest
from src.slack_api import SlackAPI,Slack_api # Ensure SlackAPI is in slack_api.py
from run import Slack_api
from typing import Any
from tests.mocks.functions import mock_get_conversations,mock_list_conversation_fail

from configparser import ConfigParser
config=ConfigParser()
config.read("config/slack_connector.cfg")

Token = config["credentials"]["slack_api_token"]
# TOKEN = "slack_api_token"
import os
TOKEN = os.getenv("SLACK_API_TOKEN")

def test_get_conversations_success():
    """
    Test the get_conversations method with a valid token.
    """
    slack_api = SlackAPI(TOKEN)
    response = slack_api.get_conversations()
    assert response is not None, "Response should not be None."
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert isinstance(data, dict), "Response data should be a dictionary."
    assert data["ok"], "Response 'ok' field should be True."
    assert "channels" in data, "Response should contain 'channels' key."

def test_get_users_success():
    """
    Test the get_users method with a valid token.
    """
    slack_api = SlackAPI(TOKEN)
    response = slack_api.get_users()
    assert response is not None, "Response should not be None."
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert isinstance(data, dict), "Response data should be a dictionary."
    assert data["ok"], "Response 'ok' field should be True."
    assert "members" in data, "Response should contain 'members' key."

def test_get_files_success():
    """testing the get_files with a valid token"""
    slack_api=SlackAPI(TOKEN)
    response=slack_api.get_files()
    assert response is not None,"Response should not be None"
    assert response.status_code==200, f"Expected status code 200, got {response.status_code}"


def test_get_user_information_success():
    """testing the get_files with a valid token"""
    slack_api=SlackAPI(TOKEN)
    response=slack_api.get_users_info()
    assert response is not None,"Response should not be None"
    assert response.status_code==200, f"Expected status code 200, got {response.status_code}"

def test_get_conversations_invalid_token():
    """
    Test the get_conversations method with an invalid token.
    """
    invalid_token = "invalid-token"
    slack_api = SlackAPI(invalid_token)
    response = slack_api.get_conversations()
    assert response is not None, "Response should not be None."
    data = response.json()
    assert not data["ok"], "Response 'ok' field should be False for invalid token."
    assert "error" in data, "Response should contain 'error' key."

def test_get_users_invalid_token():
    """
    Test the get_users method with an invalid token.
    """
    invalid_token = "invalid-token"
    slack_api = SlackAPI(invalid_token)
    response = slack_api.get_users()
    assert response is not None, "Response should not be None."
    data = response.json()
    assert not data["ok"], "Response 'ok' field should be False for invalid token."
    assert "error" in data, "Response should contain 'error' key."

def test_get_conversations_http_400():
    """
    Simulate an HTTP 400 Bad Request for get_conversations.
    """
    invalid_token = "invalid-token"
    slack_api = SlackAPI(invalid_token)
    response = slack_api.get_conversations()
    assert response is not None, "Response should not be None."
    data = response.json()
    assert "error" in data, "Expected error in response."
    assert data["error"] == "invalid_auth", "Expected 'invalid_auth' error for invalid token."

def test_get_users_http_400():
    """
    Simulate an HTTP 400 Bad Request for get_users.
    """
    invalid_token = "invalid-token"
    slack_api = SlackAPI(invalid_token)
    response = slack_api.get_users()
    assert response is not None, "Response should not be None."
    data = response.json()
    assert "error" in data, "Expected error in response."
    assert data["error"] == "invalid_auth", "Expected 'invalid_auth' error for invalid token."


def test_get_converstion_success_mocker(mocker:Any):
    """_summary_
    Args:
        mocker (Any): _description_
    """
    mocker.patch("requests.get",mock_get_conversations)
    response=Slack_api.get_conversations()
    data=response.json()
    assert response.status_code==200
    assert data["ok"]=="true"

def test_get_converstion_failure_mocker(mocker:Any):
    """_summary_
    Args:
        mocker (Any): _description_
    """
    mocker.patch("requests.get",mock_list_conversation_fail)
    response=Slack_api.get_users()
    data=response.json()
    assert response.status_code==404
    assert data["error"]=="Invalid authorization"

@pytest.mark.vcr()
def test_get_conversation_vcr():
    """_summary_
    """
    response=Slack_api.get_conversations()
    assert response.status_code==200


@pytest.mark.vcr()
def test_get_user_vcr():
    """_summary_
    """
    response=Slack_api.get_users()
    assert response.status_code==200