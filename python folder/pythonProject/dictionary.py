students = {
    "S001": "Alice Johnson",
    "S002": "Bob Smith",
    "S003": "Charlie Brown",
    "S004": "Diana Miller",
    "S005": "Ethan Davis"
}
print("Original dictionary:", students)


students["S006"] = "Fiona White"
students.update({"S007": "George Black"})
print("\nAfter adding values:", students)


students["S001"] = "Alice Thompson"
students.update({"S002": "Robert Smith"})
print("\nAfter updating values:", students)


print("\nAccessing specific value:", students["S003"])
print("Using get method:", students.get("S004"))


nested_students = {
    "S001": {"name": "Alice Thompson", "grade": "A"},
    "S002": {"name": "Robert Smith", "grade": "B"},
    "S003": {"name": "Charlie Brown", "grade": "A-"},
    "S004": {"name": "Diana Miller", "grade": "B+"},
    "S005": {"name": "Ethan Davis", "grade": "A"}
}
print("\nNested dictionary:", nested_students)


print("\nNested value - name:", nested_students["S001"]["name"])
print("Nested value - grade:", nested_students["S002"]["grade"])


print("\nKeys in original dictionary:", students.keys())
print("Keys in nested dictionary:", nested_students.keys())


del students["S006"]
students.pop("S007")
print("\nAfter deleting values:", students)