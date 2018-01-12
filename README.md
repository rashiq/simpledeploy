# simpledeploy

A simple flask app that serves as a webhook for github to send a post request to whenever something was pushed to one of my repositories.
So I can then run custom logic defined in my `config.json` file. I currently have mine running on https://deploy.rashiq.me.

Sample `config.json` file:

```json
[
  {
    "repository": "rashiq.me",
    "steps": [
      "cd /srv/rashiq.me/html",
      "git pull",
      "docker restart flask"
    ]
  }
]
```

This will just update my website.

<img src="https://derpixel.com/simpledeploy-gh.png" width="0px" height="0px" style="display:none;"/>
