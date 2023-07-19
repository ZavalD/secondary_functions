from sec_funcs.constans import Order


# TODO: ADD objects
def binary_search_iterative(
        arr: list, item, key: str = None,
        order: Order = Order.ASC) -> int | None:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        obj = arr[mid]
        if key is not None:
            obj = obj.get(key, None)
        if order == Order.ASC:
            order_flag = obj > item
        else:
            order_flag = obj < item
        if obj == item:
            return mid
        elif order_flag:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_recursive(
        arr: list, item, low: int, high: int, key: str = None,
        order=Order.ASC) -> int | None:
    if low <= high:
        mid = (low + high) // 2
        obj = arr[mid]
        if key is not None:
            obj = obj.get(key, None)
        if order == Order.ASC:
            order_flag = obj > item
        else:
            order_flag = obj < item
        if obj == item:
            return mid
        elif order_flag:
            return binary_search_recursive(arr, item, low, mid-1, key, order)
        else:
            return binary_search_recursive(arr, item, mid-1, high, key, order)
    return None
