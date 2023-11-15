from django.contrib import admin

from book.models import Review, Ticket, UserFollows


admin.site.register(Review)
admin.site.register(Ticket)
admin.site.register(UserFollows)
