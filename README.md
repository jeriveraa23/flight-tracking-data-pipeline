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
* **dbt (Data Build Tool)**: Integrated into the workflow as the transformation engine. It handles the SQL logic to convert raw records into business-ready models and executes data quality tests.

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

* **RealTime Operation Overview**: High-level tracking of unique routes, maximum recorded speeds (up to 982.8 km/h), and altitude thresholds (reaching 13.72 mil meters).
* **Peak Traffic Hours**: Time-series analysis identifying the highest density of flights, showing significant activity peaks around 02:00 and 17:00.
* **Vertical Status Analysis**: Breakdown of aircraft distribution by flight phase (Ascending, Descending, and Level Flight) to monitor regional traffic flow.
* **Flight Performance Profile**: Scatter plot correlation between Average Speed (km/h) and Barometric Altitude, revealing the aerodynamic efficiency of the fleet.
* **Geographical Fleet Distribution**: Ranking of unique aircraft by manufacturer and country of registration, highlighting major contributions from the United States, Colombia, and Chile.
* 

<img width="1413" height="795" alt="Insights P2" src="https://github.com/user-attachments/assets/c091b767-6211-47be-b72f-dae9a13a2b83" />


---

### Project Architecture

![Arquitecture Diagram Project 2](https://github.com/user-attachments/assets/0d55152c-b848-4e0b-a24b-bde243c9708c)

---

### How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jeriveraa23/flight-tracking-data-pipeline.git
