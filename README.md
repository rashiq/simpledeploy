# simpledeploy

A simple flask app that registers a webhook with github, So I can update my website everytime I push something. I currently have mine running on https://deploy.rashiq.me.

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

<img src="https://analytics.rashiq.me/simpledeploy-gh.png" width="0px" height="0px" style="display:none;"/>
