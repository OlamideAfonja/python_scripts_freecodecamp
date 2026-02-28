
def add_setting(settings, key_value_tuple):
    # Unpack the tuple and convert both to lowercase
    key = str(key_value_tuple[0]).lower()
    value = str(key_value_tuple[1]).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, key_value_tuple):
    # Unpack the tuple and convert both to lowercase
    key = str(key_value_tuple[0]).lower()
    value = str(key_value_tuple[1]).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    # Convert key to lowercase
    lowered_key = str(key).lower()

    if lowered_key in settings:
        del settings[lowered_key]
        return f"Setting '{lowered_key}' deleted successfully!"
    
    return "Setting not found!"


def view_settings(settings):
    # Check if dictionary is empty
    if not settings:
        return "No settings available."
    
    # Build the display string
    output = "Current User Settings:"
    for key, value in settings.items():
        # Key is capitalized, value remains as stored (lowercase)
        output += f"\n{key.capitalize()}: {value}"
    
    # Ensure the string ends with a newline character
    return output + "\n"

# --- Testing Section ---
# Initialize the required dictionary
test_settings = {}

# 2. Add some initial settings
# Note: Input can be mixed case; the function handles the lowercase conversion.
add_setting(test_settings, ("Theme", "Dark"))
add_setting(test_settings, ("Language", "English"))
add_setting(test_settings, ("Notifications", "Enabled"))

# 3. View the current state
print(view_settings(test_settings))


