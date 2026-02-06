"""Cloudflare R2 스토리지 헬퍼"""
import boto3
from botocore.config import Config as BotoConfig
from config import Config


def get_r2_client():
    """R2 S3 호환 클라이언트 생성"""
    return boto3.client(
        's3',
        endpoint_url=f'https://{Config.R2_ACCOUNT_ID}.r2.cloudflarestorage.com',
        aws_access_key_id=Config.R2_ACCESS_KEY_ID,
        aws_secret_access_key=Config.R2_SECRET_ACCESS_KEY,
        config=BotoConfig(signature_version='s3v4'),
        region_name='auto'
    )


def upload_to_r2(file_data, filename, content_type):
    """파일을 R2에 업로드"""
    r2 = get_r2_client()
    r2.put_object(
        Bucket=Config.R2_BUCKET_NAME,
        Key=filename,
        Body=file_data,
        ContentType=content_type
    )


def delete_from_r2(filename):
    """R2에서 파일 삭제"""
    try:
        r2 = get_r2_client()
        r2.delete_object(
            Bucket=Config.R2_BUCKET_NAME,
            Key=filename
        )
    except Exception as e:
        print(f"R2 파일 삭제 실패: {filename} - {e}")


def get_r2_url(filename):
    """R2 파일의 공개 URL 반환"""
    return f'{Config.R2_PUBLIC_URL}/{filename}'
