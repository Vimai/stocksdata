## Stock Data Project


This project consists of two endpoints:

1. Saving Stock Data:

Users can POST requests to save the amount of a specific stock they own.
The endpoint will fetch additional data from an external API and store it along with the user's stock quantity.


2. Retrieving Stock Information:

Users can GET requests to retrieve information about a specific stock from the database.
If the stock data has been previously fetched, it will be cached in Redis for faster retrieval.

----

## Getting Started:

This tutorial is specifically designed for use in a development environment.

#### Prerequisite: Docker and Docker Compose are required for this project.


### Clone the Repository:

### Duplicate and Configure Environment Variables:

Create a copy of the .env-example file and name it .env.
Replace the placeholder values for POLYGON_API_KEY with your actual Polygon.io API key.

### Launch the Application:


From the project directory, execute the following command:


```Bash
docker-compose up
```

This will start all the required services and deploy the application.