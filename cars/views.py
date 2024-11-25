from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer

# Create your views here.

class CarListCreateAPIView(APIView):
    def get(self, request):
        cars= Car.objects.all()
        serializer= CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer= CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, Update, Delete Cars
class CarDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return None

    def get(self, request, pk):
        car = self.get_object(pk)
        if not car:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk):
        car = self.get_object(pk)
        if not car:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car = self.get_object(pk)
        if not car:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response({"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT)            