#!/bin/bash
# Learning Objective: Analyze Git commit history to visualize project activity and identify trends.
# This script will help you understand how to extract information from your Git log
# to see who is committing, when, and how frequently. This can be useful for
# understanding team contributions, spotting busy periods, and identifying potential bottlenecks.

# --- Configuration ---
# Define the output file for our analysis. This is where the summarized data will be stored.
OUTPUT_FILE="git_activity_summary.txt"

# --- Helper Functions ---

# Function to display a friendly error message and exit the script.
# This promotes robust scripting by handling unexpected situations gracefully.
error_exit() {
    echo "Error: $1" >&2  # Redirect error messages to standard error (>&2)
    exit 1               # Exit with a non-zero status code to indicate an error
}

# Function to check if Git is installed.
# We need Git to be available for any Git-related operations.
check_git_installed() {
    if ! command -v git &> /dev/null; then
        error_exit "Git is not installed. Please install Git to use this script."
    fi
}

# --- Main Analysis Logic ---

# Function to analyze the Git commit history and generate a summary.
analyze_git_history() {
    echo "Analyzing Git commit history..."

    # Clear the output file if it already exists.
    # This ensures we start with a clean slate for each analysis run.
    > "$OUTPUT_FILE" # The '>' redirection truncates the file if it exists, or creates it if it doesn't.

    # Get the Git log.
    # The 'git log' command retrieves commit history.
    # '--pretty=format:"%ad %an"' specifies the output format:
    #   %ad: Author date (committer date if author date is not available)
    #   %an: Author name
    # We are interested in the date and author to track activity.
    # The '--date=iso' option ensures dates are in a consistent, sortable format.
    # We use 'xargs -r' to process each line of the git log safely.
    # 'xargs -r' ensures that 'process_commit' is only run if there's input, preventing errors on empty logs.
    git log --pretty=format:"%ad %an" --date=iso | xargs -r -L1 ./process_commit.sh

    echo "Git activity analysis complete. Summary saved to '$OUTPUT_FILE'."
}

# --- Script Execution ---

# Main execution block of the script.
# This is where we orchestrate the different parts of our analysis.
main() {
    check_git_installed # First, ensure Git is available.

    # Check if we are inside a Git repository.
    # The '.git' directory is the indicator of a Git repository.
    if [ ! -d ".git" ]; then
        error_exit "This script must be run from the root of a Git repository."
    fi

    analyze_git_history # Proceed with the main analysis.
}

# Execute the main function when the script is run.
main

# --- Example Usage ---
# To run this script:
# 1. Save it as a file, e.g., 'git_analyzer.sh'.
# 2. Make it executable: 'chmod +x git_analyzer.sh'.
# 3. Navigate to the root directory of your Git repository in your terminal.
# 4. Run the script: './git_analyzer.sh'.
#
# This will create a file named 'git_activity_summary.txt' in the same directory.
# The file will contain lines like:
#   2023-10-27 10:30:00 +0000 John Doe
#   2023-10-27 11:15:00 +0000 Jane Smith
#   2023-10-28 09:00:00 +0000 John Doe
#
# You can then further process this file using other Bash tools like 'sort', 'uniq', 'awk', etc.
# For example, to count commits per author:
#   sort git_activity_summary.txt | uniq -c | sort -nr
#
# Or to count commits per day:
#   cut -d' ' -f1 git_activity_summary.txt | sort | uniq -c | sort -nr
#
# Or to count commits per author and day:
#   awk '{print $1, $3}' git_activity_summary.txt | sort | uniq -c | sort -nr