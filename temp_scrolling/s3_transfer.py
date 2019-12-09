import boto3


s3=boto3.client('s3')
s3=boto3.client('s3' ,aws_access_key_id='AKIAJI5F6P6ROTNKNREQ',aws_secret_access_key='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')

def upload_s3_now():
    #param1: 가진 파일명, param2: bucket명, param3: bucket에 올라갈 파일명
    #s3.upload_file('highscore.txt','first-storage-for-practice','s3_script.txt')
    return 0
