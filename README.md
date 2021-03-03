---
tags: CSC412
---

# CSC412/2506 Project Proposal

**Group Name:** Reasonable Subway Surfers

| Name        | Email                        | Student Number |
| ----------- | ---------------------------- | -------------- |
| Zizhao Chen | zizhao.chen@mail.utoronto.ca | 1005400353     |
| Roland Gao  | roland.gao@mail.utoronto.ca  | 1005762293     |
| Robert Wu   | rupert.wu@mail.utoronto.ca   | 1004256798     |

## TL;DR: Short Abstract

Develop an application of **bayesian filters** for the problem of **state estimation** for the [Toronto Subway System](http://ttc.ca/Subway). After collecting discrete or continuous data domains for state/observation, we attempt to recursively estimate our position and orientation/direction at each iteration.

## Extended Abstract

### Summary of Technical Aspect

Bayesian Filters (aka recursive bayesian estimation) are a method for estimating unknown probability distributions recursively over time using incoming measurements and a mathematical process model.

- Data can be defined as {$(u_i,z_i)$ for action $u_i$ and observation $z_i$}.
- The a priori estimation $P(x)$ gives the probability of being in state $x$.
- The action model $P(x|u,x')$ gives the probability of arriving at state $x$ when taking action $u$ with state $x'$.
- The sensor model can be expressed as $P(z|x)$.
- The posterior of the state is defined as $Bel(x_t) = P(x_t | (u_1,z_1),...,(u_t,z_t)) = P(x_t | (u_{t},z_{t}, x_{t-1}))$
- At each iteration, given $u_t,z_t$, update $Bel(x_t)$ by using the following equation where $\lambda$ normalizes the total probability of $Bel(x_t)$ to 1.
  $$Bel(x_t) = \lambda P(z_t|x_t) \int P(x_t|u_t,x_{t-1})Bel(x_{t-1})dx_{t-1}$$
- In this project, we obtain the action model $P(x|u)$ and the sensor model $P(z|x)$ by Monte Carlo sampling.

#### Toronto Subway System

The Toronto Subway System is large and varied enough to provide an interesting domain to this problem. By no means is this an exhaustive list but here are some observations we might be looking for.

- There are plenty of features that can be interpreted from observations at every iteration.
  - Station observation.
    - Lighting properties.
      - Lighting level.
      - Shade of light.
    - Platform orientation.
      - Side platforms? Island platform? Anything special?
    - Distances within the station _(continuous)_.
      - Average perpendicular distance from walls/other train.
      - Height of the ceiling above.
    - Ridership _(can be interpreted as continuous)_.
      - Number of patrons boarding/alighting the train.
      - Number of patrons currently on the train.
    - How long the train holds?
  - Track observation (nice-to-have).
    - Above or underground?
    - Length of track between stations; distance from last station _(continuous)_.
    - This will be considered a nice-to-have because these are continuous measurements.
    - Curvature of the track segment.
- The state that we're estimating could have several components as well.
  - Time of day.
  - Direction of travel.
  - Travel path.
- The domain is sufficiently large (~70 subway stations) and has enough entropy to be interesting.
  - But it is also not too complicated for the scope and timeframe for our project.
- We may exclude Line 3 because it's mostly above-ground, and Line 5 because it's still under construction.
- Some values will be extracted from publicly available datasets (TTC, Wikipedia, City of Toronto).
  - Others may have to be estimated, randomly generated or omitted.
    - Gaussian distributions might be simple for generated data.
- We will incorporate some noise with the continuous observations, and possibly for the some discrete observations.
  - Bias values and other adjustments may have to be introduced some of the noisy data.
- Some observations will naturally be inconclusive due to exceptions or unknown data.
  - For example, Union Station's platform orientation could be misinterpreted as an island for having one between two tracks, or as side for having two platforms.

### Project Deliverable Goals

- The dataset of the Toronto Subway System stations compiled from quantitative public sources (numbers, tables, etc.) and qualitatively estimated from photographs.
- Code implementation in Julia for Bayesian Filters.
- Several test cases to verify the correctness and expected behaviour of using Bayesian Filters in this problem domain.
  - For example, a test case might have very limited information about its path.
    - Perhaps just a couple of subway stations?
    - Or large gaps between stations?
  - We can provide animated GIFs as deliverables to demonstrate the behaviour.
  - One quality measurement can be the amount of time it takes for the Bayesian Filters to converge.
  - Another quality could be the accuracy and precision of the estimation on convergence.

### Nice-to-Haves

- Applying particle filtering to generalize.
- Using more _continuous_ observations.
- Prediction more state features.
  - Example: how many passengers are currently on the train?
- Feature engineering: select the most relevant features to build a sparse model.

### Review of related work

Bayesian Filtering techniques extended Kalman Filter to work with non-Gaussian distributions. Well-established resources of Bayesian Filters are provided as follows.

- [Novel approach to nonlinear/non-Gaussian Bayesian state estimation by Goron, Salmond & Smith, 1993](https://www3.nd.edu/~lemmon/courses/ee67033/pubs/GordonSalmondSmith93.pdf)
- [Bayesian Filtering for Location Estimation by Fox, 2003](https://rse-lab.cs.washington.edu/postscripts/bayes-filter-pervasive-03.pdf)
- [Bayesian Filtering from Kalman Filters to Particle Filters and Beyond by Chen, 2003](https://www.researchgate.net/profile/Zhe-Chen-99/publication/238689222_Bayesian_Filtering_From_Kalman_Filters_to_Particle_Filters_and_Beyond/links/53f633fe0cf22be01c40ff3f/Bayesian-Filtering-From-Kalman-Filters-to-Particle-Filters-and-Beyond.pdf)

#### Data Sources

The following sources will be used to compile a spreadsheet of data for all the subway stations.

- Wikipedia.
- TTC (public website and articles).
- City of Toronto (building specifications and construction permits).
- Google Images.
- Rupert's 21 years of living in Toronto.
