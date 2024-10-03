import requests
import json
import sys


COOKIE = 'mid=Zv7CCwALAAEsROKPc63akVTvge-t; datr=C8L-ZpJ43D5OdwhM3U1SrAuI; ig_did=50F6E89E-3065-4D9B-B4C7-62E393ABE7E2; ig_nrcb=1; csrftoken=yRXhvOIHY0LhnGZxqSvh9CIKNIK5u7ZZ; ds_user_id=69701345808; sessionid=69701345808%3AMcRinOjm66vDlp%3A2%3AAYfiGgNmSZwcfM97RH4OxPRqRUg72G5nwg0zFIzh0A; wd=412x914; dpr=2.625; rur="EAG\05469701345808\0541759508197:01f71d437a1879557bd8b20019a85422a7ce569686c3d99c245b940e52fd0596635ea550"'

USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)"

headers = {"user-agent": USER_AGENT, "cookie": COOKIE}

profile = str(sys.argv[1])
getInforURL = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={profile}"

#Get ID

def GetID():
    try:
        req = requests.session()
        req.headers.update(headers)
        res = req.get(getInforURL)
        userInfo = res.json()
        return {
            "id": userInfo["data"]["user"]["id"],
            "biography": userInfo["data"]["user"]["biography"],
            "profileName": userInfo["data"]["user"]["full_name"],
            "profileImage": userInfo["data"]["user"]["profile_pic_url_hd"],
            "followersNumber": userInfo["data"]["user"]["edge_follow"]["count"],
            "isPrivate": userInfo["data"]["user"]["is_private"],
            "followed_by_viewer": userInfo["data"]["user"]["followed_by_viewer"],
        }
    except: 
        print(
            f"There was an error getting the user {profile}"
        )
        return None
    
#get stoires
def getStories(user_id):
    try:
        req = requests.session()
        req.headers.update(headers)
        res = req.get(f"https://i.instagram.com/api/v1/feed/user/{user_id}/reel_media/")
        
        if res.status_code == 200:
            stories = res.json()["items"]
            story_urls = []
            for story in stories:
                media_type = story["media_type"] 
                if media_type == 1:
                    story_urls.append({"type": "image", "url": story['image_versions2']['candidates'][0]['url']})
                elif media_type == 2:
                    story_urls.append({"type": "video", "url": story['video_versions'][0]['url']})
            return story_urls
        else:
            print("There was an error getting the stories")
            return []
    except:
        print("Error")
        return []

# formart data
def data():
    user_info = GetID()
    if user_info:
        if user_info["isPrivate"] and not user_info["followed_by_viewer"]:
            print("The account is private, you cannot get followers info.")
            return
        stories = getStories(user_info["id"])
        result = {
            "userInfo": user_info,
            "stories": stories
        }
        return result
    return None

if __name__ == "__main__":
    data_ig = data()
    if data_ig:
        print(json.dumps(data_ig))

sys.stdout.flush()





