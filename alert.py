import pickle
from datetime import datetime
import requests

from push import send_push

API_URL = 'https://api.twitch.tv/kraken/streams?channel='


def get_stream_info(channel_list):
    """Returns list of streams from channel_list that are online"""
    channel_list_string = ','.join(str(x) for x in channel_list)
    response = requests.get(API_URL + channel_list_string)
    if not response.status_code == requests.codes.ok:
        return
    channels = response.json()['streams']
    keys = [
        'status',
        'url',
        'name',
        ]
    time = datetime.now()
    online_channels = []
    for channel in channels:
        channel_dict = {key: channel['channel'][key] for key in keys}
        channel_dict['time'] = time
        channel_dict['online'] = True
        online_channels.append(channel_dict)
    return online_channels


def save_streams(stream_list):
    """Saves the stream info so that we don't need to send an alert
    if one has already been sent. Returns streams and new stream names"""

    with open('streams.pickle', 'r') as f:
        old = pickle.load(f)

    updated_streams = []
    new_stream_names = [x['name'] for x in stream_list]
    old_stream_names = [x['name'] for x in old]
    newly_online_names = list(set(new_stream_names)-set(old_stream_names))
    now_offline_streams = list(set(old_stream_names)-set(new_stream_names))

    # Ignore streams that are offline for
    # more than 15 mins since last check
    time = datetime.now()
    for stream in old:
        if stream['name'] in now_offline_streams:
            if (time - stream['time']).total_seconds() < 15*60:
                stream['online'] = False
                updated_streams.append(stream)

    # Brand new streams
    for stream in stream_list:
        if stream['name'] in newly_online_names:
            updated_streams.append(stream)

    # Still online streams
    for stream in stream_list:
        if stream['name'] in old_stream_names:
            if stream['online'] == True:
                updated_streams.append(stream)

    with open('streams.pickle', 'wb') as f:
        pickle.dump(updated_streams, f)

    # also return newly online stream names so we know what to push
    return updated_streams, newly_online_names


if __name__ == '__main__':

    with open('streams.txt') as f:
        channel_list = f.read().split('\n')

    stream_info = get_stream_info(channel_list)
    streams, new = save_streams(stream_info)

    for stream in streams:
        if stream['name'] in new:
            send_push(stream)
