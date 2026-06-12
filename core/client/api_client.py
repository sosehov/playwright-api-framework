import logging
import requests

logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url: str, headers: dict = None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {})

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"GET {url}")
        response = self.session.get(url, **kwargs)
        logger.debug(f"Response: {response.status_code}")
        return response

    def post(self, endpoint: str, json: dict = None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"POST {url} | Payload: {json}")
        response = self.session.post(url, json=json, **kwargs)
        logger.debug(f"Response: {response.status_code}")
        return response

    def put(self, endpoint: str, json: dict = None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"PUT {url} | Payload: {json}")
        response = self.session.put(url, json=json, **kwargs)
        logger.debug(f"Response: {response.status_code}")
        return response

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"DELETE {url}")
        response = self.session.delete(url, **kwargs)
        logger.debug(f"Response: {response.status_code}")
        return response
