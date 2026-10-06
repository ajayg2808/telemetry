#!/usr/bin/env python3
"""
Architecture Diagram Generator

Utility script for generating Mermaid diagram syntax from architecture descriptions.
Helps developers create consistent, well-formatted architecture diagrams.

Usage:
    python generate-architecture-diagrams.py --type class --input description.txt
    python generate-architecture-diagrams.py --type flowchart --input workflow.txt
    python generate-architecture-diagrams.py --type sequence --input interactions.txt
"""

import argparse
import json
import sys
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
from enum import Enum


class DiagramType(Enum):
    """Supported Mermaid diagram types."""
    CLASS = "class"
    FLOWCHART = "flowchart"
    SEQUENCE = "sequence"
    ERD = "erd"
    STATE = "state"


@dataclass
class ClassProperty:
    """Represents a class property/attribute."""
    name: str
    type: str
    visibility: str = "+"  # +, -, #, ~


@dataclass
class ClassMethod:
    """Represents a class method."""
    name: str
    params: List[Tuple[str, str]] = None  # [(param_name, param_type), ...]
    return_type: str = "void"
    visibility: str = "+"


@dataclass
class ClassDef:
    """Represents a class definition."""
    name: str
    properties: List[ClassProperty] = None
    methods: List[ClassMethod] = None
    stereotypes: List[str] = None  # "interface", "abstract", etc.
    
    def __post_init__(self):
        self.properties = self.properties or []
        self.methods = self.methods or []
        self.stereotypes = self.stereotypes or []


@dataclass
class ClassRelationship:
    """Represents a relationship between two classes."""
    source: str
    target: str
    type: str  # "inheritance", "implementation", "association", "aggregation", "composition"
    multiplicity_source: str = "1"
    multiplicity_target: str = "*"
    label: str = ""


@dataclass
class FlowchartNode:
    """Represents a flowchart node."""
    id: str
    label: str
    shape: str = "rectangle"  # rectangle, diamond, rounded, database, etc.


@dataclass
class FlowchartEdge:
    """Represents a flowchart edge/connection."""
    source: str
    target: str
    label: str = ""


class ClassDiagramGenerator:
    """Generates Mermaid class diagram syntax."""
    
    @staticmethod
    def generate(classes: List[ClassDef], relationships: List[ClassRelationship]) -> str:
        """Generate Mermaid class diagram from class definitions and relationships."""
        lines = ["classDiagram"]
        
        # Add classes
        for cls in classes:
            stereotype_str = ""
            if cls.stereotypes:
                stereotypes = " ".join(f"<<{s}>>" for s in cls.stereotypes)
                stereotype_str = f"\n    {stereotypes}"
            
            lines.append(f"    class {cls.name}{{{stereotype_str}")
            
            # Add properties
            for prop in cls.properties:
                lines.append(f"        {prop.visibility}{prop.name}: {prop.type}")
            
            # Add methods
            for method in cls.methods:
                params = ", ".join(f"{p[0]}: {p[1]}" for p in (method.params or []))
                lines.append(f"        {method.visibility}{method.name}({params}) {method.return_type}")
            
            lines.append("    }")
        
        # Add relationships
        for rel in relationships:
            rel_str = ClassDiagramGenerator._get_relationship_syntax(rel)
            if rel.label:
                lines.append(f"    {rel.source} {rel_str} {rel.target} : {rel.label}")
            else:
                lines.append(f"    {rel.source} {rel_str} {rel.target}")
        
        return "\n".join(lines)
    
    @staticmethod
    def _get_relationship_syntax(rel: ClassRelationship) -> str:
        """Convert relationship type to Mermaid syntax."""
        rel_map = {
            "inheritance": "<|--",
            "implementation": "<|..",
            "association": "-->",
            "aggregation": "o--",
            "composition": "*--",
        }
        
        base = rel_map.get(rel.type, "-->")
        
        # Add multiplicity if not default
        if rel.multiplicity_source != "1" or rel.multiplicity_target != "*":
            return f'"{rel.multiplicity_source}" {base} "{rel.multiplicity_target}"'
        
        return base


