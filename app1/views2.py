from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from . serializers import CustomUserSerializer

User = get_user_model()
# verfiying my send an email to user after registration
class UserRegistrationView(generics.CreateAPIView):
    serializer_class =CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate verification link
        current_site = get_current_site(request)
        relative_link = reverse('user-verification', kwargs={'pk': user.pk})
        absolute_url = f"http://{current_site.domain}{relative_link}"

        # Send verification email
        send_mail(
            subject='Verify Your Email',
            message=f'Please click the following link to verify your email: {absolute_url}',
            from_email=settings.EMAIL_HOST_USER ,
            recipient_list=[user.email],
        )

        return Response({'detail': 'Verification email sent'}, status=status.HTTP_201_CREATED)


class UserVerificationView(generics.UpdateAPIView):
    queryset = User.objects.all()
    http_method_names = ['patch']
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({'detail': 'Email verified'}, status=status.HTTP_200_OK)
