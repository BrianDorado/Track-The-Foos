# Foosball Score Tracker

This project is a foosball score tracking system that uses Twilio for text message input and Google Sheets for data storage. The program tracks player scores, updates ELO ratings, and manages player seeding for a competitive foosball league.

## Features

- Track foosball match results
- Update player ELO ratings after each match
- Store and retrieve player data using Google Sheets
- Automatically update player seeds based on ELO ratings
- Periodically reset or partially reset seeding

## How It Works

1. **Twilio Integration**: Players send match results via text message (Twilio integration will be added later).
2. **Google Sheets Storage**: Match results and player stats are stored in Google Sheets, where data is used to update scores and rankings.
3. **ELO Rating System**: The system uses ELO ratings to rank players after each match.
4. **Seeding**: Player seeds are automatically calculated based on their ELO rating, and can be reset periodically.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/foosball-score-tracker.git
