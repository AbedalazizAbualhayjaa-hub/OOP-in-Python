# Task 13 - Frozen and Ordered

from dataclasses import dataclass, FrozenInstanceError


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int


# Deliverable

v1 = Version(2, 0, 0)
v2 = Version(1, 5, 2)
v3 = Version(1, 2, 0)

# Sorting
versions = [v1, v2, v3]

print("Sorted versions:")
for version in sorted(versions):
    print(version)


# Using versions as dictionary keys
version_info = {
    v1: "Version 2",
    v2: "Version 1.5",
    v3: "Version 1.2"
}

print("\nDictionary:")
print(version_info[v2])


# Attempting mutation
try:
    v1.major = 3
except FrozenInstanceError as error:
    print("\nMutation rejected:", error)
