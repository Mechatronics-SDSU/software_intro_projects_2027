# SDSU Mechatronics Software Intro Project 2027

This repository is used for the Fall 2026 SDSU Mechatronics Software Intro Project. Recruits will use it to practice basic Python, Git, GitHub, and software-system design.

The complete instructions are available in the [Fall 2026 Software Intro Project document](https://docs.google.com/document/d/1RQsuH8H5FSkxNfYd9Z3UKJAD6pRz6F2N3AQ2v0YsKOs/edit?tab=t.0).

## Getting Repository Access

Before beginning the project:

1. Attend an SDSU Mechatronics general body meeting.
2. Come up to Andy and provide your exact GitHub username.
3. Wait to be added to the **Software Recruit 2027** GitHub team.
4. Accept the GitHub organization or team invitation if GitHub sends you one.
5. Confirm that you can access and write to this repository.

Your GitHub username is used to give you repository access. Your branch name will use your actual name.

## Clone the Repository

```bash
git clone https://github.com/Mechatronics-SDSU/software_intro_projects_2027.git
cd software_intro_projects_2027
```

## Create Your Individual Branch

Each recruit must complete their work on a separate branch created from the newest version of `main`.

```bash
git switch main
git pull
git switch -c first_last
```

Replace `first_last` with your actual first and last name in lowercase, separated by an underscore.

Example:

```text
andy_chen
```

Do not use spaces or hyphens. If two recruits have the same name, include a middle initial, such as `andy_j_chen`.

## Install NumPy

The MotorWrapper.py template requires the NumPy Python package.

For Linux, WSL, or macOS, run:

python3 -m pip install numpy

For Windows without WSL, run:

py -m pip install numpy

## Required Individual Projects

Every recruit must complete both Python exercises.

### Python Script 1: Count Up and Down

Create an `intro_proj` folder and a `count_up_down.py` file using the command line.

```bash
mkdir intro_proj
cd intro_proj
touch count_up_down.py
```

The program must create a 10-row by 20-column array that counts upward from a user-provided starting value until the halfway point and then counts back down.

### Python Script 2: Swim a Square Path

Complete the provided `MotorWrapper.py` template. The template is stored on the `main` branch and will be included when you create your individual branch.

Your program must move the simulated submarine forward, left, backward, and right to create a square path without turning.

## Push Your Work

Confirm that you are on your individual branch:

```bash
git branch
```

Add, commit, and push your work:

```bash
git add .
git commit -m "Complete software intro Python scripts"
git push -u origin first_last
```

Replace `first_last` with your actual branch name.

Your individual branch must contain:

- Your completed `count_up_down.py` file
- Your completed `MotorWrapper.py` file
- A screenshot of the console output from Python Script 1
- A screenshot of the console output from Python Script 2

Submit the link to your individual branch according to the project instructions.

## Optional Group System-Design Challenge

The system-design challenge is optional and cannot be completed individually.

- Each group must have two to four members.
- Only two groups will be accepted.
- Every member must complete the individual Python exercises.
- Every member must attend the group meeting and understand the complete design.
- The group must coordinate and submit one meeting time that works for every member.
- Wait for confirmation before beginning the optional challenge.

### Create a Group Branch

The group project must use a separate branch created from the newest version of `main`.

```bash
git switch main
git pull
git switch -c group_group_name
git push -u origin group_group_name
```

Replace `group_group_name` with a short group name using lowercase letters and underscores only.

Example:

```text
group_team_bussy
```

Other group members can access the branch using:

```bash
git fetch origin
git switch --track origin/group_group_name
```

The group branch must contain:

- The names and GitHub usernames of all group members
- The architecture diagram
- The written system-design explanation
- Any supporting files used during the meeting

## Repository Rules

- Do not push directly to `main`.
- Do not merge a branch unless instructed.
- Do not place group work on an individual branch.
- Do not place individual Python work on a group branch.
- Never commit or upload a GitHub personal access token.
- Use lowercase letters and underscores for branch names.
- You may use online resources or AI tools to learn, but you must understand and be able to explain your work.
- Ask for help at a GBM if you have trouble accessing or using the repository.