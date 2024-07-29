from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, SensorSerializer
from measurement.serializers import MeasurementsSerializer, MeasurementSerializer


class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class AddMeasurementAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementsSerializer


class SensorDetailsListAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
