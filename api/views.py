import json
import time
import redis
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0,
                                   decode_responses=True)


class LinksAPIView(APIView):

    def get(self, request, *args, **kwargs):
        from_time = int(self.request.query_params.get('from'))
        to_time = int(self.request.query_params.get('to'))
        result_list = []
        for now_time in range(from_time, to_time + 1):
            result_list += redis_instance.smembers(str(now_time))
        result_list = sorted(list(set(result_list)))
        return Response({"domains": result_list, "status": "ok"}, status=status.HTTP_200_OK)

    @staticmethod
    def clear_data(data):
        clear_data = []
        for link in data:
            link = link.replace("http://", "")
            link = link.replace("https://", "")
            link = link.replace("www.", "")
            link = link.split('/')[0]
            link = link.split('?')[0]
            clear_data.append(link)
        return clear_data

    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8").replace("'", '"'))
        except Exception as _ex:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        data = data['links']
        clear_data = self.clear_data(data)
        current_time = round(time.time())
        try:
            redis_instance.sadd(current_time, *clear_data)
            return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
        except Exception as _ex:
            return Response({"status": _ex}, status=status.HTTP_400_BAD_REQUEST)
