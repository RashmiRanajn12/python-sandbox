import os

# Define the directory where snippets will be saved
SNIPPETS_DIR = "snippets"

# Ensure the snippets directory exists; if not, create it
if not os.path.exists(SNIPPETS_DIR):
    os.makedirs(SNIPPETS_DIR)

def main():
    print("🐍 Welcome to the Python Sandbox CLI!")
    print("Type your Python code below. Type 'exit' to quit or 'save' to store your code.\n")

    lines = []  # Store lines of code

    while True:
        # Read input from the user line by line
        line = input(">>> ")

        # If the user wants to exit
        if line.strip().lower() == "exit":
            print("👋 Exiting the sandbox. Goodbye!")
            break

        # If the user wants to save the current snippet
        elif line.strip().lower() == "save":
            filename = input("Enter filename to save snippet as (without .py): ").strip()
            if filename:
                filepath = os.path.join(SNIPPETS_DIR, f"{filename}.py")
                with open(filepath, "w") as f:
                    f.write("\n".join(lines))
                print(f"✅ Code saved as: {filepath}")
                lines = []  # Clear lines after saving
            else:
                print("⚠️ Invalid filename.")
            continue

        # Otherwise, treat it as Python code
        try:
            exec(line)  # Execute the current line
            lines.append(line)  # Save the line for later if needed
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
