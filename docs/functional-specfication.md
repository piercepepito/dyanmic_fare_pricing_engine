# Project Overview
This portfolio project simulates a ride hailing company, and focuses a dynamic fare pricing engine that is highly dependent on the conditions of the ride.

## Objectives
1. Create a rule engine design
2. Testing
    1. Unit
    2. Integration
3. FastAPI Integration
4. Functions and Business Logic

## Scope
1. Calculate the fare dependent on the ride information details:
    1. Distance
    2. Estimated duration
    3. Pick up Zone

## API Requirements
- `POST /fares/calculate`
    - recieves ride information and marketplace conditions before calculating the fare

## Pricing Requirements
**Base Cost:**

$$
\text{Base Cost} = \text{Base Fare} + (\text{Distance} \times \text{Distance Rate}) + (\text{Duration} \times \text{Duration Rate})
$$

**Pre-discount Fare:**

$$
\text{Pre-discount Fare} = \text{Base Cost} \times \text{Surge Multiplier}
$$

**Final Fare:**

$$
\text{Final Fare} = \max(0, \text{Pre-discount Fare} - \text{Promotion Discount})
$$

## Functional Requirements
### Rule Evaluation
- [x] FR-001: Accept valid distance and duration values
- [x] FR-002: Accept *demand* and *supply* information
- [x] FR-003: Define demand and supply rules
- [x] FR-004: Create rule engine for demand and supply
- [x] FR-005: Define time based rules
- [x] FR-006: Create rule engine for time based rules
- [x] FR-007: Define promos
- [x] FR-008: Create a rule engine for promos
- [x] FR-009: Calculate the final cost fare
- [x] FR-010: Enforce max surge multiplier
- [x] FR-011: Return final fare
- [x] FR-012: Added observability of cache performance

### Caching
- [x] FR-013: Cache frequently requested route information
- [x] FR-014: Implement cache expiration (TTL)
- [x] FR-015: Implement dynamic cache expiration for cache invalidation
- [x] FR-016: Implement Cache Eviction

## API
- [x] FR-017: Add API endpoint for fare_calculation

## Non-Functional Requirements
## Inputs and Outputs
Input:
1. distance: the estimated distance convered for the ride
2. duration: the estimated duration of the ride
3. datetime_str: the datetime request in string format
4. demand: the number of drivers inside an area
5. supply: the number of customers in an area
5. is_airport: If the destination or origin is an airport
6. partner_cc: if the credit card being used is part of the partner credit card of the simulated hail riding company
7. promo_name: The name of the promotion

Output:
1. total_fare: The total calculated fare while checking distance, duration, demand/supply, time based metrics, and promotions

## Expected System Behavior
### 1. Fare Calculation Request
- The system accepts a fare calculation request containing distance, duration, date and time, demand, supply, airport status, partner credit card status, and promotional information.
- The system validates the incoming request before performing any fare calculations.
- the system validates the functions response to ensure consistent format.
- Invalid requests are rejected with appropriate validation errors.

### 2. Fare Calculation
- The system calculates the base fare using the provided trip information.
- The pricing rule engine evaluates demand and supply conditions to determine the applicable multiplier.
- Time-based pricing rules are evaluated using the provided date and time.
- Applicable pricing modifiers, such as airport surcharges, partner credit card benefits, and promotional discounts, are applied.
- The system returns the calculated fare.

### 3. Caching
- The system checks Redis for a previously calculated fare matching the incoming request.
- If a valid cached result exists, the system returns the cached fare without recalculating it.
- If no cached result exists, the system calculates the fare and stores the result in Redis with an appropriate expiration time.
- If Redis is unavailable, the system continues the fare calculation without caching the result.

### 4. Error Handling
- Invalid inputs are rejected before fare calculation.
- Unexpected errors during fare calculation are handled without exposing internal system details to the client.
- Cache-related failures do not prevent the system from calculating and returning a fare.

### 5. Response
- The system returns the calculated fare in a structured response.
- The response includes the total fare and, where applicable, relevant pricing components or multipliers.
- The API returns appropriate HTTP status codes based on the outcome of the request.

## Out of Scope Features (future phases)
1. Calling in Google Maps API to calculate the distance from the origin to the desination