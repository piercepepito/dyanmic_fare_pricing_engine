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

**Final Fare:**

$$
\text{Final Fare} = \text{Base Cost} \times \text{Surge Multiplier}
$$

## Functional Requirements
### Rule Evaluation
- [x] FR-001: Accept valid distance and duration values
- [x] FR-002: Accept *demand* and *supply* information
- [] FR-003: Calculate the base fare
- [] FR-004: Evaluate the applicable pricing numbers
- [] FR-005: Apply the correct surge multiplier
- [] FR-006: Enforce max surge multiplier
- [] FR-007: Handle zero available drivers safely
- [] FR-008: Return a fare breadkown

### Caching
- [] FR-009: Cache frequently requested route information
- [] FR-010: Implement cache expiration (TTL)
- [] FR-011: Track cache hits and misses

## Non-Functional Requirements

## Business rules

## Inputs and Outputs

## Expected System Behavior

## Out of Scope Features (future phases)
1. Calling in Google Maps API to calculate the distance from the origin to the desination