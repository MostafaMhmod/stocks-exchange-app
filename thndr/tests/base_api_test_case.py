class BaseAPITestCase(object):

    def send_request(self, request_method, *args, **kwargs):
        request_func = getattr(self.client, request_method)
        status_code = None

        if "status_code" in kwargs:
            status_code = kwargs.pop("status_code")

        self.response = request_func(*args, **kwargs)

        if status_code:
            self.assertEqual(status_code, self.response.status_code)

        return self.response

    def post(self, *args, **kwargs):
        return self.send_request("post", *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.send_request("get", *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.send_request("put", *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.send_request("patch", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.send_request("delete", *args, **kwargs)
