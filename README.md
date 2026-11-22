# Dynamic Fare Pricing Engine

A backend application that calculates dynamic trip fares based on distance, duration, demand, supply, time-based pricing rules, and promotional discounts.

The project demonstrates how dynamic pricing systems can combine multiple independent pricing factors to calculate fares while using Redis caching to improve performance and reduce redundant calculations.

## Key Features

- **Dynamic Fare Calculation:** Calculates fares using trip distance and duration.
- **Demand and Supply Pricing:** Adjusts fares based on the relationship between available supply and customer demand.
- **Time-Based Pricing:** Applies pricing multipliers based on the time of the trip.
- **Rule Engine:** Separates pricing rules into independent components, making the pricing logic easier to maintain and extend.
- **Promotional Discounts:** Supports promotion codes with different discount calculations.
- **Redis Caching:** Stores previously calculated fares to reduce unnecessary recalculations.
- **Dynamic Cache TTL:** Determines cache expiration based on the time the trip has been requested.
- **Error Handling:** Handles cache failures without preventing fare calculations.
- **Automated Testing:** Includes unit and integration tests.

## Pricing Logic

The pricing engine calculates fares in two main stages.

### 1. Pre-discount Fare

The pre-discount fare is calculated by multiplying the base cost by the surge multiplier.

$$
\text{Pre-discount Fare} = \text{Base Cost} \times \text{Surge Multiplier}
$$

The surge multiplier combines independent pricing factors:

$$
\text{Surge Multiplier} = \text{Demand/Supply Multiplier} \times \text{Time-Based Multiplier}
$$

### 2. Final Fare

The applicable promotional discount is deducted from the pre-discount fare.

$$
\text{Final Fare} = \max(0, \text{Pre-discount Fare} - \text{Promotion Discount})
$$

The final fare cannot fall below zero.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| FastAPI | REST API framework |
| Pydantic | Request validation and response schemas |
| Redis | Cache system |
| Docker | Containerization |
| Docker Compose | Running application services |
| Pytest | Unit and integration testing |

## System Architecture

The application follows a layered structure:

- **API Layer:** Receives fare calculation requests and validates input.
- **Service Layer:** Coordinates fare calculations, caching, and business logic.
- **Rule Engine:** Evaluates demand/supply and time-based pricing rules.
- **Cache Layer:** Retrieves and stores calculated fares using Redis.
- **Calculator:** Combines the pricing components and applies promotional discounts whenever applied.

## Project Structure

```text
app/
├── api/
├── cache/
├── rules/
├── schemas/
├── services/
├── docs/
├── utils/
└── main.py

tests/
├── unit/
└── integration/

.env
.pytest.ini
Dockerfile
compose.yaml
requirements.txt
```

## Running the Application

### Prerequisites

- Python
- Docker
- Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/piercepepito/dyanmic_fare_pricing_engine
```

### 2. Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run with Docker Compose

```bash
docker compose up --build
```

### 4. Access the API

Once the application is running, access the FastAPI interactive documentation at:

```text
http://localhost:8000/docs
```

## Testing

Run all tests (unit and integration):

```bash
python -m pytest
```

## Project Goals

This project was made for backend engineering concepts, such as:

- Designing modular and maintainable pricing logic.
- Implementing rule-based dynamic pricing from time-based and demand/supply metrics.
- Understanding caching strategies and cache expiration.
- Handling failures in external infrastructure such as Redis.
- Writing unit and integration tests for backend services.

**Note:** This is a learning and portfolio project focused on demonstrating backend engineering principles through a simplified dynamic pricing system.