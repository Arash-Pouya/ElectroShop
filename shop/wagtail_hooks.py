from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from shop.models import Category, Brand, Product


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_order = 100
    menu_label = 'Category'


class BrandAdmin(ModelAdmin):
    model = Brand
    menu_label = 'Brand'
    menu_order = 200


class ProductAdmin(ModelAdmin):
    model = Product
    menu_order = 300
    menu_label = 'Product'


class ShopGroup(ModelAdminGroup):
    menu_label = 'Shop'
    menu_order = 200
    items = [ProductAdmin, CategoryAdmin, BrandAdmin]


modeladmin_register(ShopGroup)