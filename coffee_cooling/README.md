# Coffee Cooling Model

This project models the cooling of coffee in a ceramic mug using Newton's Law of Cooling.

## Model
dT/dt = -k(T - T_room)

where T is the coffee temperature, T_room is the room temperature, and k is the cooling constant. 

## Data

The data is synthetic data measured every minute for two hours. 

## Method 

Euler's method was used to approximate the solution for different values of k. The model was compared to the data using residuals. 

## Result 

The best tested value was approximately: 

k = 0.025

## What I Learned

- How to model a physical process with a differential equation 
- How to compare model predictions with data
- How residuals help measure error
- How parameter estimation works in a simple applied math setting 