# RLC Circuit Simulation (Euler's Method)
This project aims to showcase how Euler's Method could be used to numerically solve the differential equation of an RLC circuit.

## Acknowledgement
Euler's Method is not the most accurate or computationally efficient method of numerically solving differential equations. This is simply showcasing how Euler's Method and other numerical analysis methods could be applied to problems in Electrical Engineering.

## Units

| Quantity        | Base Unit | Symbol |
| --------------- | --------- | ------ |
| Resistance      | Ohm       |   R    |
| Inductance      | Henry     |   L    |
| Capacitance     | Farad     |   C    |
| Electric Charge | Coulomb   |   q    |
| Electric Current| Ampere    |   i    |


## RLC Circuit Second-Order Differential Equation
The differential equation for a series RLC circuit is typically denoted as follows:
```math
L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{1}{C}q=E(t)
```

Recall that:
```math
\frac{dq}{dt} = i
```

Given this, we can rewrite the equation as:
```math
L\frac{di}{dt}+Ri+\frac{1}{C}q=E(t)
```

Rearranging for di/dt:
```math
\frac{di}{dt}=E(t)-\frac{R}{L}i+\frac{1}{LC}q
```

With that, we have our system of First-Order Differential Equations

## System of First-Order Differential Equations
### Equation 1:
```math
\frac{di}{dt}=E(t)-\frac{R}{L}i+\frac{1}{LC}q
```
### Equation 2:
```math
\frac{dq}{dt} = i
```

## Applying Euler's Method
### Equation 1:
```math
i_{n+1} = i_{n} + (E(t)-\frac{R}{L}i_{n}-\frac{1}{LC}q_{n}) \Delta t 
```
### Equation 2:
```math
q_{n+1}= q_{n} + (i_{n})\Delta t
```

