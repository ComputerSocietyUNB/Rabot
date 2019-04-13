# Rabot

[![Maintainability](https://api.codeclimate.com/v1/badges/c12b3cacf48f121f0a6a/maintainability)](https://codeclimate.com/github/ComputerSocietyUNB/Rabot/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/c12b3cacf48f121f0a6a/test_coverage)](https://codeclimate.com/github/ComputerSocietyUNB/Rabot/test_coverage)

New version of a Telegram bot to help students with psychological/emotional issues during their academic years on Universidade de Brasília (UnB)

This project is aimed at all students that suffer through their academic years and might need more help than it's usually provided.

This bot is expected to run on Telegram using RASA api. It's development team is composed of psychology, computer science and engineering students. The project started in 2017 with various steps to improve the student's knowledge to be capable of building a fully-fledged bot. Latest stable version is 2.0 on another repository. Currently at version 3.0 beta, the bot has greatly changed it's architecture.

## Installing locally

Download this repository and go to it's folder

```
git clone {this repo}
cd {this repo}
```

Create a virtual environment, activate it and install it's requirements

```
python3 -m venv venv
source venv/bin/activate
pip install -r bot.requirements.txt
```

Train the bot

`docker-compose run -d --rm bot make train`

Run the bot on console

`docker-compose run --rm bot run-console`

## Setting up environment for development

## Timeline

**v3.0.0 (est. 1 week)** d: 23/03
- [X] Set up basic RASA bot
- [ ] Set up Heroku
- [ ] Set up CI/CD with Travis CI
- [ ] Verificar possíveis instituições parceiras

**v3.0.1 (est. 1 week)** d: 30/03
- [ ] Create simple dialog
- [ ] Create commands 
  - [ ] `/about` - Message about repository and team
  - [ ] `/help` - Message with emergency numbers
  - [ ] `/contact` - Message with all numbers available
  - [ ] `/joke`- Message with a simple joke to enlighten the day 
- [ ] Contactar instituições (email, telefone, reunião, etc)
 
**v3.0.2 (est. 2 weeks)** d: 06/04
- [ ] Create first dialog from simulated environment
- [ ] Create method to detect negative emotions
- [ ] Create documentation with readthedocs
- [ ] Implementação de parceira Rabot & Instituição

**v3.0.3 (est. 3 weeks)** d: 27/04
- [ ] Create 3 new dialogs
- [ ] Create method to detect positive emotions
- [ ] Set up automatic deploy on Heroku to use in other Universities
- [ ] Feedback das instituições

**v3.0.4 (est. 4 weeks)** d: 25/05
- [ ] Create 5 more dialogs
- [ ] Create method to recognize individual emotional level
- [ ] Set up automatic deploy on Raspberry Pi
- [ ] Act on institution's feedback

**v3.0.5 (est. 1 week)** d: 01/06
- [ ] Battery of tests with students
- [ ] Battery of tests with institutions
- [ ] Improve documentation 

**v3.1.0 (est. 2 weeks)** d: 15/06
- [ ] Battery of tests to find possible bugs and error prone dialogs
- [ ] Check if bot is fully-fledged 
  - [ ] Can maintain coherent dialog
  - [ ] Can maintain entretaining dialog 
  - [ ] Can identify user's mood
  - [ ] Can follow up on possible treatment

**v3.1.1**
- [ ] Improve on 3.1.0 feedback
- [ ] Set up bot to work with Facebook Messenger

**v3.1.2** - TBD

# Challenges

Obstacle: Open ended conversations, multiple choices
Possibe solution: Narrow bot's questions and emulate possible answers
