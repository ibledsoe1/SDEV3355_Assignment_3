def test_product_service():
    from product_service.src.db.items import Item
    assert Item is not None

def test_order_service():
    from order_service.src.db.orders import Order
    assert Order is not None