from rest_framework import serializers
from .models import ReportData

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportData
        fields = ['report_type', 'report_date', 'report_data']
