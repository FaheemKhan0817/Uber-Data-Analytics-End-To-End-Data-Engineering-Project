# Uber Data Analytics: End-to-End Data Engineering Project 🚖💻

Welcome to my **Uber Data Analytics** project, an end-to-end data engineering pipeline that transforms raw Uber trip data into actionable insights using modern cloud and MLOps tools. This project showcases my expertise in **data pipelines**, **cloud infrastructure**, and **data visualization**, built with Google Cloud Platform (GCP), Mage AI, Docker, BigQuery, and Looker Studio.

📺 **Watch the Project Walkthrough**: [YouTube Video](https://youtu.be/bwKvjfUDKac)  
📊 **Explore the Dashboard**: [Looker Studio Dashboard](https://lookerstudio.google.com/reporting/3c1c4e41-c3d5-4bca-ac0c-af37e905b9d7)  
🌐 **Connect with Me**: [LinkedIn](https://linkedin.com/in/faheemkhanml)  
📂 **Source Code**: [GitHub Repository](https://github.com/FaheemKhan0817/Uber-Data-Analytics-End-To-End-Data-Engineering-Project.git)

---

## 🚀 Project Overview

This project builds a scalable data pipeline to process Uber trip data (e.g., `trips.csv`) and deliver interactive visualizations. The pipeline:
- **Ingests** raw data from a GCP Storage Bucket.
- **Processes** data using a Mage AI pipeline on a GCP VM instance.
- **Stores** transformed data in BigQuery.
- **Visualizes** insights via a Looker Studio dashboard, showcasing metrics like trip volume, fares, and geographic trends.

### Workflow Diagram
```
[Start]
  ↓
[GCP Bucket (gs://uber-data-2025)]
  ↓
[VM Instance (uber-data-instance)]
  ↓
[Install Docker]
  ↓
[Run Mage AI Container]
  ↓
[Mage AI Pipeline]
  ├───>[Data Loader Block]───>[Load Data (trips.csv)]
  │     ↓
  ├───>[Transformer Block]───>[Transform Data (clean, convert types)]
  │     ↓
  └───>[Data Exporter Block]───>[Export to BigQuery]
        ↓
[BigQuery (uber_data_dataset.trips_table)]
  ↓
[Looker Studio]
  ↓
[Uber Dashboard Visualization]
  ↓
[End]
```

---

## 🛠️ Tools & Technologies

- **Google Cloud Platform (GCP)**:
  - **Cloud Storage**: Stores raw data (e.g., `gs://uber-data-2025/trips.csv`).
  - **Compute Engine**: Hosts the VM instance (`uber-data-instance`).
  - **BigQuery**: Stores transformed data (`uber_data_dataset.trips_table`).
- **Docker**: Containerizes Mage AI for pipeline orchestration.
- **Mage AI**: Builds and manages the ETL pipeline (Extract, Transform, Load).
- **Looker Studio**: Creates interactive dashboards for data visualization.
- **Python**: Powers data processing in Mage AI (e.g., Pandas for transformations).
- **SQL**: Queries data in BigQuery.

---

## 📂 Project Structure

```
Uber-Data-Analytics-End-To-End-Data-Engineering-Project/
├── data/
│   └── uber_data.csv               # Sample Uber trip data
├── mage_pipeline/
│   ├── data_loader.py         # Loads data from GCP Bucket
│   ├── transformer.py         # Cleans and transforms data
│   └── data_exporter.py       # Exports to BigQuery
├── docker-compose.yml         # Docker configuration for Mage AI
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```

---

## ⚙️ Setup Instructions

Follow these steps to replicate the project locally or on GCP.

### Prerequisites
- Google Cloud account with billing enabled.
- Docker installed on your machine or VM.
- Python 3.8+ installed.
- GCP SDK (`gcloud`) configured.
- Access to BigQuery and Looker Studio.

### Step-by-Step Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/FaheemKhan0817/Uber-Data-Analytics-End-To-End-Data-Engineering-Project.git
   cd Uber-Data-Analytics-End-To-End-Data-Engineering-Project
   ```

2. **Set Up GCP**
   - Create a GCP project (e.g., `uber-data-project`).
   - Enable APIs: Cloud Storage, Compute Engine, BigQuery.
   - Create a Storage Bucket: `gs://uber-data-2025`.
   - Upload `trips.csv` to the bucket.
   - Create a VM instance (e.g., `uber-data-instance`, n2-standard-4, Ubuntu 20.04).

3. **Install Docker on VM**
   ```bash
   sudo apt-get update
   sudo apt-get install -y docker.io
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

4. **Run Mage AI Container**
   ```bash
   docker run -p 6789:6789 -v $(pwd)/mage_pipeline:/home/src mageai/mageai
   ```
   - Access Mage AI at `http://<VM_EXTERNAL_IP>:6789`.

5. **Configure Mage AI Pipeline**
   - Create a new pipeline in Mage AI.
   - Add blocks:
     - **Data Loader**: Load `uber_data.csv` from `gs://uber-data-2025`.
     - **Transformer**: Clean data (e.g., remove nulls, convert dates).
     - **Data Exporter**: Export to BigQuery (`uber_data_dataset.table`).
   - Authenticate GCP in Mage AI (use service account key).

6. **Set Up BigQuery**
   - Create a dataset: `uber_data_dataset`.
   - Let Mage AI create the table (`table`) during export.

7. **Create Looker Studio Dashboard**
   - Connect Looker Studio to BigQuery (`uber_data_dataset.table`).
   - Build visualizations (e.g., bar charts for trip volume, maps for pickup locations).
   - View the dashboard: [Link](https://lookerstudio.google.com/reporting/3c1c4e41-c3d5-4bca-ac0c-af37e905b9d7).

8. **Run the Pipeline**
   - Execute the pipeline in Mage AI.
   - Verify data in BigQuery and visualizations in Looker Studio.

---

## 📊 Dashboard Highlights

The Looker Studio dashboard provides insights into Uber trip data, including:
- **Trip Volume**: Daily/monthly trip counts.
- **Average Fares**: Trends over time.
- **Geographic Heatmaps**: Pickup and drop-off locations.
- **Trip Duration**: Distribution of trip lengths.

🔗 **View Dashboard**: [Looker Studio](https://lookerstudio.google.com/reporting/3c1c4e41-c3d5-4bca-ac0c-af37e905b9d7)

---

## 🎥 Video Explanation

For a detailed walkthrough of the project, including setup and pipeline execution, check out my YouTube video:

🔗 **Watch Now**: [YouTube Video](https://youtu.be/bwKvjfUDKac)

---

## 🌟 Why This Project?

This project demonstrates my skills in:
- **MLOps**: Orchestrating pipelines with Mage AI and Docker.
- **Cloud Engineering**: Leveraging GCP for storage, compute, and analytics.
- **Data Engineering**: Building robust ETL pipelines.
- **Data Visualization**: Creating impactful dashboards with Looker Studio.

---

## 👨‍💻 About Me

Hi, I’m **Faheem Khan**, a passionate **Machine Learning Engineer** and **Data Engineer** specializing in MLOps, cloud platforms, and data pipelines. I’m actively seeking opportunities to build scalable AI solutions.

- **LinkedIn**: [Faheem Khan](https://linkedin.com/in/faheemkhanml)
- **GitHub**: [FaheemKhan0817](https://github.com/FaheemKhan0817)
- **Portfolio**: [Faheem Khan](https://www.datascienceportfol.io/Faheem_Khan)

---

## 🙌 Acknowledgments

- **Darshil Parmar** YouTube tutorials.
- **Mage AI** and **GCP** communities for excellent documentation.

---

## 📬 Get in Touch

Interested in collaborating or hiring? Reach out via [LinkedIn](https://linkedin.com/in/faheemkhanml) or explore the code on [GitHub](https://github.com/FaheemKhan0817/Uber-Data-Analytics-End-To-End-Data-Engineering-Project.git). Let’s build something amazing together! 🚀

---