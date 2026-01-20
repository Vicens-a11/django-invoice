from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    """
    Name        : Customer model definition
    Description : Représente un client du système de facturation.
    Author      : kenmatiovicens@icloud.com
    Date        : 20-01-2026
    Version     : 1.0
    Purpose     : Stocker toutes les informations personnelles et de contact des clients.
    Usage       : Utilisé pour créer, consulter et gérer les clients dans le système.
    
    Fields      :
        - name        : CharField, nom complet du client
        - email       : EmailField, adresse email
        - phone       : CharField, numéro de téléphone
        - address     : TextField, adresse postale
        - sex         : CharField, sexe du client ('M' ou 'F')
        - age         : CharField, âge du client
        - city        : CharField, ville de résidence
        - zip_code    : CharField, code postal
        - created_date: DateTimeField, date de création automatique
        - save_by     : ForeignKey vers User, indique qui a créé l'entrée

    Notes       :
        - Les clients sont ordonnés par date de création décroissante.
        - Les utilisateurs qui créent les clients sont protégés contre la suppression
          grâce à on_delete=models.PROTECT.
        - Le champ `sex` utilise le tuple `SEX_TYPES` pour les choix possibles.
    """
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    
    name = models.CharField(max_length=100)
    
    email = models.EmailField()
    
    phone = models.CharField(max_length=132)
    
    address = models.TextField(max_length=64)
    
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    
    age = models.CharField(max_length=12)
    
    city = models.CharField(max_length=32)
    
    zip_code = models.CharField(max_length=16)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Customer" # 
        verbose_name_plural = "Customers"
        ordering = ['-created_date']  
         
    def __str__(self):
        return self.name 

class Invoice(models.Model):
    """
    Name        : Invoice
    Description : Modèle représentant une facture émise à un client.
    Author      : kenmatiovicens@icloud.com
    Date        : 20-01-2026
    Version     : 1.0
    Purpose     : Stocker et gérer les informations des factures émises aux clients.

    Fields      :
        - customer          : ForeignKey(Customer) - Client associé à la facture (relation many-to-one, protégée contre suppression).
        - save_by           : ForeignKey(User) - Utilisateur ayant créé la facture.
        - invoice_date_time : DateTimeField(auto_now_add=True) - Date et heure de création de la facture.
        - last_updated_date : DateTimeField(auto_now=True, null=True) - Date de dernière mise à jour automatique.
        - total             : DecimalField(max_digits=10, decimal_places=2) - Montant total de la facture.
        - paid              : BooleanField(default=False) - Statut de paiement de la facture.
        - invoice_type      : CharField(max_length=1, choices=INVOICE_TYPE) - Type de facture : reçu (R), proforma (P), facture (F).
        - comments          : TextField(max_length=1000, null=True, blank=True) - Commentaires optionnels.

    Choices     :
        - INVOICE_TYPE : Tuple définissant les types de facture possibles ('R', 'P', 'F').

    Notes       :
        - Les factures sont liées à un client unique mais un client peut avoir plusieurs factures.
        - `save_by` protège l’utilisateur lié contre la suppression.
        - `invoice_date_time` et `last_updated_date` sont automatiquement gérés par Django.
        - `comments` est optionnel et peut être laissé vide.
    """
    
    INVOICE_TYPE = (
        ('R', 'RECU'),
        ('P', 'PROFORMA FACTURE'),
        ('F', 'FACTURE'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
   
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    
    invoice_date_time = models.DateTimeField(auto_now_add=True)
    
    last_updated_date = models.DateTimeField(null=True, auto_now=True)
    
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    paid = models.BooleanField(default=False)
    
    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
    
    comments = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return f"{self.customer.name} {self.invoice_date_time}"
    
    @property
    def get_total(self):
        articles = self.article_set.all()
        total = sum(article.get_total for article in articles)
        return total
        


class Article(models.Model):
    """
    Name        : Article
    Description : Modèle représentant un article ou un produit facturé dans une facture.
    Author      : kenmatiovicens@icloud.com
    Date        : 20-01-2026
    Version     : 1.0
    Purpose     : Stocker et gérer les informations des articles ou produits facturés.

    Fields      :
        - name              : CharField(max_length=100) - Nom de l'article.
        - description       : TextField(max_length=500, null=True, blank=True) - Description optionnelle de l'article.
        - price             : DecimalField(max_digits=10, decimal_places=2) - Prix unitaire de l'article.
        - quantity          : IntegerField(default=1) - Quantité de l'article dans une facture.
        - created_date      : DateTimeField(auto_now_add=True) - Date de création de l'article.

    Notes       :
        - Les articles sont indépendants des factures et peuvent être réutilisés dans plusieurs factures.
        - `description` est optionnelle et peut être laissée vide.
        - `quantity` est initialisée à 1 par défaut.
        - `created_date` est automatiquement gérée par Django.  
    """
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    
    quantity = models.IntegerField(default=1)
    
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    
    @property
    def get_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.name