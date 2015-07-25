#!/usr/bin/python

"""
Author: Patrick W.
Date: 7/2/15

Script to distribute an AMI from one region to all others.

Requires: Ec2ConnectionBundle class, boto.
Set excludeRegion to the region where you're copying from, the ami ID should be the ID of the ami you're copying, the amiName will be what the copied AMI's name is.
"""

from Ec2ConnectionBundle import Ec2ConnectionBundle

apiKey = ''
apiSecret = ''
amiRegion = ''
amiID = ''
amiName = ''

connectBundle = Ec2ConnectionBundle(apiKey, apiSecret)

for connection in connectBundle.generateConnections(excludeRegion=amiRegion):
    connection.copy_image(amiRegion, amiID, name=amiName)
