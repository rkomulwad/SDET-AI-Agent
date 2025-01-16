# SDET-AI-Agent - Agentic API Contract Test Generator

Welcome to the SDET-AI-Agent project, an intelligent test generation system powered by [crewAI](https://crewai.com). This tool automatically generates comprehensive API contract tests from a OpenAPI Specification, ensuring API implementation adheres to its contract.

> This project was created as a learning exercise to explore and demonstrate Agentic capabilities

## Features
- Intelligent test scenario creation based on endpoint specifications
- Coverage for various response codes and edge cases
- Data validation against schema definitions
- Automated generation of API contract tests from OpenAPI Specifications


## Agents and Tasks Overview

### Agents

#### Test Designer
- **Role**: API Test Case Designer
- **Purpose**: Specializes in comprehensive API test case design
- **Expertise**: 
  - Deep understanding of API design principles
  - Knowledge of common vulnerabilities and failure modes
  - Skilled at identifying edge cases and boundary conditions
  - Expert in interpreting OpenAPI specifications

#### Test Case Coder
- **Role**: Expert Postman Test Case Coder
- **Purpose**: Transforms test cases into executable code
- **Expertise**:
  - Postman test automation
  - API testing principles
  - Clean code practices
  - OpenAPI/Swagger interpretation

### Tasks

#### 1. Generate Test Cases
- **Agent**: Test Designer
- **Objective**: Create comprehensive test suite covering:
  - Positive tests (valid inputs/outputs)
  - Negative tests (invalid inputs)
- **Output Format**: Markdown table with Test Case ID, Description, and Test Type

#### 2. Generate Edge Test Cases
- **Agent**: Test Designer
- **Objective**: Identify and document:
  - Boundary value tests
  - Edge case scenarios
  - Unusual conditions
- **Output Format**: Markdown table with Test Case ID and Description

#### 3. Generate Test Code
- **Agent**: Test Case Coder
- **Objective**: Create executable Postman test scripts that:
  - Implement test cases using `pm.test()`
  - Include appropriate assertions
  - Handle setup/teardown
  - Manage environment variables
- **Output Format**: JavaScript code for Postman test runner

### Workflow

1. Test Designer analyzes OpenAPI spec and generates standard test cases
2. Test Designer identifies edge cases and boundary conditions
3. Test Case Coder converts all test cases into executable Postman scripts

This agent-task structure ensures comprehensive API testing from specification through execution.

## Installation

Requires Python >=3.10 <3.13. This project uses [pyenv](https://pypi.org/project/pyenv/) & [Poetry](https://python-poetry.org/) for python environment and dependency management.

1. Install Dependencies and activate virtual environment:
```bash
pyenv virtualenv 3.12.8 sdet-ai-agent-env
pyenv activate sdet-ai-agent-env
poetry install
```

2. Set Env Variable:
```bash
export GEMINI_API_KEY=your_gemini_api_key
export MODEL=gemini/gemini-1.5-flash
```

## Usage

Run the test generation:

```bash
poetry run sdet_ai_agent
```

## Cleanup
```bash
pyenv deactivate sdet-ai-agent-env
pyenv virtualenv-delete sdet-ai-agent-env
```