class FlowchartGenerator:
    """Generates Mermaid flowchart diagram syntax."""
    
    @staticmethod
    def generate(nodes: List[FlowchartNode], edges: List[FlowchartEdge], 
                 direction: str = "TD") -> str:
        """Generate Mermaid flowchart from nodes and edges."""
        lines = [f"flowchart {direction}"]
        
        # Add nodes
        for node in nodes:
            shape_open, shape_close = FlowchartGenerator._get_shape_delimiters(node.shape)
            # Escape brackets in labels
            label = node.label.replace("[", "\[").replace("]", "\]")
            lines.append(f"    {node.id}{shape_open}{label}{shape_close}")
        
        # Add edges
        for edge in edges:
            if edge.label:
                lines.append(f"    {edge.source} -->|{edge.label}| {edge.target}")
            else:
                lines.append(f"    {edge.source} --> {edge.target}")
        
        return "\n".join(lines)
    
    @staticmethod
    def _get_shape_delimiters(shape: str) -> Tuple[str, str]:
        """Get opening and closing delimiters for node shapes."""
        shapes = {
            "rectangle": ("[", "]"),
            "rounded": ("([", "])"),
            "diamond": ("{", "}"),
            "database": ("[(", ")]"),
            "circle": ("((", "))"),
            "subroutine": ("[[", "]]"),
            "start": ("([", "])"),
            "end": ("([", "])"),
        }
        return shapes.get(shape, ("[", "]"))


class SequenceDiagramGenerator:
    """Generates Mermaid sequence diagram syntax."""
    
    @staticmethod
    def generate(participants: List[str], interactions: List[Dict[str, str]]) -> str:
        """
        Generate Mermaid sequence diagram.
        
        Interactions format:
        [
            {"from": "A", "to": "B", "message": "request", "type": "sync"},
            {"from": "B", "to": "A", "message": "response", "type": "response"},
        ]
        """
        lines = ["sequenceDiagram"]
        
        # Add participants
        for participant in participants:
            lines.append(f"    participant {participant}")
        
        # Add interactions
        for interaction in interactions:
            from_p = interaction.get("from", "")
            to_p = interaction.get("to", "")
            message = interaction.get("message", "")
            int_type = interaction.get("type", "sync")
            
            if not from_p or not to_p:
                continue
            
            # Choose arrow based on type
            arrow_map = {
                "sync": "->",
                "async": "-x",
                "response": "-->>",
                "async_response": "--x",
            }
            arrow = arrow_map.get(int_type, "->")
            
            lines.append(f"    {from_p}{arrow}{to_p}: {message}")
        
        return "\n".join(lines)


class ERDGenerator:
    """Generates Mermaid entity relationship diagram syntax."""
    
    @staticmethod
    def generate(entities: Dict[str, Dict[str, Any]], 
                 relationships: List[Dict[str, str]]) -> str:
        """
        Generate Mermaid ERD.
        
        Entities format:
        {
            "User": {
                "attributes": [
                    {"name": "id", "type": "int", "constraints": ["PK"]},
                    {"name": "email", "type": "string", "constraints": ["UK"]},
                ]
            }
        }
        """
        lines = ["erDiagram"]
        
        # Add relationships
        for rel in relationships:
            source = rel.get("source", "")
            target = rel.get("target", "")
            cardinality = rel.get("cardinality", "||--o{")
            label = rel.get("label", "")
            
            if not source or not target:
                continue
            
            if label:
                lines.append(f"    {source} {cardinality} {target} : {label}")
            else:
                lines.append(f"    {source} {cardinality} {target}")
        
        # Add entity definitions
        for entity_name, entity_def in entities.items():
            lines.append(f"    {entity_name} {{")
            
            attributes = entity_def.get("attributes", [])
            for attr in attributes:
                attr_name = attr.get("name", "")
                attr_type = attr.get("type", "string")
                constraints = " ".join(attr.get("constraints", []))
                
                if constraints:
                    lines.append(f"        {attr_type} {attr_name} {constraints}")
                else:
                    lines.append(f"        {attr_type} {attr_name}")
            
            lines.append("    }")
        
        return "\n".join(lines)


class StateDiagramGenerator:
    """Generates Mermaid state diagram syntax."""
    
    @staticmethod
    def generate(states: List[str], transitions: List[Dict[str, str]]) -> str:
        """
        Generate Mermaid state diagram.
        
        Transitions format:
        [
            {"from": "State1", "to": "State2", "trigger": "event"},
        ]
        """
        lines = ["stateDiagram-v2", "    [*] --> " + (states[0] if states else "Start")]
        
        # Add transitions
        for transition in transitions:
            from_state = transition.get("from", "")
            to_state = transition.get("to", "")
            trigger = transition.get("trigger", "")
            
            if not from_state or not to_state:
                continue
            
            if trigger:
                lines.append(f"    {from_state} --> {to_state}: {trigger}")
            else:
                lines.append(f"    {from_state} --> {to_state}")
        
        # Add end state
        if states:
            lines.append(f"    {states[-1]} --> [*]")
        
        return "\n".join(lines)


