def load_orders_from_file(filename):
    try:
        order_list = []
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file.readlines():
                order_list.append(line)
        return order_list
    except FileNotFoundError:
        print("Не удалось создать или перезаписать файл")
        return []
    
def calculate_order_total(price, discount_rate):
    return round(price * (1 - discount_rate),2)

def get_discount_by_total(total):
    discount = 0
    if(total <= 0):
        discount = 0
    elif(total > 10000):
        discount = 0.15
    elif(total > 5000):
        discount = 0.10
    else:
        discount = 0.05
    return discount

def process_orders(orders_data):
    orders = []
    for data in orders_data:
        try:
            cur_order = data.strip().split(":")
            order_id, total_sum, status,user = cur_order
            cur_discount = get_discount_by_total(int(total_sum))
            total = calculate_order_total(int(total_sum), cur_discount)
            orders.append({"order_id": order_id, "total": total, "status": status, "user": user })
        except ValueError:
            print(f"Ошибка в строке: {data}")
    return orders


def analyze_orders(processed_orders):
    status = {
        "total_orders": 0,
        "total_sum": 0,
        "by_status": {},
        "unique_users": set()
    }

    for order in processed_orders:
        status['total_orders']+=1
        status["total_sum"]+=order['total']
        cur_status = order['status']
        status["by_status"][cur_status] = status["by_status"].get(cur_status, 0) + 1
        status["unique_users"].add(order['user'])

    return status


def process_order_file(input_file, output_file):
    orders = load_orders_from_file(input_file)
    orders_procces = process_orders(orders)
    orders_analyze = analyze_orders(orders_procces)
    try:
        with open(output_file, 'w', encoding="utf-8") as file:
            statuses = ", ".join(f"{k}: {v}" for k,v in orders_analyze["by_status"].items())
            file.writelines(f"Обработано заказов: {orders_analyze['total_orders']}\n")
            file.writelines(f"Общая сумма: {orders_analyze['total_sum']} руб.\n")
            file.writelines(f"По статусам: {statuses}\n")
            file.writelines(f"Уникальных пользователей: {len(orders_analyze['unique_users'])}\n")
    except Exception:
        print("Не удалось создать или перезаписать файл")