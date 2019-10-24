from rest_framework import generics
from .models import InstallationRequest
from .serializer import InstallationRequestSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class InstallationRequestListView(APIView):
    """Get all installation requests or create a new one"""

    def get(self, request, format=None):
        installationRequests = InstallationRequest.objects.all()
        serializer = InstallationRequestSerializer(installationRequests, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = InstallationRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class InstallationRequestDetailsView(APIView):
    """
    Retrieve or update a InstallationRequest instance.
    """
    def get_object(self, pk):
        try:
            return InstallationRequest.objects.get(pk=pk)
        except InstallationRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        installationRequests = self.get_object(pk)
        serializer = InstallationRequestSerializer(installationRequests)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        installationRequests = self.get_object(pk)
        serializer = InstallationRequestSerializer(installationRequests, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





