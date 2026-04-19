from kickapi import KickAPI
# https://github.com/Enmn/KickApi
import os


class KickPoc:
    @staticmethod
    def get_channel_clips(username: str) -> None:
        kick_api = KickAPI()

        channel = kick_api.channel(username)

        for clip in channel.clips:
            print(clip)

    @staticmethod
    def get_channel_details(username: str) -> None:
        kick_api = KickAPI()

        channel = kick_api.channel(username)

        print(f'Channel ID: {channel.id}\nUsername: {channel.username}')
        print(f'Follower Count: {channel.followers}\nBio: {channel.bio}')
        print('Avatar URL:', channel.avatar)
        print('Playback URL:', channel.playback)


if __name__ == '__main__':
    channel_names: list[str] = str(os.getenv('KickChannels')).split('|')

    for channel_name in channel_names:
        # KickPoc.get_channel_details(channel_name)
        KickPoc.get_channel_clips(channel_name)
        print('')
