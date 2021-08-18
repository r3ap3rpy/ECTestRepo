import unittest
import requests

def test_google():
    assert requests.get(url = "https://google.com").status_code == 200

def test_arstechnica():
    assert requests.get(url = "https://arstechnica.com/").status_code == 200

def test_dummypage():
    assert requests.get(url = "https://arstechnica.com/whatever").status_code == 400