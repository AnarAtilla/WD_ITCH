from operations import (add_categories_and_products, read_categories_and_products,
                        update_product_price, aggregate_and_group_products,
                        filter_categories_with_multiple_products,
                        close_session)

if __name__ == "__main__":
    add_categories_and_products()
    read_categories_and_products()
    update_product_price()
    aggregate_and_group_products()
    filter_categories_with_multiple_products()
    close_session()
