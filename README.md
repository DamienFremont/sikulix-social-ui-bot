:warning: WORK IN PROGRESS
==========================

# SikuliX IDE - Twitter Bot

[![Twitter Follow](https://img.shields.io/twitter/follow/Damien_Fremont?style=social)](https://x.com/Damien_Fremont)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

2024's advanced Twitter Bot using Sikulix-IDE and web-browser UI (ex: Firefox).

![alt text](./docs/README/thumb.png)

## Content

  - [Dependencies](#dependencies)
  - [Screenshots](#screenshots)
  - [Features](#features)
  - [Install](#install)
  - [Usage](#usage)
  - [Resources](#resources)

---------------------------------------

## Dependencies

- Java 8+
- FireFox + Container
- [SikuliX IDE v2.0.5](http://sikulix.com/)

## Screenshots

![alt text](./docs/README/screenshot.gif)

![alt text](./docs/README/screenshot-1.png)

![alt text](./docs/README/screenshot-2.png)

## Features

- Targets:
  - [x] Win64 (Windows)
- Twitter
  - [x] site: open, close
  - [x] favtweet.py
  - [x] retweetuser.py
  - [x] followback.py
  - [ ] followfriendsof.py
  - [ ] tweetfile.py
  - [ ] tweet_saturdayscreenshot.py
- Firefox
  - [x] app: start, stop
  - [x] container: open
  - [ ] gesture: swipe
  - [ ] display: mobile

Repository layout:
```
├── docs
├── platform
│   └── firefox...
│   └── twitter...
├── standalone
│   ├── twitter-bot
└── tools
    └── ci
```

## Install

### Windows

Java:
- use your existing Java version 
- ...or follow SikuliX official [quickstart](http://sikulix.com/quickstart/)

FireFox + Container:
- download app [FireFox](https://www.mozilla.org/en-US/firefox/download/thanks/)
- install extension [Firefox Multi-Account Containers](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
- open a tab with a container (ex: `Work`)

![alt text](./docs/README/firefox-install-1.png)

![alt text](./docs/README/firefox-install-2.png)

![alt text](./docs/README/firefox-install-3.png)

![alt text](./docs/README/firefox-install-4.png)

SikuliX IDE:
- Download the `v2.0.5` release of `SikuliX IDE` at https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar.

## Usage

### CLI

TODO

### SikuliX IDE

- Start `SikuliX IDE`
- Run (SikuliX):
  - Menu > "File" > "Open" > `C:/...git/sikulix-twitter-bot/plateform/bot-twitter`
  - click "Run"

![alt text](./docs/README/sikulix-usage.png)

- Stop a running script with: <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>

## Resources

- Sikulix
  - [SikuliX](http://sikulix.com/)
  - [Keys](https://sikulix-2014.readthedocs.io/en/latest/keys.html)
  - [Running Scripts](https://sikulix.github.io/docs/scripts/running-scripts/)
