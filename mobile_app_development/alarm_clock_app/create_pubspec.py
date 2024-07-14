import os

# Define the content of the pubspec.yaml file
pubspec_content = """
name: alarm_clock_app
description: "A Flutter alarm clock app that allows users to set and manage alarms."
publish_to: 'https://pub.dev'

version: 1.0.0+1

environment:
  sdk: '>=3.4.3 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  intl: ^0.17.0
  flutter_local_notifications: ^8.2.0
  cupertino_icons: ^1.0.6

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true

  # To add assets to your application, add an assets section, like this:
  assets:
    - assets/sounds/alarm_tone.mp3

# Additional sections for publishing
repository: https://github.com/jeanluchabi/CodSoft/mobile_app_development/alarm_clock_app
issue_tracker: https://github.com/jeanluchabi/CodSoft/mobile_app_development/alarm_clock_app/issues
homepage: https://luc.com
"""

# Define the path to save the pubspec.yaml file
file_path = "pubspec.yaml"

# Write the content to the file
with open(file_path, "w") as file:
    file.write(pubspec_content.strip())

print(f"pubspec.yaml file has been created at {os.path.abspath(file_path)}")

