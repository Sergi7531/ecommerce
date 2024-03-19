#  Base ecommerce API:

This is a bare-bones API oriented for a certain business type, most especifically, a clothing e-commerce.  

The project is entirely made using Django web framework, layered with the Django REST Framework package to provide your typical REST API structure.

The entire application is stored inside the `api` source folder.

The structure that features this project is dockerized. There are 3 containers by default defined in `docker-compose-api.yaml` 
file: `ecommerce_api`, `db` and `test-unit`, each of them serving one different purpose but interconnected to form the architecture:  

## Download the project:

    git clone https://github.com/Sergi7531/ecommerce

## Assuming docker is already installed on your system, the project setup is pretty easy:

### Move inside the project's base directory

    cd ecommerce

### And run the docker-compose-api.yaml file to run the project:

    docker-compose -f docker/docker-compose-api.yaml up --build

### Start a database shell:
<a name="deploy_api_local_cmd"></a>

    docker exec -ti ecommerce_db mysql -u ecommerce_user -p

#### And enter the password, defaulted to:

    ecommerce_password

## Testing the application:

Tests are ran inside an **isolated container** "test-unit", as defined in `docker-compose-api-local.yaml` file.

To manually perform the tests, follow one of this two options:

- Deploy the API as stated [above](#deploy_api_local_cmd)


- Or run the isolated tests container:

    
    docker-compose -f docker-compose-api.yaml run test-unit

--- 

## The public, official documentation for each endpoint of the application is available [here](https://www.postman.com/base-ecommerce-api/workspace/e-commerce-api/documentation/21377778-fb07d91a-046c-4d2c-b4ef-ebd31101de37)