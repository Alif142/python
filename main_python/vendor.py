def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }
    
    # Don't touch above this line
    unpurchased_items = []
    for item in pinned_list:
        if item not in items_purchased:
            unpurchased_items.append(item)
  

    reciept = {}
    for item in items_purchased:
        if item in item_prices:
            reciept[item] = item_prices[item]

    total = 0
    for value in reciept:
        total +=reciept[value]

    return unpurchased_items,reciept,total

