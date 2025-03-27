# Supermarket Checkout System

class PriceCalculator:
    def __init__(self, price_per_unit, bulk_deal=None):
        self.unit_price = price_per_unit
        self.bulk_offer = bulk_deal

    def compute_total(self, item_count):
        if not self.bulk_offer:
            return item_count * self.unit_price
            
        bulk_quantity, bulk_price = self.bulk_offer
        bulk_sets = item_count // bulk_quantity
        remaining_items = item_count % bulk_quantity
        
        return (bulk_sets * bulk_price) + (remaining_items * self.unit_price)

class ProductCart:
    
    def __init__(self, pricing_strategy):
        self.pricing_model = pricing_strategy
        self.quantity = 0

    def add_to_cart(self):
        self.quantity += 1

    def calculate_item_total(self):
        return self.pricing_model.compute_total(self.quantity)

class SupermarketCheckout:
    
    def __init__(self, product_pricing):
        self.pricing_rules = {
            product: PriceCalculator(
                price_per_unit=details.get('unit_price'),
                bulk_deal=details.get('bulk_offer')
            ) for product, details in product_pricing.items()
        }
        
        self.shopping_cart = {}

    def scan_product(self, product_code):
        if product_code not in self.pricing_rules:
            raise ValueError(f"Unknown product: {product_code}")
        
        if product_code not in self.shopping_cart:
            self.shopping_cart[product_code] = ProductCart(
                self.pricing_rules[product_code]
            )
        
        self.shopping_cart[product_code].add_to_cart()

    def calculate_total_bill(self):
        return sum(
            cart_item.calculate_item_total() 
            for cart_item in self.shopping_cart.values()
        )

store_pricing = {
    'A': {
        'unit_price': 50,
        'bulk_offer': (3, 130)
    },
    'B': {
        'unit_price': 30,
        'bulk_offer': (2, 45)
    },
    'C': {'unit_price': 20},
    'D': {'unit_price': 15}
}

def main():
    checkout = SupermarketCheckout(store_pricing)
    
    test_purchase = "DABABA"
    for product in test_purchase:
        checkout.scan_product(product)
    
    total_bill = checkout.calculate_total_bill()
    print(f"Total Purchase Amount: ${total_bill/100:.2f} or {total_bill}")

if __name__ == "__main__":
    main()
    
    
