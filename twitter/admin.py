from django.contrib import admin
from.models import posts,like_button,follow_button,comment
# Register your models here.
admin.site.register(posts)
admin.site.register(like_button)
admin.site.register(follow_button)
admin.site.register(comment)