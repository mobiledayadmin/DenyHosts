import re

#################################################################################
# REGULAR EXPRESSIONS ARE COOL.  Check out Kodos (http://kodos.sourceforge.net) #
#################################################################################

#DATE_FORMAT_REGEX = re.compile(r"""(?P<month>[A-z]{3,3})\s*(?P<day>\d+)""")

SSHD_FORMAT_REGEX = re.compile(r""".* (sshd.*:|\[sshd\]) (?P<message>.*)""")
#SSHD_FORMAT_REGEX = re.compile(r""".* sshd.*: (?P<message>.*)""")

FAILED_ENTRY_REGEX = re.compile(r"""Failed (?P<method>.*) for (?P<invalid>invalid user |illegal user )?(?P<user>.*?) .*from (::ffff:)?(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})""")

FAILED_ENTRY_REGEX2 = re.compile(r"""(?P<invalid>(Illegal|Invalid)) user (?P<user>.*?) .*from (::ffff:)?(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})""")

FAILED_ENTRY_REGEX3 = re.compile(r"""Authentication failure for (?P<user>.*) .*from (::ffff:)?(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})""")

FAILED_ENTRY_REGEX4 = re.compile(r"""Authentication failure for (?P<user>.*) .*from (?P<host>.*)""")

FAILED_ENTRY_REGEX5 = re.compile(r"""User (?P<user>.*) .*from (?P<host>.*) not allowed because none of user's groups are listed in AllowGroups""")

FAILED_ENTRY_REGEX6 = re.compile(r"""Did not receive identification string .*from (::ffff:)?(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})""")

FAILED_ENTRY_REGEX7 = re.compile(r"""User (?P<user>.*) not allowed because not listed in AllowUsers""")


# these are reserved for future versions
FAILED_ENTRY_REGEX8 = re.compile(r"""authentication failure for (?P<user>.*) .*from (?P<host>.*) via""")

FAILED_ENTRY_REGEX9 = None
FAILED_ENTRY_REGEX10 = None

FAILED_ENTRY_REGEX_NUM = 9 # this should match the highest num failed_entry_regex + 1

FAILED_ENTRY_REGEX_RANGE = range(1, FAILED_ENTRY_REGEX_NUM)
FAILED_ENTRY_REGEX_MAP = {}

# create a hash of the failed entry regex'es indexed from 1 .. FAILED_ENTRY_REGEX_NUM 
for i in FAILED_ENTRY_REGEX_RANGE:
    if i == 1: extra = ""
    else: extra = "%i" % i
    rx = eval("FAILED_ENTRY_REGEX%s" % extra)
    FAILED_ENTRY_REGEX_MAP[i] = rx


SUCCESSFUL_ENTRY_REGEX = re.compile(r"""Accepted (?P<method>.*) for (?P<user>.*?) from (::ffff:)?(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})""")

TIME_SPEC_REGEX = re.compile(r"""(?P<units>\d*)\s*(?P<period>[smhdwy])?""")

ALLOWED_REGEX = re.compile(r"""(?P<first_3bits>\d{1,3}\.\d{1,3}\.\d{1,3}\.)((?P<fourth>\d{1,3})|(?P<ip_wildcard>\*)|\[(?P<ip_range>\d{1,3}\-\d{1,3})\])""")

PREFS_REGEX = re.compile(r"""(?P<name>.*?)\s*[:=]\s*(?P<value>.*)""")


