import json

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from . import Worker


class SyncData(APIView):

    def post(self, request):
        Worker.add_sync(json.loads(request.data))
        return Response({}, status=200)
