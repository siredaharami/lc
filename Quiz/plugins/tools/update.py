import subprocess
import os
import sys
from pyrogram import Client, filters

# Your GitHub repository URL
GITHUB_REPO = 'https://github.com/nortoxs/Quizbot'


# Function to clone the repository if it doesn't exist
def ensure_repo_exists():
    repo_name = GITHUB_REPO.split("/")[-1].replace(".git", "")
    if not os.path.exists(repo_name):
        print("Cloning the repository...")
        subprocess.run(["git", "clone", GITHUB_REPO], check=True)
    os.chdir(repo_name)  # Change to the repository directory

# Git pull and restart function
def git_pull_and_restart():
    # Ensure the repository exists
    ensure_repo_exists()
    
    # Pull the latest changes from the repository
    print("Pulling the latest changes from the repository...")
    subprocess.run(["git", "pull"], check=True)
    
    # Restart the bot
    print("Restarting the bot...")
    os.execv(sys.executable, ['python'] + sys.argv)

# Command to trigger git pull and restart
@app.on_message(filters.command("pull", prefixes="/"))
async def git_pull_command(client, message):
    # Only allow authorized user to use this
    allowed_user_id = 7648939888  # Replace with your user ID

    if message.from_user.id == allowed_user_id:
        git_pull_and_restart()
        await message.reply("Bot is updating and restarting.")
    else:
        await message.reply("You are not authorized to use this command.")
