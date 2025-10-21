# dans-quantum-integration-prototyping

Explore and demonstrate the possibilities of integrating the quantum tool with DANS DataStations

The QUANTUM Labelling Tool provides a standardized mechanism to evaluate and label the quality, utility, and maturity of datasets. 
The QUANTUM labeling tool is also found online: https://quantumpilot.upv.es/

At the time of writing it does not have a public API.

This project contains the following parts:
- The [`data-quality-label-service`](./data-quality-label-service/README.md). 
- The [`dataverse-display`](./dataverse-display/README.md). 

The basic idea is that the display code will use the service to find and extract quality information. This allows for experimenting without changing the quantum label tool. 
It could even become useful outside of the testing scope, because it allows for adapting a quality service API to DANS specific needs. 

