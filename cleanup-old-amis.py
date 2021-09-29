#!/usr/bin/env python3

import botocore.session
session = botocore.session.get_session()
client = session.create_client('ec2', region_name='eu-west-1')

print("It works!")
