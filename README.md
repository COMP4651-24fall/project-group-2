[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jzfQvm5J)
# Project
# Distributed Web Scraping: Local vs Cloud-Based Approaches

## **Overview**
This project explores and compares two approaches to distributed web scraping:
1. **Local parallel computing** using PySpark.
2. **Cloud-based distributed computing** using AWS.

The goal is to efficiently scrape large datasets, such as cryptocurrency data from **CoinMarketCap**, and analyze the performance, scalability, and resource utilization of these methods.

---

## **Approaches**

### **1. Local Parallel Computing**
- Utilized PySpark to distribute scraping tasks across CPU cores on a single machine.
- Improved execution time for small-to-medium datasets, but faced scalability limitations with larger workloads.

### **2. Cloud-Based Distributed Computing**
- Implemented a **Master-Slave architecture** on AWS EC2 instances with WebSocket communication for task distribution.
- Achieved seamless scalability and faster execution for large datasets, leveraging cloud resources effectively.

---

## **Tools Used**
- **Amazon Web Services (AWS)**: For cloud-based scalability.
- **Selenium**: For dynamic web scraping.
- **WebSocket**: For real-time communication between nodes.
- **PySpark**: For local parallelization.

---

## **Key Results**
- **Local Scraping**: Best for small-scale tasks, but limited by hardware.
- **Cloud-Based Scraping**: Superior for large datasets, offering scalability, reliability, and faster processing.

---
