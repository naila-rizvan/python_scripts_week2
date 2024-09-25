import re           # import regular expression library


with open("./Logs/Log.txt", "r") as f:          # Open log file to be parsed
    log_file_lines = f.readlines()

war_pattern = '(.*level=warning.*file)'             # Pattern to be checked for in the log file
war_match_list = []

print("Creating Log file with Warning messages...")

for line in log_file_lines:
    for match in re.finditer(war_pattern,line): # Find lines that match the pattern
        match_text = match.group()
        war_match_list.append(match_text[:-4])       # Add all matched lines to a list

# Open/Create file to add Warning messages
with open("./Logs/Warning Logs.txt","w") as f:
    clean = list(set(war_match_list))           # Convert to set to remove duplicate values
    for item in clean:
        f.write(item + '\n')


# Get all error messages into a separate file
error_pattern = '(.*level=error.*)'
error_match_list = []

print("Creating Log file with Error messages...")

for line in log_file_lines:
    for match in re.finditer(error_pattern,line):
        match_text = match.group()
        error_match_list.append(match_text)

with open("./Logs/Error Logs.txt","w") as f:
    error_clean = list(set(error_match_list))  # Convert to set to remove duplicate values
    for item in error_clean:
        f.write(item + '\n')

print('\nWarning & Error messages are extracted')