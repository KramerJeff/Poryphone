from django.contrib import admin
from .models import Trainer, Move, Pokemon, SyncPair, Type, Role, Category, Target, RecruitMethod
# Register your models here.

admin.site.register(Trainer)
admin.site.register(Move)
admin.site.register(Pokemon)
admin.site.register(SyncPair)
admin.site.register(Type)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Target)
admin.site.register(RecruitMethod)