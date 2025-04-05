from django.contrib import admin
from .models import*

class ProyektEnjamInline(admin.TabularInline):
    model = ProyektEnjam  
    extra = 1

class IsYazygyInline(admin.TabularInline):
    model = Is_Hasabatlar
    extra = 1

class SuratInline(admin.TabularInline):
    model = Surat
    extra = 1


class TaslamaAdmin(admin.ModelAdmin):
    list_display = ['ady', 'gornusi', 'status', 'baslanan_senesi', 'tamamlanjak_senesi']
    list_filter = ['gornusi', 'status']
    search_fields = ['ady', 'müşderi__ady']
    inlines = [ProyektEnjamInline, IsYazygyInline]

admin.site.register(Taslama, TaslamaAdmin)
admin.site.register(Ulanyjy)
admin.site.register(Enjam)
admin.site.register(Is_Hasabatlar)
admin.site.register(Surat)


admin.site.site_header = "Admin-Dolandyryş Paneli"
admin.site.site_title = "Dolandyryş Paneli"
admin.site.index_title = ""