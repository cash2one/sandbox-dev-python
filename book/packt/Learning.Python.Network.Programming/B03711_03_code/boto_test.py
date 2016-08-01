
import sys
import requests
import requests_aws4auth
import xml.etree.ElementTree as ET
import mimetypes
import xml.dom.minidom as minidom
import boto

access_id = 'AKIAJY5II3SZNHZ25SUA'
access_key = 'YJ0jPomyIdPKiJ5IKvSbSASFaqeNPlN5XX7Aea56'
# access_key = ''
region = 'eu-west-1'
auth = requests_aws4auth.AWS4Auth(access_id, access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'
endpoint = 's3-{}.amazonaws.com'.format(auth.region)


def xml_pprint(xml_string):
    print(minidom.parseString(xml_string).toprettyxml())


if __name__ == '__main__':
    conn = boto.connect_s3(access_id, access_key)
    bucket = conn.get_bucket('sammo')
    print([k.name for k in bucket.list()])




































