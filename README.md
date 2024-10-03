# Api | Anonymous Instagram Stories


api to watch instagram stories anonymously

## version

```
1.0.0
```

## Install

1. Clone the respository

```
git clone https://github.com/bryanjossephyf/api-ig-stories-viewer
```

2. Install dependencies

for Python
```
cd api-instagram
cd ig

python -m vienv ig/ig

ig\Scritps\activate
pip install -r requirements.txt

```

for node

```
npm install
```
o 

```
pnpm install
```

3. run the api

```
npm start
```
o
```
pnpm start
```

## use

open your navigator and type 

```
http:localhost:3000/api/[user instagram]
```
response

```
{
    "userInfo": {
        "id": "account ID",
        "biography": " account biography",
        "profileName": "full account name",
        "profileImage": "https://",
        "followersNumber": folloers,
        "isPrivate": false,
        "followed_by_viewer": false
    },
    "stories": [
        {
            "type": "video",
            "url": "https://"
        },
        {
            "type": "video",
            "url": "https://"
        },
        {
            "type": "image",
            "url": "https://"
        }
    ]
}
```


## /***/

if you have a error, is probably the cookie  code
to get your cookie, yo have to login with your instagram account, then:

1. press f12 > Network tab
2. Press f5 to realod the page
3. Search for "www.instagram.com" o your instagram user, it should be the first
4. Search for Request Headers
5. Copy all the content of "Cookie
6. go to the proyect ig/igMain.py
7. search COOKIE and replace with your cookie
