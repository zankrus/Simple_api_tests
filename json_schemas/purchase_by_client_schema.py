PURCHASE_BY_CLIENT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string"
                        },
                        "purchased": {
                            "type": "boolean"
                        },
                        "last_order_number": {
                            "type": "string"
                        },
                        "last_purchase_date": {
                            "type": "string"
                        },
                        "purchase_count": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "item_id",
                        "purchased",
                        "last_order_number",
                        "last_purchase_date",
                        "purchase_count"
                    ]
                }
            ]
        }
    },
    "required": [
        "items"
    ]
}
