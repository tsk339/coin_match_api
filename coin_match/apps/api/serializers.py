from rest_framework import serializers
from .models import *

class ExchangeSerializer(serializers.ModelSerializer):
    admin = serializers.ReadOnlyField(source='admin.username')
    class Meta:
        model= Exchange
        fields=("name", "admin", "buy_fee", "sell_fee", "desc","products", "created_at", "updated_at", "past_trades")
        read_only_fields = ("created_at", "updated_at")

class CryptoCurrencySerializer(serializers.ModelSerializer):
    admin = serializers.ReadOnlyField(source='admin.username')
    class Meta:
        model= CryptoCurrency
        fields=("name", "admin", "abbreviation", "symbol", "supply_limit","founder", "created_at", "updated_at","trade")
        read_only_fields = ("created_at", "updated_at")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields=("cryptocurrencies", "exchanges", "volume", "buy_price", "sell_price", "spot_price", "time_stamp")
        read_only_fields = ("created_at", "updated_at")
