import argparse

from metasdk import read_developer_settings
from metasdk.tools import exec_cmd

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--service', help='Name of API Service. Example: hello', type=str, required=True)
    parser.add_argument('--lang', help='For each language generating code. Example: python', type=str, required=True)
    args = parser.parse_args()

    gcloud_params = read_developer_settings().get('gcloudDev')
    if not gcloud_params:
        raise ValueError("gcloudDev не установлены в developer_settings")

    grpc_service = args.service

    gcloud_project = gcloud_params['project']
    gcloud_prefix = gcloud_params.get('prefix', '')
    endpoint_service_name = gcloud_prefix + "-" + grpc_service if gcloud_prefix else grpc_service

    exec_cmd("""
        docker run \
            --rm \
            --publish=8083:8083 \
            --publish=8084:8084 \
            gcr.io/endpoints-release/endpoints-runtime:1 \
            --service={endpoint_service_name}.endpoints.{project}.cloud.goog \
            --rollout_strategy=managed \
            --http_port=8084 \
            --http2_port=8083 \
            --backend=grpc://docker.for.mac.localhost:50051 \
            --service_account_key=/esp/test-esp-service-account-creds.json
            --volume=~/esp:/esp \
        """.format(
        project=gcloud_project,
        endpoint_service_name=endpoint_service_name
    ))
