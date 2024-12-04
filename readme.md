from django.db import transaction
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

def add_to_cart(user, product_variant_id, quantity):
    # Step 1: Fetch the Product Variant (or return 404 if not found)
    product_variant = get_object_or_404(ProductVariant, id=product_variant_id, is_active=True)

    # Step 2: Check if there is enough stock available
    if product_variant.stock_quantity < quantity:
        raise ValidationError(f"Only {product_variant.stock_quantity} units available in stock.")

    # Step 3: Check if the user has an open cart or create one
    cart, created = Cart.objects.get_or_create(user=user, status='open')

    # Step 4: Check if the product variant is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product_variant=product_variant)
    
    if not item_created:
        # If the item is already in the cart, check total quantity with the new addition
        new_quantity = cart_item.quantity + quantity
        if new_quantity > product_variant.stock_quantity:
            raise ValidationError(f"Only {product_variant.stock_quantity} units available in stock.")

        # Step 5: Update the cart item’s quantity and total price
        cart_item.quantity = new_quantity
    else:
        # For new item, just set the quantity
        cart_item.quantity = quantity

    cart_item.price = product_variant.price  # Step 6: Ensure correct price is applied
    cart_item.total_price = cart_item.price * cart_item.quantity
    cart_item.save()

    # Step 7: Recalculate cart totals
    cart.recalculate_total()

    return cart  # Return the updated cart state




2. Core Add-to-Cart Logic (Direct Control in View/Service):
Here we define a core function that performs:

Product validation.
Cart item creation or update.
Explicit error handling.

from django.shortcuts import get_object_or_404
from django.db import transaction
from django.core.exceptions import ValidationError

@transaction.atomic
def add_product_to_cart(user, product_variant_id, quantity):
    # Step 1: Fetch product variant
    product_variant = get_object_or_404(ProductVariant, id=product_variant_id, is_active=True)

    # Step 2: Check stock before proceeding (core logic)
    if product_variant.stock_quantity < quantity:
        raise ValidationError(f"Only {product_variant.stock_quantity} units available in stock.")

    # Step 3: Fetch or create user's open cart
    cart, created = Cart.objects.get_or_create(user=user, status='open')

    # Step 4: Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product_variant=product_variant)
    
    # Step 5: Update quantity or add as new item
    if not item_created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    
    # Save the cart item (this will trigger the signals for other tasks)
    cart_item.save()

    return cart


Transaction Atomicity: We wrap the process in transaction.atomic() to ensure the operations succeed or fail together (this is important for consistency when dealing with stock and cart updates).



3. Signals for Stock Management and Cart Total Recalculation (Decoupled Logic):
Next, we handle stock updates and cart total recalculation in signal handlers. These are triggered automatically when a CartItem is saved.

python
Copy code
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import CartItem, ProductVariant

@receiver(pre_save, sender=CartItem)
def check_and_reduce_stock(sender, instance, **kwargs):
    """
    Ensure that stock is reduced and that the stock check logic runs before adding a CartItem.
    This signal ensures stock is always up-to-date.
    """
    # Check stock (additional safety check, just in case)
    product_variant = instance.product_variant
    if instance.quantity > product_variant.stock_quantity:
        raise ValidationError(f"Only {product_variant.stock_quantity} units available.")

    # Reduce stock quantity
    product_variant.stock_quantity -= instance.quantity
    product_variant.save()

@receiver(post_save, sender=CartItem)
def update_cart_total(sender, instance, **kwargs):
    """
    Recalculate the total price of the cart every time a CartItem is saved or updated.
    This ensures that the cart total is updated automatically.
    """
    cart = instance.cart
    cart.total_price = sum(item.total_price for item in cart.items.all())
    cart.save()


Explanation of Signal Handlers:
check_and_reduce_stock:
Pre-save signal: Ensures stock is checked and reduced before the cart item is actually saved.
Reduces the stock of the ProductVariant once the item is successfully added to the cart.
update_cart_total:
Post-save signal: Recalculates the cart total after every CartItem save (triggered when a new item is added or an existing one is updated).
This ensures that the cart’s total price is always up-to-date without needing explicit logic in the core add_to_cart function.
4. Connecting the Signals:
Make sure your signals are connected to the models by including the signals in apps.py or by importing them in the __init__.py of the app module.

In apps.py:
python
Copy code
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        import your_app.signals  # Import the signal handlers


How the Hybrid Approach Works:
Direct logic (core add_product_to_cart function):

Controls the product variant validation, stock checking, and basic cart item updates.
Keeps critical logic (like checking if the item is in stock) within the view/service, ensuring tight control over the most essential part of the business logic.
Signals (non-essential but important tasks):

The pre_save signal ensures the stock is correctly adjusted whenever a cart item is saved.
The post_save signal recalculates the cart total, ensuring that the cart’s total price remains accurate without the need to add this logic in every function that modifies the cart.
Advantages of This Hybrid Approach:
Simplicity and control: The core add-to-cart functionality remains in direct control, making the flow clear and explicit.
Extensibility: By offloading non-essential tasks (e.g., stock management, cart recalculations) to signals, you decouple these responsibilities, making it easier to extend and maintain.
Modularity: Adding more functionality (e.g., discounts, notifications) can be done via additional signals without changing the core logic.
Debugging: Core logic is straightforward and easy to debug, while signal-based tasks can be modified independently if needed.
Conclusion:
The hybrid approach gives you the best of both worlds:

Explicit control over critical logic in the core function.
Decoupled, reusable logic for tasks like stock management and cart recalculations, using signals.
This makes it ideal for building scalable e-commerce systems where flexibility and maintainability are key considerations.
