try:
    # python2
    from urlparse import urlparse
except Exception:
    # python3
    from urllib.parse import urlparse

from consolemenu.validators.base import BaseValidator


class UrlValidator(BaseValidator):

    def __init__(self, url):
        """
        URL Validator class

        :param url: URL String to check if is a valid url
        """
        super(UrlValidator, self).__init__(input_string=url)

    @property
    def url(self):
        return self.input_string

    def validate(self):
        """
        Validate url

        :return: True if match / False otherwise
        """
        parsed_url = urlparse(url=self.url)
        return parsed_url.scheme and parsed_url.netloc
