from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name


class PurchaseHistory(models.Model):
    # Use product_id instead of id for foreign key
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases', to_field='product_id')  
    company_name = models.CharField(max_length=100)
    units = models.IntegerField()
    amount_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    order_placed_date = models.DateField()

    def __str__(self):
        return f"{self.product.name} - {self.company_name} - {self.order_placed_date}"


class EquipmentInstallation(models.Model):
    type_of_product = models.CharField(max_length=255)
    equipment = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='installations', to_field='product_id')  # Referencing product_id
    company_name = models.CharField(max_length=255)
    units = models.IntegerField()
    installation_location = models.CharField(max_length=255)
    installed_by = models.CharField(max_length=255, null=True, blank=True)
    installation_date = models.DateField()
    additional_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipment.name} installed at {self.installation_location}"
