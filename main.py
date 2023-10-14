class ConceptGraph:
    def __init__(self, concept_names=[]):
        self.concepts = []
        self.matrix = []
        for x in concept_names:
            self.add_concept(x)

    def __str__(self):
        header = "\t" + "\t".join(self.concepts)
        rows = [
            f"{self.concepts[i]}\t" + "\t".join(
                [str(link) if link is not None else '-' for link in row]
            ) for i, row in enumerate(self.matrix)
        ]
        return header + "\n" + "\n".join(rows)
    def add_concept(self, concept):
        if concept in self.concepts:
            raise ValueError(f"The concept '{concept}' already exists.")
        self.concepts.append(concept)

        # also add a new column to the matrix
        for row in self.matrix:
            row.append(None)

        # add a new row for the new concept
        self.matrix.append([None] * len(self.concepts))

    def remove_concept(self, concept_name):
        if concept_name not in self.concepts:
            raise ValueError(f"The concept '{concept_name}' does not exist.")
        index = self.concepts.index(concept_name)
        # remove the corresponding row
        del self.matrix[index]
        # remove the corresponding column
        for row in self.matrix:
            del row[index]
        self.concepts.remove(concept_name)

    def modify_concept(self, prev_concept, new):
        if prev_concept not in self.concepts:
            raise ValueError(f"The concept '{prev_concept}' does not exist.")
        if new in self.concepts:
            raise ValueError(f"The concept 'new' already exists.")
        index = self.concepts.index(prev_concept)
        self.concepts[index] = new

    def add_link(self, concept1, concept2, link):
        if concept1 not in self.concepts or concept2 not in self.concepts:
            raise ValueError("Both concepts should exist before adding a link.")
        index1 = self.concepts.index(concept1)
        index2 = self.concepts.index(concept2)
        self.matrix[index1][index2] = link

    def remove_link(self, concept1, concept2):
        if concept1 not in self.concepts or concept2 not in self.concepts:
            raise ValueError("Both concepts should exist before removing a link.")
        index1 = self.concepts.index(concept1)
        index2 = self.concepts.index(concept2)
        self.matrix[index1][index2] = None

    def modify_link(self, concept1, concept2, new_link):
        if concept1 not in self.concepts or concept2 not in self.concepts:
            raise ValueError("Both concepts should exist before modifying a link.")
        if self.matrix[self.concepts.index(concept1)][self.concepts.index(concept2)] is None:
            raise ValueError(f"No link exists between '{concept1}' and '{concept2}'.")
        index1 = self.concepts.index(concept1)
        index2 = self.concepts.index(concept2)
        self.matrix[index1][index2] = new_link
