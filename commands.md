# Arc command docs
### Updated as of 24/6/18  

# General commands  
## help
Displays basic help information for the user commands that can be ran.  
Only requires that DMs are open.  
## about  
Shows basic information about Arc and other resources.  
## stats
Shows the techniacal stats of Arc (discord.py version, ping, command count, etc.)  
Requires no permissions to run.  
## support  
DMs the support link to the user who ran the command.  
Only requires that DMs are open.  
## donate  
DMs the user a link to the Discord Bot List listing and the Patreon.  
Only requires that DMs are open.  
## ping
Test the response time of the bot in milliseconds.  
Requires no permissions to run.
## invite
DMs the bot invite link to the user who ran the command.  
Requires that DMs are open.
# Moderation commands
## serverinfo  
Displays information about the server the command was ran in (user count, server ID, role count, etc.)  
Requires no permissions to run.
## userinfo `user mention`  
Fetch information on the mentioned user (profile picture, user ID, playing status, etc.)  
Requires no permissions to run.
## warn `user mention` `reason`  
Warn a mentioned user to send a DM to them with a reason for the warning.
Requires Administrator, kick or ban to be ran, as well as the user to have DMs open.
## kick `user mention`
Kick the mentioned user from the server, they can rejoin with a new invite after.  
Requires Administrator or kick permissions.  
## ban `user mention`  
Ban a specified user from the server. They will need to be unbanned manually to rejoin.  
Requires administrator or ban permissions to be ran, as well as the user to have DMs open for an alert.  
## purge `number of messages`  
Mass deletes the specified number of messages in that channel.  
Requires Administrator or manage messages to be ran.  
## avatar `user mention`  
Gets the mentioned users avatar as well as a URL to view in a web browser or to link.  
Requires no permissions to be ran.  
## mute `user mention`  
Mutes a specified user. **Requires a role called `mute` exists or this will error!**  
Requires Administrator or manage roles to be ran.  
## unmute `user mention`  
Unmutes a user with the `Muted` role. **User must of already been muted or this will not work!**  
## addrole `user mention` `role name`  
Adds a specified role to the mentioned user. **Role name must be the correct capitalisation or this won't work.**  
Requires Administrator or manage roles to be ran.  
## removerole `user mention` `role name`  
Removes the specified role from the mentioned user. **User must have role or this will not work.**  
Requires Administrator or manage roles to be ran.  
## announce `channel mention` `message`  
Announce a message to the specified channel.  
Requires Administrator or manage server to be ran.  
# Fun
## slap `user mention`
Slap a user.  
## lick `user mention`  
Lick a user.  
## punch `user mention`  
Punch a user.  
## hug `user mention`  
Hug a user.  
## cookie `user mention`  
Give a cookie to a user.  
## cat  
Shows a random picture of a cat from  [random-d.uk](https://random-d.uk)  
## duck  
Shows a random picture of a duck from [The cat API](http://thecatapi.com)  
## roll `NdN`  
Roll a dice in NdN format, example would be `arc!roll 1d4`.  
## wherewedroppin  
Picks a random location from the Fortnite Season 4 map to drop at.  
## eightball `question`  
Ask the 8ball a question.  
## choose `values`  
Pick a random choice. **Requires that all individual values be wrapped in a quotation mark!**  
eg `arc!choose "1" "2" "3"`  
## speak `message`  
Send a message via the bot.  
## gamenews `steam game ID`  
Get news on a steam game from the Steam API.  
## json `JSON API URL`  
Makes a request to the specifed JSON API and prints the results.  
## weather `location`  
Gets local weather forcast from [wttr.in](https://wttr.in)  
## hex  
Generate a random hex color code.  
