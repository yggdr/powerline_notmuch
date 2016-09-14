import subprocess

# cheap python 2/3 compatability
try:
    unicode
except NameError:
    unicode = str

def _divider(divider):
    return {
        u'contents': divider,
        u'highlight_groups': ['window_status']
    }

def _segment(num_mails, search):
    try:
        icon = search['icon']
        if icon != u"":
            icon += u" "
    except KeyError:
        icon = u"\u2709 "
    return {
                u'contents': u"{0}{1}".format(icon, unicode(num_mails, "utf-8")),
                u'highlight_groups': ['window_status'],
    }

def _get_num_mails(pl, search):
    proc = subprocess.Popen(['notmuch', 'count', search], stdout=subprocess.PIPE)
    num_mails, err = proc.communicate()
    if err is None:
        return num_mails.strip()
    pl.error("Could not get number of mails for search '{0}' due to error: {1}".format(search, err))
    return "-"

def _intersperse_dividers(segments, divider):
    for segment in segments:
        yield segment
        yield _divider(divider)

def notmuch(pl, searches=[{'search': 'tag:unread'}], divider=u" "):
    u"""Return number of mails matching notmuch search strings.

    Args:
        searches (list of dict):
            Each dictionary must contain the key "search" which will be used as the
            final part of a "notmuch count" query. A dictionary may contain an
            "icon" key holding the (unicode) icon used to mark the number mails.
            Defaults to "\u2709". Set to empty string to deactivate.
        divider (str):
            String used to divide individual mail counts. May be used as an
            alternative to `draw_inner_divider` configuration option. Can be nicely
            combined with the `before` and `after` configuration options.
    """

    num_mails = [_get_num_mails(pl, search['search']) for search in searches]
    segments = [_segment(num, search) for num, search in zip(num_mails, searches)]
    interspersed = [segment for segment in _intersperse_dividers(segments, divider)]
    interspersed.pop()  # Should be handled by intersperse function...
    return interspersed
