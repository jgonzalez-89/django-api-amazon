from rest_framework import serializers
from .models import Producto
import datetime

def parse_custom_date(date_string):
    if isinstance(date_string, datetime.date):
        return date_string
    try:
        day, month, year = map(int, date_string.split('-'))
        return datetime.date(year, month, day)
    except Exception as e:
        raise serializers.ValidationError(f"Error al analizar la fecha: {e}")

class ProductoSerializer(serializers.ModelSerializer):
    fecha = serializers.CharField(write_only=True)

    class Meta:
        model = Producto
        fields = '__all__'

    def validate_fecha(self, value):
        return parse_custom_date(value)

    def create(self, validated_data):
        fecha = validated_data.pop('fecha')
        validated_data['fecha'] = self.validate_fecha(fecha)
        return super().create(validated_data)