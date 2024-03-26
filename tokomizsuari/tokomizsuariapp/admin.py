from django.contrib import admin
from django.utils.html import format_html
from . models import Customer
from . models import Category
from . models import Employee
from . models import OrderDetail
from . models import Order
from . models import Product
from . models import Shipper
from . models import Supplier
from . models import Contact
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['CustomerID', 'CustomerName', 'ContactName', 'Address', 'City', 'PostalCode', 'Country']
    search_fields = ['CustomerName__startswith']
    list_filter = ['CustomerName']
    
admin.site.register(Customer, CustomerAdmin)
    
    
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['CategoryID', 'CategoryName', 'Description']
    search_fields = ['CategoryName__startswith']
    list_filter = ['CategoryName']
 
admin.site.register(Category,CategoryAdmin)
   
class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['EmployeeID', 'LastName', 'FirstName', 'BirthDate', 'Photo', 'Notes',]
    search_fields = ['LastName__startswith']
    list_filter = ['LastName']
    
admin.site.register(Employee, EmployeeAdmin)
    
class OrderDetailAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['OrderDetailID', 'OrderID', 'ProductID', 'Quantity']
    search_fields = ['ProductID_startswith']
    list_filter = ['ProductID']
    
admin.site.register(OrderDetail,OrderDetailAdmin)
    
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['OrderID', 'CustomerID', 'EmployeeID', 'OrderDate', 'ShipperID']
    search_fields = ['ShipperID_startswith']
    list_filter = ['ShipperID']
    
admin.site.register(Order, OrderAdmin)
    
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ProductID', 'ProductName', 'SupplierID', 'CategoryID', 'Unit', 'Price', 'image_display', 'description']
    search_fields = ['ProductName_startswith']
    list_filter = ['ProductName']
    
    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />'.format(obj.image.url))
        return "No Image"

    image_display.short_description = 'Image'  # Judul kolom gambar
    

admin.site.register(Product, ProductAdmin)
    
class ShipperAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ShipperID', 'ShipperName', 'Phone']
    search_fields = ['ShipperName_startswith']
    list_filter = ['ShipperName']
    
admin.site.register(Shipper, ShipperAdmin)
    
class SupplierAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['SupplierID', 'SupplierName', 'ContactName', 'Address', 'City', 'PostalCode', 'Country', 'Phone']
    search_fields = ['SupplierName__startswith']
    list_filter = ['SupplierName']
    
admin.site.register(Supplier, SupplierAdmin)

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['ProductID', 'Nama', 'Email', 'Message']
    search_fields = ['Nama']
    list_display = ['Nama']

admin.site.register(Contact, ContactAdmin)



#Modify Site Header
admin.site.site_header = "Admin Toko Mizsuari"
#Modify Site Title
admin.site.site_title = "Toko Mizsuari"
#Modify Site Index Title
admin.site.index_title = "Admin Toko Mizsuari"

