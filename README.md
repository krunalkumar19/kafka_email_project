# 📧 Kafka Email Streaming Pipeline (KRaft Mode, Python)
Using simple Kafka server with python to produce script that takes only email id from producer and uses consumer script to save it in .txt file.

This project demonstrates a lightweight **Kafka-based email ingestion pipeline** using Python. It showcases how to capture user input (email addresses), stream it through Apache Kafka, and consume it in real time — all without ZooKeeper, using **KRaft mode** for Kafka.

---

## 🚀 Project Overview

This project includes:

- A **Python Producer** script that:
  - Accepts user emails via terminal input.
  - Validates and saves them to a local file (`emails.txt`).
  - Sends the emails as Kafka messages to a topic called `user-signups`.

- A **Python Consumer** script that:
  - Connects to the Kafka topic.
  - Continuously listens for new messages.
  - Prints the received emails to the terminal.

- A **Kafka environment** running in **KRaft (Kafka Raft Metadata) mode** — no ZooKeeper needed.

---

## 🧱 Tech Stack

- **Apache Kafka** (KRaft mode - no ZooKeeper)
- **Kafka-Python** (Producer & Consumer)
- **Python 3.8+**
- **Command Prompt / Windows Batch Execution**
- **File-based storage (`emails.txt`)**

---

## 🎯 Use Case

This simple pipeline can be extended for:
- Real-time user sign-up ingestion.
- Data streaming for analytics or ETL pipelines.
- Integrating with databases or dashboards.
- Learning and demonstrating Kafka + Python integration.

---

## 📂 Repo Structure

