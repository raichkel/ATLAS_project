# ATLAS HZZ Data Processing

Project to write a cloud data processing software to read and plot ATLAS HZZ data in parallel for (theoretically) many noddes.
## How to Run This Code
- Edit the `scale` variable in the `docker-compose.yml` file:
    scale:
        worker: 3 # change this to the number of desired workers
