from .models import RECICLAQUIapp, Avaliacao
from django.contrib import admin
from .models import todo


@admin.register(RECICLAQUIapp)
class RECICLAQUIAdmin(admin.ModelAdmin):
    list_display = ('título', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('RECICLAQUI', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')


admin.site.register(todo)
# Register your models here.
