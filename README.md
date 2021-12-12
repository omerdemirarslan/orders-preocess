## Orders Process

### Project Explaning:

This project is built using on the basic Django framework, Django REST framework libraries and Redis. Apart from these, the project is
dockerized with the docker application. When you download the project to your local, for you to deal with extra database
operations; SQLite3 database, which is Django's default database, is used. You don't need migrate for models; docker
make it for you.

The purpose of this project includes: Taking and completing food orders and displaying information about the orders.


* This project name: **Foodbasket**
* This project's apps:
  * **orders**
  * **partners**

### Required Application:

For the project to up; Docker application must be installed and running in your local.

### Install Project:

    git clone https://github.com/omerdemirarslan/orders-process.git

### Run The Project:

    docker-compose build
    docker-compose up

### In Browser:
    * http://localhost:8000/ or http://0.0.0.0:8000/ : You Can Show The Project Explaning
    * http://localhost:8000/api/v1/ : You Can Show The Available API URL's

### API Endpoints:

    * /api/v1/                              (All Available API URL's)
    * /api/v1/products/get-products/        (All Products)
    * /api/v1/categories/get-categories/    (All Categories)
    * /api/v1/partners/get-restaurants/     (All Restaurants)
    * /api/v1/orders/create-order/          (Order Creating)
    * /api/v1/orders/get-order/             (All Order)

### Endpoints

#### Get Restaurants

#### Request
    api/v1/partners/get-restaurants/

#### Response

```json
{
  "name": "Burger King",
  "is_active": true
}
```

---

#### Get Categories

#### Request
    /api/v1/categories/get-categories/

#### Response

```json
{
  "name": "Fast Food"
}
```

---

#### Get Products

#### Request
    /api/v1/products/get-products/

#### Response

```json
{
  "name": "Hamburger",
  "category": 1,
  "restaurant": 1
}
```

#### Create Order

#### Request
    /api/v1/orders/create-order/

#### Response

```json
{
    "id": 43,
    "user": 1,
    "address": "Yeni Mahalle",
    "order": 1,
    "price": 34,99
    "quantity": 45,
    "status": "preparing"
}
```

---

#### Get Order

#### Request
    /api/v1/orders/get-orders/

#### Response

```json
{
  "user": 1,
  "address": "Yeni Mahalle",
  "order": 1,
  "price": 34,99,
  "quantity": 45,
  "status": "Completed",
  "created_at": "2021-12-07T13:33:58.882846Z"
    }
```

---

#### Confirm Order

#### Request
    This API Control Orders and Change Order Status
    /api/v1/orders/confirm/

---
---

### Last Notes:

My project is always open to development. I admit it's not perfect, but my goal is not to be perfect, but to always be
able to do better. I am waiting for your positive or negative feedback.


---
---
