view_product_counts = {}
view_category_counts = {}

def track_product_views(func):
    def wrapper(*args):
        args_value = ', '.join(str(arg) for arg in args)
        count = 1
        if args_value in view_product_counts:
            view_product_counts[args_value] += count
        else:
            view_product_counts[args_value] = count
        result = func(*args)
        return result
    return wrapper

def track_category_views(func):
    func_name = func.__name__
    def wrapper(*args):
        count = 1
        if func_name in view_category_counts:
            view_category_counts[func_name] += count
        else:
            view_category_counts[func_name] = count
        result = func(*args)
        return result
    return wrapper

def display_product_view_counts():
    print("\n\nProduct views counts:")
    for product, count in view_product_counts.items():
        print(f"{product}: {count}")

def display_category_view_counts():
    print("\n\nCategory view counts:")
    for category, count in view_category_counts.items():
        print(f"{category}: {count}")

@track_category_views
# @track_product_views
def view_book(title):
    print(f"Viewing Book: {title}")

@track_category_views
# @track_product_views
def view_electronics(item):
    print(f"Viewing Electronics: {item}")

view_book("The Hitchhiker's Guide to the Galaxy")
view_electronics("Smart Television")
view_book("The Hitchhiker's Guide to the Galaxy")
view_electronics("Wireless Headphones")
view_book("The Lord of the Rings")

display_product_view_counts()
display_category_view_counts()