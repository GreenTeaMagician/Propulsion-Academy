from django.shortcuts import redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from project.api.serializers import RegistrationValidationSerializer, RegistrationSerializer, PasswordResetSerializer, \
    PasswordResetValidationSerializer


class RegistrationView(GenericAPIView):
    permission_classes = []
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = serializer.register_user(
            email=serializer.validated_data.get('email'),
        )
        return Response(self.get_serializer(new_user).data)


class RegistrationValidationView(GenericAPIView):
    permission_classes = []
    serializer_class = RegistrationValidationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=Exception)
        user = serializer.save(
            serializer.validated_data,
        )
        return Response(self.get_serializer(user).data)


class PasswordResetView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_pwReset_email(
            user=serializer.validated_data.get('email'),
        )
        return redirect('validation/') and Response('Email sent!')


class PasswordResetValidationView(GenericAPIView):
    permission_classes = []
    serializer_class = PasswordResetValidationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=Exception)
        user = serializer.save(
            serializer.validated_data,
        )
        return Response(self.get_serializer(user).data)
