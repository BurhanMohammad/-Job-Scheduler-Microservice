

# Job Scheduler Microservice

### Project Overview
This project is a Job Scheduler Microservice built with Django, Django REST Framework, and Celery. The service allows you to schedule jobs, such as sending email notifications or performing number crunching tasks, with flexible configurations. The project is scalable and designed to handle a large number of jobs and API requests efficiently.

## Features

- Job Scheduling: Schedule jobs to run at specific intervals ( weekly, hourly).
- API Endpoints:
  - GET /jobs: List all jobs.
  - GET /jobs/:id: Retrieve details of a specific job by ID.
  - POST /jobs: Create new jobs with customizable intervals.
- Database Integration: Jobs are stored in a SQLite3 database with fields like job name, last run, next run, and interval.

- Scalability: Designed to handle up to 10,000 users globally with 1,000 services and 6,000 API requests per minute.

- API Documentation: Integrated Swagger UI for interactive API documentation.


## Project Setup
## 1. Prerequisites
     - Python 3.x
     - Redis (for Celery message broker)
     - any database


## 2. Clone the Repository



```bash
  git clone https://github.com/BurhanMohammad/-Job-Scheduler-Microservice.git
  cd job_scheduler_service

```

## 3.  Create and Activate Virtual Environment



```bash
  python3 -m venv venv
  `venv\Scripts\activate`
```

## 4.  Install Dependencies

```bash
  pip install -r requirements.txt

```


## 5.  Install Dependencies

```bash
  python manage.py migrate

```

## 6. Set Up Redis

  - Install Redis on your system.
  - Start the Redis server:

    ```bash
      redis-server --service-start
    ```

## 7.  Install Dependencies

```bash
  python manage.py runserver

```

##  8. Start Celery Worker and Beat Scheduler
  - Start the Celery worker:

    ```bash
      celery -A job_scheduler_service worker --loglevel=info --pool=gevent

    ```

  - Start the Celery Beat scheduler:

    ```bash
      celery -A job_scheduler_service beat --loglevel=info

    ```

## 9. Access Swagger API Documentation
  - Visit http://127.0.0.1:8000/swagger/ to interact with the API documentation.





---------





# Scaling the Job Scheduler Microservice

## Scaling Strategies
-  #### 1. Horizontal Scaling with Multiple Services
   - #### Celery Workers:
     - Increase the number of Celery workers to handle more concurrent tasks. Each worker can be deployed on separate servers or containers (e.g., Docker).
     - using a load balancer to distribute tasks evenly across the workers.
     - Adjusting the CELERYD_CONCURRENCY setting to allow each worker to process multiple tasks simultaneously.
   - #### Django Application Servers:
       - Deploy multiple instances of the Django application behind a load balancer (e.g., Nginx, HAProxy).
      - Use container orchestration tools like Kubernetes to manage multiple instances, ensuring high availability and auto-scaling based on demand.
   - #### Redis and PostgreSQL:
       - Redis can be scaled by setting up a Redis cluster, allowing for distributed storage and processing of task queues.
       - PostgreSQL can be scaled by using read replicas for load balancing read requests and a primary server for write operations. Consider partitioning large tables if necessary.
- #### 2. API Management
  - API Gateway:
       - Use an API Gateway (e.g., AWS API Gateway, Kong) to manage and route API requests efficiently. The gateway can handle rate limiting, authentication, and routing to different microservices.
   - Caching:
       - Implement caching (e.g., with Redis or Memcached) for frequently accessed API responses, reducing the load on the database and application servers.
      - Use Django’s built-in caching framework or tools like Varnish for HTTP caching.
    - Throttling and Rate Limiting:
       - Implement API rate limiting to protect the service from excessive requests, ensuring stability under heavy load.
       - Django REST Framework provides built-in support for throttling, which can be configured per user or globally.
