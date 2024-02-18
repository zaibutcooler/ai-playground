topics = [
    ("Basic Concepts of Algebra", "Introduction to fundamental algebraic concepts such as variables, expressions, equations, and inequalities."),
    ("Linear Equations and Inequalities", "Solving linear equations and inequalities, including systems of linear equations and inequalities."),
    ("Quadratic Equations", "Understanding quadratic equations, including factoring, completing the square, and the quadratic formula."),
    ("Polynomials and Polynomial Functions", "Exploration of polynomials, polynomial operations, and polynomial functions."),
    ("Rational Expressions and Equations", "Solving equations involving rational expressions and exploring their properties."),
    ("Exponential and Logarithmic Functions", "Introduction to exponential and logarithmic functions, including properties and applications."),
    ("Radical Functions", "Understanding radical expressions and functions, including simplifying radicals and solving radical equations."),
    ("Linear Algebra", "Fundamental concepts of linear algebra, including vectors, matrices, and matrix operations."),
    ("Systems of Linear Equations", "Solving systems of linear equations using methods such as substitution, elimination, and matrices."),
    ("Matrix Algebra", "Exploring matrix operations, determinants, inverses, and solving linear systems using matrix methods."),
    ("Vector Spaces", "Introduction to vector spaces, subspaces, linear independence, and basis vectors."),
    ("Eigenvalues and Eigenvectors", "Understanding eigenvalues and eigenvectors, including applications in systems of linear equations and differential equations."),
    ("Abstract Algebra", "Introduction to abstract algebraic structures such as groups, rings, and fields."),
    ("Number Theory", "Exploration of properties of integers, prime numbers, divisibility, and modular arithmetic."),
    ("Complex Numbers", "Introduction to complex numbers, including operations, polar form, and applications."),
    ("Graph Theory", "Introduction to graph theory, including graph representations, basic concepts, and graph algorithms."),
    ("Discrete Mathematics", "Exploration of discrete mathematical structures and concepts, including sets, functions, relations, and combinatorics."),
    ("Algebraic Geometry", "Introduction to algebraic geometry, including equations of curves and surfaces in the plane and space."),
    ("Algebraic Topology", "Introduction to algebraic topology, including homotopy, homology, and fundamental groups."),
    ("Computational Algebra", "Exploration of computational methods in algebra, including symbolic computation and algebraic algorithms.")
]


import os
import json

# Loop through the list of topics and create notebooks
for index, (topic, description) in enumerate(topics, start=1):
    # Construct the notebook filename
    notebook_filename = f"./{index:02d}_{topic.replace(' ', '_')}.ipynb"
    
    # Write description to the top cell of the notebook
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {topic}",
                    "",
                    description
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    # Write notebook content to file
    with open(notebook_filename, "w") as file:
        json.dump(notebook_content, file)

print("Notebooks created successfully!")
