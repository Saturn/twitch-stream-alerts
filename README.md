## Twitch Stream Alerts

Simple script that sends Pushbullet notifications when a [Twitch.tv](http://www.twitch.tv/) stream you specify comes online.

The script will keep a record of the streams it records and only alert you when a stream is 'newly online'.

Once a stream goes offline it will still keep a record of it for a while. This is because often a stream will go offline briefly and come back. In this situation you would not want to recieve a fresh push notification.

One push alert per stream.

Designed to be ran via cron. Currently Python 2.7 only.
#### Installation

`git clone https://github.com/Saturn/twitch-stream-alerts.git`

#### Config

You need to have a Twitch Client ID in order to use the Twitch API. Read more here https://blog.twitch.tv/client-id-required-for-kraken-api-calls-afbb8e95f843

`TWITCH_CLIENT_ID`

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

#### Todo

- [ ] Add tests
- [ ] Support for Python 3
