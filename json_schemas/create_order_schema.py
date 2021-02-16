CREATE_ORDER_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "order_id": {
      "type": "string"
    },
    "order_number": {
      "type": "string"
    }
  },
  "required": [
    "order_id",
    "order_number"
  ]
}
