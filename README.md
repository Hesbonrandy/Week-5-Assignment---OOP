# Python OOP Assignments

This repository contains two Python Object-Oriented Programming assignments demonstrating key OOP concepts.

## Assignment 1:

### Smartphone Class System
Created a comprehensive `Smartphone` class hierarchy with inheritance and encapsulation features:

#### Features:
- **Base Class**: `Smartphone` with attributes like brand, model, storage, battery life
- **Encapsulation**: Private storage attribute with getter method
- **Methods**: Install apps, show specifications
- **Inheritance**: `GamingSmartphone` extends `Smartphone` with cooling system features
- **Polymorphism**: Overridden `show_specs()` method in child class


## Activity 2: 

### Vehicle Movement System
Demonstrates polymorphism with different vehicles implementing the same method differently:

#### Classes:
- `Vehicle` (Base class with abstract move method)
- `Car` (Drives 🚗)
- `Plane` (Flies ✈️)
- `Boat` (Sails ⛵)
- `Bicycle` (Cycles 🚴)

#### Polymorphism in Action:
```python
vehicles = [Car(), Plane(), Boat(), Bicycle()]
for vehicle in vehicles:
    vehicle.move()  # Each vehicle moves differently!
```

**Output:**
```
Driving 🚗
Flying ✈️
Sailing ⛵
Cycling 🚴
```

