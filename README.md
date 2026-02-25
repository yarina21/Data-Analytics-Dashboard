💰 Wealth Manager - Full-Stack Finance Tracker
A modern personal finance application built to track, analyze, and visualize transactions in real-time. This project demonstrates a complete integration between a high-performance FastAPI backend and a sleek, responsive Tailwind CSS frontend.

🚀 Features
Full CRUD Functionality: Create, Read, and Delete financial transactions with persistent storage.

Real-Time Analytics: Automatic calculation of total balance and transaction counts.

Data Visualization: Interactive Doughnut Chart that breaks down spending by category using Chart.js.

Smart Data Processing: Uses Pandas on the server side to aggregate and group financial data efficiently.

Modern UI: Dark-mode, glassmorphic design built with Tailwind CSS.

Responsive Connection: Seamless communication between the UI and the Python server via REST API and CORS.

🛠️ Tech Stack
Backend
Python 3.10+

FastAPI: Modern, high-performance web framework.

SQLAlchemy: SQL toolkit and Object-Relational Mapper (ORM).

SQLite: Lightweight, serverless relational database.

Pandas: Data analysis library for aggregating spending metrics.

Frontend
HTML5 / JavaScript (ES6+)

Tailwind CSS: Utility-first CSS framework for modern styling.

Chart.js: Flexible JavaScript charting for data visualization.


📊 API Endpoints
GET /transaction - Fetch all recorded transactions.

POST /transaction - Add a new transaction (Title, Amount, Category).

DELETE /transaction/{id} - Remove a specific transaction.

GET /stats - Get aggregated spending data and category breakdown for the charts.
