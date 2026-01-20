from django.contrib import admin
from .models import *

# Register your models here.



from django.contrib import admin
from .models import Customer, Invoice

# ------------------------------------------
# Admin configuration for Customer
# ------------------------------------------

# admin.site.register(Customer, AdminCustomer)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage du modèle Customer dans l'admin Django.
    """
    list_display = (
        'name', 
        'email', 
        'phone', 
        'address', 
        'sex', 
        'age', 
        'city', 
        'zip_code', 
        'created_date', 
        'save_by'
    )
    
    list_filter = ('sex', 'city', 'created_date')  # Filtre sur sexe, ville et date de création
    
    search_fields = ('name', 'email', 'phone', 'city')  # Barre de recherche
    
    ordering = ('-created_date',)  # Ordre par date de création décroissante
    
    readonly_fields = ('created_date',)  # Les champs en lecture seule


# class AdminCustomer(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone_number', 'address', 'sex', 'age', 'city', 'zip_code', 'created_date', 'save_by')
    


# ------------------------------------------
# Admin configuration for Invoice
# ------------------------------------------
# admin.site.register(Invoice, AdminInvoice)  
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage du modèle Invoice dans l'admin Django.
    """
    list_display = (
        'customer', 
        'invoice_date_time', 
        'save_by', 
        'paid', 
        'last_updated_date', 
        'invoice_type'
    )
    
    list_filter = ('invoice_type', 'paid', 'invoice_date_time')  # Filtres pratiques
    
    search_fields = ('customer__name',)  # Recherche par nom de client
    
    ordering = ('-invoice_date_time',)
   
    readonly_fields = ('invoice_date_time', 'last_updated_date')

# class AdminInvoice(admin.ModelAdmin):
#     list_display = ('customer', 'invoice_date_time', 'save_by', 'paid', 'last_updated_date', 'invoice_type')   


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage du modèle Article dans l'admin Django.
    """
    list_display = (
        'name', 
        'invoice', 
        'quantity', 
        'unit_price', 
        'total'
    )
    
    # search_fields = ('name', 'invoice__customer__name')  # Recherche par nom d'article et nom de client