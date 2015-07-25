#!/usr/bin/python

"""
Author: Patrick W.
Date: 7/2/15

Script to distribute an AMI from one region to all others.

Requires: Ec2ConnectionBundle class, boto.
Set excludeRegion to the region where you're copying from.
"""

from Ec2ConnectionBundle import Ec2ConnectionBundle

connectBundle = Ec2ConnectionBundle("EC2 API KEY","EC2 SECRET KEY")

for connection in connectBundle.generateConnections(excludeRegion='REGION WHERE AMI RESIDES'):
    connection.copy_image('REGION WHERE AMI RESIDES', 'AMI ID', name="AMI Name")