class DiagramGeneratorCLI:
    """Command-line interface for diagram generation."""
    
    @staticmethod
    def main():
        """Main CLI entry point."""
        parser = argparse.ArgumentParser(
            description="Generate Mermaid architecture diagrams"
        )
        
        parser.add_argument(
            "--type",
            choices=[dt.value for dt in DiagramType],
            required=True,
            help="Diagram type to generate"
        )
        
        parser.add_argument(
            "--input",
            type=str,
            help="Input file (JSON or text format)"
        )
        
        parser.add_argument(
            "--output",
            type=str,
            default=None,
            help="Output file (default: stdout)"
        )
        
        parser.add_argument(
            "--example",
            action="store_true",
            help="Show example usage for diagram type"
        )
        
        args = parser.parse_args()
        
        if args.example:
            DiagramGeneratorCLI.show_example(args.type)
            return
        
        if not args.input:
            print("Error: --input is required (or use --example to see format)")
            sys.exit(1)
        
        try:
            diagram = DiagramGeneratorCLI.generate_from_file(args.type, args.input)
            
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(diagram)
                print(f"Diagram written to {args.output}")
            else:
                print(diagram)
                
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    @staticmethod
    def generate_from_file(diagram_type: str, input_file: str) -> str:
        """Generate diagram from input file."""
        with open(input_file, 'r') as f:
            content = json.load(f)
        
        diagram_type = DiagramType[diagram_type.upper()].value
        
        if diagram_type == "class":
            classes = [ClassDef(**c) for c in content.get("classes", [])]
            relationships = [ClassRelationship(**r) for r in content.get("relationships", [])]
            return ClassDiagramGenerator.generate(classes, relationships)
        
        elif diagram_type == "flowchart":
            nodes = [FlowchartNode(**n) for n in content.get("nodes", [])]
            edges = [FlowchartEdge(**e) for e in content.get("edges", [])]
            direction = content.get("direction", "TD")
            return FlowchartGenerator.generate(nodes, edges, direction)
        
        elif diagram_type == "sequence":
            participants = content.get("participants", [])
            interactions = content.get("interactions", [])
            return SequenceDiagramGenerator.generate(participants, interactions)
        
        elif diagram_type == "erd":
            entities = content.get("entities", {})
            relationships = content.get("relationships", [])
            return ERDGenerator.generate(entities, relationships)
        
        elif diagram_type == "state":
            states = content.get("states", [])
            transitions = content.get("transitions", [])
            return StateDiagramGenerator.generate(states, transitions)
        
        raise ValueError(f"Unknown diagram type: {diagram_type}")
    
    @staticmethod
    def show_example(diagram_type: str):
        """Show example input format for diagram type."""
        examples = {
            "class": {
                "description": "Class diagram example",
                "format": {
                    "classes": [
                        {
                            "name": "User",
                            "properties": [
                                {"name": "id", "type": "UUID", "visibility": "-"},
                                {"name": "email", "type": "string", "visibility": "+"}
                            ],
                            "methods": [
                                {"name": "getFullName", "params": [], "return_type": "string"}
                            ]
                        }
                    ],
                    "relationships": [
                        {
                            "source": "User",
                            "target": "Profile",
                            "type": "association"
                        }
                    ]
                }
            },
            "flowchart": {
                "description": "Flowchart example",
                "format": {
                    "direction": "TD",
                    "nodes": [
                        {"id": "A", "label": "Start", "shape": "rounded"},
                        {"id": "B", "label": "Decision", "shape": "diamond"}
                    ],
                    "edges": [
                        {"source": "A", "target": "B", "label": ""}
                    ]
                }
            },
            "sequence": {
                "description": "Sequence diagram example",
                "format": {
                    "participants": ["Client", "Server", "Database"],
                    "interactions": [
                        {"from": "Client", "to": "Server", "message": "Request", "type": "sync"},
                        {"from": "Server", "to": "Database", "message": "Query", "type": "sync"},
                        {"from": "Database", "to": "Server", "message": "Result", "type": "response"}
                    ]
                }
            },
            "erd": {
                "description": "ERD example",
                "format": {
                    "entities": {
                        "User": {
                            "attributes": [
                                {"name": "id", "type": "int", "constraints": ["PK"]},
                                {"name": "email", "type": "string", "constraints": ["UK"]}
                            ]
                        }
                    },
                    "relationships": [
                        {"source": "User", "target": "Post", "cardinality": "||--o{", "label": "writes"}
                    ]
                }
            },
            "state": {
                "description": "State diagram example",
                "format": {
                    "states": ["Pending", "Active", "Completed"],
                    "transitions": [
                        {"from": "Pending", "to": "Active", "trigger": "Start"},
                        {"from": "Active", "to": "Completed", "trigger": "Finish"}
                    ]
                }
            }
        }
        
        if diagram_type in examples:
            example = examples[diagram_type]
            print(f"\n{example['description']}:")
            print(json.dumps(example['format'], indent=2))
        else:
            print(f"No example available for type: {diagram_type}")


if __name__ == "__main__":
    DiagramGeneratorCLI.main()
