## 0.73.0 (2021-10-14)

### Feat

- get resume from profile

## 0.72.1 (2021-10-11)

### Fix

- **Dependency**: Bump tensorflow to 2.6.0

## 0.72.0 (2021-10-08)

### Feat

- Add transactions.get (#174)

## 0.71.0 (2021-10-05)

### Feat

- Add naas-auth and naas-credits drivers. (#172)

## 0.70.11 (2021-09-27)

### Fix

- lint error in slack.py, variable not used
- lint error in slack.py, variable not used
- error in the driver

## 0.70.10 (2021-09-27)

### Fix

- rename class and path in init.py

### Refactor

- rename of the driver zappier -> zapier

## 0.70.9 (2021-09-20)

### Refactor

- notion driver api

## 0.70.8 (2021-09-16)

### Refactor

- delete folder input/output and have only one folder (#160)

## 0.70.7 (2021-08-31)

### Fix

- huggingface driver

## 0.70.6 (2021-08-31)

### Fix

- **Streamlit**: Do not create ngrok tunnel when loading Streamlit class

### Refactor

- change streamlit 'run_app' into 'add' and fix the function

## 0.70.5 (2021-08-26)

## 0.70.4 (2021-08-18)

### Fix

- put the query into args

## 0.70.3 (2021-08-17)

### Refactor

- change params on gets fucntions

## 0.70.2 (2021-08-16)

## 0.70.1 (2021-08-16)

### Fix

- lint code, remove line break
- get() got multiple values for argument fields

## 0.70.0 (2021-08-04)

### Fix

- lint hubspot

### Feat

- get pipelines on hubspot

## 0.69.3 (2021-08-03)

### Refactor

- get request error
- get by page

## 0.69.2 (2021-07-15)

### Fix

- (qonto) import emailbuilder

## 0.69.1 (2021-07-15)

### Fix

- (qonto) remove from naas_drivers import emailbuilder

## 0.69.0 (2021-07-15)

### Fix

- change headers in requests
- lint code with black

### Feat

- (linkedin) get company info

## 0.68.0 (2021-07-15)

### Fix

- (qonto) get dates
- (qonto) code smell + email
- (qonto) remove raise
- (emailbuilder) remove header in generate (deprecated)

### Feat

- create weekly email with barline, cash sumary, last transactions

## 0.67.1 (2021-07-12)

### Fix

- remove deprecated from emailbuilder
- remove drepecated from linkedin driver

## 0.67.0 (2021-06-28)

### Refactor

- black format

### Feat

- get conversation in loop
- loop to get conversations

## 0.66.8 (2021-06-23)

### Fix

- gsheet change type to string to send data

## 0.66.7 (2021-06-23)

### Fix

- change randint by secret.randbelow
- random.randint
- add sensitive for randint (security)
- avoid object error
- add random time sleep to mimic human behavior
- linkedin remove tags and reorder post get stats
- get_user_urn

## 0.66.6 (2021-06-22)

### Fix

- linkedin post get stats columns order

## 0.66.5 (2021-06-22)

### Fix

- remove tests
- post.get_stats get good urn

### Refactor

- post.get_stats format based on profile.get_posts_stats
- post.get_stats POST_URL column in second position

## 0.66.4 (2021-06-21)

### Fix

- email builder table text align is not always set to left

## 0.66.3 (2021-06-21)

### Fix

- lint black
- linkedin get posts stats, improve send message
- remove a debug print
- post.get_stats

## 0.66.2 (2021-06-18)

### Fix

- linkedin driver bugs

## 0.66.1 (2021-06-18)

### Fix

- linkedin inheritance
- uncomment import + format black

### Refactor

- rename invitation.send_invitation to invitation.send

## 0.66.0 (2021-06-18)

## 0.65.1 (2021-06-17)

### Fix

- change function name get posts stats from profile and get stats from post

## 0.65.0 (2021-06-17)

### Refactor

- black format

### Feat

- add invitation.send + message.get_conversations + message.get_messages
- get post info and get profile posts + deprecated function

## 0.64.0 (2021-06-15)

### Fix

- change api event/getGuests

### Feat

- linkedin get guests from event

## 0.63.0 (2021-06-15)

### Feat

- add post get_likes(), get_comment()

## 0.62.0 (2021-06-14)

### Fix

- linkedin api lint - variable not used

### Feat

- linkedin network get connections / get followers

## 0.61.2 (2021-06-14)

### Fix

- get_identity change address name
- error connected_at and change params names

## 0.61.1 (2021-06-14)

### Fix

- params json in requests
- error lint linkedin driver
- refacto linkedin function with heritage
- refacto linkedin code profile

## 0.61.0 (2021-06-08)

### Refactor

- allow user to target one user for message

### Feat

- Linkedin add send_message

## 0.60.0 (2021-06-02)

### Fix

- hubspot lint
- (hubspot) import re

### Feat

- create note in hubspot, get contacts / deals with multiples properties

## 0.59.0 (2021-05-31)

### Fix

- lint code
- catch exception when request for post like

### Feat

- linkedin add get_post_likes()

## 0.58.1 (2021-05-31)

## 0.58.0 (2021-05-30)

### Fix

- missing comma

### Feat

- update text style option
- new email functions
- the emailBuilder allow to set tables headers

### Refactor

- code lint fix
- table text has the same size than others

## 0.57.1 (2021-05-26)

## 0.57.0 (2021-05-26)

## 0.56.0 (2021-05-25)

## 0.55.0 (2021-05-17)

### Fix

- rename ADDRESS in dataframe get profile
- get activity from url
- update get post data

## 0.54.8 (2021-04-29)

### Fix

- revert numpy

## 0.54.7 (2021-04-26)

### Refactor

- badge is now github friendly

## 0.54.6 (2021-04-06)

### Fix

- use fixed get-changelog version

## 0.54.5 (2021-04-06)

### Fix

- add changelog output in slack

## 0.54.4 (2021-04-01)

### Fix

- numpy

## 0.54.3 (2021-04-01)

### Fix

- revert idna version

## 0.54.2 (2021-04-01)

### Fix

- rollback cython version

## 0.54.1 (2021-04-01)

### Fix

- readme

## 0.54.0 (2021-03-26)

### Feat

- allow send df in airtable

## 0.53.1 (2021-03-23)

### Fix

- ci

## 0.53.0 (2021-03-23)

### Feat

- add pyppeteer

## 0.52.2 (2021-03-22)

### Fix

- google sheet display error

## 0.52.1 (2021-03-18)

### Fix

- version for now htmlbuilder

## 0.52.0 (2021-03-18)

## 0.51.8 (2021-03-18)

### Fix

- chardet version

## 0.51.7 (2021-03-18)

### Fix

- tag commit

## 0.51.6 (2021-03-18)

### Fix

- commit message

## 0.51.5 (2021-03-18)

### Fix

- ci remove useless step

## 0.51.4 (2021-03-17)

### Fix

- make naas_drivers update naas

## 0.51.3 (2021-03-16)

### Fix

- ci slack notif

## 0.51.2 (2021-03-16)

### Fix

- username

## 0.51.1 (2021-03-16)

### Fix

- slack notif

## 0.51.0 (2021-03-16)

### Feat

- add slack notif in ci

## 0.50.0 (2021-03-16)

### Feat

- add google lib

## 0.49.0 (2021-03-15)

### Feat

- add delete method in gsheet + fix append

## 0.48.12 (2021-03-12)

### Fix

- gsheet timestamp convert

## 0.48.11 (2021-03-12)

### Fix

- pr action

## 0.48.10 (2021-03-12)

### Fix

- remove useless module

## 0.48.9 (2021-03-12)

### Fix

- version numpy

## 0.48.8 (2021-03-12)

### Fix

- idna version

## 0.48.7 (2021-03-12)

### Fix

- version Cython

## 0.48.6 (2021-03-12)

### Fix

- version cython

## 0.48.5 (2021-03-12)

### Fix

- fix dependency

## 0.48.4 (2021-03-11)

### Fix

- email builder name

## 0.48.3 (2021-03-11)

### Fix

- awesome notebook

## 0.48.2 (2021-03-10)

### Fix

- add missing libs

## 0.48.1 (2021-03-09)

### Fix

- awesome notebook badges

## 0.48.0 (2021-03-03)

### Feat

- allow branch settting

## 0.47.0 (2021-03-03)

### Feat

- add badge generator

## 0.46.1 (2021-03-02)

### Fix

- get_authorize_user and change_authorize_user

## 0.46.0 (2021-03-01)

### Feat

- add torch

## 0.45.0 (2021-02-23)

### Fix

- awesomenotebook list return
- open or read function

### Feat

- make __open_or_read generic

## 0.44.0 (2021-02-22)

### Feat

- add awesomenotebook

## 0.43.1 (2021-02-22)

### Fix

- pdf error in request mode

## 0.43.0 (2021-02-19)

## 0.42.5 (2021-02-11)

### Fix

- missing function from gilson merge :/

## 0.42.4 (2021-02-10)

### Fix

- notion token or email

## 0.42.3 (2021-02-10)

### Fix

- email missing code + notion

## 0.42.2 (2021-02-10)

### Fix

- color logo

## 0.42.1 (2021-02-10)

### Fix

- linkedin issue

## 0.42.0 (2021-02-02)

### Feat

- add linkedin get_profil

## 0.41.5 (2021-01-28)

### Fix

- refactore Zappier and integromat make it work like all

## 0.41.4 (2021-01-28)

### Fix

- gsheet send data

## 0.41.3 (2021-01-27)

### Fix

- deprecated message

## 0.41.2 (2021-01-26)

### Refactor

- **html**: :boom: rename html in emailBuilder since it's used for that

## 0.41.1 (2021-01-25)

### Fix

- add documentation link

## 0.41.0 (2021-01-25)

### Feat

- add image upload
- allow send image in teams
- add teams connector

### Fix

- add missing module

## 0.40.0 (2021-01-25)

### Feat

- add slack to send messages

## 0.39.0 (2021-01-25)

### Feat

- add makrdown viewer

## 0.38.1 (2021-01-13)

### Fix

- update readme to deploy new release tag

## 0.38.0 (2021-01-13)

### Fix

- remove buggy changelog
- readme add return line
- **linkedin**: remove useless code + add missing import

## 0.38.0b7 (2021-01-11)

### Fix

- **linkedin**: indentation fix

### Feat

- **linkedin**: added linkedin driver
- **linkedin**: added linkedin connector

## 0.38.0b6 (2021-01-05)

### Fix

- ci script python version
- ci script python version

## 0.38.0b5 (2021-01-05)

### Fix

- ci script

## 0.38.0b4 (2021-01-05)

### Fix

- tensorflow version

## 0.38.0b3 (2021-01-05)

### Fix

- remove useless build command

## 0.38.0b2 (2021-01-05)

### Fix

- lint errors

## 0.38.0b1 (2021-01-05)

### Fix

- remove dup code

## 0.38.0b0 (2021-01-05)

### Feat

- add sessions endpoint
- **notion**: add notion driver updated notion driver
- **notion**: notion driver added notion driver to get collection view
- use crud everywhere
- add raise_for_error everywhere
- add raise_for_error

### Fix

- get hubspot from main
- lint use function for error
- **notion**: notion driver updated notion driver fix
- **notion**: notion driver fixed env
- **thinkific**: merge main into thinkific branch
- **thinkific**: change thinkific name in import module
- **thinkific**: add thinkific to __init__
- **hubspot**: reinit self.param after get_all
- jup use username everywhere
- code smell
- except catch

## 0.37.0 (2020-11-30)

### Feat

- refactor with api and use dataframe

### Fix

- correct user_id by self.user_id in request
- correct __filter_dates parameters
- code smell and duplicates
- change variable object_id
- apply pycodestyle
- apply pycodestyle
- apply pycodestyle

## 0.36.0 (2020-11-28)

### Feat

- add set_seen and set_flag
- add criteria in get email

### Fix

- use reverse mode

## 0.35.0 (2020-11-28)

### Fix

- **ci**: switch to conventional-pr-title-action
- **ci**: switch to conventional-pr-title-action
- **ci**: pr script
- **ci**: pr script

### Feat

- add get attachement
- add get attachement
- add get email from email box
- add get email from email box

## 0.34.6 (2020-11-26)

### Fix

- export screenshotmap
- export screenshotmap
- udpate new formulas
- update thinkific driver
- update hubspot driver

### Feat

- init qonto driver
- init hubspot driver
- add hubspot to init

## 0.35.0b1 (2020-11-19)

### Feat

- **jupyter**: add default token

## 0.35.0b0 (2020-11-17)

## 0.34.5 (2020-11-17)

### Fix

- **email**: args

## 0.34.4 (2020-11-14)

### Fix

- **jupyter**: token

## 0.34.3 (2020-11-14)

### Fix

- **airtable**: connector

## 0.34.2 (2020-11-14)

### Fix

- **jupyter**: use normal token to connect
- **airtable**: send

## 0.34.1 (2020-11-14)

### Fix

- **airtable**: connector

## 0.34.0 (2020-11-13)

### Feat

- add jupyter authorize

## 0.33.0 (2020-11-12)

### Feat

- add change_password_user

## 0.32.0 (2020-11-11)

### Feat

- **thinkific**: add course_reviews

## 0.31.1 (2020-11-10)

### Fix

- **thinkific**: use api as expected with subdomain

## 0.31.0 (2020-11-10)

### Feat

- **thinkific**: add v0 connector

## 0.30.1 (2020-11-10)

### Fix

- **html**: connector

## 0.30.0 (2020-11-09)

### Feat

- **jupyter**: add list and delete users

## 0.30.0b0 (2020-11-09)

## 0.29.3 (2020-11-09)

### Fix

- remove docker build
- remove docker build

## 0.29.2 (2020-11-09)

### Fix

- **bobapp**: use send instead of insert
- **bobapp**: use send instead of insert

## 0.29.1 (2020-11-09)

### Fix

- bobapp print
- bobapp print

## 0.29.0 (2020-11-09)

### Feat

- add canny
- add canny

## 0.28.1 (2020-11-09)

### Fix

- add print when file creating
- add print when file creating

## 0.28.0 (2020-11-09)

### Feat

- **html**: add utils
- **html**: add utils

## 0.27.2 (2020-11-09)

### Fix

- connect return self
- connect return self
- **gsheet**: fix connect
- **gsheet**: fix connect

## 0.27.1 (2020-11-09)

### Fix

- **bobapp**: create_or_update function
- **bobapp**: create_or_update function

## 0.27.0 (2020-11-04)

### Feat

- **html**: table
- **html**: table

## 0.26.1 (2020-11-04)

### Fix

- **html**: padding
- **html**: padding

## 0.26.0 (2020-11-04)

### Feat

- **plotly**: allow show or not graph
- **plotly**: allow show or not graph
- **prediction**: add concat_label feature
- **prediction**: add concat_label feature

## 0.25.6 (2020-11-04)

### Fix

- **plotly**: colors for ma20 ma50
- **plotly**: colors for ma20 ma50

## 0.25.5 (2020-11-04)

### Fix

- **plotly**: allow any moving average
- **plotly**: allow any moving average

## 0.25.4 (2020-11-04)

### Fix

- bobapp remove token in services
- bobapp remove token in services

## 0.25.3 (2020-11-04)

### Fix

- **jupyter**: create_user
- **jupyter**: create_user

## 0.25.2 (2020-11-04)

### Fix

- allow connect default api newapi cityfalcon
- allow connect default api newapi cityfalcon

## 0.25.1 (2020-11-04)

### Fix

- **cityfalcon**: change default field for logo
- **cityfalcon**: change default field for logo

## 0.25.0 (2020-11-04)

### Feat

- **optimise**: add optimise lib for eavy df
- **optimise**: add optimise lib for eavy df

## 0.24.24 (2020-11-04)

### Fix

- **cityfalcon**: add wrong field name when error
- **cityfalcon**: add wrong field name when error

## 0.24.23 (2020-11-04)

### Fix

- error in mongo connector
- error in mongo connector

## 0.24.22 (2020-11-03)

### Fix

- **mongo**: allow get client
- **mongo**: allow get client

## 0.24.21 (2020-11-03)

### Fix

- import errors
- import errors

## 0.24.20 (2020-11-03)

### Fix

- setup config
- setup config

## 0.24.19 (2020-11-03)

### Fix

- import
- import

## 0.24.18 (2020-11-03)

### Fix

- path import
- path import

## 0.24.17 (2020-11-03)

### Fix

- build
- build

## 0.24.16 (2020-11-03)

### Fix

- **ftp**: code smell
- **ftp**: code smell

## 0.24.15 (2020-11-03)

### Fix

- code smells
- code smells

## 0.24.14 (2020-11-03)

### Fix

- code smells
- code smells
- code smells use const
- code smells use const

## 0.24.13 (2020-11-03)

### Fix

- error class naming
- error class naming

## 0.24.12 (2020-11-03)

### Fix

- code smells
- code smells

## 0.24.11 (2020-11-03)

### Fix

- **plotly**: add missing self
- **plotly**: add missing self

## 0.24.10 (2020-11-03)

### Fix

- code smells prediction
- code smells prediction

## 0.24.9 (2020-11-03)

### Fix

- code smells Out_Driver
- code smells Out_Driver

## 0.24.8 (2020-11-03)

### Fix

- **toucan**: code smel
- **toucan**: code smel

## 0.24.7 (2020-11-03)

### Fix

- error
- error

## 0.24.6 (2020-11-03)

### Fix

- halthchecks
- halthchecks

## 0.24.5 (2020-11-03)

### Fix

- naming
- naming

## 0.24.4 (2020-11-03)

### Fix

- arg name to better naming for bobapp api
- arg name to better naming for bobapp api

## 0.24.3 (2020-11-03)

### Fix

- bobapp functions location
- bobapp functions location

## 0.24.2 (2020-11-03)

### Fix

- BOBAPP_API env var
- BOBAPP_API env var

## 0.24.1 (2020-11-02)

### Fix

- cityfalcon logo field
- cityfalcon logo field

## 0.24.0 (2020-11-02)

### Fix

- class parent
- class parent
- start prediction with last know day
- start prediction with last know day
- plot stock if no company
- plot stock if no company
- naming
- naming
- airtable connector convertor
- airtable connect
- for dk connect

### Feat

- **cityfalcon**: add date
- **cityfalcon**: add date
- expose sentiment categorize
- expose sentiment categorize

## 0.23.4 (2020-11-02)

### Fix

- airtable connector convertor
- airtable connect

## 0.23.3 (2020-11-02)

### Fix

- for dk connect

## 0.23.2 (2020-10-29)

### Fix

- sentiment analysis
- sentiment analysis

## 0.23.1 (2020-10-29)

### Fix

- **newsapi**: add missing import
- **newsapi**: add missing import

## 0.23.0 (2020-10-29)

### Feat

- **newsapi**: :sparkles: add newsapi driver
- **newsapi**: :sparkles: add newsapi driver

## 0.22.1 (2020-10-29)

### Fix

- **cityfalcon**: allow default config for cityfalcon
- **cityfalcon**: allow default config for cityfalcon

## 0.22.0 (2020-10-29)

### Feat

- **plotly**: allow multi export
- **plotly**: allow multi export

## 0.21.0 (2020-10-27)

### Feat

- **jupyter**: add create_user
- **jupyter**: add create_user

## 0.20.1 (2020-10-27)

### Fix

- add doc function
- add doc function

## 0.20.0 (2020-10-27)

### Feat

- add jupyter drivers
- add jupyter drivers

## 0.19.0 (2020-10-27)

### Feat

- add linechart simple in plot and candlestick
- add linechart simple in plot and candlestick

## 0.18.12 (2020-10-27)

### Fix

- prediction with prediction_type COMPOUND default
- prediction with prediction_type COMPOUND default

## 0.18.11 (2020-10-27)

### Fix

- readme
- readme

## 0.18.10 (2020-10-27)

### Fix

- remove update description
- remove update description

## 0.18.9 (2020-10-26)

### Fix

- show only open or close on stock plotly
- show only open or close on stock plotly

## 0.18.8 (2020-10-26)

### Fix

- remove useless plot var
- remove useless plot var

## 0.18.7 (2020-10-26)

### Fix

- allow multi company group
- allow multi company group

## 0.18.6 (2020-10-26)

### Fix

- predict for multi company
- predict for multi company

## 0.18.5 (2020-10-26)

### Fix

- prediction
- prediction

## 0.18.4 (2020-10-26)

### Fix

- prediction work with yahoo and plotly
- prediction work with yahoo and plotly

## 0.18.3 (2020-10-26)

### Fix

- prediction
- prediction

## 0.18.2 (2020-10-26)

### Fix

- import airtable
- import airtable

## 0.18.1 (2020-10-25)

### Fix

- allow HealthCheck to connect
- allow HealthCheck to connect

## 0.18.0 (2020-10-25)

### Feat

- deploy new singleuser
- deploy new singleuser
- deploy new singleuser
- deploy new singleuser
- switch all drivers to nocall
- switch all drivers to nocall

### Fix

- airtable
- airtable

## 0.17.0 (2020-10-22)

### Feat

- mix all ftp libs
- mix all ftp libs

## 0.16.0 (2020-10-21)

### Feat

- add update check
- add update check

## 0.15.3 (2020-10-21)

### Fix

- plotly for not supported
- plotly for not supported

## 0.15.2 (2020-10-21)

### Fix

- plotly html remove
- plotly html remove

## 0.15.1 (2020-10-21)

### Fix

- allow plotly export jpeg
- allow plotly export jpeg

## 0.15.0 (2020-10-21)

### Feat

- add integromat
- add integromat

## 0.14.2 (2020-10-21)

### Fix

- ifft issue who don't return json
- ifft issue who don't return json

## 0.14.1 (2020-10-21)

### Fix

- simplify gsheet driver
- simplify gsheet driver

## 0.14.0 (2020-10-21)

### Feat

- split plot in plotly and yahoo
- split plot in plotly and yahoo

## 0.13.1 (2020-10-19)

### Fix

- build ci
- build ci

## 0.13.0 (2020-10-19)

### Feat

- **ifttt**: :sparkles: add ifttt connector
- **ifttt**: :sparkles: add ifttt connector

## 0.12.0 (2020-10-19)

### Feat

- **bubble**: :sparkles: add bubble connector
- **bubble**: :sparkles: add bubble connector

## 0.11.0 (2020-10-19)

### Feat

- **zappier**: :zap: create zappier connector
- **zappier**: :zap: create zappier connector

## 0.10.0 (2020-10-19)

### Feat

- **airtable**: :sparkles: add airtable
- **airtable**: :sparkles: add airtable

## 0.9.13 (2020-10-16)

### Fix

- python version build to 8
- python version build to 8

## 0.9.12 (2020-10-16)

### Fix

- tensorflow error version
- tensorflow error version

## 0.9.11 (2020-10-16)

### Fix

- embed_small_app_slide
- embed_small_app_slide

## 0.9.10 (2020-10-15)

### Fix

- **gsheets**: comment test for now
- **gsheets**: comment test for now

## 0.9.9 (2020-10-15)

### Fix

- add missing lib
- add missing lib

## 0.9.8 (2020-10-15)

## 0.9.7 (2020-10-15)

### Fix

- ci typo pr check

## 0.9.6 (2020-10-14)

### Fix

- **html**: :bug: Correct preview text

## 0.9.5 (2020-10-14)

### Fix

- :sparkles: refactor name and follow good practice
- **gsheet**: fix google spreadsheet driver
- ci typo pr check
- **html**: :bug: Correct preview text
- :sparkles: refactor name and follow good practice
- **html**: :bug: fix display feature
- **html**: :bug: fix display into jupyter
- **html**: :bug: font familly
- **ftp**: :bug: add missign toucan_ftp
- **html**: :bug: rename default button
- **plot**: :sparkles: add moving average
- update to AGPL
- **gsheet**: fix google spreadsheet driver

### Feat

- **ftp**: :sparkles: add ftp toucan lib and fix ftps lib
- **ci**: :sparkles: add pandas datareader

## 0.9.4 (2020-10-13)

### Fix

- **html**: :bug: fix display feature

## 0.9.3 (2020-10-13)

### Fix

- **html**: :bug: fix display into jupyter

## 0.9.2 (2020-10-13)

### Fix

- **html**: :bug: font familly

## 0.9.1 (2020-10-12)

### Fix

- **ftp**: :bug: add missign toucan_ftp

## 0.9.0 (2020-10-12)

### Feat

- **ftp**: :sparkles: add ftp toucan lib and fix ftps lib

## 0.8.3 (2020-10-12)

### Fix

- **html**: :bug: rename default button

## 0.8.2 (2020-10-12)

### Fix

- **plot**: :sparkles: add moving average

## 0.8.1 (2020-10-12)

### Fix

- update to AGPL

## 0.8.0 (2020-10-12)

### Feat

- **ci**: :sparkles: add pandas datareader

## 0.7.4 (2020-10-12)

### Fix

- **citifalcon**: :bug: fix typo
- **citifalcon**: :bug: fix typo

## 0.7.3 (2020-10-11)

### Fix

- **citifalcon**: :bug: fix get image\
- **citifalcon**: :bug: fix get image\

## 0.7.2 (2020-10-11)

### Fix

- **plot**: :bug: allow 0 value, for date_to
- **plot**: :bug: allow 0 value, for date_to

## 0.7.1 (2020-10-11)

### Fix

- **html**: :sparkles: allow change order to template
- **html**: :sparkles: allow change order to template

## 0.7.0 (2020-10-11)

### Feat

- **citifalcon**: :sparkles: add limit in get
- **citifalcon**: :sparkles: add limit in get

## 0.6.2 (2020-10-11)

### Fix

- **plot**: :bug: dont remove html if already exist
- **plot**: :bug: dont remove html if already exist

## 0.6.1 (2020-10-11)

### Fix

- **plot**: :sparkles: allow stock to be only one
- **plot**: :sparkles: allow stock to be only one

## 0.6.0 (2020-10-11)

### Feat

- **plot**: :sparkles: allow date to be number
- **plot**: :sparkles: allow date to be number

## 0.5.0 (2020-10-11)

### Feat

- **citifalcon**: :sparkles: add cityfalcon api + refactor html lib to make it simple
- **citifalcon**: :sparkles: add cityfalcon api + refactor html lib to make it simple

## 0.4.11 (2020-10-10)

### Fix

- **html**: :bug: fix order link args
- **html**: :bug: fix order link args

## 0.4.10 (2020-10-09)

### Fix

- **html**: :art: auto add uid to image to alow user send new image with same name
- **html**: :art: auto add uid to image to alow user send new image with same name

## 0.4.9 (2020-10-09)

### Fix

- triger ci build
- triger ci build

## 0.4.8 (2020-10-09)

### Refactor

- **html**: :art: use kwargs
- **html**: :art: use kwargs

## 0.4.7 (2020-10-09)

### Refactor

- **html**: :truck: tempalte_basic t0 main
- **html**: :truck: tempalte_basic t0 main

## 0.4.6 (2020-10-09)

### Fix

- **html**: change table to support mode usecase
- **html**: change table to support mode usecase

## 0.4.5 (2020-10-09)

### Fix

- **ci**: :bug: use latest ref for build naas
- **ci**: :bug: use latest ref for build naas

## 0.4.4 (2020-10-09)

### Fix

- **html**: :bug: change color of subsubtitle
- **html**: :bug: change color of subsubtitle

## 0.4.3 (2020-10-09)

### Fix

- **html**: :bug: fix subtitle of title
- **html**: :bug: fix subtitle of title

## 0.4.2 (2020-10-09)

### Fix

- :green_heart: fix event who is send to naas build
- :green_heart: fix event who is send to naas build

## 0.4.1 (2020-10-08)

### Fix

- **html**: :bug: fix missing module
- **html**: :bug: fix missing module

## 0.4.0 (2020-10-08)

### Feat

- **html**: :sparkles: add new html lib
- **html**: :sparkles: add new html lib

## 0.3.1 (2020-10-08)

### Fix

- **plot**: :bug: add default css to all css
- **plot**: :bug: add default css to all css

## 0.3.0 (2020-10-07)

### Feat

- add PR linter
- add PR linter

### Fix

- add upgrade before install
- add upgrade before install

## 0.2.7 (2020-10-06)

### Fix

- :green_heart: create our own github action
- :green_heart: create our own github action

### Perf

- :construction_worker: add cache for faster build
- :construction_worker: add cache for faster build

## 0.2.6 (2020-10-06)

### Fix

- :bug: ci fix
- :bug: ci fix

## 0.2.5 (2020-10-06)

### Fix

- :bug: fix build docker image
- :bug: fix build docker image

## 0.2.4 (2020-10-06)

### Fix

- force deploy to dockerhub
- force deploy to dockerhub

## 0.2.3 (2020-10-06)

### Fix

- :bug: fix append error in scatter chart
- :bug: fix append error in scatter chart

## 0.2.2 (2020-10-06)

## 0.2.2b0 (2020-10-06)

## 0.2.1b1 (2020-10-06)

### Fix

- :art: rewrite and fix plot lib

## 0.2.1b0 (2020-10-05)

## 0.2.1 (2020-10-05)

### Fix

- :construction_worker: fix error branch ci
- :bug: change version
- :green_heart: remove ci dependabot for now
- :ci: add missing tag
- :bug: fix plot function
- try to trigger ci again
- tag format

## 0.2.0b0 (2020-10-04)

### Feat

- add new ci for dev branch

## 0.1.7 (2020-10-04)

### Fix

- try to trigger ci again

## 0.1.6 (2020-10-03)

### Fix

- :bug: add fake test to make the ci pass

## 0.1.5 (2020-10-03)

### Fix

- :bug: remove dependency for test

## 0.1.4 (2020-10-03)

### Fix

- :bug: fix for toucan v74

## 0.1.3 (2020-10-03)

### Fix

- :bug: add missing payload

## 0.1.2 (2020-10-03)

### Fix

- :bug: fix typo in toucan connector

## 0.1.1 (2020-10-03)

### Fix

- :bug: fix import datetime in toucan

## 0.1.0 (2020-10-03)

### Feat

- :sparkles: add embed function to toucan driver

## 0.0.28 (2020-09-29)

### Fix

- :bug: change path of codecov

## 0.0.27 (2020-09-29)

### Fix

- :bug: fix ci workflow for test

## 0.0.26 (2020-09-29)

### Fix

- :bug: ci fix typo docker image name

## 0.0.25 (2020-09-29)

### Fix

- ci typo in dockerhub config

## 0.0.24 (2020-09-29)

### Fix

- :bug: fix ci var name

## 0.0.23 (2020-09-29)

### Fix

- :construction_worker: use new pip syntaxt to install

## 0.0.22 (2020-09-29)

### Fix

- :bug: add missing dependency for test

## 0.0.21 (2020-09-29)

### Fix

- :bug: fix dev dependency
- ci add auto bump
- :hammer: centralyse conf
- add upgrade on pip
- swith back to python 3
- bump version
- :bug: fix docker build
- :construction_worker: better build
- :bug: fix requierements
- :bug: remove test on build with nb_user
- :bug: install naas_drivers as user not root
- :heavy_plus_sign: add missing pysftp
- change mail to email
- :bug: fix mongo connector allow persistency
- error typo class name
- :fire: remove old reference to secret
- manual bump

### Refactor

- :lipstick: add log to email function

## 0.0.7 (2020-09-23)

## 0.0.2 (2020-09-23)
