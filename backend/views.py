from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect
from .models import PurchaseHistory, Product
from .forms import PurchaseHistoryForm
from django.http import JsonResponse
from .models import PurchaseHistory
from django.shortcuts import render, redirect
from .models import Product, PurchaseHistory
from .forms import PurchaseHistoryForm

def product_list(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, product_id=product_id)
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product_list')

    products = Product.objects.all()  
    total_inventory_amount = 0  

    # Calculate the total inventory amount for each product
    for product in products:
        # Fetch all purchase records for the current product
        purchase_history = PurchaseHistory.objects.filter(product=product)
        
        # Add the value of each record to the total inventory amount
        for record in purchase_history:
            total_inventory_amount += record.units * record.amount_per_unit

    return render(request, 'product_list.html', {
        'products': products, 
        'total_inventory_amount': total_inventory_amount
    })

# View to display details of a specific product
def product_detail(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)  # Get product by product_id
    return render(request, 'product_detail.html', {'product': product})

# View to add a new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Get form data (including image)
        if form.is_valid():
            form.save()  # Save the new product to the database
            return redirect('product_list')  # Redirect to the product list view
    else:
        form = ProductForm()  # Empty form for GET request
    return render(request, 'product_create.html', {'form': form})


def purchase_create(request):
    if request.method == 'POST':
        form = PurchaseHistoryForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            product = form.cleaned_data['product']
            units = form.cleaned_data['units']
            amount_per_unit = form.cleaned_data['amount_per_unit']

            # Check if the product and company combination already exists
            purchase_history = PurchaseHistory.objects.filter(product=product, company_name=company_name).first()

            if purchase_history:
                # If the record exists, update the units and amount per unit
                purchase_history.units += units  # Add new units to the existing ones
                purchase_history.amount_per_unit = amount_per_unit  # Update amount per unit
                purchase_history.save()  # Save the updated record
            else:
                form.save()

            return redirect('purchase_list') 
    else:
        form = PurchaseHistoryForm()

    return render(request, 'purchase_create.html', {'form': form})



def purchase_list(request):
    purchases = PurchaseHistory.objects.all()  # Get all purchase records
    return render(request, 'purchase_list.html', {'purchases': purchases})


def company_autocomplete(request):
    if 'term' in request.GET:
        term = request.GET['term']
        companies = PurchaseHistory.objects.filter(company_name__icontains=term).distinct()
        company_names = [company.company_name for company in companies]
        return JsonResponse(company_names, safe=False)
    return JsonResponse([], safe=False)

from django.shortcuts import render
from .models import PurchaseHistory

def purchase_history(request):
    # Fetch all purchase history records
    purchase_history = PurchaseHistory.objects.all()
    return render(request, 'purchase_history.html', {'purchase_history': purchase_history})

def purchase_history_by_company(request):
    # Group products by company name
    companies = {}
    purchase_history = PurchaseHistory.objects.all()

    for record in purchase_history:
        if record.company_name not in companies:
            companies[record.company_name] = []
        companies[record.company_name].append(record)

    return render(request, 'purchase_history_by_company.html', {'companies': companies})

def purchase_history_by_product_type(request):
    # Group purchases by product type
    product_types = {}
    purchase_history = PurchaseHistory.objects.select_related('product').all()

    for record in purchase_history:
        product_type = record.product.product_type  # Access the product type
        if product_type not in product_types:
            product_types[product_type] = []
        product_types[product_type].append(record)

    return render(request, 'purchase_history_by_product_type.html', {'product_types': product_types})


from django.shortcuts import render, redirect
from .models import EquipmentInstallation, Product, PurchaseHistory
from .forms import EquipmentInstallationForm
from django.contrib import messages
from .forms import EquipmentInstallationForm
from .models import Product, PurchaseHistory

def equipment_installation_list(request):
    installations = EquipmentInstallation.objects.all()  # Fetch all installations
    return render(request, 'equipment_installation_list.html', {'installations': installations})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EquipmentInstallationForm
from .models import Product, PurchaseHistory

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, EquipmentInstallation, PurchaseHistory
from .forms import EquipmentInstallationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, PurchaseHistory, EquipmentInstallation
from .forms import EquipmentInstallationForm
from django.contrib import messages

def out_of_stock_products(request):
    return render('out_of_stock_products.html')

def equipment_installation_create(request):
    if request.method == 'POST':
        # Handle the form submission for selling and installing equipment
        product_id = request.POST.get('product_id')
        units_to_sell = int(request.POST.get('units'))
        installed_by = request.POST.get('installed_by')

        product = get_object_or_404(Product, product_id=product_id)
        purchase_history = PurchaseHistory.objects.filter(product=product, company_name=request.POST.get('company_name')).first()

        if not purchase_history or purchase_history.units < units_to_sell:
            messages.error(request, "Not enough stock available.")
            return redirect('equipment_installation_create')  # Go back if there's an error

        # Create the installation record
        EquipmentInstallation.objects.create(
            type_of_product=product.product_type,
            equipment=product,
            company_name=purchase_history.company_name,
            units=units_to_sell,
            installation_location=request.POST.get('installation_location'),
            installed_by=installed_by,
            installation_date=request.POST.get('installation_date'),
            additional_details=request.POST.get('additional_details')
        )

        # Update the purchase history by subtracting the sold units
        purchase_history.units -= units_to_sell
        purchase_history.save()

        messages.success(request, "Equipment installation and sale successfully recorded.")
        return redirect('equipment_installation_list')  # Redirect to the installation list view

    else:
        # Display products grouped by their product type
        product_types = {}
        purchase_history = PurchaseHistory.objects.select_related('product').all()

        for record in purchase_history:
            product_type = record.product.product_type
            if product_type not in product_types:
                product_types[product_type] = []
            product_types[product_type].append(record)

        return render(request, 'equipment_installation_create.html', {'product_types': product_types})
