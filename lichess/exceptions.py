import requests


class ApiException(Exception):
    """
    This class represents a base Exception thrown when a call to the Lichess API fails.
    In addition to an informative message, it has a `function_name` and a `result` attribute, which respectively
    contain the name of the failed function and the returned result that made the function to be considered  as
    failed.
    """

    def __init__(self, message: str, function_name: str, result: requests.Response):
        super(ApiException, self).__init__(f"A request to the Lichess API was unsuccessful. {message}")
        self.function_name = function_name
        self.result = result


class ApiHTTPException(ApiException):
    """
    This class represents an Exception thrown when a call to the
    Lichess API server returns HTTP code that is not 200.
    """

    def __init__(self, function_name: str, result: requests.Response):
        status_code = result.status_code
        reason = result.reason
        response_body = result.text.encode("utf8")
        message = f"The server returned HTTP {status_code} {reason}. Response body:\n[{response_body}]"

        super(ApiHTTPException, self).__init__(message, function_name, result)


class ApiInvalidJSONException(ApiException):
    """
    This class represents an Exception thrown when a call to the
    Lichess API server returns invalid json.
    """

    def __init__(self, function_name: str, result: requests.Response):
        response_body = result.text.encode("utf8")
        message = f"The server returned an invalid JSON response. Response body:\n[{response_body}]"

        super(ApiInvalidJSONException, self).__init__(message, function_name, result)


class ApiLichessException(ApiException):
    """
    This class represents an Exception thrown when a Lichess API returns error code.
    """

    def __init__(self, function_name: str, result: requests.Response, result_json):
        error_code = result_json["error_code"]
        description = result_json["description"]
        message = f"Error code: {error_code}. Description: {description}"

        super(ApiLichessException, self).__init__(message, function_name, result)

        self.result_json = result_json
        self.error_code = error_code
        self.description = description
