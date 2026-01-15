# Real-Time Flight Tracking: End-to-End Data Pipeline (ELT)

This project implements an automated, containerized **ELT** (Extract, Load, Transform) pipeline designed to monitor air traffic. Unlike traditional ETL processes, this architecture prioritizes raw data ingestion directly into the warehouse, leveraging the processing power of PostgreSQL and dbt for in-database transformations.

---

### Geospatial Scope: Colombian Airspace

The pipeline is configured to monitor a strategic "bounding box" over **Colombia**, covering the most congested flight routes in the country (including the Medellín-Bogotá-Eje Cafetero triangle).

The monitoring parameters are defined by the following coordinates:
* **Latitude**: 4.0 to 8.5 (From Ibagué/Bogotá to Northern Antioquia).
* **Longitude**: -77.5 to -73.0 (From the Pacific Coast/Chocó to Eastern Cundinamarca).

This scope captures real-time data from major aeronautical hubs, providing a comprehensive view of the Colombian central and western air traffic.

---

### Infrastructure (Docker)

The project uses **Docker Compose** to orchestrate the environment in isolated containers:

* **Apache Airflow Container**: Orchestrates the Python extraction scripts and manages the scheduling of the entire ELT workflow.
* **PostgreSQL Container**: Serves as the centralized Data Warehouse where raw data is stored and then transformed.
* **dbt (Data Build Tool)**: The core of the transformation layer. It handles the SQL logic to convert raw records into validated, business-ready models.

---

### Core Components

* **Data Ingestion (EL)**: Python-based scripts that extract JSON data from flight tracking APIs and load it directly into PostgreSQL "raw" tables.
* **Orchestration**: End-to-end workflow management via Apache Airflow.
* **Data Transformation (T)**: In-warehouse transformation using dbt, following a modular architecture (Staging -> Marts).
* **Data Quality**: Automated testing layer with dbt to ensure schema integrity and business logic consistency.
* **Analytics**: Power BI integration for operational visualization and historical trend analysis.

---

### Dashboard Insights

The Power BI report provides answers to key operational questions:

* **Airline Popularity Ranking**: Analysis of the most active carriers within the monitored airspace.
* **Traffic Peak Analysis**: Identification of the busiest hours of operation during the day.
* **Fleet Distribution**: Comparison of aircraft manufacturers and registration origins.
* **Flight Dynamics**: Correlation between altitude, speed, and vertical rate.
* **Safety Monitoring**: Real-time tracking of Squawk codes and emergency status.

---

### Project Architecture

[Insert Architecture Diagram Here]

---

### How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jeriveraa23/flight-tracking-pipeline.git](https://github.com/jeriveraa23/flight-tracking-pipeline.git)