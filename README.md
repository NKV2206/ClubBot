# ClubBot
Discord bot application to display the events of WEC Club 

Using API hikari and A command handler library lightbulb

Slash Commands have been used to display the following commands..

(1)events : Command to display the upcoming Technical Events of the Club

(2)past-events : Command to display the technical events that conculded in the past 30 days

(3)non-tech-events :  Command to display the upcoming Non-Technical Events of the Club

(4)past-nontech-events : Command to display the non-technical events that conculded in the past 30 days 

(5)wec-core : Command that displays the Present WEC Core team

(6)A slash command for each sig : Displays small Details pertaining to the sig and also their upcoming events

The Data is stored in mongodb database

To Update The contents of the database An Interface is created using Express,EJS Templating Engine, MongoDB and Node JS

Through the interface The user can add events,edit the existing data and/or delete the existing data


