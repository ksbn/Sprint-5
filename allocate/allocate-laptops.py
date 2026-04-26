from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Dict, Optional
 
 
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
 
 
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_systems: tuple[OperatingSystem, ...]
 
 
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
 
 
def sadness(person: Person, laptop: Laptop) -> int:
    try:
        return person.preferred_operating_systems.index(laptop.operating_system)
    except ValueError:
        return 100  # OS not in their preferred list
 
 
def total_sadness(allocation: Dict[Person, Laptop]) -> int:
    return sum(sadness(person, laptop) for person, laptop in allocation.items())
 
 
def allocate_laptops(people: Tuple[Person], laptops: Tuple[Laptop]) -> Dict[Person, Laptop]:
    from itertools import permutations
 
    best_allocation: Optional[Dict[Person, Laptop]] = None
    best_sadness = float("inf")
 
    # Try every possible way to assign laptops to people
    for laptop_combo in permutations(laptops, len(people)):
        allocation = dict(zip(people, laptop_combo))
        current_sadness = total_sadness(allocation)
 
        if current_sadness < best_sadness:
            best_sadness = current_sadness
            best_allocation = allocation
 
    if best_allocation is None:
        raise ValueError("Could not allocate laptops — not enough laptops for everyone.")
 
    return best_allocation
 
 
 
people = [
    Person(name="Imran", age=22, preferred_operating_systems=(OperatingSystem.UBUNTU, OperatingSystem.ARCH)),
    Person(name="Eliza", age=34, preferred_operating_systems=(OperatingSystem.ARCH, OperatingSystem.UBUNTU)),
    Person(name="Sima",  age=28, preferred_operating_systems=(OperatingSystem.MACOS,))
]
 
laptops = [
    Laptop(id=1, manufacturer="Dell",  model="XPS",     screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell",  model="XPS",     screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]
 
allocation = allocate_laptops(people, laptops)
 
print("Laptop allocations:")
for person, laptop in allocation.items():
    s = sadness(person, laptop)
    print(f"  {person.name} → {laptop.manufacturer} {laptop.model} ({laptop.operating_system.value}) | sadness: {s}")
 
print(f"\nTotal sadness: {total_sadness(allocation)}")
 