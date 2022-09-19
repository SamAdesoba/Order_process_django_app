from unicodedata import category

from django.db import models


# Create your models here.
class Suppliers(models.Model):
    REGIONS = (
        ('SOUTH_SOUTH', 'South South'),
        ('SOUTH_WEST', 'South West'),
        ('SOUTH_EAST', 'South East'),
        ('NORTH_EAST', 'North East'),
        ('NORTH_WEST', 'North West'),
        ('NORTH_CENTRAL', 'North Central')
    )
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    contact_name = models.CharField(max_length=255, verbose_name="Contact Name")
    contact_title = models.CharField(max_length=255, verbose_name="Contact Title")
    address = models.CharField(max_length=255, verbose_name="Address")
    city = models.CharField(max_length=255, verbose_name="City")
    region = models.CharField(max_length=255, verbose_name="Regions", choices=REGIONS)
    postal_code = models.CharField(max_length=255, verbose_name="Postal Code")
    country = models.CharField(max_length=255, verbose_name="Country")
    phone = models.PositiveBigIntegerField()
    fax = models.PositiveSmallIntegerField()
    home_page = models.CharField(max_length=255, verbose_name="Home Page")


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="Category Name")
    description = models.CharField(max_length=255, verbose_name="Description")


class Products(models.Model):
    REORDER_LEVEL = (
        ('HIGH', 'High'),
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium')
    )
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, verbose_name="Product Name")
    quantity_per_unit = models.IntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()
    reorder_level = models.CharField(max_length=255, verbose_name="Reorder Level", choices=REORDER_LEVEL)


class Customers(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    contact_name = models.CharField(max_length=255, verbose_name="Contact Name")
    contact_title = models.CharField(max_length=255, verbose_name="Contact Title")
    address = models.CharField(max_length=255, verbose_name="Address")
    city = models.CharField(max_length=255, verbose_name="City")
    region = models.CharField(max_length=255, verbose_name="Region")
    postal_code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=255, verbose_name="Country")
    phone = models.CharField(max_length=255, verbose_name="Phone")
    fax = models.CharField(max_length=255, verbose_name="Fax")


class Employees(models.Model):
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    title = models.CharField(max_length=25, verbose_name="Title")
    title_of_courtesy = models.CharField(max_length=25, verbose_name="Title Of Courtesy")
    birthday = models.DateField()
    hire_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255, verbose_name="Address")
    city = models.CharField(max_length=255, verbose_name="City")
    region = models.CharField(max_length=255, verbose_name="Region")
    postal_code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=255, verbose_name="Country")
    home_page = models.CharField(max_length=255, verbose_name="Home Page")
    extension = models.CharField(max_length=255, verbose_name="Extension")
    photo = models.CharField(max_length=255, verbose_name="Photo")
    notes = models.CharField(max_length=255, verbose_name="Notes")
    reports_to = models.CharField(max_length=255, verbose_name="Reports To")


class Shippers(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    phone = models.CharField(max_length=255, verbose_name="Phone")


class Orders(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    employees_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    shippers_id = models.ForeignKey(Shippers, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateTimeField()
    shipped_date = models.DateTimeField(auto_now_add=True)
    freight_date = models.PositiveBigIntegerField()
    ship_name = models.CharField(max_length=255, verbose_name="Ship Name")
    ship_Address = models.CharField(max_length=255, verbose_name="ShipAddress")
    ship_city = models.CharField(max_length=255, verbose_name="Ship City")
    ship_region = models.CharField(max_length=255, verbose_name="Ship Region")
    ship_postal_code = models.PositiveSmallIntegerField()
    ship_country = models.CharField(max_length=255, verbose_name="Ship Country")


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=8, decimal_places=2)

