import logging

logger = logging.getLogger(__name__)


class DciRocks:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # before
        print(dir(request))
        print("Hello before response")
        logger.info("Hello class, you are awesome, don't give up!")
        response = self.get_response(request)
        print("Hello after response")

        # after

        return response
