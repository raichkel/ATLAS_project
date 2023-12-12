# ATLAS HZZ Data Processing

Project to write a cloud data processing software to read and plot ATLAS HZZ data in parallel for (theoretically) many noddes.
## How to Run This Code
- Edit the `scale` variable in the `docker-compose.yml` file:
    ```
    scale:
        worker: 3 # change this to the number of desired workers
    ```
- Run the following in the command line:

    ```
    docker-compose up -d
    ```
- Once completed, run the following to retrieve the graph:
    ```
    docker cp shared_volume:/app/data/plot.png /path/to/desired/local/file
    ```