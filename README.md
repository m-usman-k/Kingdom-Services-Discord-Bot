# Discord Bot: Announce & Activision ID Commands

This Discord bot provides several commands for administrators to make announcements in text channels, retrieve Activision IDs, and manage other administrative tasks.

## Features

- **Announcement Command**: 
  - Sends a message with an optional mention of a specific role in all text channels of a given category.
  - Optionally deletes the announcement after a set period (in minutes).
  
- **Activision ID Commands**: 
  - Retrieve Activision IDs for specific categories (`h1` to `h12`).
  - Only available to users with administrator permissions.

## Commands

### `/announce`
- **Description**: Makes an announcement in all text channels of a specified category.
- **Usage**: `/announce [message] [category] [delete_after]`
  - `message`: The announcement message.
  - `category`: The category in which all text channels will receive the announcement.
  - `delete_after`: Time (in minutes) to wait before deleting the announcement. Set to `0` to keep the announcement indefinitely.

### `/h1` to `/h12`
- **Description**: Show the Activision ID for a specific category (`h1` to `h12`).
- **Usage**: `/h1` (or `/h2`, `/h3`, etc.)
  - The bot responds with the Activision ID for the respective category. Only available to administrators.

## Requirements

- Python 3.8 or higher
- `discord.py` library
- `python-dotenv` for environment variables
- `json` to read the Activision ID file

## Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/your-repo-name/discord-bot.git](https://github.com/m-usman-k/Kingdom-Services-Discord-Bot.git)
    cd Kingdom-Services-Discord-Bot
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root of the project with your bot token:

    ```bash
    BOT_TOKEN=your_bot_token_here
    ```

4. Create an `ids.json` file containing the Activision IDs for each category, for example:

    ```json
    {
        "h1": "ActivisionID1",
        "h2": "ActivisionID2",
        "h3": "ActivisionID3",
        ...
    }
    ```

## Usage

1. Start the bot:

    ```bash
    python main.py
    ```

2. The bot will sync with the server and be ready to accept commands. Administrators can use the commands listed above.

## Contributing

Feel free to fork the repository, submit issues, or send pull requests with improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the `discord.py` library for providing the foundation for the bot.
- Special thanks to contributors and the community for their support.
