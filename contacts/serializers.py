from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact

        fields = ['country_code', 'id', 'first_name', 'last_name', 'phone_number',
                  'contact_picture', 'is_favorite'
                  ]
