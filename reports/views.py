from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ReportData
from .serializers import ReportSerializer

class ReportAPIView(APIView):
    def get(self, request, format=None):
        # Get all reports from database
        reports = ReportData.objects.all()

        # Serialize reports data
        serializer = ReportSerializer(reports, many=True)

        # Return serialized report data as a response
        return Response(serializer.data)

    def post(self, request, format=None):
        # Deserialize request data
        serializer = ReportSerializer(data=request.data)

        # Validate request data
        if serializer.is_valid():
            # Save new report to database
            serializer.save()

            # Return serialized report data as a response
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return error response if request data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
