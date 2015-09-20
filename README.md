## Twitch Stream Alerts

Simple script that sends Pushbullet notifications when a stream you specify comes online.

The script will keep a record of the streams it records and only alert you when a stream is 'newly online'.

Once a stream goes offline it will still keep a record of it for a while. This is because often a stream will go offline briefly and come back. In this situation you would not want to recieve a fresh push notification.

One push alert per stream.

Designed to be ran via cron.
#### Installation

`git clone https://github.com/Saturn/twitch-stream-alerts.git`

#### Config
`PUSHBULLET_API_KEY`
`PUSHBULLET_IDEN_KEY` *(optional)*

To obtain an API key please visit https://www.pushbullet.com/#settings/account

An `iden_key` is optional. Without one it will simply push to all of your devices.

To obtain a connected device's iden key:

```
curl --header 'Access-Token: <PUSHBULLET_API_KEY>' \
https://api.pushbullet.com/v2/devices
```

#### Cron

A possible cron configuration:

 `*/5 * * * * cd ~/twitch_stream_alerts && /usr/bin/python alert.py >/dev/null 2>&1`
 
It will check every five minutes.
