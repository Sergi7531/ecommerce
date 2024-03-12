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

## Automated tests:

### Run the automated tests with the following command:
    docker-compose -f docker-compose-api.yaml run ecommerce_api pytest /code/tests --verbose

### Or use the verbose option for more details about the :
    docker-compose -f docker-compose-api.yaml run ecommerce_api pytest /code/tests --verbose

--- 

## The public, official documentation for each endpoint of the application is available [here](https://www.postman.com/base-ecommerce-api/workspace/e-commerce-api/documentation/21377778-fb07d91a-046c-4d2c-b4ef-ebd31101de37)