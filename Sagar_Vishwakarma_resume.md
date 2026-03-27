# SAGAR VISHWAKARMA

[(551) 362-7679](tel:5513627679) | [sagar.vishwakarma042@gmail.com](mailto:sagar.vishwakarma042@gmail.com) | [LinkedIn](https://www.linkedin.com/in/sagar-vishwakarma042/) | [GitHub](https://github.com/sagarv42) | [GitHub](https://github.com/sagarsv04)

Data Scientist and ML Engineer with 8+ years of experience, skilled in various programming languages, frameworks, models, and proficient in building pipelines and deploying models to production.

---

## SKILL

| Category | Technologies |
|-----------|-------------|
| **Languages** | Python, Go, Rust, Julia, C, C++, JavaScript, Scala, Bash, R, SQL, NoSQL |
| **Library** | Keras, TensorFlow, PyTorch, PySpark, Pandas, Numpy, Scipy, Scikit-learn, Matplotlib, NLTK, OpenCV, RegEx, FastAPI, LangChain, XGBoost |
| **Others** | NLP, DNN, CNN, LSTM, RNN, Word2Vec, Random Forest, GAN, LLM, Apache Spark, CUDA, Statistics, Computer Vision, Predictive & Descriptive Models, Forecasting, Docker, Kubernetes, Argo CD, Luigi, Airflow, MLOps, DevOps, Git, gRPC, Rclone, Hadoop, Snowflake, Pinecone, Elasticsearch, SageMaker, MLFlow, Grafana, MATLAB, Prometheus, ONNX, Databricks, AWS Bedrock, AWS Cloud Services, Oracle Cloud Infrastructure |

---

## EXPERIENCE

### Machine Learning Engineer - Kargo, Hybrid, US
**Jan 2025 -- Present**

**Direct-OBC Bid Optimization** *(Python, Go, C++, Rust, ONNX, SageMaker, MLflow)*

- Collaborated with the Director of Data Science to build a daily SageMaker training pipeline for a custom Hurdle Negative Binomial win rate prediction model, with 50+ categorical features, dynamic time-window lookback, and comprehensive QA gates validating parity across Python, ONNX
- Built an end-to-end multi-language inference pipeline (Python → ONNX → C++ → Go), achieving **~0.4ms latency** and **100K+ requests/sec** per host with zero-network-overhead in-process inference
- Designed and implemented a Go-based ML client with CGO wrapper for C++ ONNXRuntime, working with the header bidding team to integrate into Kargo's real-time bidding and pacing platform serving **350K+ requests/sec** across 4 global regions

**Creative Intelligence** *(Rust, Python, FastAPI, AWS Bedrock, Claude LLM, Kubernetes)*

- Collaborating with cross-functional teams across US and UK to improve creative scoring technology, building a multi-service system that analyzes ad creatives using LLM-powered analysis (Claude, Qwen, GPT-4o) and Random Forest models to predict CTR and VCR, deployed on AWS EKS
- Developed a Rust CLI tool for creative HTML rendering, asset extraction, animation derivation, and OCR analysis, producing 86+ scoring factors for creative performance evaluation
- Architected a config-driven LLM switching system enabling seamless migration between models (Qwen → Claude Opus) without code changes, reducing vendor lock-in

**Cohort Intelligence** *(Go, Python, Qwen vLLM, AWS Bedrock, Kubernetes)*

- Built faster and cheaper in-house LLM-based solutions as replacements for IBM Watson (IAB classification with 704 labels + 8 Plutchik emotions) and Diffbot (keyword extraction) APIs, benchmarking Claude, DeepSeek, and Qwen for accuracy vs. cost trade-offs, with prompt caching achieving **2.6x speedup**
- Collaborating with teams across US and UK to improve cohort and identity-based projects, building async classification and keyword extraction APIs deployed on Kubernetes with Tailscale ingress, serving content targeting for Kargo's platform

**ML Platform** *(Python, Go, C++, ONNX, SageMaker, MLflow, Kubernetes)*

- Working with the team to build Kargo's ML platform, solving core infrastructure challenges including model versioning and registry management, automated training pipeline orchestration, multi-language inference serving (Python/ONNX/C++/Go), feature store design, and model governance with automated DEPLOY/HOLD/RETRAIN decisions

**Supply Shaper** *(Go, gRPC, Kubernetes, Grafana, SageMaker)*

- Provided monitoring and oncall support for the Supply Shaper pipeline and inference service (Go/gRPC) handling multiple models (OptimalBidCPM, DynamicFloor, VideoStart) across 4 global regions, managing Grafana alerts, debugging timeout issues during **1.4M requests/sec** stress tests, and maintaining Kubernetes HPA configurations

**Vector Embeddings** *(Python, SageMaker, AWS Batch, AWS Bedrock, Pinecone, Snowflake)*

- Collaborated with the product team to build a daily SageMaker Pipeline leveraging AWS Batch that processes millions of records across all e-commerce catalogs (CTV, Facebook, OpenWeb), handling both new additions and updates of 6GB+ JSONL files with parallel image downloads, Bedrock embedding generation, checkpoint recovery, and upserting to Pinecone vector database

**Video Recommender** *(Python, PySpark, AWS Glue, Snowflake, CloudFormation)*

- Collaborated with data scientists to build a Spark-based video recommendation pipeline on AWS Glue, integrating Snowflake for data I/O and deploying with CloudFormation and Step Functions for orchestration

**VidiVision** *(FastAPI, Python, Docker, Kubernetes, fal.ai)*

- Collaborated with the VP of Data and Analytics to build and deploy a video creative analysis API to Kubernetes, leveraging parallel multi-model inference (Moondream2, Whisper, GOT-OCR, SAM3) via fal.ai to generate creative quality scores, retention curves, and brand safety signals

### Data Scientist - Oracle, Remote, US
**Jul 2021 -- Jun 2024**

**Identity Graph Core** *(Python, Scala, Spark, Docker, Kubernetes, ArgoCD, Luigi)*

- Developed ML pipelines for processing and modeling online and offline personal data, applying entity resolution techniques and utilizing XGBoost model to create identity profiles, enabling advertisers to reach targeted audiences effectively
- Migrated ML pipelines from Qubole/AWS to OCI, processing terabytes of data and optimizing Spark jobs to enhance performance and reduce compute costs
- Streamlined the opt-out process for audience removal from targeted ads, ensuring user privacy and cutting down our delivery time by almost **48 hours**

**Rotational Program** *(Python, Keras, Spark)*

- Led the Retail Taxonomy project under the **Activation Applied Research** team, replacing the legacy manual string comparison system with a 1D CNN model that achieved **81% accuracy**, significantly impacting around **$92 million** across OA products
- Developed a data validation regression suite for **Moat Reach** to ensure the correctness and consistency of reach, frequency, and impression numbers, as well as graphs across different feature tabs
- Trained a new **word2vec** model in the **Emergent Product** team, incorporating an updated vocabulary to improve embedding vectors for current keywords. Trained on approximately **150GB** of keyword data to enhance target rate prediction accuracy
- Grapeshot applies TF-IDF to a webpage's text data to identify top terms and matches them with segment-specific terms, filtering key terms based on their relevance to the URL content. Developed and compared **DNN as regression models** using both key terms and webpage text data to assess performance differences between models

### Graduate Research Assistant - The Research Foundation for SUNY, New York, US
**Aug 2020 -- May 2021**

- Developed machine learning models to predict server load in data centers, utilizing current resource usage to optimize resource allocation and improve energy efficiency in cloud computing, resulting in up to **32% energy savings**. This research was published in a peer-reviewed paper

**Publication:** *Latency-Aware Dynamic Server and Cooling Capacity Provisioner for Data Centers*

### Data Science Intern - Oracle, Remote, US
**Jun 2020 -- Aug 2020**

- Conducted research on alternative methods to predict future action-takers based on previous server data transfer feeds for audience recommendation tool, using a **28-day** SDT rollup window defined before buyers are identified. Employed two-sample t-tests to compare both approaches, integrating A/B testing and causal inference to evaluate the effectiveness of the new prediction model

### Analyst ML/AI - Decimal Point Analytics, Mumbai, India
**Sep 2017 -- May 2019**

**Scoring Model** *(Python, Keras, NLTK, Flask, EC2, RDS, Redis)*

- Implemented mathematical models to generate credit ratings for companies in the USA and Canada, incorporating financial quarter reporting, stock prices, and sentiment analysis from news articles to produce a weighted score for investment strategies

**RoboAdvisor** *(Julia, Node.js, MySQL)*

- Collaborated with finance professionals to develop a Portfolio Recommendation and Rebalancing system for the Indian market. The server uses the Black-Litterman model and Monte Carlo simulation for portfolio generation and performance insights and an API to handle user requests and server interactions

**Transaction Classify** *(Python, Keras, NLTK, NER)*

- Developed an application using NLP and CNN models to classify bank transaction data, detect anomalies, and identify potential fraud, while also analyzing user purchase patterns to provide recommendations based on purchase history

**Portfolio Manager** *(C#, ASP.Net, Javascript, MySQL)*

- Developed a web portal using ASP.Net Core MVC to help users manage portfolios, receive tailored recommendations, and track investments. Integrated loan calculators for effective financial planning. Collaborated with a team of developers and finance professionals

**ATRS** *(Python, Scikit-learn, Matplotlib, MySQL)*

- Developed applications to predict buy, hold, or sell decisions using OHLC data, incorporating technical indicators and weights from other indices. Trained multiple models and averaged predictions to provide recommendations

### Software Engineer - Electropneumatics & Hydraulics(I) Pvt. Ltd., Mumbai, India
**Sep 2016 -- Aug 2017**

**PLC Executor** *(C, C++)*

- Worked in a team of four to develop a PLC ladder logic compiler in C, compatible with Linux environments and embedded systems using the GCC compiler

**Hal LinuxCNC** *(C, C++, Linux Kernel)*

- Utilized HAL LinuxCNC to develop a series of building blocks, which were then employed to seamlessly interconnect with the PLC compiler. Mapped GPIOs and data registers to ensure precise control and data flow from the PLC to the LinuxCNC

**Alekh** *(Python, Numpy, Pandas, Matplotlib)*

- Developed an application to visualize graphs and plots from labeled data in CSV files. Utilized PyQt for the GUI, and employed NumPy and Matplotlib for efficient numerical computing and plotting, which enhanced data analysis and decision-making

**My Machine** *(Python, C++, Redis, MQTT)*

- Created an interactive application module for monitoring and controlling the Siemens 828D CNC Controller. Used the OPC UA Python library for communication, PyQt for the GUI, and integrated Redis and MQTT for logging and remote control, ensuring effective management of the CNC system

---

## ACADEMIC

### Binghamton University, State University of New York
**Aug 2019 -- May 2021**

- Worked with the Robot Operating System (ROS) to control and navigate a Turtlebot in both virtual (Gazebo) and real-world environments. Developed functionality for autonomous navigation using scanned maps and 3D image data, allowing Turtlebot to move from point to point. Implemented computer vision techniques for tracking and following a ball while maintaining a safe distance. Integrated natural language processing to enable Turtlebot control via voice commands, enhancing interactive capabilities
- Developed an MNIST handwritten digit recognition system from scratch in C++ using **CUDA** for accelerated computing. Implemented a K-Nearest Neighbors (KNN) algorithm with a KD Tree, optimizing it to run in parallel on the CPU using threads for enhanced performance
- Developed a handwritten digit recognition system using digital image processing techniques. Implemented a Deep Neural Network from scratch with activation, loss, and error functions using NumPy. Built a **Generative Adversarial Network** (GAN) in PyTorch to generate additional handwritten digit samples, enhancing the dataset for training supervised models. Additionally, utilized PyTorch to create a handwritten digit recognition system using **Capsule Networks**, improving the model's ability to learn hierarchical and spatial relationships between features compared to traditional **CNNs**
- Implemented key functions of the Chord distributed hash table (DHT) to manage distributed data efficiently. Developed a distributed key-value store to facilitate communication and data exchange among various entities within the system
- Developed a character device driver in C++ to list processes at the kernel level, enhancing system monitoring capabilities. Additionally, created a kernel module to track page faults based on process IDs, providing detailed insights into memory management and fault handling

---

## EDUCATION

**Master's in Computer Science** - Binghamton University, State University of New York — **May 2021**<br>
Courses: Social Media Data Science, Distributed Systems, High-Performance Computing, Robotics

**Bachelor's in Electronics Engineering** - Rizvi College of Engineering, Mumbai, India — **May 2016**<br>
Courses: Structured Programming, Microcontrollers, Digital Image Processing, Robotics, Microprocessors, Power Electronics, Discrete Electronics, Applied Mathematics

---

## NOTABLE

**Creative Scoring Bot - Kargo Hackathon Winner** — **2025**<br>
Worked with designers from the creative team to build a Slack bot using Python, Slack Bolt, and OpenAI GPT-4o that provides instant AI-driven creative feedback, analyzing ad images against curated examples and historical performance data, delivering scores and actionable suggestions in Slack threads

**Machine Learning in Production** - DeepLearning.AI, Coursera — **Feb 2025**<br>
Courses: Data Definition and Baseline, Modeling Challenges and Strategies, Lifecycle and Deployment

**Generative AI with Large Language Models** - DeepLearning.AI, Coursera — **Aug 2024**<br>
Courses: Transformer Architecture, Project Lifecycle, Model Pre-training & Fine-tuning, Reinforcement Learning

**Data Science Hackathon** - Binghamton University, State University of New York — **Jul 2020**<br>
Won 2021 hackathon by developing a cosine similarity-based movie recommendation model

**Mathematics for Machine Learning** - Imperial College London, Coursera — **Jul 2018**<br>
Courses: Linear Algebra, Multivariate Calculus, PCA

**Deep Learning Specialization** - DeepLearning.AI, Coursera — **May 2018**<br>
Courses: Deep Neural Networks, Hyperparameter Tuning, Regularization and Optimization, CNN, Sequence Models
