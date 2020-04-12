from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile, Label, Category, Carousel


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False,refund_granted=True)

make_refund_accepted.short_description = 'Update orders to refund granted'

def make_order_received(modeladmin, request, queryset):
    queryset.update(received=True)

make_order_received.short_description = 'Update orders to received'


def make_order_being_delivered(modeladmin, request, queryset):
    queryset.update(being_delivered=True)

make_order_being_delivered.short_description = 'Update orders to being delivered'


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'ordered', 
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = [
        'ordered', 
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted'
    ]
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [
        make_refund_accepted,
        make_order_being_delivered,
        make_order_received
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]

    list_filter = [
        'address_type',
        'default',
        'country',
    ]
    search_fields = [
        'user',
        'street_address',
        'apartment_address',
        'zip'
    ]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Carousel)
