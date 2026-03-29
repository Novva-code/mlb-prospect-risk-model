# MLB Prospect Risk Model

## Overview
This project aims to determine whether a AAA-level MLB batting prospect will have a successful Major League career using performance from their first 200 plate appearances (PA) at the AAA level.

## Definition of Success
A successful career is defined as:
- Career WAR > 5.0

## Methodology (Planned)
- Collect AAA batting data for players between 2007–2012
    - Players are limited to those aged 26 or younger during their first 200 AAA plate appearances. Age is calculated as a plate-appearance-weighted average across the player’s initial AAA sample. 
- Aggregate each player’s first 200 AAA plate appearances
- Engineer key performance features (wRC+, K%, BB%, ISO)
- Train a classification model to predict career success

## Handling Missing MLB Data
Players who did not appear in the MLB dataset were assigned a career WAR of 0, under the assumption that they did not have a meaningful major league career.

---

## Limitations

### 1. Elite Prospect Exclusion
Elite prospects who skip AAA entirely are not included in this dataset. These players are typically high-certainty successes, meaning the model may underrepresent top-tier talent and instead focus more on mid-tier prospects.

### 2. Selection Bias
The model only includes players who reached AAA and accumulated at least 200 plate appearances. As a result, it excludes earlier-stage prospects and does not represent the full player development pipeline.

### 3. Model Timeframe
The dataset is limited to AAA seasons from 2007–2012. Changes in league environment, player development, and offensive trends over time may limit how well the model generalizes to modern players.

### 4. Small Sample Size (Early Evaluation Window)
Each player is evaluated using only their first 200 AAA plate appearances. While this reflects an early scouting window, it introduces variability due to the small sample size in a high-variance sport like baseball.

### 5. Lack of Contextual Adjustments
The model does not completely adjust for external factors such as park effects (with the exception of wRC+), league difficulty, or quality of competition. These factors may influence raw performance statistics.

### 6. Snapshot Limitation
The model evaluates players based on a single early-career snapshot and does not account for player development, adjustments, or long-term growth trajectories.

### 7. Defense
The model does not evalute defensive value provided by players. Prospects whose primary tools are defensive will be appear undervalued.

---

## Future Improvements
