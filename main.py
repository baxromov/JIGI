# f = {
#     "dash_manifest": "\u003C?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\u003CMPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http:\/\/www.w3.org\/2001\/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT29.88408088684082S\" FBTagsetUsed=\"gen2hwbasic\" FBManifestIdentifier=\"FgAYC2dlbjJod2Jhc2ljGTbW6eTa9rJH5te56739vAKA18fl9pSRDwA=\">\u003CPeriod id=\"0\" duration=\"PT29.88408088684082S\">\u003CAdaptationSet id=\"0\" contentType=\"video\" frameRate=\"15360\/512\" subsegmentAlignment=\"true\" par=\"1:1\">\u003CRepresentation id=\"697047132354035v\" bandwidth=\"414728\" codecs=\"avc1.64001e\" mimeType=\"video\/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_gen2hwbasic_hq2_frag_2_video\" FBPlaybackResolutionMos=\"0:100,360:91.6,480:90.6,720:90.6,1080:90.6\" FBPlaybackResolutionMosConfidenceLevel=\"high_derived_from_valid_ssim\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:96.6,720:96.6,1080:96.6\" FBAbrPolicyTags=\"hvq_www_inline\" width=\"480\" height=\"480\" FBDefaultQuality=\"1\" FBQualityClass=\"sd\" FBQualityLabel=\"480p\">\u003CBaseURL>https:\/\/video.ftas1-2.fna.fbcdn.net\/v\/t39.25447-2\/394764436_973774753715240_1022829760673677949_n.mp4?_nc_cat=101&amp;ccb=1-7&amp;_nc_sid=9a5d50&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfZ2VuMmh3YmFzaWNfaHEyX2ZyYWdfMl92aWRlbyJ9&amp;_nc_ohc=ptcBBIbMXzoAX9JMeXN&amp;_nc_ht=video.ftas1-2.fna&amp;oh=00_AfB77bes_gGt6O5iHuRjMHDeBshP1okJ9KLqGuyH9Trx2A&amp;oe=654987F6\u003C\/BaseURL>\u003CSegmentBase indexRange=\"865-968\" timescale=\"15360\" FBFirstSegmentRange=\"969-259288\">\u003CInitialization range=\"0-864\"\/>\u003C\/SegmentBase>\u003C\/Representation>\u003CRepresentation id=\"157005577493099v\" bandwidth=\"198497\" codecs=\"avc1.4d0015\" mimeType=\"video\/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_gen2hwbasic_hq1_frag_2_video\" FBPlaybackResolutionMos=\"0:100,360:79.6,480:78.3,720:78.3,1080:78.3\" FBPlaybackResolutionMosConfidenceLevel=\"high_derived_from_valid_ssim\" FBPlaybackResolutionCsvqm=\"0:100,360:92.9,480:92.2,720:92.2,1080:92.2\" FBAbrPolicyTags=\"\" width=\"360\" height=\"360\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\">\u003CBaseURL>https:\/\/video.ftas1-2.fna.fbcdn.net\/v\/t39.25447-2\/2.mp4?_nc_cat=100&amp;ccb=1-7&amp;_nc_sid=9a5d50&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfZ2VuMmh3YmFzaWNfaHExX2ZyYWdfMl92aWRlbyJ9&amp;_nc_ohc=Q8GLuIIinegAX8XLdnQ&amp;_nc_ht=video.ftas1-2.fna&amp;oh=00_AfDAmtQRjxZ8xEzowrkzpwIZAXX_uGi67HgXN5Nw9CfDbg&amp;oe=654987D3\u003C\/BaseURL>\u003CSegmentBase indexRange=\"862-965\" timescale=\"15360\" FBFirstSegmentRange=\"966-115748\">\u003CInitialization range=\"0-861\"\/>\u003C\/SegmentBase>\u003C\/Representation>\u003C\/AdaptationSet>\u003CAdaptationSet id=\"1\" contentType=\"audio\" subsegmentAlignment=\"true\">\u003CRepresentation id=\"4259867587573184a\" bandwidth=\"49550\" codecs=\"mp4a.40.5\" mimeType=\"audio\/mp4\" FBAvgBitrate=\"49550\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_ln_heaac_48_audio\" FBDefaultQuality=\"1\">\u003CAudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"\/>\u003CBaseURL>https:\/\/video.ftas1-1.fna.fbcdn.net\/v\/t58.16807-2\/1.mp4?_nc_cat=110&amp;ccb=1-7&amp;_nc_sid=9a5d50&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfNDhfYXVkaW8ifQ\u00253D\u00253D&amp;_nc_ohc=yPePvcOXNxUAX_Z7Xx_&amp;_nc_ht=video.ftas1-1.fna&amp;oh=00_AfBDdbRWz-O-QN84v54gxyZkskwyP5TupSDtrU4MQO1lIw&amp;oe=654A36CF\u003C\/BaseURL>\u003CSegmentBase indexRange=\"817-1028\" timescale=\"44100\" FBFirstSegmentRange=\"1029-14511\">\u003CInitialization range=\"0-816\"\/>\u003C\/SegmentBase>\u003C\/Representation>\u003C\/AdaptationSet>\u003C\/Period>\u003C\/MPD>\n",
# }
# # xml_string = f['dash_manifest']
# # import html
# # unescaped_xml_string = html.unescape(xml_string)
# #
# # # Now you can work with the unescaped XML string
# # print(unescaped_xml_string)
# # xml_file_name = "output.xml"
# #
# # # Write the unescaped XML string to a file
# # with open(xml_file_name, "w", encoding="utf-8") as xml_file:
# #     xml_file.write(unescaped_xml_string)
# #
# # print(f"XML content has been written to '{xml_file_name}'")
# import subprocess
#
# # Paths to your audio and video files
# audio_file = '1.mp4'  # Replace with your audio file path
# video_file = '2.mp4'  # Replace with your video file path
#
# # Output file name
# output_file = 'output_video.mp4'
#
# # FFmpeg command to merge audio and video
# ffmpeg_cmd = [
#     'ffmpeg',
#     '-i', video_file,
#     '-i', audio_file,
#     '-c:v', 'copy',  # Copy video codec
#     '-c:a', 'aac',   # Choose an audio codec, like AAC
#     '-strict', 'experimental',  # Allow the use of the experimental AAC codec
#     '-map', '0:v:0',  # Map the video stream from the first input
#     '-map', '1:a:0',  # Map the audio stream from the second input
#     output_file
# ]
#
# # Run the FFmpeg command
# subprocess.run(ffmpeg_cmd)
#
# print(f'Merged audio and video into {output_file}')
# import asyncio
#
# from jigi.instagram.download import Instagram
#
# if __name__ == '__main__':
#     async def main():
#         url = "https://www.instagram.com/p/Cy0b81yRaXs/?utm_source=ig_web_copy_link"
#         instagram = Instagram()
#         result = await instagram.getting_video_url(url)
#         print(result)
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

import asyncio

from jigi.facebook.download import Facebook
from jigi.vk.download import VK

if __name__ == '__main__':
    pass
    # async def main():
        # url = "https://www.instagram.com/reel/Cy-T2kzAFAA/?igshid=MzRlODBiNWFlZA=="
        # instagram = Instagram()
        # result = await instagram.getting_video_url(url)
        # print(result)
        #
        # url = 'https://www.facebook.com/100003184976981/videos/317042617709670/'
        # facebook = Facebook()
        # result = await facebook.getting_video_url(url)
        # print(result)
    #     url = "https://vk.com/video-55155418_456241422"
    #     vk = VK()
    #     result = await vk.getting_video_url(url)
    #     print(result)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

