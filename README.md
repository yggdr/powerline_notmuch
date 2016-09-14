Notmuch powerline
===========

Easily query your [notmuch](https://notmuchmail.org/) database from [powerline](https://github.com/powerline/powerline).

ISC licenced, see the LICENCE file.

Examples:
---------
The most basic example would be:

    {
        "function": "powerline_notmuch.notmuch",
        "args": {
            "searches": [
                {"search": "tag:unread and not tag:list"},
            ]
        }
    }

results in

✉·2

A bit more, playing around with before and after:

    {
        "function": "powerline_notmuch.notmuch",
        "before": "[",
        "after": "]",
        "args": {
            "divider": "] [",
            "searches": [
                {"search": "tag:unread and not tag:list"},
                {"icon": "", "search": "tag:unread and tag:list"},
                {"icon": "BUGS", "search": "tag:unread and tag:bugs"}
            ]
        }
    }

results in

[✉ 2] [ 106] [BUGS 0]
