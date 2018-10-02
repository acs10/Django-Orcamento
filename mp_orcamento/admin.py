from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    pass
