<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/resources/appIcon.png"  alt="App Icon" width="100" height="100">
  </a>

  <h1 align="center">Intellicash - AI Personal Finance guide</h1>

  <p align="center">
    Intellicash is a next-gen personal finance platform powered by Google Cloud services including Firebase, Vertex AI, and Fi Money's MCP server, delivering enterprise-grade financial intelligence with consumer simplicity.
    <br />
    <a href="#about-the-project"><strong>Start exploring »</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#why-intellicash">Why Intellicash?</a></li>
        <li><a href="#core-google-cloud-integrations">Core Google Cloud Integrations</a></li>
        <li><a href="#hybrid-ai-architecture">Hybrid AI Architecture</a></li>
        <li><a href="#enhanced-technical-stack">Enhanced Technical Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#run-the-code-locally-">Run the code locally</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#contributing-">Contributing</a>
      <ul>
        <li><a href="#how-to-get-started">How to get started</a></li>
        <li><a href="#why-to-contribute">Why to contribute?</a></li>
      </ul>
    </li>
  </ol>
</details>

## About the project

### 📸 Screenshots

|                                                                                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |
| :----------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| ![1](https://github.com/enrique-lozano/Monekin/blob/main/app-marketplaces/screenshots/en/Mockups/Diapositiva1.PNG) | ![2](https://github.com/enrique-lozano/Monekin/blob/main/app-marketplaces/screenshots/en/Mockups/Diapositiva2.PNG) | ![3](https://github.com/enrique-lozano/Monekin/blob/main/app-marketplaces/screenshots/en/Mockups/Diapositiva3.PNG) | ![4](https://github.com/enrique-lozano/Monekin/blob/main/app-marketplaces/screenshots/en/Mockups/Diapositiva4.PNG) |
| ![5](https://github.com/enrique-lozano/Monekin/blob/main/app-marketplaces/screenshots/en/Mockups/Diapositiva5.PNG) | ![6](https://github.com/enrique-lozano/Monekin/blob/main/app-marketplaces/screenshots/en/Mockups/Diapositiva6.PNG) |

### 🌟 Why Intellicash? 

- **Hybrid AI Intelligence**  
  Combines on-device processing with cloud AI through Fi Money's MCP server and Google Vertex AI.
- **Google Cloud Powered**  
  Enterprise-grade infrastructure with Firebase, Cloud Functions, and BigQuery analytics.
- **Smart Transaction Categorization**  
  Uses both local ML models and cloud AI for 98% accurate categorization.
- **Natural Language Processing**  
  Ask questions like "Show food spending last month" using Vertex AI's NLP.
- **Financial Forecasting**  
  Vertex AI time-series forecasting for budget predictions.
- **Unlimited Transactions**  
  Scales to millions of transactions via Firestore and Cloud SQL.
- **Multi-Device Sync**  
  Real-time data synchronization across devices with Firebase.
- **Advanced Security**  
  Google Cloud IAP, Secret Manager, and encryption at rest.
- **Open Source Core**  
  Fully transparent local-first architecture.

### 🚀 Core Google Cloud Integrations

1. **Firebase Platform**
   - Authentication with OAuth, biometrics, and 2FA
   - Firestore with offline persistence
   - Cloud Functions for transaction processing
   - Crashlytics for performance monitoring

2. **Vertex AI Services**
   - Custom financial classification models
   - AutoML Tables for cash flow forecasting
   - NLP for transaction memo analysis
   - Anomaly detection algorithms

3. **Google Cloud Infrastructure**
   - Cloud Run microservices
   - Pub/Sub event processing
   - Secret Manager for credentials
   - Cloud SQL for analytics

### 🔄 Hybrid AI Architecture

**Data Flow:**
[Device] → [Firebase] → [Cloud Functions] → [Vertex AI] → [BigQuery] ↑____________↓ ↑ [Local SQLite] [Fi Money MCP]


**Key Features:**
1. **On-Device Processing**
   - TensorFlow Lite models
   - Local SQLite database
   - Offline transaction recording

2. **Cloud Enhancements**
   - Vertex AI model serving
   - Firestore synchronization
   - MCP server integrations

3. **Security Model**
   - End-to-end encryption
   - IAM role-based access
   - Audit logging

### 🔧 Enhanced Technical Stack

**Frontend:**
- Flutter with Firebase plugins
- Google Maps Platform for location tagging
- Charts powered by Google Charts

**Backend Services:**
- Cloud Run containers
- Cloud Scheduler for batch jobs
- Memorystore for caching

**Data Pipeline:**
- Dataflow for ETL
- BigQuery analytics
- Looker Studio dashboards

**ML Operations:**
- Vertex AI Pipelines
- Model monitoring
- Continuous retraining
