import subprocess
# Then, convert the .dvi file to PostScript using 'dvips'
ps_command = [
    'dvips',
    'main.dvi',
    '-o',
    'output.ps'  # Renaming the output file
]
subprocess.run(ps_command, check=True, capture_output=True, text=True)

print("✅ Step 2: Successfully created output.ps")