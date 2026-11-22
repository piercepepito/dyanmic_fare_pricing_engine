# Pricing Rules and Business Logic

## 1. Overview
The pricing rules are what dictate the surge mutlipliers onto the base fare. There are 2 main components, which are: 
Demand/Supply and Time Based Rules.

## 2. Demand and Supply Rules

### 2.1 Demand/Supply Ratio
Demand and supply shows the relationship between the number of drivers vs the count of trip requests in that area.

Formula:
Demand/Supply Ratio = Demand / Supply

### 2.2 Pricing Conditions

| Condition | Multiplier |
|---|---:|
| Ratio > 2 | 2.2 |
| Ratio = 2 | 1.8 |
| 1 < Ratio < 2 | 1.5 |
| Ratio <= 1 | 1.0 |

A higher ratio would give a large surge multiplier mainly because there's a large amount of demand but very little supply, but will be maxed out when the ratio goes above 2. There's also a lower limit of 1, as it does not make sense if we give the base calculation a multiplier of less than 1.

## 3. Time-Based Rules

### 3.1 Weekday Rules
During weekdays, the rush hours is what usually dictate the supply/demand between drivers, and ride requests. In the morning, rush hour starts at about 7AM to 9AM. While in the afternoon it starts at about 4PM to 7PM.

### 3.2 Weekend Rules
During the weekends, areas around malls are what dictates the multiplier, especially during closing hours. Closing hours start an hour early which is around 8PM to 10PM. 

### 3.3 Business Rationale
Whenever the ride requests are around the rush hours, or during mall closing hours, then price usually goes up mainly because of the high demand of ride requests but the low availability of drivers.

## 4. Rule Evaluation and Execution
1. How are rules evaluated
    1. Demand/Supply rules
        1. Definition: Evaluated by priority based. Once a condition has been fulfilled, then the loop will end.
        2. Rules according to priority:
            1. Extremely high demand > 2
            2. High Demand 1.5 <= x <= 2
            3. Moderate Demand: 1 < x <= 1.5
            4. Normal Demand <= 1
    2. Time-based rules
        1. Definition: Pulls out all conditions that are succesful and takes the product.
        2. Conditions to look at:
            1. Is it a weekend?
            2. If during weekday, is it during a rush hour?
            3. If during weekend, is it during mall closing hours? 
    3. Promotions
        1. Definition: Only a single promotion can be used. The discount of the promotion, is highly dependent on the promotion conditions.
        2. What happens when no rule is matched?
            1. There will be no promotion discount, and the final fare will be the product of the base fare and the surge multiplier.

## 5. Combined Surge Multiplier

Once both the Demand/Supply and Time-Based multiplier has been calculated, the final formula will be:

Formula:
Surge Multiplier =
max(Demand/Supply Multiplier * Time-Based Multiplier, max_surge)

The reason as to why they are being multiplied is because both of these parameters influence in some way. When addition is being used, then it would mean that both have equal weights which isn't the case. A max surge is also being applied to give the users of the ride hailing app, a fair pricing strategy.

## 6. Assumptions and Limitations

The assumptions made in here is that besides the distance, and duration, prices usually go up depending on the number of driver and ride requests, and time based metrics such as if it is during a weekday/weekend, rush hour, or if the mall is closing. 

Although there are a lot more metrics to look at, the purpose of this project is to showcase the ability to create modular code, and break down the problem into sizeable chunks.

## 7. Future Improvements
1. Weather based pricing: during rainy days, whenever people are forced to ride taxis, that is when prices usually go up.
2. Location-based pricing: Areas where there is a lot of foot traffic would be a great metric to increase/decrease the surge multiplier.