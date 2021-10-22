# Techbyheart Machine Test
This is machine test of Techbyheart. Create a e-commerce application with 3 types of users. Used technology Django rest framework and JWT.

- Clone The project :- https://github.com/AthifSaheer/techbyheart-machine-test

### Built With

* Backend - `Django Rest Framework`

<!-- GETTING STARTED -->
## Getting Started

If you would love to run this project on your local env I will walk you through:

### Installation

1. Create virutal environment
   ```sh
   virtualenv venv
   ```
   
2. Activate virtualenv
   ```sh
   source venv/bin/activate
   ```
   
3. Clone the repo
   ```sh
   https://github.com/AthifSaheer/techbyheart-machine-test
   ```
   
4. Install requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
   
5. Run Project: <br>
   go to the project folder where manage.py file is present
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Check apis

Go to lading page then you can see overview of all apis.

1. Default admin panel go to - /admin/
    ```sh
    Username: admin
    Password: admin
    ```

2. Create an account(format👇)
   ```sh
    {
        "username" : "username",
        "email" : "email@gmail.com",
        "password" : "12345678"
    }
   ```
3. Login (format👇)
   ```sh
    {
        "username" : "username",
        "password" : "12345678"
    }
   ```
4. Add to cart post method format👇
    ```sh
      {
        "product": <product id>,
        "store": <store id>
      }
   ```
5. Checkout(format👇)
    ```sh
    {"user": 1}
   ```
   
6. Add product (format👇)
    ```sh
    {
        "store": <store id>,
        "product": <product id>,
        "stock": <stock number>
    }
   ```
