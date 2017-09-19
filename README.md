# workflow-automation
A tool to automate basic workflows using natural language commands.

## Code Structure
 - Intelligent scraper
   - A single file that scrapes a website and extracts information about the api call defined on it. This file writes to the csv file defined below.
 - Conecpt matching
   - A csv file that containts the api call definition.
   - A file that matches concepts in extracted sentence fragments with keywords defined in the csv file.
 - Concept extraction
   - A file that breaks a workflow automation command into its subcommands by splitting it along its verbs.

## Requirements
 - python (>2.7)
 - beautiful soup `pip install beautifulsoup4`
 - nltk `sudo pip install -U nltk`

## How to use Git
1. `git add <filename|.>` to add files to the local git repository
2. `git commit -m "Message"` to commit the files to the remote repository
3. `git push` to push the files to the remote repository
4. `git pull` to pull the most recent files from the remote repository. **Good idea to do this before starting any new code**
5. `git checkout <branchname>` to change to a different branch. **Avoid doing this unless you are afraid changes you make will break the build**
