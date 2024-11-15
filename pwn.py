import subprocess
import os

# Path to the binary file
BINARY_PATH = "./lemontree"  # Adjust this to the actual path of your binary

# Ensure the binary exists
if not os.path.exists(BINARY_PATH):
    print(f"Error: Binary file not found at {BINARY_PATH}")
    exit(1)

# Define GDB commands
GDB_COMMANDS = """
set disassembly-flavor intel
break main
run
info functions
disassemble main
quit
"""

def run_gdb(binary_path, commands):
    """Runs GDB with the provided commands on the specified binary."""
    try:
        # Write GDB commands to a temporary file
        gdb_script_path = "gdb_script.txt"
        with open(gdb_script_path, "w") as gdb_script:
            gdb_script.write(commands)
        
        # Run GDB
        result = subprocess.run(
            ["gdb", "-q", "-x", gdb_script_path, binary_path],
            capture_output=True,
            text=True
        )
        
        # Clean up the script file
        os.remove(gdb_script_path)
        
        # Return GDB output
        return result.stdout
    except FileNotFoundError:
        return "Error: gdb is not installed. Please install it using your package manager."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Execute GDB with the specified commands
output = run_gdb(BINARY_PATH, GDB_COMMANDS)

# Display the output
print("\n=== GDB Output ===\n")
print(output)
