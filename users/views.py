from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = User(**serializer.validated_data)
            user.set_password(serializer.validated_data['password'])
            user.save()

            return Response({"user": user.email, "message": "User created successfully"},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


