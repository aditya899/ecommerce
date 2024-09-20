## GET Request to Retrieve All Products

**Endpoint:** `/`

**Request Method:** `GET`

### Request Headers

- **Accept:** `application/json`

### Response

**HTTP Status:** `200 OK`

**Response Headers**

- **Allow:** `OPTIONS, GET`
- **Content-Type:** `application/json`
- **Vary:** `Accept`

### Response Body

```json
[
    {
        "id": 1,
        "name": "Soap",
        "description": "Soap used for showers.",
        "price": "20.00",
        "stock": 20
    },
    {
        "id": 2,
        "name": "Shirt",
        "description": "Colorful shirt",
        "price": "200.00",
        "stock": 2
    }
]
```

## POST Request to Create a New Product

**Endpoint:** `/post/`

**Request Method:** `POST`

### Request Headers

- **Content-Type:** `application/json`
- **Accept:** `application/json`

### Request Body

```json
{
    "name": "Shirt",
    "description": "Colorful shirt",
    "price": "200.00",
    "stock": 2
}
```
