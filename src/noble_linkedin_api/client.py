import requests
import logging
from .cookie_repository import CookieRepository
from bs4 import BeautifulSoup
import json

logger = logging.getLogger(__name__)


class ChallengeException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


class Client(object):
    """
    Class to act as a client for the Linkedin API.
    """

    # Settings for general Linkedin API calls
    LINKEDIN_BASE_URL = "https://www.linkedin.com"
    API_BASE_URL = f"{LINKEDIN_BASE_URL}/voyager/api"
    NAVIGATOR_BASE_URL = f"{LINKEDIN_BASE_URL}/sales-api"
    # REQUEST_HEADERS = {
    #     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.33 Safari/537.36",
    #     # "accept": "application/vnd.linkedin.normalized+json+2.1",
    #     "accept-language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    #     "x-li-lang": "en_US",
    #     "x-restli-protocol-version": "2.0.0",
    #     # "x-li-track": '{"clientVersion":"1.2.6216","osName":"web","timezoneOffset":10,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    # }

    # AUTH_REQUEST_HEADERS = {
    #     "X-Li-User-Agent": "LIAuthLibrary:3.2.4 \
    #                         com.linkedin.LinkedIn:8.8.1 \
    #                         iPhone:8.3",
    #     "User-Agent": "LinkedIn/8.8.1 CFNetwork/711.3.18 Darwin/14.0.0",
    #     "X-User-Language": "en",
    #     "X-User-Locale": "en_US",
    #     "Accept-Language": "en-us",
    # }

    def __init__(
        self, headers, proxies, cookies, *, debug=False, refresh_cookies=False, cookies_dir=None
    ):
        self.session = requests.session()
        self.session.proxies.update(proxies)
        self.session.headers.update(headers)
        self.proxies = proxies
        self.logger = logger
        self.metadata = {}
        self._use_cookie_cache = not refresh_cookies
        self._cookie_repository = CookieRepository(cookies_dir=cookies_dir)
        self.set_session_cookies(cookies)

        logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)

    def _request_session_cookies(self):
        """
        Return a new set of session cookies as given by Linkedin.
        """
        self.logger.debug("Requesting new cookies.")

        res = requests.get(
            f"{Client.LINKEDIN_BASE_URL}/uas/authenticate",
            headers=self.session.headers, #Client.AUTH_REQUEST_HEADERS,
            proxies=self.proxies,
        )
        return res.cookies

    def set_session_cookies(self, cookies):
        """
        Set cookies of the current session and save them to a file named as the username.
        """
        self.session.cookies.update(cookies)


    @property
    def cookies(self):
        return self.session.cookies

    def authenticate(self, username, password):
        if self._use_cookie_cache:
            self.logger.debug("Attempting to use cached cookies")
            cookies = self._cookie_repository.get(username)
            if cookies:
                self.logger.debug("Using cached cookies")
                self.set_session_cookies(cookies)
                self._fetch_metadata()
                return

        self._do_authentication_request(username, password)
        self._fetch_metadata()

    def _fetch_metadata(self):
        """
        Get metadata about the "instance" of the LinkedIn application for the signed in user.

        Store this data in self.metadata
        """
        res = requests.get(
            f"{Client.LINKEDIN_BASE_URL}",
            cookies=self.session.cookies,
            headers=self.session.headers,
            proxies=self.proxies,
        )

        soup = BeautifulSoup(res.text, "lxml")

        clientApplicationInstanceRaw = soup.find(
            "meta", attrs={"name": "applicationInstance"}
        )
        if clientApplicationInstanceRaw:
            clientApplicationInstanceRaw = (
                clientApplicationInstanceRaw.attrs.get("content") or {}
            )
            clientApplicationInstance = json.loads(clientApplicationInstanceRaw)
            self.metadata["clientApplicationInstance"] = clientApplicationInstance

        clientPageInstanceIdRaw = soup.find(
            "meta", attrs={"name": "clientPageInstanceId"}
        )
        if clientPageInstanceIdRaw:
            clientPageInstanceId = clientPageInstanceIdRaw.attrs.get("content") or {}
            self.metadata["clientPageInstanceId"] = clientPageInstanceId

    def _do_authentication_request(self, username, password):
        """
        Authenticate with Linkedin.

        Return a session object that is authenticated.
        """
        self.set_session_cookies(self._request_session_cookies())

        payload = {
            "session_key": username,
            "session_password": password,
            "JSESSIONID": self.session.cookies["JSESSIONID"],
        }

        res = requests.post(
            f"{Client.LINKEDIN_BASE_URL}/uas/authenticate",
            data=payload,
            cookies=self.session.cookies,
            headers=self.session.headers, #Client.AUTH_REQUEST_HEADERS,
            proxies=self.proxies,
        )

        data = res.json()

        if data and data["login_result"] != "PASS":
            raise ChallengeException(data["login_result"])

        if res.status_code == 401:
            raise UnauthorizedException()

        if res.status_code != 200:
            raise Exception()

        self._set_session_cookies(res.cookies)
        self._cookie_repository.save(res.cookies, username)
