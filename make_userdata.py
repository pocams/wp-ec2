#!/bin/env python
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

source_directory = 'cloud-init'

def get_mime_type(filename):
  if filename == 'cloud-config':
    return 'text/cloud-config'
  elif filename.endswith('.sh'):
    return 'text/x-shellscript'
  else:
    raise ValueError("Unable to guess mime type of %s" % (filename))

message = MIMEMultipart()

for filename in os.listdir(source_directory):
  mime_type = get_mime_type(filename)
  contents = open(os.path.join(source_directory, filename), 'r').read()

  part = MIMEText(contents, mime_type)
  part.add_header('Content-Disposition', 'attachment; filename="%s"' % (filename))

  message.attach(part)

print message
