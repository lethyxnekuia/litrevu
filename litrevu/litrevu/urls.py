from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import authentication.views
import book.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', book.views.home, name='home'),
    path('posts/', book.views.posts, name='posts'),
    path('subscriptions/', book.views.subscriptions, name='subscriptions'),
    path('ticketAsking/', book.views.ticket_asking, name='ticketAsking'),
    path('ticketCreation/', book.views.ticket_creation, name='ticketCreation'),
    path(
        'ticketAnswer/<int:pk>', book.views.ticket_answer, name='ticketAnswer'
    ),
    path('followUser/<int:id>', book.views.follow_user, name='followUser'),
    path(
        'unfollowUser/<int:id>', book.views.unfollow_user, name='unfollowUser'
    ),
    path(
        'deleteTicket/<int:id>', book.views.delete_ticket, name='deleteTicket'
    ),
    path(
        'modifyTicket/<int:id>', book.views.modify_ticket, name='modifyTicket'
    ),
    path(
        'deleteReview/<int:id>', book.views.delete_review, name='deleteReview'
    ),
    path(
        'modifyReview/<int:id>', book.views.modify_review, name='modifyReview'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
