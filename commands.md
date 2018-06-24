# Arc command docs
### Updated as of 24/6/18  

# General commands  
## help
Displays basic help information for the user commands that can be ran.  
Only requires that DMs are open.  
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
Requires Administrator
