# Enhanced-learning-assistant
Project Overview

EILA is an AI-powered personalized learning assistant designed to streamline self-directed learning. It conducts deep research on user-defined topics, interacts to clarify learning objectives, and generates comprehensive educational reports with visual aids and references.

Features

Accepts user-defined learning topics and objectives

Clarifies scope and preferences through interactive questions

Gathers data from simulated or real sources:

Web content

Academic sources

Video transcripts

Summarizes and organizes information

Generates structured, citation-backed reports with visuals

Supports report modifications based on feedback and follow-up

System Architecture

Modules:

interaction.py: Handles user queries and preferences

research.py: Simulates or accesses external sources for content

summarizer.py: Processes and condenses raw content

report_generator.py: Compiles the final report with structure and citations

feedback_handler.py: Manages report modifications post-feedback

Flow:
User Input → Interactive Questions → Research Engine → Summarizer → Report Generator → Feedback Loop

CODE FOLDER STRUCTURE
/eila
├── main.py                      # Entry point for the application
├── interaction.py              # Manages user input, questions, and preferences
├── research.py                 # Handles data collection from simulated or real APIs
├── summarizer.py               # Performs summarization and information synthesis
├── report_generator.py         # Generates structured, visual-rich reports
├── feedback_handler.py         # Accepts user feedback and updates reports accordingly
├── assets/                     # Stores images, diagrams, and static files
├── templates/                  # HTML templates for report rendering (if web-based)
├── requirements.txt            # Python dependencies
└── .env                        # (Optional) API keys and environment variables
