# ConceptGraph
A data structure on Python that allows concepts and relationships between such concepts to be stored in the form of a modified weighted graph.
## Methods
ConceptGraph could be used using these methods:

- **`add_concept(concept: str)`**: Adds a new concept to the graph.
- **`remove_concept(concept_name: str)`**: Removes an existing concept from the graph.
- **`modify_concept(prev_concept: str, new: str)`**: Modifies the name of an existing concept.
- **`add_link(concept1: str, link: str, concept2: str)`**: Creates a link between two concepts.
- **`remove_link(concept1: str, concept2: str)`**: Removes the link between two concepts.
- **`modify_link(concept1: str, new_link: str, concept2: str)`**: Modifies the link between two concepts.

## Example Usage
```py
# create a new graph
graph = ConceptGraph(["Student", "Apple"])

# add a new concept 
graph.add_concept("Pen")

# add links between two concepts
graph.add_link("Student", "Can Buy", "Apple")
graph.add_link("Student", "Uses", "Pen")
graph.add_link("Apple", "Eaten By", "Student")

# modify the name of a concept from Pen to Pencil
graph.modify_concept("Pen", "Pencil")

# remove the link between two concepts
graph.remove_link("Student", "Apple")

# print the current state of the graph
print(graph)
```
```
	Student	Apple	Pencil
Student	-	-	Uses
Apple	Eaten By	-	-
Pencil	-	-	-
```
