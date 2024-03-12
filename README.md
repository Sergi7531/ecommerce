#  Base ecommerce API:

This is a bare-bones API oriented for an "ecommerce" that can be in the need of a backend architecture.

The project is entirely made using the Django framework, more specifically layered with the Django REST package to provide the structure of a typical API.

The entire application is stored inside the `api` source folder.

The structure that features this project is dockerized. There are 2 containers by default defined in `docker-compose-api.yaml` 
file: `ecommerce_api` and `db`:  

## Download the project:

    git clone https://github.com/Sergi7531/ecommerce

## Assuming docker is already installed on your system, the project setup is pretty easy:

### Move inside the directory of the project

    cd ecommerce

### And run the docker-compose-api.yaml file to run the project:

    docker-compose -f docker/docker-compose-api.yaml up --build

### Start a database shell:

    docker exec -ti ecommerce_db mysql -u ecommerce_user -p

#### And enter the password, defaulted to:

    ecommerce_password

## Testing the application:

Tests are ran **automatically on docker build**, as specified in `entrypoint-local.sh` file.

To manually perform the tests, follow one of this two options:

<details>
<summary>Direct command via terminal</summary>

Run the following command:

    docker-compose -f docker-compose-api.yaml run ecommerce_api pytest --verbose

(RECOMMENDED!) Use the verbose flag to print a detailed output:

    docker-compose -f docker-compose-api.yaml run ecommerce_api pytest /code/tests --verbose

</details>

<details>
<summary>Pytest from inside the container</summary>

Instead, start a Django-container shell:

    docker exec -ti ecommerce_api_local bash

And execute the tests as specified in the docker compose:
    
    pytest

**(RECOMMENDED!)** Use the verbose flag to print a detailed output:
    
    pytest --verbose

</details>

--- 

## The public, official documentation for each endpoint of the application is available [here](https://www.postman.com/base-ecommerce-api/workspace/e-commerce-api/documentation/21377778-fb07d91a-046c-4d2c-b4ef-ebd31101de37)