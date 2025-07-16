import m3u8
import requests

video_uri = "https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8"

master_playlist = m3u8.load(video_uri)
print(master_playlist.dumps())
for variants in master_playlist.playlists:
    print(variants.uri)

variant_uri = master_playlist.playlists[0].absolute_uri
print( f"loading variant uri = {variant_uri}")

variant_playlist = m3u8.load(variant_uri)

for segment in variant_playlist.segments:
    print(segment.uri)
