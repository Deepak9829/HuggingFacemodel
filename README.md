# Hugging Face Top Models Report Generator

This repository contains a Dockerized Python script that fetches data from the Hugging Face model hub, compiles a list of the top 10 downloaded models, generates a report, and then stops the container. The report is saved to a file on the host machine.

## Features

- Fetches data from Hugging Face model hub.
- Compiles a list of the top 10 downloaded models.
- Generates a report and saves it to a file.
- Runs in a Docker container for easy setup and execution.

## Prerequisites

- Docker installed on your machine.

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/Deepak9829/HuggingFacemodel.git
cd HuggingFacemodel
```
### Build the Docker Image
In the directory containing the Dockerfile build by the github action CI will trigger once github tag is created, build the Docker image:

```sh
    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        platforms: linux/amd64,linux/arm64
        push: true
        tags: deepakdocker25/huggingfacemodel:${{ steps.tag.outputs.tag }}
```

### Run the Docker Container
To run the container and generate the report, use the following command. This command mounts the local report directory to the container's /report directory so that the generated report is accessible on the host machine.

```sh
docker run --rm -v $(pwd)/report:/report deepakdocker25/huggingfacemodel:v1.0.1
```