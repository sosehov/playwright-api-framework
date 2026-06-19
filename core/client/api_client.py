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
        try:
            response = self.session.get(url, timeout=30, **kwargs)
            logger.debug(f"Response: {response.status_code}")
            return response
        except requests.exceptions.Timeout:
            logger.error(f"GET {url} timed out")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"GET {url} - connection error")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"GET {url} failed: {e}")
            raise

    def post(self, endpoint: str, json: dict = None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"POST {url} | Payload: {json}")
        try:
            response = self.session.post(url, timeout=30, json=json, **kwargs)
            logger.debug(f"Response: {response.status_code}")
            return response
        except requests.exceptions.Timeout:
            logger.error(f"POST {url} timed out")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"POST {url} - connection error")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"POST {url} failed: {e}")
            raise

    def put(self, endpoint: str, json: dict = None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"PUT {url} | Payload: {json}")
        try:
            response = self.session.put(url, timeout=30, json=json, **kwargs)
            logger.debug(f"Response: {response.status_code}")
            return response
        except requests.exceptions.Timeout:
            logger.error(f"PUT {url} timed out")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"PUT {url} - connection error")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"PUT {url} failed: {e}")
            raise

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"DELETE {url}")
        try:
            response = self.session.delete(url, timeout=30, **kwargs)
            logger.debug(f"Response: {response.status_code}")
            return response
        except requests.exceptions.Timeout:
            logger.error(f"DELETE {url} timed out")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"DELETE {url} - connection error")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"DELETE {url} failed: {e}")
            raise
