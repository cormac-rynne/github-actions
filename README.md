# GitHub Actions Exploration Project

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Workflow Overview](#workflow-overview)
- [Workflow Steps](#workflow-steps)
  - [Formatting](#formatting)
  - [Linting](#linting)
  - [Testing](#testing)
  - [Version Bumping](#version-bumping)
  - [Build and Publish](#build-and-publish)
  - [Slack Notification](#slack-notification)
- [Custom Action: Setup Python Environment](#custom-action-setup-python-environment)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is an exploration of GitHub Actions, demonstrating how to set up a comprehensive CI/CD pipeline for a Python project. It includes steps for code quality checks, testing, version management, building, publishing, and notifications.

## Project Structure

The main workflow is defined in `.github/workflows/main.yml`. The project also includes a custom action for setting up the Python environment, located in `.github/actions/setup-python/action.yml`.

## Workflow Overview

The workflow is triggered on pushes to the `main` branch, pull requests to the `main` branch, and when a release is created. It consists of several jobs that run in sequence:

1. Formatting (using Black)
2. Linting (using Flake8)
3. Testing (using Pytest)
4. Version Bumping (using python-semantic-release)
5. Build and Publish
6. Slack Notification

## Workflow Steps

### Formatting

- Uses the Black code formatter to check Python code style
- Runs on Ubuntu latest
- Uses the custom "Setup Python Environment" action

### Linting

- Uses Flake8 to check for code quality issues
- Runs on Ubuntu latest
- Uses the custom "Setup Python Environment" action

### Testing

- Runs the project's test suite using Pytest
- Runs on Ubuntu latest
- Uses the custom "Setup Python Environment" action

### Version Bumping

- Uses python-semantic-release to automatically bump the version based on commit messages
- Requires successful completion of formatting, linting, and testing jobs
- Runs on Ubuntu latest
- Uses the custom "Setup Python Environment" action

### Build and Publish

- Builds the Python package and publishes it to TestPyPI
- Requires successful completion of the version bumping job
- Runs on Ubuntu latest
- Uses the custom "Setup Python Environment" action
- Outputs the build and publish status for use in the Slack notification

### Slack Notification

- Sends a summary of the workflow run to a Slack channel
- Runs after all other jobs, regardless of their outcome
- Provides a detailed breakdown of each step's status
- Includes a link to the full workflow run on GitHub

## Custom Action: Setup Python Environment

This project includes a custom composite action for setting up the Python environment. It performs the following tasks:

- Sets up the specified Python version (default: 3.10)
- Caches dependencies for faster subsequent runs
- Installs dependencies from specified files (default: requirements.txt and requirements-dev.txt)
- Supports both pip (requirements.txt) and poetry (poetry.lock) dependency management

## Getting Started

To use this workflow in your project:

1. Copy the `.github/workflows/main.yml` file to your repository.
2. Copy the `.github/actions/setup-python/action.yml` file to your repository.
3. Modify the workflow as needed to fit your project structure and requirements.
4. Ensure you have the necessary secrets set up in your repository settings:
   - `PYPI_TEST_USERNAME` and `PYPI_TEST_PASSWORD` for TestPyPI publishing
   - `SLACK_WEBHOOK_URL` for Slack notifications

## Contributing

Contributions to improve the workflow are welcome! Please submit a pull request with your proposed changes.

## License

[MIT License](LICENSE)