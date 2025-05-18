# Manufacturing Digital Twin

A **digital twin** is a digital representation of a real-life system or entity, often built using IoT devices. This project simulates machinery with temperature and vibration sensors and seeks to predict mechanical failures through predictive modeling. The application architecture is intentionally simplistic, as it is meant to be a proof of concept
for building such a system and deploying it to production.

---

## Features

- **Synthetic data generation:** 1k data points including features for vibration and temperature, and a binary classification for predicted failure.
- **Django web app:** provides a dashboard where the user can input data and predict failures in real time.
- **ML predictive maintenance:** trained on the 1k data points mentioned above. Typical readings would be 75 degrees Fahrenheit (F) for temperature and 0.5 gravity (g) for vibration. A classification of "failure" would indicate the need for prompt maintenance of the manufacturing equipment.
- **Containerized deployment with Docker**
- **Infrastructure as Code with Terraform:** provisions AWS resources (see tech stack)
- **CI/CD using Github Actions:** triggered by releases to main, executes a terraform apply, builds and tags the Docker image, pushes the image to the ECR repo, and forces a new deployment. Terraform state is saved in S3. There is an additional workflow for executing a terraform destroy that can be triggered manually.

## Tech Stack

- **Language:** Python 3.11
- **App:** Django, WSGI, Gunicorn
- **Data and ML:** Pandas, NumPy, Scikit-learn
- **Infra:** Nginx (used in local development), Docker, Docker Compose, Terraform, AWS: ECR, ECS, Fargate, VPC, ALB, security groups, target group, CloudWatch logging, S3
- **CI/CD:** GitHub Actions

## Requirements

- Python 3.11
- Docker & Docker Compose
- Terraform ≥ 1.5
- AWS CLI configured

## Installation

1. Clone this repo. Then do the following steps:
   cd into the cloned repo and create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
    ```
   Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Make sure you have an AWS account.

- For the region, I used "us-east-1". If you want to use another region, you will need to update your environment variables.
- Create an S3 bucket called "digital-twin-terraform" to save the Terraform state.
- Create an access key and secret for your user in AWS.
- You will need to have the aws cli installed. On your computer, go to .aws/credentials and provide your access key id and secret:
  ```
  [default]                   
  aws_access_key_id = <your access key>
  aws_secret_access_key = <your access secret>
  ```

- Log Docker into the ECR
  ```bash
  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your aws account url>
  ```

### To run locally, do:

```bash
docker-compose up
```
Go to `localhost` in your browser.

### To use Github Actions for deploying to the cloud:

In your Github repo, go to **Settings > Secrets and variables > Actions** and set the following environment variables:

- AWS_ACCESS_KEY_ID = <your access key>
- AWS_SECRET_ACCESS_KEY = <your access secret>
- AWS_REGION = "us-east-1"
- ECR_REPOSITORY = "digital-twin"
- TF_VAR_REGION = "us-east-1"
  Run the "Deploy to AWS" workflow. Go to the ALB DNS name in your browser (It should be printed in the workflow output).
  You can also look this up in AWS by navigating to the ALB.

## Example Usage

- For temperature, enter 50 or 100
- For vibration, enter 0.2 or 0.8