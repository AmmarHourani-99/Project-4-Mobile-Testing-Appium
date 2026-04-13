# Project 4 — Mobile Automation Testing | Appium + Python

## Overview
Mobile automation testing project using Appium and Python.
This project automates key user flows on the Wikipedia Android app
running on an Android emulator, including app launch, search,
navigation, article loading, and Arabic language switching.

## Test Summary
| Field | Details |
|---|---|
| Tester | Ammar Hourani |
| Environment | Mac / Android Emulator API 36 / Python 3.9.6 / Appium 3.0.2 |
| App Tested | Wikipedia for Android (v50575) |
| Total Scripts | 5 |
| Passed | 5 |
| Failed | 0 |
| Overall Status | Pass — All automated mobile test scripts executed successfully |

## Test Scripts
| Script | Description | Result |
|---|---|---|
| test_wikipedia_launch.py | Verify app launches and search bar is visible | ✅ Pass |
| test_wikipedia_search.py | Search for "Jordan" and verify results load | ✅ Pass |
| test_wikipedia_navigation.py | Tap Search tab and verify screen loads | ✅ Pass |
| test_wikipedia_article.py | Search Jordan and open article page | ✅ Pass |
| test_wikipedia_language.py | Switch to Arabic language and verify results | ✅ Pass |

## Tools Used
- Python 3.9.6
- Appium 3.0.2
- Appium Python Client 3.1.0
- UiAutomator2 Driver 5.0.3
- Android Studio (Android Emulator API 36)
- VS Code

## App Tested
- Wikipedia for Android v50575
- Package: org.wikipedia
- Downloaded from F-Droid

## How to Run
1. Start Android emulator
2. Install Wikipedia APK on emulator
3. Start Appium server: appium
4. Run any script: python3 test_wikipedia_launch.py
