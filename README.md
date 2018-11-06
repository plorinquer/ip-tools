# ip-tools

## `ip_range_to_subnets.py`

This script allows to "summarize" an IP address range into subnets.

    python ip_range_to_subnets.py -first 192.0.2.129 -last 192.0.2.225
    192.0.2.129/32
    192.0.2.130/31
    192.0.2.132/30
    192.0.2.136/29
    192.0.2.144/28
    192.0.2.160/27
    192.0.2.192/27
    192.0.2.224/31