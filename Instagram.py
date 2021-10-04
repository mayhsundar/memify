from instagramy import InstagramUser
import random as rd


class InstagramCrawler:
    results = []
    instaPages = ["memes", "epicfunnypage", "theindianmemes", "_garib_raja"]
    userName = instaPages[rd.randint(0, len(instaPages)-1)]

    def __init__(self):
        self.getPosts(self.userName)

    def getPosts(self, userName: str):
        userData = InstagramUser(userName).user_data
        posts = userData["edge_owner_to_timeline_media"]["edges"]
        self.results.append({userName: self.getPostDetails(posts)})

    def getPostDetails(self, posts: {}):
        postDetails = []
        for _ in posts:
            cP = _["node"]
            cPData = {}
            if not cP["is_video"]:
                cPData["img"] = True
            else:
                cPData["img"] = False
                cPData["vUrl"] = cP["video_url"]
            cPData["iUrl"] = cP["display_url"]
            cPData["timestamp"] = cP["taken_at_timestamp"]
            postDetails.append(cPData)
        return postDetails
