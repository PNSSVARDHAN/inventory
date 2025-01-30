from django import forms
from .models import Product, PurchaseHistory, EquipmentInstallation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'product_type']  # Fields to display in the form
        widgets = {
            'product_id': forms.TextInput(attrs={'style': 'width: 600px; height: 35px; display: block; margin: 5px auto;', 'label': 'Product ID'}),
            'name': forms.TextInput(attrs={'style': 'width: 600px; height: 35px; display: block; margin: 5px auto;', 'label': 'Product Name'}),
            'product_type': forms.TextInput(attrs={'style': 'width: 600px; height: 35px; display: block; margin: 5px auto;', 'label': 'Product Type'}),
        }


class PurchaseHistoryForm(forms.ModelForm):
    class Meta:
        model = PurchaseHistory
        fields = ['company_name', 'units', 'amount_per_unit', 'order_placed_date', 'product']

    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=True)
    company_name = forms.CharField(max_length=255, required=True)



class EquipmentInstallationForm(forms.ModelForm):
    type_of_product = forms.ChoiceField(
        choices=[('', 'Select')], 
        required=True, 
        widget=forms.Select(attrs={'style': 'height: 35px; width: 800px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;'})
    )
    equipment = forms.ChoiceField(
        choices=[], 
        required=True, 
        widget=forms.Select(attrs={'style': 'width: 800px; height: 35px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;'})
    )
    company_name = forms.ChoiceField(
        choices=[], 
        required=True, 
        label="Company Name", 
        widget=forms.Select(attrs={'style': 'width: 800px; height: 35px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;'})
    )

    class Meta: 
        model = EquipmentInstallation
        fields = [
            'type_of_product',
            'equipment',
            'company_name',
            'units',
            'installation_location',
            'installed_by',
            'installation_date',
            'additional_details',
        ]
        widgets = {
            'units': forms.TextInput(attrs={'style': 'width: 800px; height: 35px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;'}),
            'installation_location': forms.TextInput(attrs={'style': 'width: 800px; height: 35px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;'}),
            'installed_by': forms.TextInput(attrs={'style': 'width: 800px; height: 35px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;'}),
            'installation_date': forms.DateInput(attrs={'style': 'width: 800px; height: 35px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;', 'type': 'date'}),
            'additional_details': forms.Textarea(attrs={'style': 'width: 800px; height: 35px; display: block; margin-top: 5px; margin-left: auto; margin-right: auto;'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Populate the type_of_product with distinct product types from Product model
        product_types = Product.objects.values_list('product_type', flat=True).distinct()
        self.fields['type_of_product'].choices = [(ptype, ptype) for ptype in product_types]
        
        # Populate the equipment field with products and display the name
        products = Product.objects.all()
        self.fields['equipment'].choices = [(product.product_id, product.name) for product in products]
        
        # Populate the company_name field with distinct company names from PurchaseHistory model
        company_names = PurchaseHistory.objects.values_list('company_name', flat=True).distinct()
        self.fields['company_name'].choices = [(company, company) for company in company_names]
    
    def clean_equipment(self):
        # Convert the product_id to a Product instance
        try:
            product = Product.objects.get(product_id=self.cleaned_data['equipment'])
        except Product.DoesNotExist:
            raise forms.ValidationError("Invalid product ID.")
        return product
