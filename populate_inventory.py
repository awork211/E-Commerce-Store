from .models import Inventory

def populate_inventory():
    from . import db
    inventory_items = [
        {
            'image_src': 'mug_candle1.jpg',
            'description': 'A windows-open, incense-burning Saturday with nowhere to be. Cream, sweetgrass, and smoke.',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Mug'
        },
        {
            'image_src': 'sand_fog.jpg',
            'description': 'The one that started it all. A vibrant scent of leather, teak, and orange.',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Sand + Fog'
        },
        {
            'image_src': 'forest.jpg',
            'description': 'Big Sur magic, wild sage baking in the sun, the rumble of waves and rocks. Eucalyptus, sea salt, redwood, and palo santo.',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Forest'
        },
        {
            'image_src': 'bergamont_1.jpg',
            'description': 'Coastal mornings blanketed in a gentle marine layer, the warmth of the rising sun, wild white blossoms collecting dew. Ozonic, crisp, clean. Bergamot, sea moss, and sandalwood.',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Bergamont'
        },
        {
            'image_src': 'pine_forest.jpg',
            'description': 'A weekend in the mountains, sun gleaming through the canopy. Sage, moss, and lavender.',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Pine Forest'
        },
        {
            'image_src': 'firewood_figs.jpg',
            'description': 'Salty skin, steady tides, endless afternoons in the hot summer sun. Vibrant, juicy, aquatic. Black currant, tuberose, and sea moss.',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Firewood Figs'
        },
        {
            'image_src': 'coconut_fire.jpg',
            'description': 'Heatwaves, late-night crowds, the lure of the dance floor melding smoke and strange perfumes. Balmy, ambiguous, free. Yuzu, Indian jasmine, and smoked',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Coconut Fire'
        },
        {
            'image_src': 'bergamont_2.jpg',
            'description': 'A windows-open, incense-burning Saturday with nowhere to be. Cream, sweetgrass, and smoke.',
            'price': 24.99,
            'category': 'candles',
            'item_name': 'Bergamont 2'
        },
        {
            'image_src': 'after_hours_diffuser.jpg',
            'description': 'A windows-open, incense-burning Saturday with nowhere to be. Cream, sweetgrass, and smoke.',
            'price': 14.99,
            'category': 'diffusers',
            'item_name': 'After Hours'
        },
        {
            'image_src': 'botanical_diffuser.jpg',
            'description': 'Heatwaves, late-night crowds, the lure of the dance floor melding smoke and strange perfumes. Balmy, ambiguous, free. Yuzu, Indian jasmine, and smoked',
            'price': 14.99,
            'category': 'diffusers',
            'item_name': 'Botanical'
        },
        {
            'image_src': 'cedarwood_diffuser.jpg',
            'description': 'Salty skin, steady tides, endless afternoons in the hot summer sun. Vibrant, juicy, aquatic. Black currant, tuberose, and sea moss.',
            'price': 14.99,
            'category': 'diffusers',
            'item_name': 'Cedarwood'
        },
        {
            'image_src': 'champagne_reed_diffuser.jpg',
            'description': 'A weekend in the mountains, sun gleaming through the canopy. Sage, moss, and lavender.',
            'price': 14.99,
            'category': 'diffusers',
            'item_name': 'Champagne'
        },
        {
            'image_src': 'islands_diffuser.jpg',
            'description': 'Coastal mornings blanketed in a gentle marine layer, the warmth of the rising sun, wild white blossoms collecting dew. Ozonic, crisp, clean. Bergamot, sea moss, and sandalwood.',
            'price': 14.99,
            'category': 'diffusers',
            'item_name': 'Islands'
        },
        {
            'image_src': 'serenity_diffuser.jpg',
            'description': 'Big Sur magic, wild sage baking in the sun, the rumble of waves and rocks. Eucalyptus, sea salt, redwood, and palo santo.',
            'price': 14.99,
            'category': 'diffusers',
            'item_name': 'Serenity'
        },
        {
            'image_src': 'tea_tree_diffuser.jpg',
            'description': 'The one that started it all. A vibrant scent of leather, teak, and orange.',
            'price': 14.99,
            'category': 'diffusers',
            'item_name': 'Tea Tree'  
        },
        {
            'image_src': 'beach_soap_variety_bundle.jpg',
            'description': 'The one that started it all. A vibrant scent of leather, teak, and orange.',
            'price': 19.99,
            'category': 'soaps',
            'item_name': 'Beach'
        },
        {
            'image_src': 'pink_splash_soap_variety_bundle.jpg',
            'description': 'Big Sur magic, wild sage baking in the sun, the rumble of waves and rocks. Eucalyptus, sea salt, redwood, and palo santo.',
            'price': 19.99,
            'category': 'soaps',
            'item_name': 'Pink Splash'
        },
        {
            'image_src': 'self_care_soap_variety_bundle.jpg',
            'description': 'Coastal mornings blanketed in a gentle marine layer, the warmth of the rising sun, wild white blossoms collecting dew. Ozonic, crisp, clean. Bergamot, sea moss, and sandalwood.',
            'price': 19.99,
            'category': 'soaps',
            'item_name': 'Self Care'
        },
        {
            'image_src': 'sensitive_skin_variety_bundle.jpg',
            'description': 'A weekend in the mountains, sun gleaming through the canopy. Sage, moss, and lavender.',
            'price': 19.99,
            'category': 'soaps',
            'item_name': 'Sensitive Skin'
        },
        {
            'image_src': 'vanilla_goat_milk_soap_variety_bundle.jpg',
            'description': 'Salty skin, steady tides, endless afternoons in the hot summer sun. Vibrant, juicy, aquatic. Black currant, tuberose, and sea moss.',
            'price': 19.99,
            'category': 'soaps',
            'item_name': 'Vanilla Goat Milk'
        },
        {
            'image_src': 'white_and_chocolate_soap_variety_bundle.jpg',
            'description': 'Heatwaves, late-night crowds, the lure of the dance floor melding smoke and strange perfumes. Balmy, ambiguous, free. Yuzu, Indian jasmine, and smoked',
            'price': 19.99,
            'category': 'soaps',
            'item_name': 'White and Chocolate'
        },
    ]
    for item in inventory_items:
        if not Inventory.query.filter_by(item_name=item['item_name']).first():
            inventory_item = Inventory(
                image_src=item['image_src'],
                description=item['description'],
                price=item['price'], 
                category=item['category'],
                item_name=item['item_name'])
            db.session.add(inventory_item)
    db.session.commit()